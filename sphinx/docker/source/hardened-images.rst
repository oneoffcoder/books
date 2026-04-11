Hardened and Minimal Images
===========================

Image hardening starts with the base image. A hardened application image has fewer packages, fewer shells and utilities, signed metadata, a known build process, and a smaller patch surface.

Minimal image choices
---------------------

There are several common base-image styles.

.. list-table:: Base image choices
   :widths: 25 40 35
   :header-rows: 1

   * - Choice
     - Use it when
     - Tradeoff
   * - Full distribution
     - You need many operating system tools or are still discovering dependencies.
     - Larger attack surface and more CVE noise.
   * - Slim distribution
     - You need compatibility with a familiar distribution but not every package.
     - Still includes more than a pure runtime needs.
   * - Alpine-style image
     - The stack works with ``musl`` libc and small packages.
     - Some language runtimes and native libraries expect ``glibc``.
   * - Distroless image
     - The application needs only runtime libraries and no shell or package manager.
     - Debugging must use external tools such as ``docker debug``.
   * - Docker Hardened Image
     - The organization wants maintained, minimal, signed, compliance-ready base images.
     - Availability and access depend on Docker's product offering.

Migration path
--------------

Start with the current official image when learning or prototyping.

.. code-block:: docker
    :linenos:

    FROM python:3-slim

Move build tools into a separate stage.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    FROM python:3-slim AS build
    WORKDIR /src
    COPY requirements.txt .
    RUN --mount=type=cache,target=/root/.cache/pip \
        pip wheel --wheel-dir /wheels -r requirements.txt

    FROM python:3-slim AS runtime
    WORKDIR /app
    COPY --from=build /wheels /wheels
    RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels
    COPY . .
    CMD ["python", "app.py"]

Then move to a more minimal or hardened runtime base when the dependency set is understood. Re-test native extensions, TLS certificates, timezone data, DNS behavior, and shell-dependent startup scripts.

glibc versus musl
-----------------

The libc choice matters.

* Debian, Ubuntu, and many slim images use ``glibc``.
* Alpine uses ``musl``.
* Many Python wheels, Node native modules, database clients, and vendor SDKs are tested first against ``glibc``.
* Alpine can be excellent for small static binaries, but it is not automatically the safest or fastest option for every stack.

Distroless runtime pattern
--------------------------

Distroless images intentionally omit shells and package managers. That is the point. The runtime image should contain the application and the libraries needed to run it.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    FROM golang:alpine AS build
    WORKDIR /src
    COPY . .
    RUN go build -o /out/server ./cmd/server

    FROM gcr.io/distroless/static-debian12
    COPY --from=build /out/server /server
    USER 65532:65532
    ENTRYPOINT ["/server"]

Debugging minimal images
------------------------

Do not add ``bash``, ``curl``, ``vim``, or ``sudo`` back into the runtime image just to make debugging easier. Use external debugging tools, sidecar diagnostics, test images, or ``docker debug``.

.. code-block:: bash
    :linenos:

    docker debug api
    docker logs api
    docker inspect api

Release requirements
--------------------

A hardened-image release should provide:

* A pinned base image or digest.
* SBOM for the final image.
* Provenance attestation for the build.
* Vulnerability scan result.
* Clear ownership for remediation.
* A rebuild policy for base-image updates.
* Runtime proof that the image runs without root.

Practical rules
---------------

* Use slim or hardened bases for runtime stages.
* Keep package managers and compilers out of runtime images.
* Choose ``glibc`` or ``musl`` based on dependency compatibility, not image size alone.
* Use distroless only when the application and operations model are ready for no-shell debugging.
* Prefer signed SBOM, provenance, and digest-pinned releases for production.

References
----------

* `Docker Hardened Images <https://docs.docker.com/dhi/>`_
* `What are Docker Hardened Images? <https://docs.docker.com/dhi/explore/what/>`_
* `Distroless images <https://docs.docker.com/dhi/core-concepts/distroless/>`_
* `glibc and musl <https://docs.docker.com/dhi/core-concepts/glibc-musl/>`_
