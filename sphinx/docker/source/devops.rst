DevOps
======

Let's see how we may use Docker to be a part of a simple continuous integration/continuous delivery ``CICD`` pipeline. In this example, we have an demo Python API. The file and directory structure looks like the following. It's not important what this Python API does since we are more interested in how to use Docker to build, test and publish the API to ``pypi``.

::

    python/
    ├── Dockerfile
    ├── Makefile
    ├── publish.sh
    ├── pydemo
    │   ├── __init__.py
    │   └── poco.py
    ├── README.md
    ├── README.rst
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    └── tests
        ├── __init__.py
        └── test_poco.py

Using Docker containerization to perform CI/CD is just a matter of scripting. Here's the script ``publish.sh`` that builds, tests and publishes the API. The important caveat here is the acquisition of the ``${API_VERSION}`` environment variable value. We pass this value in to the Docker container and the script now has access to it.

.. literalinclude:: _static/code/devops/python/publish.sh
   :language: bash
   :linenos:
   :emphasize-lines: 5, 14-17, 19, 26, 44, 51, 57-62

Here's the ``Dockerfile``. Here, we use the ``ARG`` instruction to pass build arguments to the container while it's being created.

.. literalinclude:: _static/code/devops/python/Dockerfile
   :language: docker
   :linenos:
   :emphasize-lines: 3-4, 6-7, 20

As we iterate through our development, we perform CI/CD by executing the command as below. Here, we specify that the API is at version ``0.0.1``. 

.. code-block:: bash
    :linenos:
    :emphasize-lines: 2-3

    docker build --no-cache \
        --build-arg ARG_VERSION=0.0.1 \
        --build-arg ARG_REPO=pydemo \
        -t pydemo:0.0.1 .

If we are at version ``0.0.2``, then the command changes to something as simple as the following.

.. code-block:: bash
    :linenos:
    :emphasize-lines: 2

    docker build --no-cache \
        --build-arg ARG_VERSION=0.0.2 \
        --build-arg ARG_REPO=pydemo \
        -t pydemo:0.0.1 .