AI Containers
=============

Docker's AI tooling focuses on packaging, running, and connecting model-related services with the same container workflow used for other applications. Keep this chapter separate from the core Docker workflow because these features move quickly and are optional for many teams.

Model Runner
------------

Docker Model Runner manages and serves AI models through Docker tooling. It can pull models from Docker Hub, OCI-compatible registries, or Hugging Face, and it can serve models through OpenAI-compatible and Ollama-compatible APIs.

Check whether the CLI plugin is available.

.. code-block:: bash
    :linenos:

    docker model --help

Pull and run a model.

.. code-block:: bash
    :linenos:

    docker model pull ai/qwen2.5-coder
    docker model run ai/qwen2.5-coder "Write a Dockerfile for a Python API"

Serve a model for an application.

.. code-block:: bash
    :linenos:

    docker model serve ai/qwen2.5-coder

Model Runner is useful for local development, AI application prototypes, and testing model-backed services without creating a separate model-serving stack.

Compose and models
------------------

Use Compose when an AI application needs an API, a frontend, and a model service together. Keep model configuration explicit and avoid assuming every developer has the same GPU.

.. code-block:: yaml
    :linenos:

    services:
      api:
        build: ./api
        environment:
          MODEL_BASE_URL: http://model:8080
        depends_on:
          - model
      model:
        image: model-runner:local
        ports:
          - "8080:8080"

For production, use the model-serving runtime that matches the deployment platform, GPU availability, and latency requirements.

Model artifacts
---------------

Treat model files as release artifacts.

* Record model name, version, source, and digest when available.
* Keep large model files out of application images unless there is a clear reason to bake them in.
* Store model artifacts in registries, object storage, or managed model repositories.
* Scan application images separately from model artifacts.
* Watch disk usage and startup time.

MCP Catalog
-----------

The Docker MCP Catalog is a curated catalog of MCP servers packaged as Docker images and distributed through Docker Hub. It helps avoid local dependency conflicts by running tools as isolated containers.

MCP servers can be local or remote.

* Local MCP servers run as containers on the machine.
* Remote MCP servers connect to provider infrastructure and often use OAuth.
* Catalog entries can include provenance and SBOM metadata.

Browse or pull catalog entries through Docker Desktop or the Docker MCP CLI.

.. code-block:: bash
    :linenos:

    docker mcp catalog ls
    docker mcp catalog pull <oci-reference>

Security notes
--------------

AI containers often handle prompts, source code, credentials, documents, or customer data. Treat them as sensitive workloads.

* Keep API keys in runtime secrets, not images.
* Limit filesystem mounts exposed to model and MCP containers.
* Prefer read-only mounts for source context.
* Review network access for remote model and MCP services.
* Pin model and MCP server versions for reproducible behavior.
* Keep GPU access explicit with ``--gpus`` or Compose GPU settings.

When to add this to a project
-----------------------------

Add AI container workflows when the application itself depends on local model serving, model-adjacent services, or MCP tools. Do not add them to every Docker project by default.

References
----------

* `Docker Model Runner <https://docs.docker.com/ai/model-runner/>`_
* `Model Runner API <https://docs.docker.com/ai/model-runner/api/>`_
* `Docker MCP Catalog <https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/>`_
* `AI and Docker Compose <https://docs.docker.com/ai/compose/>`_
