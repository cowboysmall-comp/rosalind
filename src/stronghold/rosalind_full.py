import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import tables


def infer_peptide(L, table, length):
    peptide = ''

    L  = [l - L[0] for l in L[1:]]

    while len(peptide) < length:
        for i in xrange(len(L)):
            found = filter(lambda x: abs(x[0] - L[i]) < 0.0001, table)
            if found:
                peptide += found[0][1]
                L        = [l - L[i] for l in L[i + 1:]]
                break

    return peptide


def main(argv):
    table = tables.reverse_mass(argv[0])
    L     = files.read_floats(argv[1])

    print infer_peptide(sorted(L[1:]), table, (len(L) - 3) / 2)


if __name__ == "__main__":
    main(sys.argv[1:])
