import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import genetics
import tables
import xerox


def main(argv):
    table   = tables.codon(argv[0])
    strings = fasta.read_ordered(argv[1])

    dna     = strings[0]
    introns = strings[1:]

    for intron in introns:
        dna = dna.replace(intron, '')

    protein = genetics.encode_protein(genetics.dna_to_rna(dna), table)

    xerox.copy(protein)
    print protein


if __name__ == "__main__":
    main(sys.argv[1:])
