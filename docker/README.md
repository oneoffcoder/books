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

To access the Jupyter Lab environments.

* [Java](http://localhost:7770)
* [Python](http://localhost:7771)
* [PyTorch](http://localhost:7772)
* [Scikit](http://localhost:7773)
* [Spark](http://localhost:7774)
* [Data Science](http://localhost:7775)
* [Python, Do This, Not That!](http://localhost:7776)

To run the containers in the background.

```bash
docker-compose up -d 
docker-compose ps 
docker-compose down
```

Some useful commands.

```bash
# get realtime events from docker containers
docker-compose events

# observe status e.g. health
docker ps
```
