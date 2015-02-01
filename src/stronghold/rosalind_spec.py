import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import tables
import xerox


def calculate_protein(prefix, table):
    protein = ''

    for i in xrange(1, len(prefix)):
        mass     = prefix[i] - prefix[i - 1]
        protein += filter(lambda x: abs(x[0] - mass) < 0.001, table)[0][1]

    return protein


def main(argv):
    table   = tables.reverse_mass(argv[0])
    prefix  = files.read_floats(argv[1])
    protein = calculate_protein(prefix, table)

    xerox.copy(protein)
    print protein


if __name__ == "__main__":
    main(sys.argv[1:])
