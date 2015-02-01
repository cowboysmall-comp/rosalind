import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import genetics


def reverse_palindromes(dna):
    rps  = []

    for i in xrange(4, 13):
        for j in xrange(len(dna) - i + 1):
            c = dna[j:j + i]
            if c == genetics.dna_complement(c):
                rps.append((j + 1, i))

    return sorted(rps)


def main(argv):
    dna = fasta.read_one(argv[0])
    rps = reverse_palindromes(dna)

    print '\n'.join(['%s %s' % rp for rp in rps])


if __name__ == "__main__":
    main(sys.argv[1:])
