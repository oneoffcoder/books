Networking
==========

Docker networking controls how containers talk to each other, the host, and the outside world. Most application problems show up as one of three symptoms: DNS does not resolve, a port is not published, or traffic is going to the wrong network.

Default rule
------------

Use a user-defined bridge network for local multi-container applications. Containers on the same user-defined bridge network can resolve each other by service or container name.

.. code-block:: bash
    :linenos:

    docker network create appnet
    docker run -d --name db --network appnet mysql:latest
    docker run --rm --network appnet alpine:latest getent hosts db

Compose creates a project network automatically, so services can usually talk to each other by service name.

.. code-block:: yaml
    :linenos:

    services:
      api:
        image: api:local
        depends_on:
          - db
      db:
        image: mysql:latest

The ``api`` container connects to the database host named ``db``.

Published ports
---------------

Publishing a port makes a container port reachable from the host.

.. code-block:: bash
    :linenos:

    docker run --rm -p 8080:80 nginx:alpine

The left side is the host port. The right side is the container port. In the example, open ``http://localhost:8080`` on the host.

Compose uses the same mapping.

.. code-block:: yaml
    :linenos:

    services:
      web:
        image: nginx:alpine
        ports:
          - "8080:80"

Expose versus publish
---------------------

``EXPOSE`` in a Dockerfile is documentation and metadata. It does not publish the port to the host. Use ``-p`` or Compose ``ports`` when the host must connect to the container.

Host access
-----------

Containers can reach the host differently depending on the platform.

* Docker Desktop provides ``host.docker.internal``.
* Linux Docker Engine can add the host gateway explicitly.

.. code-block:: bash
    :linenos:

    docker run --rm \
        --add-host=host.docker.internal:host-gateway \
        alpine:latest ping -c 1 host.docker.internal

Use host access sparingly. A containerized dependency is usually easier to reproduce than a dependency running directly on a developer laptop.

Host network mode
-----------------

Host network mode removes Docker's network namespace isolation for that container.

.. code-block:: bash
    :linenos:

    docker run --rm --network host nginx:alpine

This can be useful for diagnostics or high-performance network appliances on Linux. It is not the default application pattern because it bypasses normal port publishing and increases coupling to the host.

Internal networks
-----------------

Use internal networks for services that should not be reachable from outside the Compose project.

.. code-block:: yaml
    :linenos:

    services:
      api:
        image: api:local
        networks:
          - frontend
          - backend
      db:
        image: mysql:latest
        networks:
          - backend

    networks:
      frontend:
      backend:
        internal: true

Debugging
---------

Start with these commands.

.. code-block:: bash
    :linenos:

    docker network ls
    docker network inspect appnet
    docker container inspect api
    docker port api
    docker exec -it api sh

Inside a debugging shell, check DNS and ports.

.. code-block:: bash
    :linenos:

    getent hosts db
    nc -vz db 3306
    wget -S -O - http://api:8080/health

Practical rules
---------------

* Use user-defined bridge networks.
* Connect containers by DNS name, not by container IP address.
* Publish only the ports that humans or external systems need.
* Do not use host network mode unless the workload truly needs it.
* Separate frontend and backend networks when the topology matters.
* Debug from inside a container on the same network.

References
----------

* `Docker networking <https://docs.docker.com/engine/network/>`_
* `Bridge network driver <https://docs.docker.com/engine/network/drivers/bridge/>`_
* `Docker Desktop networking <https://docs.docker.com/desktop/features/networking/>`_
