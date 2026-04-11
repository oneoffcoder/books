Cross Builds
============

Cross builds create an image for a CPU architecture that is different from the machine doing the build. This comes up constantly with Apple Silicon Macs, x86 CI runners, and cheaper ARM cloud instances.

The standard Docker path is:

* Use BuildKit through ``docker buildx``.
* Declare the target architecture with ``--platform``.
* Push multi-platform release images to a registry.
* Use native builders or language-level cross-compilation for slow or fragile builds.
* Use QEMU emulation for convenience, not as the default for heavy compilation.

Terminology
-----------

Docker uses platform strings such as ``linux/amd64`` and ``linux/arm64``.

* ``linux/amd64`` is the common x86-64 Linux target.
* ``linux/arm64`` is the common ARM64 Linux target used by Apple Silicon Linux containers, AWS Graviton, ARM Kubernetes nodes, and many low-cost cloud instances.
* ``BUILDPLATFORM`` is where the build command is running.
* ``TARGETPLATFORM`` is what the image being built must run on.

Check what the current builder supports.

.. code-block:: bash
    :linenos:

    docker buildx version
    docker buildx ls
    docker buildx inspect --bootstrap

Create a builder
----------------

For repeatable cross builds, create a named Buildx builder using the ``docker-container`` driver.

.. code-block:: bash
    :linenos:

    docker buildx create \
        --name cross-builder \
        --driver docker-container \
        --bootstrap \
        --use

    docker buildx inspect --bootstrap

The ``docker-container`` driver supports advanced BuildKit behavior and multi-platform builds. Images built with that driver are not automatically loaded into the local Docker image store. Use ``--load`` for a single-platform local test image or ``--push`` for registry output.

Mac to x86
----------

On an Apple Silicon Mac, build an x86 Linux image with ``linux/amd64``.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --platform linux/amd64 \
        --load \
        -t app:amd64 .

Run it locally with the same platform flag.

.. code-block:: bash
    :linenos:

    docker run --rm --platform linux/amd64 app:amd64

This normally works on Docker Desktop because Docker Desktop includes QEMU support. It can be slow when the Dockerfile compiles source code, compresses large layers, or installs packages with architecture-specific native extensions.

x86 to ARM64
------------

On an x86 Linux workstation or CI runner, build an ARM64 image with ``linux/arm64``.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --platform linux/arm64 \
        --load \
        -t app:arm64 .

If the builder is Docker Engine on Linux and QEMU is not already installed, register binfmt handlers.

.. code-block:: bash
    :linenos:

    docker run --privileged --rm tonistiigi/binfmt --install arm64,amd64

For deployment to ARM64 cloud instances, push the result to a registry instead of loading it locally.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --platform linux/arm64 \
        -t registry.example.com/team/app:arm64 \
        --push .

Release one image name
----------------------

For applications that should run on both x86 and ARM64, publish one multi-platform image.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --platform linux/amd64,linux/arm64 \
        -t registry.example.com/team/app:latest \
        --push .

Inspect the registry manifest.

.. code-block:: bash
    :linenos:

    docker buildx imagetools inspect registry.example.com/team/app:latest

When a host pulls that image, Docker selects the matching platform variant from the manifest list. An x86 host gets ``linux/amd64``. An ARM64 host gets ``linux/arm64``.

Choose a strategy
-----------------

There are three practical strategies.

.. list-table:: Cross-build strategies
   :widths: 25 40 35
   :header-rows: 1

   * - Strategy
     - Use it when
     - Tradeoff
   * - QEMU emulation
     - You need a quick cross build and the Dockerfile mostly installs packages or copies files.
     - Easiest setup, but slow and sometimes flaky for compilation-heavy builds.
   * - Native builders
     - Builds are slow under emulation or native dependencies fail under QEMU.
     - Best compatibility and speed, but requires both ARM64 and AMD64 builder nodes.
   * - Language cross-compilation
     - The language has strong cross-compile support, such as Go or Rust.
     - Fast and deterministic, but the Dockerfile must pass target platform values to the compiler.

Native builder nodes
--------------------

If QEMU is too slow, attach native x86 and ARM64 machines to one builder. First create Docker contexts for each host.

.. code-block:: bash
    :linenos:

    docker context create node-amd64 --docker host=ssh://builder-amd64
    docker context create node-arm64 --docker host=ssh://builder-arm64

Create a multi-node builder.

.. code-block:: bash
    :linenos:

    docker buildx create --name native-builder node-amd64 --use
    docker buildx create --name native-builder --append node-arm64
    docker buildx inspect --bootstrap

Then build the same multi-platform image.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --builder native-builder \
        --platform linux/amd64,linux/arm64 \
        -t registry.example.com/team/app:latest \
        --push .

Cross-compile in the Dockerfile
-------------------------------

For compiled languages, avoid emulation during the expensive build stage. Pin the compiler stage to the builder platform and compile for the target platform.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    FROM --platform=$BUILDPLATFORM golang:alpine AS build
    ARG TARGETOS
    ARG TARGETARCH
    WORKDIR /src
    COPY . .
    RUN GOOS=${TARGETOS} GOARCH=${TARGETARCH} go build -o /out/server ./cmd/server

    FROM alpine:latest
    COPY --from=build /out/server /server
    ENTRYPOINT ["/server"]

Build both targets.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --platform linux/amd64,linux/arm64 \
        -t registry.example.com/team/server:latest \
        --push .

Troubleshooting
---------------

If a cross build fails, check these items first.

* The base image must publish the target platform. Check with ``docker buildx imagetools inspect python:3-slim``.
* Native dependencies must exist for the target architecture. Python wheels, Node native modules, and system packages are common failure points.
* ``--load`` is for a single local platform. Use ``--push`` for multi-platform releases.
* ``docker run`` should use ``--platform`` when testing the non-native image locally.
* QEMU failures usually mean the build should move to native builder nodes or language-level cross-compilation.
* CI runners should use a persistent registry cache so each architecture does not rebuild everything from scratch.

Cost-oriented ARM64 builds
--------------------------

ARM64 instances are often cheaper for the same workload. Build and publish ``linux/arm64`` explicitly before moving a service to ARM64 capacity.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --platform linux/arm64 \
        --cache-from type=registry,ref=registry.example.com/team/app:buildcache \
        --cache-to type=registry,ref=registry.example.com/team/app:buildcache,mode=max \
        -t registry.example.com/team/app:arm64 \
        --push .

Before switching production, test the image on an actual ARM64 node. Emulation proves the image can start; native testing proves performance and dependency behavior.

References
----------

* `Multi-platform builds <https://docs.docker.com/build/building/multi-platform/>`_
* `Build drivers <https://docs.docker.com/build/builders/drivers/>`_
* `Buildx <https://docs.docker.com/build/>`_
