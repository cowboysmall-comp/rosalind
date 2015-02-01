import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import distance


def main(argv):
    strings = fasta.read_ordered(argv[0])
    matrix  = distance.p_matrix(strings)

    print '\n'.join([' '.join(['%0.5f' % col for col in row]) for row in matrix])


if __name__ == "__main__":
    main(sys.argv[1:])
