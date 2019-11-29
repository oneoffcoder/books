ARM
===

Thus far, we assumed that you are building your Docker containers on a x86 CPU architecture. However, you may also build Docker containers for the ARM CPU architecture too, such as the `Raspberr Pi <https://www.raspberrypi.org/>`_. Typically, you build x86 CPU targeted Docker containers on a computer with a x86 CPU, and likewise, you build ARM CPU targeted Docker containers on a ARM CPU computer. However, you may also build ARM CPU targeted Docker containers from a x86 CPU computer by typing in the following.

.. code-block:: bash
    :linenos:

    docker run --rm --privileged hypriot/qemu-register

Basic ARM container
-------------------

An example ``Dockerfile`` to build a basic ARM container is as follows.

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
* We setup a mount volume at ``/ipynb`` so that we can mout our local notebooks onto the container at runtime.
* We expose port ``8888``, which is what Jupyer Lab is running on. 
* We use ``supervisor`` to start up Jupyter Lab at runtime.

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