import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import table


def main(argv):
    int_mass = table.integer_mass(argv[0])
    spectrum = files.read_line_of_ints(argv[1])

    masses   = genetics.masses_from_cyclo_spectrum(spectrum)
    matches  = genetics.matching_peptides(masses, spectrum, int_mass)

    print ' '.join(set('-'.join(str(m) for m in match) for match in matches))


if __name__ == "__main__":
    main(sys.argv[1:])
