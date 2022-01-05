# ECS - Docker

Docker container with external volume.

```bash
aws --region us-east-1 ec2 describe-subnets --filter Name=vpc-id,Values=vpc-0ca5772d21c774589

docker context use myecscontext
docker compose up
```
