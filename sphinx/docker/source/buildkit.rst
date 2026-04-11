BuildKit and Buildx
===================

BuildKit is Docker's modern build backend. It improves build speed, cache behavior, Dockerfile features, and multi-platform output. Docker Engine uses BuildKit by default in current releases, and ``docker buildx`` is the CLI front end for advanced builds.

Check the local builder first.

.. code-block:: bash
    :linenos:

    docker buildx version
    docker buildx ls

The default builder is enough for many local builds. For multi-platform builds, shared registry cache, or isolated CI builders, create a named builder that uses the ``docker-container`` driver.

.. code-block:: bash
    :linenos:

    docker buildx create --name book-builder --driver docker-container --use
    docker buildx inspect --bootstrap

Dockerfile syntax
-----------------

Start Dockerfiles that use newer BuildKit features with the syntax directive.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    FROM python:3-slim

The directive lets Docker use the current stable Dockerfile frontend even when the builder host is not upgraded at the same pace as the project.

Cache mounts
------------

Cache mounts keep dependency caches outside the final image while still reusing them across builds. This pattern is useful for package managers such as ``pip``, ``npm``, ``apt``, ``maven`` and ``gradle``.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    FROM python:3-slim

    WORKDIR /app
    COPY requirements.txt .
    RUN --mount=type=cache,target=/root/.cache/pip \
        pip install --no-cache-dir -r requirements.txt

    COPY . .
    CMD ["python", "app.py"]

The cache directory is available while the ``RUN`` instruction executes. It is not copied into the image layer.

Build secrets
-------------

Do not pass tokens through ``ARG`` or ``ENV``. They can leak through image history or build logs. Use BuildKit secrets so credentials are mounted only for the instruction that needs them.

.. code-block:: bash
    :linenos:

    export PIP_TOKEN="..."
    docker buildx build \
        --secret id=pip_token,env=PIP_TOKEN \
        -t example/app:dev .

The Dockerfile reads the secret from the temporary mount.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    RUN --mount=type=secret,id=pip_token \
        PIP_TOKEN="$(cat /run/secrets/pip_token)" && \
        pip config set global.extra-index-url "https://token:${PIP_TOKEN}@packages.example.com/simple"

Registry cache
--------------

CI runners are often ephemeral. Registry-backed cache lets each new runner reuse layers from previous builds.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --cache-from type=registry,ref=registry.example.com/team/app:buildcache \
        --cache-to type=registry,ref=registry.example.com/team/app:buildcache,mode=max \
        -t registry.example.com/team/app:${GIT_SHA} \
        --push .

Use a separate cache tag so application tags and build-cache metadata have different lifecycles.

Build output
------------

Buildx can load an image into the local Docker image store, push it to a registry, or write files to disk.

.. code-block:: bash
    :linenos:

    # Local single-platform development image
    docker buildx build --load -t example/app:dev .

    # Registry image for deployment
    docker buildx build --platform linux/amd64 -t registry.example.com/team/app:prod --push .

Keep ordinary ``docker build`` for quick local work when it is enough. Move to ``docker buildx build`` when the build needs cache export, secrets, attestations, or multi-platform output.

References
----------

* `Docker Build overview <https://docs.docker.com/build/>`_
* `BuildKit <https://docs.docker.com/build/buildkit/>`_
* `Build cache <https://docs.docker.com/build/cache/>`_
* `Build secrets <https://docs.docker.com/build/building/secrets/>`_
