import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from ete2 import Tree


def construct_tree(species, table):
    print


def main(argv):
    lines   = files.read_lines(argv[0])
    species = lines[0].split()
    length  = len(species)
    table   = ['1' * length] + lines[1:] + ['0' * length]
    table   = sorted(table, reverse = True)

    # unfinished - to be completed...

    print ' '.join(s for s in species)
    print '\n'.join(str(row) for row in table)


if __name__ == "__main__":
    main(sys.argv[1:])
