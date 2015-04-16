import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from itertools import product
from operator  import add, mul

import fasta
import strings


def main(argv):
    dna_strings = fasta.read_ordered(argv[0])
    results     = strings.quadruple_alignment(*dna_strings)

    # print strings.pairwise_scores(results[1:])
    print results[0]
    print '\n'.join(results[1:])


if __name__ == "__main__":
    main(sys.argv[1:])
