# ECS - Docker

Docker container with external volume.

```bash
aws --region us-east-1 ec2 describe-subnets --filter Name=vpc-id,Values=vpc-0ca5772d21c774589

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 982057254752.dkr.ecr.us-east-1.amazonaws.com

docker context use myecscontext
docker compose up
docker compose ps
docker compose down
```
