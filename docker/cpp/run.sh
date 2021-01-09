#!/bin/bash

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/cpp/source:/root/ipynb \
    oneoffcoder/book-cpp:latest
