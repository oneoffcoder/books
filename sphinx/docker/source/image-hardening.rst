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

Containers should not need root for normal application work. Create an application user and switch to it with ``USER``. Also configure the runtime or orchestrator to drop Linux capabilities when possible.

.. code-block:: yaml
    :linenos:

    services:
      api:
        image: example/api:dev
        cap_drop:
          - ALL
        read_only: true
        tmpfs:
          - /tmp

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
* Run as a non-root user.
* Keep credentials out of Dockerfiles, build args, image layers, and logs.
* Maintain ``.dockerignore``.
* Scan images and fail CI on policy violations.
* Publish SBOM and provenance attestations for release images.

References
----------

* `Dockerfile best practices <https://docs.docker.com/build/building/best-practices/>`_
* `Build secrets <https://docs.docker.com/build/building/secrets/>`_
* `Docker Scout <https://docs.docker.com/scout/>`_
