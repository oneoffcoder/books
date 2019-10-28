#!/bin/bash

port=8001

python -m sphinx_autobuild ./source ./build -b html -p $port -B
