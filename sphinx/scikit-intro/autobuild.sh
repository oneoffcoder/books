#!/bin/bash

port=8003

python -m sphinx_autobuild ./source ./build -b html -p $port -B
