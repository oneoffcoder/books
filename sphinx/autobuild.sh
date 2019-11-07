#!/bin/bash

projects=( "java-intro" "python-intro" "pytorch-intro" "scikit-intro" "spark-intro" "datascience" )
port=8000

for project in "${projects[@]}"
do
    python -m sphinx_autobuild $project/source $project/build -b html -p $port -B &
    port=$((port+1))
done
