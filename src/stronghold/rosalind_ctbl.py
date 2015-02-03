import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from ete2 import Tree


def create_row(node, names):
    split = [0] * len(names)

    for leaf in node:
        split[names.index(leaf.name)] = 1

    return split


def main(argv):
    tree  = Tree(files.read_line(argv[0]), format = 1)
    names = sorted(tree.get_leaf_names())

    table = []

    for node in tree.get_descendants():
        if not node.is_leaf():
            table.append(create_row(node, names))

    print '\n'.join(''.join(str(r) for r in row) for row in table)


if __name__ == "__main__":
    main(sys.argv[1:])
