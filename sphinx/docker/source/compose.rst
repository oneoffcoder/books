Docker Compose
==============

Compose runs a set of related containers as one project. Use the current Compose plugin through ``docker compose``. The old standalone Compose v1 command is retired and should not be used for new work.

Check the plugin.

.. code-block:: bash
    :linenos:

    docker compose version
    docker compose ls

Compose files
-------------

The preferred file name is ``compose.yaml``. Current Compose files follow the Compose Specification; do not add a top-level ``version`` key to new files.

The sample below defines three services: a MySQL database, a Flask API, and an nginx-hosted frontend.

.. literalinclude:: _static/code/compose/compose.yaml
   :language: yaml
   :linenos:

The ``YAML`` file is mostly self-explanatory.

* We create three services: ``db``, ``flask`` and ``ng``.
* Each service has a specified container image: ``db-app:local``, ``rest-app:local`` and ``ui-app:local``.
* The database mounts initialization scripts and receives its root password through environment configuration.
* Health checks describe how Compose can tell whether a service is healthy.

For services that need a dependency to be healthy before startup, use long-form ``depends_on``.

.. code-block:: yaml
    :linenos:

    services:
      api:
        image: rest-app:local
        depends_on:
          db:
            condition: service_healthy

Environment files
-----------------

Keep local defaults in a ``.env`` file or pass an explicit environment file. Do not commit real secrets.

.. code-block:: bash
    :linenos:

    docker compose --env-file .env.local config
    docker compose --env-file .env.local up --build

Profiles
--------

Profiles let optional services stay out of the default development loop.

.. code-block:: yaml
    :linenos:

    services:
      worker:
        image: worker-app:local
        profiles:
          - jobs

Run the optional service only when the profile is requested.

.. code-block:: bash
    :linenos:

    docker compose --profile jobs up

Secrets and configs
-------------------

Compose supports secrets and configs. For local development, a secret can be mounted from a file.

.. code-block:: yaml
    :linenos:

    services:
      api:
        image: rest-app:local
        secrets:
          - db_password

    secrets:
      db_password:
        file: ./secrets/db_password.txt

The application reads the mounted file rather than receiving the value through an environment variable.

Networks and volumes
--------------------

Compose creates a project network by default. Add named networks when you need explicit boundaries, and use named volumes for persistent state.

.. code-block:: yaml
    :linenos:

    services:
      db:
        image: db-app:local
        volumes:
          - db_data:/var/lib/mysql
        networks:
          - backend

    volumes:
      db_data:

    networks:
      backend:

Daily commands
--------------

The commands below cover the normal loop.

.. code-block:: bash
    :linenos:

    docker compose -f compose.yaml config
    docker compose -f compose.yaml up --build
    docker compose -f compose.yaml ps
    docker compose -f compose.yaml logs -f
    docker compose -f compose.yaml exec flask sh
    docker compose -f compose.yaml down --volumes

Use Compose for local development, integration tests, and simple single-host deployments. For managed cloud deployments, translate the same image and configuration ideas into the target platform's native model, such as ECS task definitions or Kubernetes manifests.

Dockerfiles
-----------

MySQL
^^^^^

.. literalinclude:: _static/code/compose/mysql/Dockerfile
   :language: docker
   :linenos:

Flask
^^^^^

.. literalinclude:: _static/code/compose/flask/Dockerfile
   :language: docker
   :linenos:

Angular
^^^^^^^

.. literalinclude:: _static/code/compose/ng/Dockerfile
   :language: docker
   :linenos:

References
----------

* `Docker Compose <https://docs.docker.com/compose/>`_
* `Compose Specification <https://docs.docker.com/reference/compose-file/>`_
* `Compose profiles <https://docs.docker.com/compose/how-tos/profiles/>`_
* `Compose secrets <https://docs.docker.com/compose/how-tos/use-secrets/>`_
