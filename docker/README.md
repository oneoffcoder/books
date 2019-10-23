![One-Off Coder Logo](../logo.png "One-Off Coder")

# Intro

A collection of Docker containers to be used with the corresponding online books for learning data science, computer science and coding!

# Running the containers

## Install docker-compose

You need to install `docker-compose`. To install docker compose on `*nix` systems [or other systems](https://docs.docker.com/compose/install/).

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version
```

## Run

To run the containers in the foreground. Hit `CTRL-C` to quit.

```bash
docker-compose up
```

To run the containers in the background.

```bash
docker-compose up -d 
docker-compose ps 
docker-compose down
```