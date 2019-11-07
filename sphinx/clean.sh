#!/bin/bash

projects=( "java-intro" "python-intro" "pytorch-intro" "scikit-intro" "spark-intro" "datascience" )

for project in "${projects[@]}"
do
    cd $project && make clean && cd ..
done