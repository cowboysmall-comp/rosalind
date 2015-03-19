import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import table


def main(argv):
    int_mass = table.integer_mass(argv[0])
    peptide  = files.read_line(argv[1])
    masses   = [int_mass[p] for p in peptide]

    print ' '.join(str(mass) for mass in genetics.cyclo_spectrum(masses, int_mass))


if __name__ == "__main__":
    main(sys.argv[1:])
