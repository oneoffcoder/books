![One-Off Coder Logo](../../logo.png "One-Off Coder")

# Purpose

This docker container is meant to be used for learning purpose for programming in C++ 17.

# Docker

To run the container.

```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/docker/cpp/ipynb:/root/ipynb \
    local:book-cpp

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/docker/cpp/ipynb:/root/ipynb \
    oneoffcoder:book-cpp

```

Then point your browser to [http://localhost:8888](http://localhost:8888).

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/book-cpp)
