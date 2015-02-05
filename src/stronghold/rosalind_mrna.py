import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import tables
import genetics


def main(argv):
    table  = tables.reverse_codon(argv[0])
    string = files.read_line(argv[1])

    print genetics.count_rnas_from_protein(string, table)


if __name__ == "__main__":
    main(sys.argv[1:])
