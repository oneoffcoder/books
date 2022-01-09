```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 982057254752.dkr.ecr.us-east-1.amazonaws.com

docker build --no-cache -t ww1:local .
docker tag ww1:local 982057254752.dkr.ecr.us-east-1.amazonaws.com/ww1:latest
docker push 982057254752.dkr.ecr.us-east-1.amazonaws.com/ww1:latest

docker context use myecscontext
docker compose up
docker compose ps
```