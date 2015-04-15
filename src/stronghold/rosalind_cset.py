import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import phylogeny


def main(argv):
    lines = files.read_lines(argv[0])
    table = phylogeny.find_consistent_character_table(lines)

    print '\n'.join(table)


if __name__ == "__main__":
    main(sys.argv[1:])
