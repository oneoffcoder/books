# ECS - Docker

## Local

```bash
# local
docker compose -f compose.local.yaml --env-file .env.local build --force-rm --no-cache
docker compose -f compose.local.yaml --env-file .env.local up --force-recreate
```

## ECR

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 982057254752.dkr.ecr.us-east-1.amazonaws.com

docker build --no-cache -t fs-demo-db:local .
docker build --no-cache -t fs-demo-rest:local .
docker build --no-cache -t fs-demo-www:local .

docker tag fs-demo-db:local 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-db:latest
docker tag fs-demo-rest:local 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-rest:latest
docker tag fs-demo-www:local 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-www:latest

docker push 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-db:latest
docker push 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-rest:latest
docker push 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-www:latest
```

## ECS

Use Compose locally, then deploy to ECS with ECS-native task definitions, AWS Copilot, AWS CDK, Terraform, CloudFormation, or the AWS CLI. See the ECS chapter for the current deployment model.
