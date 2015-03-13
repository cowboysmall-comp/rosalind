import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import tables


def main(argv):
    table   = tables.integer_mass(argv[0])
    peptide = files.read_line(argv[1])
    masses  = [table[p] for p in peptide]

    print ' '.join(str(mass) for mass in genetics.cyclo_spectrum(masses, table))


if __name__ == "__main__":
    main(sys.argv[1:])
