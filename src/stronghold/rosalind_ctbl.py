import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import phylogeny


def main(argv):
    tree = files.read_line(argv[0])

    print '\n'.join(phylogeny.create_table_from_tree(tree))


if __name__ == "__main__":
    main(sys.argv[1:])
