import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings


def main(argv):
    dna_strings = fasta.read(argv[0]).values()

    print strings.longest_common_substring(dna_strings)


if __name__ == "__main__":
    main(sys.argv[1:])
