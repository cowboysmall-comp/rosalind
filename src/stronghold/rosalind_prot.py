import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import tables
import genetics
import files


def main(argv):
    table = tables.codon(argv[0])
    rna   = files.read_line(argv[1])

    print genetics.encode_protein(rna, table)


if __name__ == "__main__":
    main(sys.argv[1:])
