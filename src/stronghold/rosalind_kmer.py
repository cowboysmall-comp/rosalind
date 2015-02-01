import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import re

from itertools import product


def main(argv):
    dna   = fasta.read_one(argv[0])
    kmers = [''.join(p) for p in product(*[['A', 'C', 'G', 'T']] * 4)]

    A = []
    for kmer in kmers:
        A.append(len(re.findall(r'(?=(%s))' % kmer, dna)))

    print ' '.join(str(a) for a in A)


if __name__ == "__main__":
    main(sys.argv[1:])
