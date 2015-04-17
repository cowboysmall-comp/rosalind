import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from ete2 import Tree

import files
import combinatorics
import phylogeny


def main(argv):
    lines  = files.read_lines(argv[0])
    taxa   = lines[0].split()
    trees  = lines[1:]

    table1 = phylogeny.create_table_from_tree_and_leaves(trees[0], taxa)

    # print 'first tables created...'
    # print

    table2 = phylogeny.create_table_from_tree_and_leaves(trees[1], taxa)

    # print table1
    # print table2
    # print table1 & table2
    # print table1 - table2
    # print table2 - table1
    # print 

    # print 'second tables created...'
    # print

    count  = combinatorics.combinations(len(taxa), 4)

    # print 'count completed...'
    # print

    common = phylogeny.count_common_quartets(table1, table2)
    # common = phylogeny.count_common_quartets(trees[0], trees[1], taxa)

    # print 'common completed...'
    # print

    print (2 * count) - (2 * common)


if __name__ == "__main__":
    main(sys.argv[1:])
