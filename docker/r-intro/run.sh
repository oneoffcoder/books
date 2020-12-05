#!/bin/bash

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/r-intro/source:/root/ipynb \
    oneoffcoder/book-r-intro:latest
