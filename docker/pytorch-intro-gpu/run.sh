#!/bin/bash

docker run -it \
    -p 8888:8888 \
    -p 6006:6006 \
    -v $HOME/git/books/sphinx/pytorch-intro/source:/root/ipynb \
    -v $HOME/git/books/sphinx/pytorch-intro/source/tensorboard:/root/tensorboard \
    -e NOTEBOOK_PASSWORD=sha1:6676da7235c8:9c7d402c01e330b9368fa9e1637233748be11cc5 \
    --gpus all \
    oneoffcoder/book-pytorch-intro-gpu:latest
