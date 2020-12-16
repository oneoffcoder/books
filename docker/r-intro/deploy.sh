#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-r-intro
VERSION=0.0.9
IMAGEID=book-r-intro:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest
