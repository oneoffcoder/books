#!/bin/bash

docker run -it \
    -p 9870:9870 \
    -p 8088:8088 \
    -p 8080:8080 \
    -p 18080:18080 \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/spark-intro/source:/root/ipynb \
    oneoffcoder/book-spark-intro:latest
