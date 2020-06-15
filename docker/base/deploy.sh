#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=book-base
VERSION=0.0.9

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest