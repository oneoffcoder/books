# ECS - Docker

## Local

```bash
# local
docker-compose -f docker-compose.local.yml --env-file .env.local build --force-rm --no-cache 
docker-compose -f docker-compose.local.yml --env-file .env.local up --force-recreate 
```

## ECR

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 982057254752.dkr.ecr.us-east-1.amazonaws.com

docker build --no-cache -t fs-demo-db:local .
docker build --no-cache -t fs-demo-es:local .
docker build --no-cache -t fs-demo-rest:local .
docker build --no-cache -t fs-demo-www:local .

docker tag fs-demo-db:local 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-db:latest
docker tag fs-demo-es:local 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-es:latest
docker tag fs-demo-rest:local 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-rest:latest
docker tag fs-demo-www:local 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-www:latest

docker push 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-db:latest
docker push 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-es:latest
docker push 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-rest:latest
docker push 982057254752.dkr.ecr.us-east-1.amazonaws.com/fs-demo-www:latest
```

## ECS

```bash
# context
docker context ls
docker context create ecs myecscontext
docker context use myecscontext
docker context use default

# ecs deploy
docker compose up
docker compose down
```

# Research

- [Deploy applications on Amazon ECS using Docker Compose](https://aws.amazon.com/blogs/containers/deploy-applications-on-amazon-ecs-using-docker-compose/?utm_source=pocket_mylist)
- [yelb](https://github.com/mreferre/yelb/)
- [compose-cli](https://github.com/docker/compose-cli)
- [Externalize environment variables](https://docs.docker.com/compose/environment-variables/)
- [Using volumes in Docker Compose](https://devopsheaven.com/docker/docker-compose/volumes/2018/01/16/volumes-in-docker-compose.html)