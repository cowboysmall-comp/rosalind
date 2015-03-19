import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import table


def main(argv):
    int_mass = table.integer_mass(argv[0])
    mass     = files.read_int(argv[1])

    print genetics.count_peptides_with_mass(mass, int_mass)


if __name__ == "__main__":
    main(sys.argv[1:])
