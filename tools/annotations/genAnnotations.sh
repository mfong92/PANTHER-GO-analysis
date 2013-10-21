#!/bin/bash

FILES=*.arbre

for f in $FILES
do
    python pairs.py ${f%.arbre} > ${f%.arbre}.pair
    python makeMap.py ${f%.arbre} > ${f%.arbre}.map
    rm ${f%.arbre}.pair
done

