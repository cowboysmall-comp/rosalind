import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import tables


def main(argv):
    table = tables.integer_mass(argv[0])
    mass  = files.read_int(argv[1])

    print genetics.count_peptides_with_mass(mass, table)


if __name__ == "__main__":
    main(sys.argv[1:])
