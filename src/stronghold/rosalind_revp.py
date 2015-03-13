import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import genetics


def main(argv):
    dna = fasta.read_one(argv[0])
    rps = genetics.reverse_palindromes(dna)

    print '\n'.join('%s %s' % rp for rp in rps)


if __name__ == "__main__":
    main(sys.argv[1:])
