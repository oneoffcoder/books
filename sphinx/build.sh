#!/bin/bash

projects=( "java-intro" "python-intro" "pytorch-intro" "scikit-intro" "spark-intro" "datascience" "python-dothis" "scratch" )

for project in "${projects[@]}"
do
    cd $project && make clean && make html && cd ..
done