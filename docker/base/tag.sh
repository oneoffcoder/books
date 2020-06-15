#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-base
VERSION=0.0.9
IMAGEID=book-base:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest