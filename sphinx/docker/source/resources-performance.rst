Resources and Performance
=========================

Containers share host CPU, memory, disk, and network resources. Without limits, a container can consume as much as the host scheduler allows. Production containers should have measured resource requests and limits.

Memory limits
-------------

Set a hard memory limit for workloads that can spike or leak.

.. code-block:: bash
    :linenos:

    docker run --rm \
        --memory 512m \
        --memory-swap 512m \
        api:local

When ``--memory`` and ``--memory-swap`` are equal, the container cannot use swap. This is useful for latency-sensitive workloads where swapping is worse than a clean failure.

Avoid disabling the OOM killer unless a memory limit is also set. If the host runs out of memory, the kernel can kill important host processes.

CPU limits
----------

Limit CPU with ``--cpus``.

.. code-block:: bash
    :linenos:

    docker run --rm --cpus 1.5 api:local

For relative scheduling weight, use CPU shares.

.. code-block:: bash
    :linenos:

    docker run --rm --cpu-shares 512 worker:local

Compose resources
-----------------

Compose can describe resource expectations. The exact enforcement depends on the runtime mode and platform.

.. code-block:: yaml
    :linenos:

    services:
      api:
        image: api:local
        deploy:
          resources:
            limits:
              cpus: "1.0"
              memory: 512M
            reservations:
              cpus: "0.25"
              memory: 128M

Kubernetes resources
--------------------

Kubernetes separates requests from limits. Requests affect scheduling. Limits cap usage.

.. code-block:: yaml
    :linenos:

    resources:
      requests:
        cpu: 250m
        memory: 128Mi
      limits:
        cpu: 1000m
        memory: 512Mi

Measure first
-------------

Use runtime metrics before guessing limits.

.. code-block:: bash
    :linenos:

    docker stats
    docker stats api

Inside the container, remember that some tools report host-level values. Validate behavior with load tests and runtime metrics from the platform.

Image performance
-----------------

Image size affects pull time, deployment speed, storage use, and vulnerability noise.

Improve image performance with:

* A tight ``.dockerignore`` file.
* Multi-stage builds.
* Cache mounts for dependency managers.
* Smaller runtime bases.
* Avoiding package-manager caches in final layers.
* Grouping commands so cleanup happens in the same layer.
* Pushing multi-platform images only for platforms that are actually deployed.

Startup performance
-------------------

Slow container startup usually comes from one of these:

* The image pull is large.
* The entrypoint runs migrations or dependency installation.
* The application waits on an unavailable dependency.
* Health checks have long grace periods.
* The process performs cold compilation or model loading.

Keep containers ready to run. Install dependencies during the image build, not at container startup.

Cost control
------------

Resource limits are also cost controls.

* Right-size memory to avoid over-provisioned nodes.
* Use ARM64 images when the workload performs well on cheaper ARM capacity.
* Keep build caches separate from release images and expire them.
* Use native builders for expensive cross-architecture compilation.
* Remove stale volumes, images, and caches on shared hosts.

Practical checklist
-------------------

* Load test before setting production limits.
* Set memory limits for services.
* Use CPU limits or scheduling policy for noisy workloads.
* Keep dependency installation out of startup.
* Keep final images small.
* Watch pull time, startup time, memory high-water marks, and restart counts.

References
----------

* `Docker resource constraints <https://docs.docker.com/engine/containers/resource_constraints/>`_
* `Runtime metrics <https://docs.docker.com/engine/containers/runmetrics/>`_
* `Docker stats <https://docs.docker.com/reference/cli/docker/container/stats/>`_
* `Dockerfile best practices <https://docs.docker.com/build/building/best-practices/>`_
