#!/bin/bash

FILES=*.arbre
for f in $FILES
do
	python extract.py ${f%.arbre}
done

