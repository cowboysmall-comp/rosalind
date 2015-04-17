import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import combinatorics
import phylogeny


def main(argv):
    lines  = files.read_lines(argv[0])
    taxa   = lines[0].split()
    trees  = lines[1:]

    table1 = phylogeny.create_table_from_tree(trees[0])
    table2 = phylogeny.create_table_from_tree(trees[1])

    print (2 * combinatorics.combinations(len(taxa), 4)) - (2 * phylogeny.count_common_quartets(table1, table2))


if __name__ == "__main__":
    main(sys.argv[1:])
