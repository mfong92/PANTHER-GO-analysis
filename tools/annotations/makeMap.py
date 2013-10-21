import sys
from collections import defaultdict
import re
import itertools

pattern = re.compile(r'AN(\d+)')
GOPattern = re.compile(r'GO:(\d+)')


def attrCheck(x):
	master = []
	infile = open(str(sys.argv[1] + ".attr"))
	for line in infile:
		current = list(line.strip('\n\t').split())
		for i in current:
			if (i == '\t'):
				current.remove(i)
		master.append(current)
	for each in master:
		if (each[0].replace("'","") == str("AN" + str(x))):
			return "PANTHER="+each[-1].replace("'","")

def arbreCheck(x):
	arbreFile = []
	infile = open(str(sys.argv[1] + ".arbre"))
	for line in infile: 
		arbreFile.append(line.strip())
	for i in range(2, len(arbreFile)):
		current = re.findall(pattern, arbreFile[i])
		if int(current[0]) == x:
			entries = arbreFile[i].strip('\n;').split('|')
			if entries: return entries

def gafCheck(x):
	ga = "gene_association.paint_"
	gafArray = [sys.argv[1], "dictyBase", "ecocyc", "fb", "goa_chicken", "goa_human", "mgi", "other", "pombase", "rgd", "sgd", "tair", "wb", "zfin"]
	possible = map(lambda x: ga+x, gafArray)
	possible[0] = sys.argv[1]
	result = []
	for i in possible:
		infile = open(str(i + ".gaf"))
		for line in infile:
			GO = None
			categ = None
			isNot = False
			current =  list(line.strip('\n\t').split())
			identifier = current[0] + "=" + current[1]
			identifier = identifier.replace(":","=")
			identifier = identifier.replace("-PA", "")
			identifier2 = "AAAAAAAAAAAAAAAAA"	
			if current [0] == "TAIR":
				identifier2 = current[0] + "=" + current[2]
			if identifier.lower() in x.lower() or identifier2.lower() in x.lower() or current[1].lower() in x.lower():
				for term in current:
					if re.findall(GOPattern, term):
						GO = "GO:" + str(re.findall(GOPattern, term)[0])
					if (term == "C" or term == "F" or term == "P"):
						categ = term
					if (term == "NOT"):
						isNot = True
				if GO:
					if isNot:
						if (categ + " " + str(GO) + " " + "NOT") not in result:
							result.append(categ + " " + str(GO) + " " + "NOT")
					else:
						if (categ + " " + str(GO)) not in result:
							result.append(categ + " " + str(GO))
				if not possible[0] in i:
					break
	if result:
		return result

def main():
	pairsList = []
	ANMappings = defaultdict(list)
	ANtoGO = defaultdict(list)
	infile = open(str(sys.argv[1] + ".pair"))
	for line in infile:
		pairsList = line
	pairsList = eval(pairsList)
	for x,y in pairsList:
		if x not in ANMappings:
			ANMappings[x].append(arbreCheck(x))
			ANMappings[x].append(attrCheck(x))
		if y not in ANMappings:
			ANMappings[y].append(arbreCheck(y))
			ANMappings[y].append(attrCheck(y))
	for key in ANMappings:
		if ANMappings[key][0]:
			ANMappings[key][0].remove(ANMappings[key][0][0])
		if not ANMappings[key][1]:
			ANMappings[key].remove(ANMappings[key][1])
		if not ANMappings[key][0]:
			ANMappings[key].remove(ANMappings[key][0])
		if ANMappings[key]:
			if type(ANMappings[key][0]) is list:
				ANMappings[key] = ANMappings[key][0]
	for key,value in ANMappings.iteritems():
		for each in value:
			if gafCheck(each):
				ANtoGO[key].append(gafCheck(each))
		if ANtoGO[key]:
			if type(ANtoGO[key][0]) is list:
				ANtoGO[key] = ANtoGO[key][0]
	for x in ANtoGO.iteritems():
		print str(x[0]) + ": " + str(x[1])

main()
