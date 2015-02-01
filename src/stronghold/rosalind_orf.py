import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import genetics
import tables
import re


def encode(rna, table):
    encoded = []

    for match in re.compile(r'(?=(AUG))').finditer(rna):
        sub    = rna[match.start():]

        encode = ''

        for chunk in [sub[i:i + 3] for i in xrange(0, len(sub), 3)]:
            amino = table[chunk]
            if amino != 'Stop':
                encode += amino
            else:
                encoded.append(encode)
                break

    return encoded


def main(argv):
    table   = tables.codon(argv[0])
    dna     = fasta.read_one(argv[1])

    rna1    = genetics.dna_to_rna(dna)
    rna2    = genetics.dna_to_rna(genetics.dna_complement(dna))

    encoded = set()

    encoded.update(encode(rna1, table))
    encoded.update(encode(rna2, table))

    print '\n'.join(list(encoded))


if __name__ == "__main__":
    main(sys.argv[1:])
