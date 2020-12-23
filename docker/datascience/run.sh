#!/bin/bash

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/datascience/source:/root/ipynb \
    --gpus all \
    oneoffcoder/book-datascience:latest
