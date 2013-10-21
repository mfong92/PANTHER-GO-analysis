#!/bin/bash
FILES=*.arbre

for f in $FILES
do
    sed -i '' -e 's/ID=/S=/g' $f
    java -cp forester_1021.jar org.forester.application.phyloxml_converter -f=nn "$f" "${f}.out1"
    python xmlread.py ${f}.out1 > ${f}.out2
    python final.py ${f}.out2 > ${f%.arbre}.branch
    rm ${f}.out2
done
