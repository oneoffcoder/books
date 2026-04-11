Compose Watch
=============

``docker compose watch`` turns Compose into a development loop. Instead of rebuilding manually after every code change, Compose watches files and runs the action declared for each service.

Use watch for local development. Use ordinary image builds for CI and releases.

Watch actions
-------------

Compose watch supports these common actions:

* ``sync`` copies changed files into the running container.
* ``rebuild`` rebuilds the service image and recreates the container.
* ``sync+restart`` copies changed files and restarts the container.

The right action depends on the application.

.. list-table:: Watch action choices
   :widths: 25 40 35
   :header-rows: 1

   * - Action
     - Use it for
     - Avoid it when
   * - ``sync``
     - Interpreted source files, templates, static assets.
     - Dependency files changed.
   * - ``rebuild``
     - ``package.json``, ``requirements.txt``, system package changes, generated native extensions.
     - Fast source-only feedback loops.
   * - ``sync+restart``
     - Configuration or source files that are read only at process startup.
     - The application already reloads itself.

Python example
--------------

This Compose file syncs source changes and rebuilds when dependencies change.

.. code-block:: yaml
    :linenos:

    services:
      api:
        build: ./api
        ports:
          - "8000:8000"
        develop:
          watch:
            - action: sync
              path: ./api/app
              target: /app/app
            - action: rebuild
              path: ./api/requirements.txt

Start the watch loop.

.. code-block:: bash
    :linenos:

    docker compose up --watch

Node example
------------

Do not bind-mount ``node_modules`` across macOS and Linux. Native modules and filesystem behavior often differ. Sync source files and rebuild when dependency metadata changes.

.. code-block:: yaml
    :linenos:

    services:
      web:
        build: ./web
        ports:
          - "3000:3000"
        develop:
          watch:
            - action: sync
              path: ./web/src
              target: /app/src
            - action: rebuild
              path: ./web/package.json
            - action: rebuild
              path: ./web/package-lock.json

Watch versus bind mounts
------------------------

Bind mounts are still useful when the container needs a live view of a directory. Watch is often better when:

* The host is macOS or Windows and the container is Linux.
* The application has architecture-specific dependencies.
* The container should own generated files.
* The source tree has large dependency folders.
* You want the same image filesystem layout locally and in CI.

Ignore noisy paths
------------------

Use ``ignore`` to avoid syncing generated files.

.. code-block:: yaml
    :linenos:

    services:
      api:
        build: ./api
        develop:
          watch:
            - action: sync
              path: ./api
              target: /app
              ignore:
                - .venv/
                - __pycache__/
                - .pytest_cache/

Practical rules
---------------

* Watch source files with ``sync``.
* Rebuild when dependency files change.
* Keep package caches and dependency directories inside the container.
* Use ``sync+restart`` when the process does not reload changed files.
* Keep CI on deterministic ``docker buildx build`` or Bake targets.

References
----------

* `Compose Watch <https://docs.docker.com/compose/how-tos/file-watch/>`_
* `Compose Develop Specification <https://docs.docker.com/reference/compose-file/develop/>`_
