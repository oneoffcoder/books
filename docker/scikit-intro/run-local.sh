#!/bin/bash

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/scikit-intro/source:/root/ipynb \
    book-scikit-intro:local
