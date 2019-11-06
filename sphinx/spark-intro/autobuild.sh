#!/bin/bash

port=8000

python -m sphinx_autobuild ./source ./build -b html -p $port -B
