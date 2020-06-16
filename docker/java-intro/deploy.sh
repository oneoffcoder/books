#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-java-intro
VERSION=0.3.0

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest