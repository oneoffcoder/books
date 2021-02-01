#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-scikit-intro
VERSION=1.0.0
IMAGEID=${REPOSITORY}:local

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest
