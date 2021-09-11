#!/bin/bash

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/spark-intro/source:/root/ipynb \
    oneoffcoder/book-spark-intro:latest
