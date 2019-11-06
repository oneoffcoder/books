![One-Off Coder Logo](../logo.png "One-Off Coder")

# Purpose

This docker container is meant to be used for learning data science topics.

# Docker

To run the container.

```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/datascience/source:/root/ipynb \
    --gpus all \
    book-datascience:local

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/datascience/source:/root/ipynb \
    -e NOTEBOOK_PASSWORD=sha1:6676da7235c8:9c7d402c01e330b9368fa9e1637233748be11cc5 \
    --gpus all \
    book-datascience:local
```

Then point your browser to [http://localhost:8888](http://localhost:8888).

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/book-datascience)
