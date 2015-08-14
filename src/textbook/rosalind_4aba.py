import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import table


def main(argv):
    codon = table.codon(argv[0])
    rna   = files.read_line(argv[1])

    print genetics.encode_protein(rna, codon)


if __name__ == "__main__":
    main(sys.argv[1:])
