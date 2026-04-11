Dev Containers
==============

A development container defines a repeatable coding environment. It is different from a production image: development containers contain tools for editing, testing, debugging, and local workflow, while production images should contain only what the application needs to run.

The Dev Container Specification uses ``.devcontainer/devcontainer.json`` as structured metadata that tools can read.

Single-container example
------------------------

Create ``.devcontainer/devcontainer.json``.

.. code-block:: json
    :linenos:

    {
      "name": "python-api",
      "build": {
        "dockerfile": "Dockerfile",
        "context": "..",
        "target": "development"
      },
      "workspaceFolder": "/workspace",
      "remoteUser": "app",
      "forwardPorts": [8000],
      "postCreateCommand": "pip install -r requirements-dev.txt"
    }

Use a development target in the Dockerfile.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    FROM python:3-slim AS base
    RUN useradd --uid 10001 --create-home app
    WORKDIR /workspace

    FROM base AS development
    RUN apt-get update -y && \
        apt-get install --no-install-recommends git curl -y && \
        rm -rf /var/lib/apt/lists/*
    USER app

    FROM base AS runtime
    COPY --chown=app:app . .
    USER app
    CMD ["python", "app.py"]

Compose-based example
---------------------

Use Compose when the coding environment needs databases, queues, or other services.

.. code-block:: json
    :linenos:

    {
      "name": "api-stack",
      "dockerComposeFile": "../compose.yaml",
      "service": "api",
      "runServices": ["api", "db"],
      "workspaceFolder": "/workspace",
      "remoteUser": "app",
      "shutdownAction": "stopCompose"
    }

The Compose file owns the service topology. The devcontainer file tells development tools which service is the workspace.

Users
-----

Use ``remoteUser`` for tools and terminals. Use ``containerUser`` only when every process in the dev container should run as that user. On Linux, the spec can update the remote user's UID/GID to reduce bind-mount permission problems.

Do not rely on root as the default development user. A development environment that only works as root hides problems that production will later expose.

Features
--------

Dev Container Features install common tools in a reusable way.

.. code-block:: json
    :linenos:

    {
      "features": {
        "ghcr.io/devcontainers/features/github-cli": {},
        "ghcr.io/devcontainers/features/node": {
          "version": "lts"
        }
      }
    }

Use features for development tools. Do not copy those tools into the production image unless the application truly needs them at runtime.

CI reuse
--------

The same development container can be used in CI for linting, tests, and docs builds. Keep the CI command explicit.

.. code-block:: bash
    :linenos:

    devcontainer up --workspace-folder .
    devcontainer exec --workspace-folder . pytest

Practical rules
---------------

* Keep development and production targets separate.
* Use Compose for multi-service development environments.
* Use non-root users to catch permission problems early.
* Keep secrets out of ``devcontainer.json``.
* Install editor and debug tools in development targets or features, not runtime images.
* Document forwarded ports and post-create commands.

References
----------

* `Dev Container overview <https://containers.dev/overview>`_
* `devcontainer.json reference <https://containers.dev/implementors/json_reference/>`_
* `Dev Container features <https://containers.dev/features>`_
