import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import phylogeny


def main(argv):
    lines   = files.read_lines(argv[0])
    species = lines[0].split()
    tree    = phylogeny.tree_from_character_table(species, lines[1:])

    if tree:
        print tree.write(format = 9)
    else:
        print 'Inconsistent Character Table'


if __name__ == "__main__":
    main(sys.argv[1:])
