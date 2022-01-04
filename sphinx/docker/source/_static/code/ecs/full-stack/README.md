# ECS - Docker

```bash
# local
docker-compose build --force-rm --no-cache
docker-compose up --force-recreate

# context
docker context ls
docker context create ecs myecscontext
docker context use myecscontext
docker context use default

# ecs deploy
docker compose up
```

# Research

- [Deploy applications on Amazon ECS using Docker Compose](https://aws.amazon.com/blogs/containers/deploy-applications-on-amazon-ecs-using-docker-compose/?utm_source=pocket_mylist)
- [yelb](https://github.com/mreferre/yelb/)
- [compose-cli](https://github.com/docker/compose-cli)
- [Externalize environment variables](https://docs.docker.com/compose/environment-variables/)
- [Using volumes in Docker Compose](https://devopsheaven.com/docker/docker-compose/volumes/2018/01/16/volumes-in-docker-compose.html)