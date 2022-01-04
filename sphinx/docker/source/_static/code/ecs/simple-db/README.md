# ECS - Docker

Docker container with external volume.

```bash
# local
docker-compose build --force-rm --no-cache
docker-compose up --force-recreate

# context
docker context create ecs --local-simulation ecsLocal
docker context ls
docker context use ecsLocal 
docker compose build

docker context use myecscontext
docker compose up
```
