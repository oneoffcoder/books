Elastic Container Service
=========================

Amazon Elastic Container Service (ECS) runs containers on AWS. The modern path is to push images to ECR, define an ECS task definition, and run that task through an ECS service on Fargate or EC2 capacity.

The older Docker ECS Compose context workflow is no longer the primary path for new deployments. Keep Compose for local development, then express the AWS deployment with ECS-native task definitions, AWS Copilot, AWS CDK, Terraform, CloudFormation, or the AWS CLI.

Deployment shape
----------------

The usual flow is:

* Build the image with Docker Buildx.
* Push the image to ECR.
* Register an ECS task definition that references the ECR image.
* Create or update an ECS service.
* Watch logs in CloudWatch and deployments in ECS.

Task definition
---------------

The task definition is the unit ECS runs. This minimal Fargate example has one container and sends logs to CloudWatch.

.. code-block:: json
   :linenos:

    {
      "family": "student-rest",
      "networkMode": "awsvpc",
      "requiresCompatibilities": ["FARGATE"],
      "cpu": "512",
      "memory": "1024",
      "executionRoleArn": "arn:aws:iam::<account-id>:role/ecsTaskExecutionRole",
      "containerDefinitions": [
        {
          "name": "rest",
          "image": "<account-id>.dkr.ecr.us-east-1.amazonaws.com/student-rest:<tag>",
          "essential": true,
          "portMappings": [
            {
              "containerPort": 8080,
              "protocol": "tcp"
            }
          ],
          "logConfiguration": {
            "logDriver": "awslogs",
            "options": {
              "awslogs-group": "/ecs/student-rest",
              "awslogs-region": "us-east-1",
              "awslogs-stream-prefix": "ecs"
            }
          }
        }
      ]
    }

Register the task definition.

.. code-block:: bash
    :linenos:

    aws ecs register-task-definition --cli-input-json file://task-definition.json

Create a service
----------------

Create the ECS service on an existing cluster, subnet set, and security group. For internet-facing examples, the security group must allow the inbound application port and the subnets must match the public or load-balanced design.

.. code-block:: bash
    :linenos:

    aws ecs create-service \
        --cluster student-cluster \
        --service-name student-rest \
        --task-definition student-rest \
        --desired-count 1 \
        --launch-type FARGATE \
        --network-configuration "awsvpcConfiguration={subnets=[subnet-abc123],securityGroups=[sg-abc123],assignPublicIp=ENABLED}"

Deploy a new image
------------------

When a new image is pushed, register a new task definition revision and update the service.

.. code-block:: bash
    :linenos:

    aws ecs update-service \
        --cluster student-cluster \
        --service student-rest \
        --task-definition student-rest \
        --force-new-deployment

Watch rollout status.

.. code-block:: bash
    :linenos:

    aws ecs describe-services \
        --cluster student-cluster \
        --services student-rest \
        --query 'services[0].deployments'

Configuration and secrets
-------------------------

Do not put production secrets in the image or task definition plaintext.

* Put non-secret configuration in environment variables.
* Put secrets in AWS Secrets Manager or Systems Manager Parameter Store.
* Grant the task role only the permissions the container needs.
* Grant the task execution role permissions for ECR pulls and CloudWatch logs.
* Use health checks and load balancer target groups for services that receive traffic.

Local Compose remains useful
----------------------------

Use Compose to run the same application locally. The local file should model service names, ports, volumes, environment variables, and health checks. The ECS definition should model AWS-specific concerns such as IAM roles, VPC networking, logs, autoscaling, deployment configuration, and load balancing.

References
----------

* `Amazon ECS <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html>`_
* `ECS task definitions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html>`_
* `Fargate task networking <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html>`_
