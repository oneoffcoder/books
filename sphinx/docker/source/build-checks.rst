Build Checks
============

Docker build checks analyze Dockerfiles before spending time on a full build. Use them as a fast lint step in local development and CI.

Run all default checks against the current directory.

.. code-block:: bash
    :linenos:

    docker build --check .

The same check mode is available through Buildx.

.. code-block:: bash
    :linenos:

    docker buildx build --check .

Treat warnings as failures in CI so Dockerfile problems do not drift into the main branch.

.. code-block:: bash
    :linenos:

    docker build --check .
    docker buildx build --check .

Common failures
---------------

Build checks are useful because they catch mistakes that are syntactically valid but operationally weak.

* ``UndefinedArgInFrom`` catches a ``FROM`` instruction that uses an ``ARG`` that was not defined before it.
* ``SecretsUsedInArgOrEnv`` catches secrets passed through build arguments or environment variables.
* ``JSONArgsRecommended`` catches shell-form ``CMD`` or ``ENTRYPOINT`` instructions where signal handling can be surprising.
* ``StageNameCasing`` and ``ReservedStageName`` catch confusing multi-stage build names.

The right response is usually to make the Dockerfile more explicit. For example, prefer JSON-form commands.

.. code-block:: docker
    :linenos:

    CMD ["python", "app.py"]

Prefer BuildKit secrets over build arguments for credentials.

.. code-block:: docker
    :linenos:

    RUN --mount=type=secret,id=npm_token \
        npm config set //registry.npmjs.org/:_authToken="$(cat /run/secrets/npm_token)"

Policy in the Dockerfile
------------------------

When a repository wants checks to be strict everywhere, put a check directive near the top of the Dockerfile.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    # check=error=true
    FROM python:3-slim

Specific checks can be skipped when there is a documented reason.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    # check=skip=JSONArgsRecommended

Use skips sparingly. A skipped check should be reviewed like any other policy exception.

CI example
----------

Run checks before the expensive build and push step.

.. code-block:: bash
    :linenos:

    set -euo pipefail

    docker build --check .
    docker buildx build \
        --cache-from type=registry,ref="${IMAGE}:buildcache" \
        --cache-to type=registry,ref="${IMAGE}:buildcache",mode=max \
        -t "${IMAGE}:${GIT_SHA}" \
        --push .

References
----------

* `Docker build checks <https://docs.docker.com/reference/build-checks/>`_
* `Build check rules <https://docs.docker.com/reference/build-checks/>`_
