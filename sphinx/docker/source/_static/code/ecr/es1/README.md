```bash
docker build --no-cache -t es1:local .
docker tag es1:local 982057254752.dkr.ecr.us-east-1.amazonaws.com/es1:latest

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 982057254752.dkr.ecr.us-east-1.amazonaws.com

docker push 982057254752.dkr.ecr.us-east-1.amazonaws.com/es1:latest
```