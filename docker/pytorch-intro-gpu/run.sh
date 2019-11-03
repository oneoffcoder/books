#!/bin/bash

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/pytorch-intro/source:/root/ipynb \
    --gpus all \
    book-pytorch-intro-gpu:local
