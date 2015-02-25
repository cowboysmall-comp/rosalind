import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import genetics


def main(argv):
    print genetics.perfect_matchings(fasta.read_one(argv[0])) % 1000000


if __name__ == "__main__":
    main(sys.argv[1:])
