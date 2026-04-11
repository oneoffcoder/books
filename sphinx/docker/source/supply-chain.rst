Supply Chain Security
=====================

Docker images are software supply-chain artifacts. Treat each release image as something that should be traceable, inspectable, and rebuildable.

Scan images
-----------

Docker Scout can summarize vulnerabilities, base-image age, and upgrade recommendations.

.. code-block:: bash
    :linenos:

    docker scout quickview registry.example.com/team/app:1.0.0
    docker scout cves registry.example.com/team/app:1.0.0
    docker scout recommendations registry.example.com/team/app:1.0.0

In CI, run scans after the image is built and before deployment. Use policy gates for release branches so high-severity findings require an explicit decision.

Generate an SBOM
----------------

A software bill of materials lists the packages in an image. Keep the SBOM with the release metadata so incident response can quickly answer "are we affected?" questions.

.. code-block:: bash
    :linenos:

    docker scout sbom registry.example.com/team/app:1.0.0 --format spdx > sbom.spdx.json

Build attestations
------------------

Buildx can attach SBOM and provenance attestations when pushing an image. Provenance records how the image was built. SBOM records what went into it.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --platform linux/amd64,linux/arm64 \
        --sbom=true \
        --provenance=true \
        -t registry.example.com/team/app:1.0.0 \
        --push .

Registry and deployment tooling must preserve OCI attestations for the data to remain useful. Verify the target registry and promotion process before relying on attestations as a release control.

Pin what you deploy
-------------------

Tags are convenient labels, but they can move. Production systems should record the image digest that was deployed.

.. code-block:: bash
    :linenos:

    docker buildx imagetools inspect registry.example.com/team/app:1.0.0

A deployment can then reference the digest form.

.. code-block:: text
    :linenos:

    registry.example.com/team/app@sha256:<digest>

Protect the registry
--------------------

Use registry controls that match the environment.

* Require authentication for push and pull operations.
* Make release tags immutable.
* Scan on push, and rescan on a schedule when the registry supports it.
* Use lifecycle policies for old build-cache and feature-branch images.
* Separate development, staging, and production repositories or accounts.

Release checklist
-----------------

* Build with BuildKit.
* Run Docker build checks.
* Scan the image.
* Generate an SBOM.
* Attach provenance for release images.
* Record the deployed digest.
* Keep the Dockerfile, build logs, SBOM, and deployment manifest together.

References
----------

* `Docker Scout <https://docs.docker.com/scout/>`_
* `Docker Scout attestations <https://docs.docker.com/guides/docker-scout/attestations/>`_
* `Build attestations <https://docs.docker.com/build/metadata/attestations/>`_
