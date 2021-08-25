#!/bin/bash

port=8000
host=0.0.0.0

python -m sphinx_autobuild ./source ./build -b html --host $host --port $port
