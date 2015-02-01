import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import tables
import files


def calculate_weight(protein, table):
    total = 0.0

    for p in protein:
        total += table[p]

    return total


def main(argv):
    table   = tables.mass(argv[0])
    protein = files.read_line(argv[1])

    print '%0.3f' % (calculate_weight(protein, table))


if __name__ == "__main__":
    main(sys.argv[1:])
