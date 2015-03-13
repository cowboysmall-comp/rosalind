import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import genetics
import tables
import re


def main(argv):
    table   = tables.codon(argv[0])
    dna     = fasta.read_one(argv[1])

    rna1    = genetics.dna_to_rna(dna)
    rna2    = genetics.dna_to_rna(genetics.dna_complement(dna))

    encoded = set()

    encoded.update(genetics.encode_protein_from_orf(rna1, table))
    encoded.update(genetics.encode_protein_from_orf(rna2, table))

    print '\n'.join(list(encoded))


if __name__ == "__main__":
    main(sys.argv[1:])
