GPU
===

Some workloads need NVIDIA GPU access from inside a container. Install the current `NVIDIA Container Toolkit <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html>`_ and verify that Docker can pass the GPU through to a CUDA image.

Use the current CUDA image tag from NVIDIA's container registry. This book uses a current CUDA 13 image.

.. code-block:: bash
    :linenos:

    docker run --rm --gpus all nvidia/cuda:13.1.1-base-ubuntu24.04 nvidia-smi

You should see ``nvidia-smi`` output with the GPU, driver, and CUDA compatibility reported by the host.

The ``Dockerfile`` uses a current CUDA/cuDNN development image as the base image. It installs Python, Jupyter Lab, PyTorch, and ``supervisor``. Before production use, confirm that the CUDA image, host driver, and framework wheels support the same CUDA generation.

.. literalinclude:: _static/code/gpu/Dockerfile
   :language: docker
   :linenos:
   :emphasize-lines: 1

Build.

.. code-block:: bash
    :linenos:

    docker build --no-cache -t gpu-jupyter:local .

Run. Note that we have to specify the ``--gpus all`` flag to give GPU access to the container.

.. code-block:: bash
    :linenos:

    docker run \
        -it \
        --rm \
        -p 8888:8888 \
        --gpus all \
        -v `pwd`/ipynb:/ipynb \
        gpu-jupyter:local

You may now access the Jupyter Lab at `http://localhost:8888 <http://localhost:8888>`_.

References
----------

* `NVIDIA Container Toolkit <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html>`_
* `NVIDIA CUDA container images <https://catalog.ngc.nvidia.com/orgs/nvidia/containers/cuda>`_
