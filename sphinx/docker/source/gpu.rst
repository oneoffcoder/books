GPU
===

In some application, you may need Graphics Processing Unit ``GPU`` support with NVIDIA graphics card. NVIDIA has published the ``NVIDIA Container Toolkit`` to enable GPU support for Docker containers. The `GitHub <https://github.com/NVIDIA/nvidia-docker>`_ site has information on how to install this tool ``nvidia-docker``.

To see if you have installed ``nvidia-docker`` correctly, type in the following.

.. code-block:: bash
    :linenos:

    docker run --gpus all nvidia/cuda:9.0-base nvidia-smi

You should see an output similar to the below.

::

    +-----------------------------------------------------------------------------+
    | NVIDIA-SMI 430.50       Driver Version: 430.50       CUDA Version: 10.1     |
    |-------------------------------+----------------------+----------------------+
    | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
    |===============================+======================+======================|
    |   0  GeForce RTX 208...  Off  | 00000000:01:00.0  On |                  N/A |
    | 25%   33C    P8    17W / 250W |    893MiB / 11016MiB |      5%      Default |
    +-------------------------------+----------------------+----------------------+
                                                                                
    +-----------------------------------------------------------------------------+
    | Processes:                                                       GPU Memory |
    |  GPU       PID   Type   Process name                             Usage      |
    |=============================================================================|
    +-----------------------------------------------------------------------------+

The ``Dockerfile``.

.. literalinclude:: _static/code/gpu/Dockerfile
   :language: docker
   :linenos:
   :emphasize-lines: 1

Build.

.. code-block:: bash
    :linenos:

    docker build --no-cache -t gpu-jupyter:local .

Run.

.. code-block:: bash
    :linenos:

    docker run \
        -it \
        --rm \
        -p 8888:8888 \
        -v `pwd`/ipynb:/ipynb \
        gpu-jupyter:local

You may now access the Jupyter Lab at `http://localhost:8888 <http://localhost:8888>`_.