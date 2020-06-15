#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-python-intro
VERSION=0.0.6
IMAGEID=book-python-intro:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest