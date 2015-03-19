import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import table


def main(argv):
    rev_mass = table.reverse_mass(argv[0])
    L        = files.read_floats(argv[1])

    print genetics.infer_peptides_from_spectrum(L, rev_mass)


if __name__ == "__main__":
    main(sys.argv[1:])
