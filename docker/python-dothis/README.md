![One-Off Coder Logo](../../logo.png "One-Off Coder")

# Purpose

This docker container is meant to be used for learning purpose for programming in Python more efficiently, effectively and idiomatically.

# Docker

To run the container.

```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/docker/python-dothis/ipynb:/root/ipynb \
    book-python-dothis:local

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/docker/python-dothis/ipynb:/root/ipynb \
    -e NOTEBOOK_PASSWORD=sha1:6676da7235c8:9c7d402c01e330b9368fa9e1637233748be11cc5 \
    book-python-dothis:local
```

Then point your browser to [http://localhost:8888](http://localhost:8888).

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/book-python-dothis)