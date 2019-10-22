#!/bin/bash

projects=( "java-intro" "python-intro" "pytorch-intro" "scikit-intro" "spark-intro" )

for project in "${projects[@]}"
do
    cd $project/book && make clean && make html && cd ../..
done