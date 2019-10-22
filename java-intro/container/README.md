![One-Off Coder Logo](../logo.png "One-Off Coder")

# Purpose

This docker container is meant to be used for learning purpose for programming in Java 12.

# Docker

To run the container.

```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/java-intro/ubuntu/root/ipynb:/root/ipynb \
    java-jupyter:local
```

Then point your browser to [http://localhost:8888](http://localhost:8888). Jupyter Lab should show up and you can start a Java kernel.

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/java-jupyter)
