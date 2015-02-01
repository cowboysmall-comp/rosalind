import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import distance


def create_matrix(strings):
    N   = len(strings)
    D   = [[0.0 for _ in xrange(N)] for _ in xrange(N)]

    for i in xrange(N):
        for j in xrange(i + 1, N):
            D[i][j] = distance.p(strings[i], strings[j])
            D[j][i] = D[i][j]

    return D


def main(argv):
    dna = fasta.read_ordered(argv[0])

    print '\n'.join([' '.join(['%0.5f' % col for col in row]) for row in create_matrix(dna)])


if __name__ == "__main__":
    main(sys.argv[1:])
