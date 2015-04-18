import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import fasta
import strings

from ete2 import Tree
from Bio import Phylo
from StringIO import StringIO



def main(argv):
    lines   = files.read_lines(argv[0])
    tree    = Tree(lines[0], format = 1)

    # handle  = StringIO(lines[0])
    # tree    = Phylo.read(handle, "newick")
    strings = fasta.read_from(lines[1:])

    for node in tree.iter_descendants('levelorder'):
        print node.name

    print 
    # print Phylo.draw_ascii(tree)
    print tree
    print 
    print strings


if __name__ == "__main__":
    main(sys.argv[1:])
