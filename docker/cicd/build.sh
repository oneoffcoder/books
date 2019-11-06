#!/bin/bash

AWS_URL=982057254752.dkr.ecr.us-east-1.amazonaws.com

docker build --no-cache -t book-cicd:local .

docker tag book-cicd:local $AWS_URL/book-cicd:0.0.1
docker tag book-cicd:local $AWS_URL/book-cicd:latest