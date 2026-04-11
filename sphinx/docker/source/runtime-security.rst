Runtime Security
================

Image hardening controls what goes into an image. Runtime security controls what the container is allowed to do after it starts.

Default posture
---------------

Start with this posture for ordinary application containers:

* Run as a non-root user.
* Drop Linux capabilities.
* Prevent privilege escalation.
* Use a read-only root filesystem.
* Write only to declared volumes or tmpfs mounts.
* Keep Docker's default seccomp profile enabled.
* Avoid privileged containers.
* Avoid mounting the Docker socket.

Compose example
---------------

.. code-block:: yaml
    :linenos:

    services:
      api:
        image: registry.example.com/team/api:latest
        user: "10001:10001"
        read_only: true
        tmpfs:
          - /tmp
        cap_drop:
          - ALL
        security_opt:
          - no-new-privileges:true

Kubernetes example
------------------

.. code-block:: yaml
    :linenos:

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: api
    spec:
      template:
        spec:
          securityContext:
            runAsNonRoot: true
            runAsUser: 10001
            runAsGroup: 10001
            fsGroup: 10001
          containers:
            - name: api
              image: registry.example.com/team/api:latest
              securityContext:
                allowPrivilegeEscalation: false
                readOnlyRootFilesystem: true
                capabilities:
                  drop:
                    - ALL

Capabilities
------------

Linux capabilities split root privileges into smaller permissions. Most application containers need none of them.

Drop all capabilities by default, then add back only what is required and documented.

.. code-block:: bash
    :linenos:

    docker run --rm \
        --cap-drop ALL \
        --security-opt no-new-privileges:true \
        nginx:alpine

If a workload asks for ``--privileged``, treat it as a design review. ``--privileged`` gives broad host-level access and disables many isolation controls.

seccomp
-------

Docker's default seccomp profile blocks many sensitive system calls while keeping broad application compatibility. Keep it enabled unless there is a specific, reviewed reason to override it.

Use a custom seccomp profile only when the application needs a known syscall and the profile can be reviewed.

.. code-block:: bash
    :linenos:

    docker run --rm \
        --security-opt seccomp=/path/to/seccomp/profile.json \
        app:local

Avoid ``seccomp=unconfined`` in production.

AppArmor and SELinux
--------------------

AppArmor and SELinux are Linux security modules that can enforce host-level access policies around containers. Use the platform's default container policy where available, then add custom policy only when the workload requires it.

Examples of policy-controlled operations include filesystem paths, process behavior, and some network access patterns.

User namespaces and rootless Docker
-----------------------------------

User namespaces map container users to different host users. Rootless Docker runs the Docker daemon and containers without root privileges on the host. These controls reduce risk from daemon and runtime vulnerabilities.

They do not remove the need for application-level least privilege. A container should still use ``USER``, drop capabilities, and avoid privileged mounts.

Docker socket
-------------

Mounting the Docker socket gives the container control over the Docker daemon.

.. code-block:: bash
    :linenos:

    docker run -v /var/run/docker.sock:/var/run/docker.sock tool:local

Treat this as host-level access. Prefer purpose-built APIs, narrow CI permissions, or remote builders instead of giving a workload the daemon socket.

Decision checklist
------------------

Before a container runs in production, answer these:

* What UID and GID does it run as?
* Which directories are writable?
* Which Linux capabilities remain?
* Does it need privilege escalation?
* Does it use Docker's default seccomp profile?
* Does it mount the Docker socket?
* Does it need host networking, host PID, or privileged mode?
* How will operators debug it without adding tools to the runtime image?

References
----------

* `Docker Engine security <https://docs.docker.com/engine/security/>`_
* `Rootless mode <https://docs.docker.com/engine/security/rootless/>`_
* `Seccomp security profiles <https://docs.docker.com/engine/security/seccomp/>`_
* `AppArmor profiles <https://docs.docker.com/engine/security/apparmor/>`_
* `User namespace isolation <https://docs.docker.com/engine/security/userns-remap/>`_
