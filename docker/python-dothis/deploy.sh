#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-python-dothis
VERSION=0.0.3
IMAGEID=book-python-dothis:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest