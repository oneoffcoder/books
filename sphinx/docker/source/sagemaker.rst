SageMaker
=========

Amazon SageMaker uses containers for training jobs, processing jobs, batch transforms, and real-time inference. Use a custom Docker image when the built-in SageMaker images do not have the operating system packages, runtime, or serving stack that the workload needs.

The normal path is:

* Build a training or inference image with Docker.
* Push the image to ECR.
* Point a SageMaker job or model at the ECR image URI.
* Write outputs to the SageMaker paths that the platform mounts inside the container.

Training containers
-------------------

For training jobs, SageMaker mounts input channels under ``/opt/ml/input/data`` and expects model artifacts under ``/opt/ml/model``. A simple image can use the Python process as its entrypoint.

.. code-block:: docker
    :linenos:

    # syntax=docker/dockerfile:1
    FROM python:3-slim

    ENV PYTHONUNBUFFERED=1
    WORKDIR /opt/program
    COPY requirements.txt train.py ./
    RUN --mount=type=cache,target=/root/.cache/pip \
        pip install --no-cache-dir -r requirements.txt

    ENTRYPOINT ["python", "train.py"]

The training script should read inputs and write the trained model.

.. code-block:: python
    :linenos:

    from pathlib import Path
    import json

    input_dir = Path("/opt/ml/input/data/training")
    model_dir = Path("/opt/ml/model")
    model_dir.mkdir(parents=True, exist_ok=True)

    rows = sum(1 for _ in input_dir.glob("**/*") if _.is_file())
    (model_dir / "model.json").write_text(json.dumps({"training_files": rows}))

Build and push the image to ECR.

.. code-block:: bash
    :linenos:

    export AWS_REGION=us-east-1
    export AWS_ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
    export IMAGE_URI="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/sm-train:latest"

    aws ecr get-login-password --region "${AWS_REGION}" \
        | docker login --username AWS --password-stdin "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

    docker buildx build --platform linux/amd64 -t "${IMAGE_URI}" --push .

Run a training job with the SageMaker Python SDK.

.. code-block:: python
    :linenos:

    from sagemaker.estimator import Estimator

    estimator = Estimator(
        image_uri=image_uri,
        role=role_arn,
        instance_count=1,
        instance_type="ml.m5.large",
        output_path="s3://my-bucket/sagemaker/output"
    )

    estimator.fit({"training": "s3://my-bucket/sagemaker/training"})

Inference containers
--------------------

For real-time inference, SageMaker starts the container and sends traffic to port ``8080``. A custom serving container should expose health and invocation routes.

* ``GET /ping`` returns a successful health response when the model is ready.
* ``POST /invocations`` accepts inference requests and returns predictions.

Use a web framework such as FastAPI, Flask, or a model server that already implements the SageMaker inference contract.

Container rules
---------------

* Keep training and inference images separate unless the same runtime is truly needed.
* Put large model artifacts in S3, not in the image.
* Use ECR repository scanning and immutable release tags.
* Run as a non-root user when the framework allows it.
* Use ``/opt/ml/model`` for trained artifacts and ``/opt/ml/output`` for job output.
* Keep AWS credentials out of images. SageMaker injects IAM permissions through the job role.

References
----------

* `SageMaker custom Docker containers <https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html>`_
* `SageMaker training and inference toolkits <https://docs.aws.amazon.com/sagemaker/latest/dg/amazon-sagemaker-toolkits.html>`_
