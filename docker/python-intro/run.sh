#!/bin/bash

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/docker/python-intro/ipynb:/root/ipynb \
    -e NOTEBOOK_PASSWORD=sha1:6676da7235c8:9c7d402c01e330b9368fa9e1637233748be11cc5 \
    book-python-intro:local
