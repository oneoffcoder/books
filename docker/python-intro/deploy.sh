#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-python-intro
VERSION=0.0.7
IMAGEID=${REPOSITORY}:local

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest