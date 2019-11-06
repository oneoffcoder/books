#!/bin/bash

# NOTE: make sure you have created an AWS CLI conda environment

AWS_URL=982057254752.dkr.ecr.us-east-1.amazonaws.com

$(aws ecr get-login --no-include-email --region us-east-1)
docker push $AWS_URL/book-cicd:0.0.1
docker push $AWS_URL/book-cicd:latest