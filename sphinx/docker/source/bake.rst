Build Bake
==========

``docker buildx bake`` is the standard way to describe repeatable builds as code. Use it when command lines become long, when multiple images share settings, or when CI needs the same build targets as local development.

Bake can read ``docker-bake.hcl``, Compose files, and JSON files. The HCL format is the most readable for build targets.

Why Bake
--------

Use Bake when a project needs any of these:

* Several images built from one repository.
* Multi-platform release images.
* Shared tags, labels, cache settings, SBOM, and provenance settings.
* Local, test, and release build targets.
* CI builds that should not duplicate shell scripts.

Basic file
----------

Create ``docker-bake.hcl`` at the project root.

.. code-block:: text
    :linenos:

    variable "REGISTRY" {
      default = "registry.example.com/team"
    }

    variable "TAG" {
      default = "dev"
    }

    group "default" {
      targets = ["api"]
    }

    target "api" {
      context = "."
      dockerfile = "Dockerfile"
      tags = ["${REGISTRY}/api:${TAG}"]
    }

List the targets.

.. code-block:: bash
    :linenos:

    docker buildx bake --list

Build the default group.

.. code-block:: bash
    :linenos:

    docker buildx bake

Override variables from the shell.

.. code-block:: bash
    :linenos:

    TAG="$(git rev-parse --short HEAD)" docker buildx bake

Multi-platform release target
-----------------------------

Keep local and release behavior separate. Local targets usually load one image into the local Docker image store. Release targets usually push multi-platform images to a registry.

.. code-block:: text
    :linenos:

    variable "REGISTRY" {
      default = "registry.example.com/team"
    }

    variable "TAG" {
      default = "dev"
    }

    target "api-local" {
      context = "."
      dockerfile = "Dockerfile"
      tags = ["api:local"]
      output = ["type=docker"]
    }

    target "api-release" {
      context = "."
      dockerfile = "Dockerfile"
      platforms = ["linux/amd64", "linux/arm64"]
      tags = [
        "${REGISTRY}/api:${TAG}",
        "${REGISTRY}/api:latest"
      ]
      cache-from = ["type=registry,ref=${REGISTRY}/api:buildcache"]
      cache-to = ["type=registry,ref=${REGISTRY}/api:buildcache,mode=max"]
      attest = [
        "type=sbom",
        "type=provenance"
      ]
      output = ["type=registry"]
    }

Build locally.

.. code-block:: bash
    :linenos:

    docker buildx bake api-local

Build and push the release image.

.. code-block:: bash
    :linenos:

    TAG="$(git rev-parse --short HEAD)" docker buildx bake api-release

Multiple services
-----------------

Bake shines when a repository contains several services.

.. code-block:: text
    :linenos:

    variable "REGISTRY" {
      default = "registry.example.com/team"
    }

    variable "TAG" {
      default = "dev"
    }

    target "_common" {
      platforms = ["linux/amd64", "linux/arm64"]
      cache-from = ["type=registry,ref=${REGISTRY}/buildcache"]
      cache-to = ["type=registry,ref=${REGISTRY}/buildcache,mode=max"]
    }

    target "api" {
      inherits = ["_common"]
      context = "./services/api"
      tags = ["${REGISTRY}/api:${TAG}"]
    }

    target "worker" {
      inherits = ["_common"]
      context = "./services/worker"
      tags = ["${REGISTRY}/worker:${TAG}"]
    }

    group "release" {
      targets = ["api", "worker"]
    }

Run the group.

.. code-block:: bash
    :linenos:

    TAG="$(git rev-parse --short HEAD)" docker buildx bake release --push

CI pattern
----------

In CI, keep the policy in ``docker-bake.hcl`` and let the workflow supply variables.

.. code-block:: bash
    :linenos:

    set -euo pipefail

    docker buildx create --name ci-builder --driver docker-container --use
    docker buildx inspect --bootstrap
    docker buildx bake --list
    TAG="${GIT_SHA}" docker buildx bake release --push

Use the same target names locally and in CI. The less custom shell logic in CI, the easier it is to reproduce a release build.

Practical rules
---------------

* Put shared cache, platform, label, and attestation settings in inherited targets.
* Keep local targets separate from release targets.
* Prefer registry output for multi-platform images.
* Use immutable commit tags for releases.
* Use ``latest`` only as a convenience pointer, not as the deployment record.
* Keep Compose responsible for running services and Bake responsible for building images.

References
----------

* `Docker Build Bake <https://docs.docker.com/build/bake/>`_
* `Bake file reference <https://docs.docker.com/build/bake/reference/>`_
* `docker buildx bake reference <https://docs.docker.com/reference/cli/docker/buildx/bake/>`_
