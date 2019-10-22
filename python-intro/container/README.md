![One-Off Coder Logo](../logo.png "One-Off Coder")

# Purpose

This docker container is meant to be used for learning purpose for programming in Python.

# Docker

To run the container.

```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/python-intro/container/ubuntu/root/ipynb:/root/ipynb \
    book-python-intro:local
```

Then point your browser to [http://localhost:8888](http://localhost:8888).

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/book-python-intro)
