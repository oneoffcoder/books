#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-cpp
VERSION=0.0.3
IMAGEID=book-cpp:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest