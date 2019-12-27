#!/bin/bash

docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/aws-developer/source:/root/ipynb \
    -e NOTEBOOK_PASSWORD=sha1:6676da7235c8:9c7d402c01e330b9368fa9e1637233748be11cc5 \
    -e AWS_REGION="us-east-1x" \
    -e AWS_ACCESS_KEY="NEED_TO_SET_KEYX" \
    -e AWS_SECRET_KEY="NEED_TO_SET_SECRETX" \
    oneoffcoder/book-aws-developer:latest