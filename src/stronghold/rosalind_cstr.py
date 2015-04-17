import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import phylogeny


def main(argv):
    strings = files.read_lines(argv[0])

    print '\n'.join(phylogeny.create_table_from_strings(strings))


if __name__ == "__main__":
    main(sys.argv[1:])
