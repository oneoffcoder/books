Elastic Container Registry
==========================

Amazon Elastic Container Registry (ECR) is the AWS registry service for private and public container images. Use it as the registry in front of ECS, EKS, SageMaker, Batch, Lambda container images, and any other AWS service that pulls Docker-compatible images.

Set variables for the examples.

.. code-block:: bash
    :linenos:

    export AWS_REGION=us-east-1
    export AWS_ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
    export ECR_REGISTRY="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
    export ECR_REPOSITORY="student-rest"
    export IMAGE_TAG="$(git rev-parse --short HEAD)"

Create a private repository. Enable tag immutability for release repositories so pushed tags cannot be overwritten accidentally. Enable scan-on-push for immediate basic scanning, and use Amazon Inspector enhanced scanning when the account needs continuous vulnerability coverage.

.. code-block:: bash
    :linenos:

    aws ecr create-repository \
        --region "${AWS_REGION}" \
        --repository-name "${ECR_REPOSITORY}" \
        --image-tag-mutability IMMUTABLE \
        --image-scanning-configuration scanOnPush=true

Authenticate Docker to ECR. The authorization token is temporary, so CI jobs should log in during each run.

.. code-block:: bash
    :linenos:

    aws ecr get-login-password --region "${AWS_REGION}" \
        | docker login --username AWS --password-stdin "${ECR_REGISTRY}"

Build and push
--------------

Build with Buildx and push directly to ECR.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --platform linux/amd64 \
        -t "${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG}" \
        -t "${ECR_REGISTRY}/${ECR_REPOSITORY}:latest" \
        --push .

For multi-platform images, publish a manifest list.

.. code-block:: bash
    :linenos:

    docker buildx build \
        --platform linux/amd64,linux/arm64 \
        -t "${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG}" \
        --push .

Inspect the pushed image.

.. code-block:: bash
    :linenos:

    aws ecr describe-images \
        --region "${AWS_REGION}" \
        --repository-name "${ECR_REPOSITORY}" \
        --image-ids imageTag="${IMAGE_TAG}"

Pull by digest
--------------

Tags are convenient for humans. Deployments should record the digest that was promoted.

.. code-block:: bash
    :linenos:

    IMAGE_DIGEST="$(
        aws ecr describe-images \
            --region "${AWS_REGION}" \
            --repository-name "${ECR_REPOSITORY}" \
            --image-ids imageTag="${IMAGE_TAG}" \
            --query 'imageDetails[0].imageDigest' \
            --output text
    )"

    echo "${ECR_REGISTRY}/${ECR_REPOSITORY}@${IMAGE_DIGEST}"

Repository controls
-------------------

Use repository and registry controls deliberately.

* Turn on immutable tags for release repositories.
* Turn on scan-on-push, and use enhanced scanning for continuous monitoring.
* Use lifecycle policies for feature-branch images and BuildKit cache tags.
* Use separate AWS accounts or repositories for development, staging, and production.
* Grant push permissions only to build roles and pull permissions only to deployment roles.
* Prefer KMS encryption when the organization requires customer-managed keys.

References
----------

* `ECR authentication <https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html>`_
* `ECR private repositories <https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html>`_
* `ECR image scanning <https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html>`_
