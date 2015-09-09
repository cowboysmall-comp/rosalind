import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import table
import genetics


# def linear_spectrum(masses):
#     length   = len(masses)
#     spectrum = [0, sum(masses)]

#     for i in xrange(1, length):
#         for j in xrange(length - i + 1):
#             spectrum.append(sum(masses[j:j + i]))

#     return sorted(spectrum)


def main(argv):
    int_mass = table.integer_mass(argv[0])
    peptide  = files.read_line(argv[1])
    masses   = [int_mass[p] for p in peptide]

    print ' '.join(str(m) for m in genetics.linear_spectrum(masses))


if __name__ == "__main__":
    main(sys.argv[1:])
