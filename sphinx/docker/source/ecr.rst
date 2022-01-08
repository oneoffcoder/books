Elastic Container Registry
==========================

Elastic Container Registry (ECR) is a service from Amazon Web Services (AWS) to host your own docker images. To be able to publish to ECR, you must first login to the AWS console and then go to the ECR section. There, you need to create a docker repository. Afer you have used the AWS console to create an ECR repository, you must login using the AWS CLI as follows.

.. code:: bash

    aws ecr get-login-password --region [region] | docker login --username AWS --password-stdin [account].dkr.ecr.[region].amazonaws.com

Next, you may build, tag and push the image to the ECR docker repository.

.. code:: bash

    docker build --no-cache -t [image_id]:local .
    docker tag [image_id]:local [account].dkr.ecr.[region].amazonaws.com/[image_id]:[tag]
    docker push [account].dkr.ecr.us-east-1.amazonaws.com/[image_id]:latest
