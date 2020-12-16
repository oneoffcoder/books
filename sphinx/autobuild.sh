#!/bin/bash

projects=( "java-intro" "python-intro" "pytorch-intro" "scikit-intro" "spark-intro" "datascience" "python-dothis" "scratch" "docker" )
port=8000
host=0.0.0.0

for project in "${projects[@]}"
do
    python -m sphinx_autobuild $project/source $project/build -b html --host $host --port $port -B &
    port=$((port+1))
done
