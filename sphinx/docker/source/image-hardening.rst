Image Hardening
===============

Container security starts at image build time. A hardened image is smaller, has fewer packages, avoids embedded secrets, runs with least privilege, and is easy to rebuild when the base image changes.

Start from a small trusted base
-------------------------------

Use official, vendor-supported, or organization-approved base images. Prefer a slim runtime base over a full development distribution.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    FROM python:3-slim AS runtime

Pin versions for reproducibility. For high-control environments, pin the base image by digest and schedule automated digest refreshes.

.. code-block:: docker
    :linenos:

    FROM python:3-slim@sha256:<digest>

Keep build tools out of runtime images
--------------------------------------

Use multi-stage builds so compilers, package caches, test fixtures, and source-control metadata do not land in the runtime image.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    FROM python:3-slim AS build
    WORKDIR /app
    COPY requirements.txt .
    RUN --mount=type=cache,target=/root/.cache/pip \
        pip wheel --wheel-dir /wheels -r requirements.txt

    FROM python:3-slim AS runtime
    WORKDIR /app
    RUN useradd --create-home --uid 10001 appuser
    COPY --from=build /wheels /wheels
    RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels
    COPY --chown=appuser:appuser . .
    USER appuser
    EXPOSE 8080
    CMD ["python", "app.py"]

Run as a non-root user
----------------------

Containers should not need root for normal application work. Create an application user and switch to it with ``USER``. Install operating system packages as root during the build, then switch to the application user before copying application code or starting the process.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    FROM python:3-slim

    RUN apt-get update -y && \
        apt-get install --no-install-recommends curl -y && \
        rm -rf /var/lib/apt/lists/*

    RUN groupadd --gid 10001 app && \
        useradd --uid 10001 --gid app --create-home app

    WORKDIR /app
    COPY --chown=app:app requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    COPY --chown=app:app . .

    USER 10001:10001
    CMD ["python", "app.py"]

Use a numeric UID and GID for runtime ownership. User names are convenient inside one image, but numeric IDs are what the kernel, volumes, Kubernetes security contexts, and host filesystems enforce.

Avoid sudo and personal admin accounts
--------------------------------------

Do not install ``sudo`` into application images and do not bake a personal superuser account such as ``super`` into the image. A container is not a small VM that needs interactive administration. Rebuild the image when system packages change, and use logs, metrics, shell debugging, or one-off diagnostic containers for troubleshooting.

Avoid this pattern.

.. code-block:: docker
    :linenos:

    FROM ubuntu:latest
    RUN apt-get update && apt-get install sudo -y
    RUN useradd --create-home super && echo "super ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
    USER super
    CMD ["sudo", "python3", "app.py"]

Prefer this pattern.

.. code-block:: docker
    :linenos:

    FROM python:3-slim
    RUN useradd --uid 10001 --create-home app
    WORKDIR /app
    COPY --chown=10001:10001 . .
    USER 10001:10001
    CMD ["python", "app.py"]

If an image truly needs a startup action as root, keep that action narrow and drop privileges before starting the long-running process. Most web applications, workers, batch jobs, and model servers do not need this.

Runtime controls
----------------

Also configure the runtime or orchestrator to drop Linux capabilities when possible.

.. code-block:: yaml
    :linenos:

    services:
      api:
        image: example/api:dev
        user: "10001:10001"
        cap_drop:
          - ALL
        security_opt:
          - no-new-privileges:true
        read_only: true
        tmpfs:
          - /tmp

In Kubernetes, put the same policy in the Pod or container security context.

.. code-block:: yaml
    :linenos:

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: api
    spec:
      template:
        spec:
          securityContext:
            runAsNonRoot: true
            runAsUser: 10001
            runAsGroup: 10001
            fsGroup: 10001
          containers:
            - name: api
              image: registry.example.com/team/api:latest
              securityContext:
                allowPrivilegeEscalation: false
                readOnlyRootFilesystem: true
                capabilities:
                  drop:
                    - ALL

Volume ownership
----------------

Non-root images often fail when a mounted volume is owned by root. Fix the ownership model rather than running the container as root.

* Use ``COPY --chown`` for files baked into the image.
* Use named volumes or Kubernetes ``fsGroup`` for writable runtime directories.
* Write temporary files to ``/tmp`` or another explicit writable mount.
* Avoid writing into the application directory at runtime.
* Make logs go to stdout and stderr, not root-owned files inside the image.

Rootless Docker
---------------

Rootless Docker runs the Docker daemon and containers inside a user namespace without root privileges on the host. It reduces risk from daemon and runtime vulnerabilities. It does not replace image-level hardening: the application inside the image should still run as a non-root user, avoid ``sudo``, and drop unnecessary runtime privileges.

Do not bake secrets into images
-------------------------------

Do not copy ``.env`` files, cloud credentials, SSH keys, package tokens, or TLS private keys into images. Do not pass them as ``ARG`` or ``ENV`` in the Dockerfile. Use BuildKit secrets during the build and runtime secrets from the orchestrator.

Use a ``.dockerignore`` file
----------------------------

A tight build context prevents accidental data leaks and speeds up builds.

.. code-block:: text
    :linenos:

    .git
    .env
    .aws
    .ssh
    node_modules
    __pycache__
    *.pyc
    dist
    build

Add health metadata
-------------------

Images can include a health check when the process has a cheap local check. Compose and orchestrators can override it when the environment needs a different probe.

.. code-block:: docker
    :linenos:

    HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
        CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health')"

Rebuild often
-------------

Images age as soon as their base image and packages age. Rebuild on a schedule, scan the result, and redeploy even when application code has not changed. A reproducible build pipeline makes patching a normal operation instead of an emergency.

Checklist
---------

* Use approved base images.
* Prefer slim runtime images and multi-stage builds.
* Pin dependencies and refresh them intentionally.
* Create a dedicated runtime UID/GID and set ``USER``.
* Do not install ``sudo`` or create personal admin accounts in application images.
* Do not rely on root for writable directories; fix ownership and mounts.
* Drop capabilities and prevent privilege escalation at runtime.
* Keep credentials out of Dockerfiles, build args, image layers, and logs.
* Maintain ``.dockerignore``.
* Scan images and fail CI on policy violations.
* Publish SBOM and provenance attestations for release images.

References
----------

* `Dockerfile best practices <https://docs.docker.com/build/building/best-practices/>`_
* `Build secrets <https://docs.docker.com/build/building/secrets/>`_
* `Docker Engine rootless mode <https://docs.docker.com/engine/security/rootless/>`_
* `Docker Scout <https://docs.docker.com/scout/>`_
