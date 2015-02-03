import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import tables


def infer_protein(masses, table):
    protein = ''

    for i in xrange(1, len(masses)):
        mass     = masses[i] - masses[i - 1]
        protein += filter(lambda x: abs(x[0] - mass) < 0.0001, table)[0][1]

    return protein


def main(argv):
    table   = tables.reverse_mass(argv[0])
    L       = files.read_floats(argv[1])

    print infer_protein(L, table)


if __name__ == "__main__":
    main(sys.argv[1:])
