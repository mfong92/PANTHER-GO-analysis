#!/bin/bash

mkdir truncated
f=*.trans

for each in $f
do
	python truncate.py $each $1 > truncated/$each
done
