import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines   = files.read_lines(argv[0])
    dna     = lines[0]
    k, L, t = [int(i) for i in lines[1].split()]

    print ' '.join(genetics.kmer_clump(dna, k, L, t))


if __name__ == "__main__":
    main(sys.argv[1:])
