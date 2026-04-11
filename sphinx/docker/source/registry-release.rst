Registry and Release Workflow
=============================

A registry is not just a place to push images. It is part of the release system. A good workflow makes every deployed image traceable, immutable, scannable, and easy to roll back.

Name images consistently
------------------------

Use a stable repository name and clear tags.

.. code-block:: text
    :linenos:

    registry.example.com/team/api:<git-sha>
    registry.example.com/team/api:1.4.2
    registry.example.com/team/api:main
    registry.example.com/team/api:latest

Use immutable tags for release records.

* Commit SHA tags are good deployment records.
* Semantic version tags are good human release records.
* Branch tags are convenient for development environments.
* ``latest`` is only a moving convenience pointer.

Tag and push
------------

Build and push with Buildx.

.. code-block:: bash
    :linenos:

    export IMAGE=registry.example.com/team/api
    export GIT_SHA="$(git rev-parse --short HEAD)"

    docker buildx build \
        --platform linux/amd64,linux/arm64 \
        -t "${IMAGE}:${GIT_SHA}" \
        -t "${IMAGE}:latest" \
        --push .

Record the digest
-----------------

Deployments should record the digest, not just the tag.

.. code-block:: bash
    :linenos:

    docker buildx imagetools inspect "${IMAGE}:${GIT_SHA}"

The digest form is the immutable artifact reference.

.. code-block:: text
    :linenos:

    registry.example.com/team/api@sha256:<digest>

Promotion
---------

Promote the same image between environments. Do not rebuild separately for staging and production unless the build inputs are intentionally different.

.. code-block:: text
    :linenos:

    build once -> scan -> deploy to dev -> deploy same digest to staging -> deploy same digest to production

Promotion can be implemented by updating deployment manifests to point at the same digest or by copying the image into environment-specific repositories.

Cache tags
----------

BuildKit registry cache tags are not release tags. Keep them separate and expire them aggressively.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --cache-from type=registry,ref="${IMAGE}:buildcache" \
        --cache-to type=registry,ref="${IMAGE}:buildcache",mode=max \
        -t "${IMAGE}:${GIT_SHA}" \
        --push .

Registry policy
---------------

Use registry controls that match the risk of the environment.

* Authenticate every push.
* Restrict push access to CI or release automation.
* Make production tags immutable.
* Scan images on push and rescan when vulnerability data changes.
* Retain release tags and digests longer than branch and cache tags.
* Separate development and production repositories or accounts when access boundaries matter.
* Keep SBOM and provenance attestations with release images.

Rollback
--------

Rollback by digest when possible.

.. code-block:: text
    :linenos:

    registry.example.com/team/api@sha256:<previous-digest>

This avoids the ambiguity of a mutable tag. The deployment history should answer these questions quickly:

* Which digest is running?
* Which source commit created that digest?
* Which Dockerfile and build target created it?
* Which SBOM, scan report, and provenance attestation belong to it?
* Which previous digest is known-good?

CI example
----------

.. code-block:: bash
    :linenos:

    set -euo pipefail

    IMAGE="registry.example.com/team/api"
    GIT_SHA="$(git rev-parse --short HEAD)"

    docker buildx build \
        --platform linux/amd64,linux/arm64 \
        --cache-from type=registry,ref="${IMAGE}:buildcache" \
        --cache-to type=registry,ref="${IMAGE}:buildcache",mode=max \
        --sbom=true \
        --provenance=true \
        -t "${IMAGE}:${GIT_SHA}" \
        --push .

    docker buildx imagetools inspect "${IMAGE}:${GIT_SHA}"

Practical rules
---------------

* Build once and promote the same digest.
* Treat ``latest`` as optional metadata, not the deployment source of truth.
* Keep cache tags separate from release tags.
* Use immutable release tags.
* Store release metadata with the deployment.
* Prefer digest references for production rollback.

References
----------

* `docker image tag <https://docs.docker.com/reference/cli/docker/image/tag/>`_
* `docker image push <https://docs.docker.com/reference/cli/docker/image/push/>`_
* `Registry cache backend <https://docs.docker.com/build/cache/backends/registry/>`_
* `Docker tags and labels in CI <https://docs.docker.com/build/ci/github-actions/manage-tags-labels/>`_
