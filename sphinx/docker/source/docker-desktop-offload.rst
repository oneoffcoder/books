Docker Desktop, Offload, and Remote Builders
============================================

Docker can build and run locally, on remote hosts, or in managed cloud builders. Choose the environment based on what is slow or unsupported on the developer machine.

Docker contexts
---------------

A Docker context stores the endpoint and TLS settings for a Docker API target.

.. code-block:: bash
    :linenos:

    docker context ls
    docker context create remote-amd64 --docker host=ssh://builder-amd64
    docker context use remote-amd64
    docker ps

Switch back to the local engine.

.. code-block:: bash
    :linenos:

    docker context use default

Use contexts carefully in scripts. Print the active context before destructive commands.

.. code-block:: bash
    :linenos:

    docker context show

Remote Buildx builders
----------------------

Buildx can use remote contexts as builder nodes.

.. code-block:: bash
    :linenos:

    docker context create node-amd64 --docker host=ssh://builder-amd64
    docker context create node-arm64 --docker host=ssh://builder-arm64

    docker buildx create --name remote-builder node-amd64 --use
    docker buildx create --name remote-builder --append node-arm64
    docker buildx inspect --bootstrap

This pattern is useful when laptop builds are slow, when Apple Silicon emulation is fragile, or when CI needs native ARM64 and AMD64 output.

Docker Build Cloud
------------------

Docker Build Cloud provides managed builders with shared cache. Use it when the organization wants native multi-platform builders without maintaining its own build hosts.

The workflow still uses Buildx.

.. code-block:: bash
    :linenos:

    docker buildx ls
    docker buildx use <cloud-builder-name>
    docker buildx build \
        --platform linux/amd64,linux/arm64 \
        -t registry.example.com/team/api:latest \
        --push .

Docker Offload
--------------

Docker Offload is a managed Docker service that offloads building and running containers to the cloud while keeping familiar Docker commands. It is useful for virtual desktop environments, machines that cannot run nested virtualization, and local machines that do not have enough CPU, memory, or disk for the workload.

Use Offload for development convenience. For releases, keep the build policy in Buildx or Bake so the same release process works locally, in CI, or in managed builders.

Decision guide
--------------

.. list-table:: Builder choices
   :widths: 25 40 35
   :header-rows: 1

   * - Option
     - Use it when
     - Tradeoff
   * - Local Docker Desktop
     - Small projects, quick local feedback, Compose development.
     - Limited by laptop CPU, memory, disk, and architecture.
   * - Remote Docker context
     - You control a bigger host or native architecture node.
     - You operate and secure that host.
   * - Multi-node Buildx builder
     - You need native AMD64 and ARM64 builds.
     - Builder lifecycle and cache require management.
   * - Docker Build Cloud
     - You want managed native builders and shared cache.
     - Product availability and subscription requirements apply.
   * - Docker Offload
     - You need Docker workflows from constrained desktop environments.
     - Development-focused; release policy should still be explicit.

Security notes
--------------

Remote builders are part of the supply chain.

* Restrict who can use them.
* Protect SSH keys and Docker API endpoints.
* Keep build cache access scoped.
* Do not leak secrets into build logs or layers.
* Use BuildKit secrets for credentials.
* Attach provenance for release builds.

References
----------

* `Docker contexts <https://docs.docker.com/engine/manage-resources/contexts/>`_
* `Build drivers <https://docs.docker.com/build/builders/drivers/>`_
* `Docker Build Cloud <https://docs.docker.com/build-cloud/>`_
* `Docker Offload <https://docs.docker.com/offload/>`_
