#!/bin/bash

docker run \
    --rm \
    -d \
    -e MYSQL_ROOT_PASSWORD=oneoffcoder \
    -v `pwd`/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d \
    -p 3306:3306 \
    db-app:local

