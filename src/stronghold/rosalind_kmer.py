import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import genetics


def main(argv):
    dna = fasta.read_one(argv[0])
    A   = genetics.kmer_composition(dna, 4)

    print ' '.join(str(a) for a in A)


if __name__ == "__main__":
    main(sys.argv[1:])
