#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-java-intro
VERSION=0.2.0

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest