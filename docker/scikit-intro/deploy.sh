#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-scikit-intro
VERSION=0.3.0
IMAGEID=book-scikit-intro:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest