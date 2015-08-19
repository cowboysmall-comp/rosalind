import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import table


def main(argv):
    codon      = table.codon(argv[0])
    dna, amino = files.read_lines(argv[1])

    print '\n'.join(genetics.find_peptides_in_dna(dna, amino, codon))


if __name__ == "__main__":
    main(sys.argv[1:])
