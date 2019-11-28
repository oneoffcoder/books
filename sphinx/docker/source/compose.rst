Docker Compose
==============

We can use ``docker-compose`` to bring up a set of containers together. You will have to `install docker-compose separately <https://docs.docker.com/compose/install/>`_. On Linux, the following commands should install this CLI and check to see if it installed correctly.

.. code:: bash

    sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

    sudo chmod +x /usr/local/bin/docker-compose

    docker-compose --version

After you have installed docker-compose successfully, you need to create a ``docker-compose.yml`` file. The full specification of the different versions of the ``compose file`` is `available <https://docs.docker.com/compose/compose-file>`_. We create an example ``docker-compose.yml`` file as follows.

.. literalinclude:: _static/code/compose/docker-compose.yml
   :language: yaml
   :linenos:

The ``YAML`` file is self-explanatory, for the most part. 

* We create three services: ``db``, ``flask`` and ``ng``.
* Each service has a specified container image: ``db-app:local``, ``rest-app:local`` and ``ui-app:local``.
* Note that we mount volumes and set environment variables where needed.
* Lastly, we also specify ``healthchecks`` to make sure the services are running; when they fail, an attempt will be made to bring them back up.

.. code:: bash

    conda install -y SQLAlchemy flask flask-cors
    pip install mysql-connector-python