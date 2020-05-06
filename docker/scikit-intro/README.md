![One-Off Coder Logo](../../logo.png "One-Off Coder")

# Purpose

This docker container is meant to be used for learning purpose for Scikit-Learn.

# Docker

To run the container.

```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/scikit-intro/source:/root/ipynb \
    book-scikit-intro:local

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/scikit-intro/source:/root/ipynb \
    oneoffcoder/book-scikit-intro

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/scikit-intro/source:/root/ipynb \
    -e NOTEBOOK_PASSWORD=sha1:6676da7235c8:9c7d402c01e330b9368fa9e1637233748be11cc5 \
    book-scikit-intro:local
```

Then point your browser to [http://localhost:8888](http://localhost:8888).

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/book-scikit-intro)
