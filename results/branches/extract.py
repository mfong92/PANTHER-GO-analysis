import sys

infile = open(sys.argv[1] + ".arbre")
print infile.readline()[5:].strip()

