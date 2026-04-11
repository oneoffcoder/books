ARM
===

Modern Docker builds should treat CPU architecture as an explicit build output. A developer may build on an ``amd64`` laptop, deploy to ``arm64`` cloud nodes, and still publish one image name that works for both platforms. See the cross-builds chapter for the full Mac-to-x86, x86-to-ARM64, and multi-platform release workflow.

Use Buildx for multi-platform builds.

.. code-block:: bash
    :linenos:

    docker buildx ls
    docker buildx create --name multiarch --driver docker-container --use
    docker buildx inspect --bootstrap

If the builder needs CPU emulation, install QEMU/binfmt support on the build host.

.. code-block:: bash
    :linenos:

    docker run --privileged --rm tonistiigi/binfmt --install all

Build and push one manifest list containing both ``amd64`` and ``arm64`` images.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --platform linux/amd64,linux/arm64 \
        -t registry.example.com/team/app:latest \
        --push .

For local testing, load a single-platform image into the local Docker image store.

.. code-block:: bash
    :linenos:

    docker buildx build --platform linux/arm64 --load -t app:arm64 .

Do not assume that every base image supports every platform. Check the manifest before choosing the base image.

.. code-block:: bash
    :linenos:

    docker buildx imagetools inspect python:3-slim

Basic ARM container
-------------------

An example ``Dockerfile`` to build a basic ARM container for Raspberry Pi-style work is as follows.

.. literalinclude:: _static/code/arm/rpi-base/Dockerfile
   :language: docker
   :linenos:
   :emphasize-lines: 1, 3

Notice the following.

* The base image is ``arm32v7/ubuntu``.
* The ``ENV DEBIAN_FRONTEND=noninteractive`` instruction is to enable non-interactive installs (so we do not get prompted for ``Yes`` or ``No``).
* We install a lot of system libraries since we want to do interesting things later on.

Build.

.. code-block:: bash
    :linenos:

    docker build --no-cache -t rpi-base:local .

Run.

.. code-block:: bash
    :linenos:

    docker run -it rpi-base:local

Jupyter Lab
-----------

What if we want to have a reproducible, consistent data science work environment on the Raspberry Pi? We can build a container to spin up a ``Jupyter Lab`` instance.

.. literalinclude:: _static/code/arm/rpi-jupyter/Dockerfile
   :language: docker
   :linenos:
   :emphasize-lines: 1, 16-23, 26-27, 30, 35

Notice the following.

* We use the previous ``rpi-base:local`` image to bootstrap this image.
* We install ``miniconda`` to manage our Python environments and dependencies.
* We setup a mount volume at ``/ipynb`` so that we can mount our local notebooks onto the container at runtime.
* We expose port ``8888``, which is what Jupyter Lab is running on.
* We use ``supervisor`` to start up Jupyter Lab at runtime.
* If you do not like Jupyter Lab and want the classic Jupyter Notebook, override at runtime with ``-e JUPYTER_TYPE=notebook``.

Build.

.. code-block:: bash
    :linenos:

    docker build --no-cache -t rpi-jupyter:local .

Run.

.. code-block:: bash
    :linenos:

    docker run \
        -it \
        --rm \
        -p 8888:8888 \
        -v `pwd`/ipynb:/ipynb \
        rpi-jupyter:local

You may now access the Jupyter Lab at `http://localhost:8888 <http://localhost:8888>`_.

References
----------

* `Multi-platform builds <https://docs.docker.com/build/building/multi-platform/>`_
* `Buildx <https://docs.docker.com/build/>`_
