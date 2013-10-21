import sys

infile = open(sys.argv[1] + ".branch")

for line in infile:
    master = eval(line)

newList = []
for (x,y,z) in master:
    newList.append((x,z))

print newList
