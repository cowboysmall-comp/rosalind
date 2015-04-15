import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import re

import files

from ete2 import Tree


def invert(string):
    return ''.join('1' if b == '0' else '0' for b in string) if string.count('1') > string.count('0') else string


def tree_from_character_table(species, table):
    leaves  = []
    tree    = Tree()
    root    = tree.get_tree_root()

    for specie in species:
        leaves.append(root.add_child(name = specie))

    while table:
        for row in table:
            if row.count('1') == 2:
                i1, i2     = [i.start() for i in re.finditer('1', row)]
                n1, n2     = leaves[i1], leaves[i2]

                leaves[i1] = root.add_child()
                leaves[i1].add_child(n1.detach())
                leaves[i1].add_child(n2.detach())

                table.remove(row)
                leaves     = leaves[:i2] + leaves[i2 + 1:]
                table      = [row[:i2] + row[i2 + 1:] for row in table]
                break
            else:
                return None

    return tree


def main(argv):
    lines   = files.read_lines(argv[0])
    species = lines[0].split()
    table   = sorted([invert(row) for row in lines[1:]], key = lambda x: x.count('1'))

    tree    = tree_from_character_table(species, table)

    if tree:
        print tree.write(format = 9)
    else:
        print 'Inconsistent Character Table'


if __name__ == "__main__":
    main(sys.argv[1:])
