#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-aws-developer
VERSION=0.0.4
IMAGEID=book-aws-developer:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest
