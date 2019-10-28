#!/bin/bash

port=8002

python -m sphinx_autobuild ./source ./build -b html -p $port -B
