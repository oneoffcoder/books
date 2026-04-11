Storage
========

Container filesystems are disposable. Store important state in volumes, bind mounts, external services, or object storage.

Storage choices
---------------

.. list-table:: Docker storage choices
   :widths: 25 40 35
   :header-rows: 1

   * - Storage
     - Use it for
     - Watch out for
   * - Image filesystem
     - Files baked into the image.
     - Changes disappear when the container is removed.
   * - Named volume
     - Database data, caches, local persistent state.
     - Ownership must match the runtime user.
   * - Bind mount
     - Source code and host-controlled files.
     - Host path layout and OS behavior leak into the container.
   * - tmpfs
     - Temporary sensitive or high-churn files.
     - Data disappears when the container stops.

Named volumes
-------------

Use named volumes for container-owned persistent state.

.. code-block:: bash
    :linenos:

    docker volume create db_data
    docker run -d \
        --name db \
        -e MYSQL_ROOT_PASSWORD=change-me \
        -v db_data:/var/lib/mysql \
        mysql:latest

Compose example:

.. code-block:: yaml
    :linenos:

    services:
      db:
        image: mysql:latest
        volumes:
          - db_data:/var/lib/mysql

    volumes:
      db_data:

Bind mounts
-----------

Use bind mounts when the host owns the files, such as local source code.

.. code-block:: bash
    :linenos:

    docker run --rm \
        --mount type=bind,source="$(pwd)",target=/workspace,readonly \
        alpine:latest ls /workspace

Prefer ``--mount`` over short ``-v`` syntax for scripts because it is explicit.

Compose example:

.. code-block:: yaml
    :linenos:

    services:
      docs:
        image: python:3-slim
        working_dir: /workspace
        volumes:
          - type: bind
            source: .
            target: /workspace
            read_only: true

tmpfs mounts
------------

Use tmpfs for temporary files that should not be written to disk.

.. code-block:: bash
    :linenos:

    docker run --rm \
        --tmpfs /run/secrets:rw,noexec,nosuid,size=1m \
        alpine:latest sh

Compose example:

.. code-block:: yaml
    :linenos:

    services:
      api:
        image: api:local
        tmpfs:
          - /tmp

Non-root ownership
------------------

Non-root containers need writable mounts owned by the runtime UID or GID. Do not solve ownership failures by running as root.

For files copied into the image, set ownership during the build.

.. code-block:: docker
    :linenos:

    RUN useradd --uid 10001 --create-home app
    WORKDIR /app
    COPY --chown=10001:10001 . .
    USER 10001:10001

For Kubernetes volumes, use ``fsGroup`` when the workload needs group write access.

.. code-block:: yaml
    :linenos:

    securityContext:
      runAsNonRoot: true
      runAsUser: 10001
      runAsGroup: 10001
      fsGroup: 10001

Back up a volume
----------------

Back up a named volume by mounting it into a one-off container.

.. code-block:: bash
    :linenos:

    docker run --rm \
        -v db_data:/data:ro \
        -v "$(pwd)":/backup \
        alpine:latest \
        tar czf /backup/db_data.tgz -C /data .

Restore into a new volume.

.. code-block:: bash
    :linenos:

    docker volume create db_data_restore
    docker run --rm \
        -v db_data_restore:/data \
        -v "$(pwd)":/backup \
        alpine:latest \
        tar xzf /backup/db_data.tgz -C /data

Practical rules
---------------

* Treat the image filesystem as read-only application code.
* Use named volumes for container-owned state.
* Use bind mounts for host-owned source files.
* Use read-only mounts by default.
* Put temporary writes in ``/tmp`` or an explicit tmpfs mount.
* Back up named volumes before destructive changes.
* Fix UID/GID ownership rather than running the container as root.

References
----------

* `Docker storage <https://docs.docker.com/engine/storage/>`_
* `Volumes <https://docs.docker.com/engine/storage/volumes/>`_
* `Bind mounts <https://docs.docker.com/engine/storage/bind-mounts/>`_
* `tmpfs mounts <https://docs.docker.com/engine/storage/tmpfs/>`_
