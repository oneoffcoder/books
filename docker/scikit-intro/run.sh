#!/bin/bash

docker run -it \
    --shm-size 2g \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/scikit-intro/source:/root/ipynb \
    oneoffcoder/book-scikit-intro:latest
