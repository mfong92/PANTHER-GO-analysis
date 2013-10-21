from collections import defaultdict
import re
import sys

ANPattern = re.compile(r'AN(\d+)')
lengthPattern = re.compile(r'branch_length=(\d+.\d+)')


infile = open(sys.argv[1])
indent = True
treeArr = []
for line in infile:
	counter = 0
	indent = True
	while indent:
		for char in line:
			if char == ' ':
				counter += 1
			else: 
				indent = False
	counter = int(counter/4)*4
	if line.strip():	
		if line.strip()[0] == 'T':
			counter -=4
		treeArr.append((line.strip(), counter))

indentList = []
depthList = []
ANList = []
branchList = []
parentDict = {}
for info, indent in treeArr:
	if depthList and indent == depthList[-1][0][1] and (not re.findall(ANPattern, str(depthList[-1]))):
		depthList[-1].append((info,indent))
	else:
		if depthList:
			indentList.append(depthList[-1][0][1])
		depthList.append([(info,indent)])



for each in depthList:
	a= str(each)
	AN = re.findall(ANPattern, a)
	length = re.findall(lengthPattern, a)
	ANList.append((AN,length))

parent = False
for i in range(len(indentList)):
	for j in range(i, -1, -1):
		if indentList[j] == indentList[i] - 4:
			parent = ANList[j][0]
			break

	for k in range (len(ANList[i][0])):
		if parent:
			parent = ' ' .join(parent)
			if ANList[i][1][k]:
				branchList.append((int(ANList[i][0][k]), float(ANList[i][1][k]), int(parent)))
	
	parent = False

if len(ANList) > len(indentList):
	i = len(indentList)
	for j in range(i-1, -1, -1):
		if indentList[j] == indentList[-1] - 4:
			parent = ANList[j][0]
			break
	if parent:
		parent = ' '.join(parent)
	for k in ANList[i][0]:
		branchList.append((int(k), float(ANList[i][1][-1]), int(parent)))

print branchList


