import sys

import numpy as np

"""
    Just out of interest, here is a version, based on a version 
    written in Ruby that I found in the forums, and translated 
    into Python. It is much slower, but I find it fascinating. 
    For some reason, examples of Dynamic Programming always tend 
    to turn my brain inside out, and this example is no different 
    in that respect.

    def matchings(rna):
        A = np.zeros((len(rna), len(rna)), dtype = int)

        for i in xrange(len(rna)):
            for j in xrange(i - 1, -1, -1):
                if rna[i] == COMPLEMENT[rna[j]]:
                    if i - 1 >= j + 1:
                        A[i, j] = A[i - 1, j + 1]
                    else:
                        A[i, j] = 1

            for j in xrange(i):
                for k in xrange(j):
                    A[i, k] += A[i, j] * A[j - 1, k]
                    A[i, k] %= 1000000

        return A

"""

COMPLEMENT = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

def read_fasta(file_path):
    dna = ''

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                dna += line

    return dna


def check_occurences(rna):
    return rna.count('A') == rna.count('U') and rna.count('C') == rna.count('G')


def matchings(rna, start, end, A):
    if end < start:
        return 1
    elif A[start, end] == -1:
        A[start, end] = 0

        if check_occurences(rna[start:end + 1]):
            for i in xrange(start + 1, end + 1, 2):
                if rna[start] == COMPLEMENT[rna[i]]:
                    A[start, end] += matchings(rna, start + 1, i - 1, A) * matchings(rna, i + 1, end, A)
                    A[start, end] %= 1000000

    return A[start, end]


def main(argv):
    rna = read_fasta(argv[0])
    N   = len(rna)

    A = np.empty((N, N), dtype = int)
    A.fill(-1)

    print matchings(rna, 0, N - 1, A)


if __name__ == "__main__":
    main(sys.argv[1:])
