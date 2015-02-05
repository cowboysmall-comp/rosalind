import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import tables
import genetics


def main(argv):
    table   = tables.mass(argv[0])
    protein = files.read_line(argv[1])

    print '%0.3f' % genetics.protein_weight(protein, table)


if __name__ == "__main__":
    main(sys.argv[1:])
