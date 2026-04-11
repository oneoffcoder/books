Debugging and Operations
========================

Operational Docker work starts with asking the container runtime what is happening. Do not guess. Inspect the image, the container, the logs, the network, and the resource usage.

Container state
---------------

List running and stopped containers.

.. code-block:: bash
    :linenos:

    docker ps
    docker ps --all

Inspect the complete container configuration.

.. code-block:: bash
    :linenos:

    docker inspect api
    docker inspect --format '{{json .State.Health}}' api

Check the process list inside a running container.

.. code-block:: bash
    :linenos:

    docker top api

Logs
----

Containers should write logs to stdout and stderr. Docker captures those streams.

.. code-block:: bash
    :linenos:

    docker logs api
    docker logs --follow --tail 100 api
    docker logs --since 30m api

Configure logging drivers at the daemon or container level when logs need to go to a platform-specific system.

.. code-block:: bash
    :linenos:

    docker run \
        --log-driver json-file \
        --log-opt max-size=10m \
        --log-opt max-file=3 \
        nginx:alpine

Shell access
------------

Use ``docker exec`` when the image has a shell.

.. code-block:: bash
    :linenos:

    docker exec -it api sh

Many production images should be slim and may not include a shell or package manager. For those images, use ``docker debug`` when it is available in your environment. It creates a debugging shell with tools without permanently changing the target image.

.. code-block:: bash
    :linenos:

    docker debug api

Resource usage
--------------

Check live resource usage.

.. code-block:: bash
    :linenos:

    docker stats
    docker stats api

Check Docker events while reproducing a problem.

.. code-block:: bash
    :linenos:

    docker events

Health checks
-------------

A health check tells Docker and Compose whether the application is actually ready.

.. code-block:: docker
    :linenos:

    HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
        CMD wget -qO- http://127.0.0.1:8080/health || exit 1

Inspect health status.

.. code-block:: bash
    :linenos:

    docker inspect --format '{{.State.Health.Status}}' api
    docker inspect --format '{{range .State.Health.Log}}{{println .Output}}{{end}}' api

Image inspection
----------------

Check image metadata and history.

.. code-block:: bash
    :linenos:

    docker image inspect api:local
    docker history api:local

Use this to catch unexpected users, commands, ports, labels, and large layers.

Network debugging
-----------------

Inspect networks and test from inside the same network namespace.

.. code-block:: bash
    :linenos:

    docker network ls
    docker network inspect appnet
    docker exec -it api sh
    getent hosts db
    nc -vz db 3306

Compose debugging
-----------------

Compose scopes commands to the project.

.. code-block:: bash
    :linenos:

    docker compose ps
    docker compose logs -f api
    docker compose exec api sh
    docker compose events
    docker compose config

Cleanup
-------

Clean up deliberately. Avoid broad prune commands on shared machines unless you know what they will remove.

.. code-block:: bash
    :linenos:

    docker container prune
    docker image prune
    docker volume ls
    docker volume rm <volume-name>

Practical checklist
-------------------

* Start with ``docker ps --all`` and ``docker logs``.
* Inspect health status before restarting a service.
* Use ``docker inspect`` to verify ports, mounts, networks, user, and entrypoint.
* Use ``docker stats`` for CPU and memory symptoms.
* Debug networking from a container on the same network.
* Use ``docker debug`` for slim images that do not include shells.
* Write logs to stdout and stderr.

References
----------

* `docker debug <https://docs.docker.com/reference/cli/docker/debug/>`_
* `docker logs <https://docs.docker.com/reference/cli/docker/container/logs/>`_
* `Configure logging drivers <https://docs.docker.com/engine/logging/configure/>`_
* `docker inspect <https://docs.docker.com/reference/cli/docker/inspect/>`_
