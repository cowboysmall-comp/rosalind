import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import genetics
import files


def main(argv):
    print genetics.dna_to_rna(files.read_line(argv[0]))


if __name__ == "__main__":
    main(sys.argv[1:])
