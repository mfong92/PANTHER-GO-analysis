import sys
from Bio import Phylo
tree = Phylo.read(sys.argv[1], 'phyloxml')
print tree