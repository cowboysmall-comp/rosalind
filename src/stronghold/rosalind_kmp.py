import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta


def compute_kmp(dna):
    N   = len(dna)
    T   = [0] * N

    pos = 1
    idx = 0
    while pos < N:
        if dna[pos] == dna[idx]:
            idx   += 1
            T[pos] = idx
            pos   += 1
        elif idx > 0:
            idx    = T[idx - 1]
        else:
            pos   += 1

    return T


def main(argv):
    dna = fasta.read_one(argv[0])

    print ' '.join(str(entry) for entry in compute_kmp(dna))


if __name__ == "__main__":
    main(sys.argv[1:])
