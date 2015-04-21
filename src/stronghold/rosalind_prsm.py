import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import genetics
import multisets
import table


def main(argv):
    mass = table.mass(argv[0])

    with open(argv[1]) as file:
        n        = int(file.readline().strip())
        lines    = file.readlines()
        proteins = [protein.strip() for protein in lines[:n]]
        R        = [float(line) for line in lines[n:]]

        M        = []
        for protein in proteins:
            S       = genetics.complete_spectrum(protein, mass)
            mult    = multisets.multiplicity(multisets.minkowski_difference(R, S))
            maximum = max(mult, key = mult.get)
            M.append((mult[maximum], protein))

        print '%d\n%s' % max(M)


if __name__ == "__main__":
    main(sys.argv[1:])
