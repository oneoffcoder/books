#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-datascience
VERSION=0.2.0
IMAGEID=${REPOSITORY}:local

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest