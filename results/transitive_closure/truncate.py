import sys
import re

def trunc(lst, d, depth):
	newLst = []
	for i in lst:
		if i in d:
			if int(d[i]) <= int(depth):
				newLst.append(i)
	return newLst

dictionary = {}
cache = {}
infile = open("term_depth")
for line in infile:
	dictionary[line.strip().split('\t')[0]] = line.strip().split('\t')[3]

infile = open(sys.argv[1])
depth = sys.argv[2]
for line in infile:
	lineList = list(line.split('['))
	number = lineList[0]
	GOList = "[" + lineList[1]
	if GOList not in cache:
		cache[GOList] = trunc(eval(GOList), dictionary, depth)
	if not cache[GOList]:
		cache[GOList] = []
	print number +  str(cache[GOList])
