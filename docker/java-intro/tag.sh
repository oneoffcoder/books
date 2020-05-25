#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-java-intro
VERSION=0.1.0
IMAGEID=book-java-intro:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest