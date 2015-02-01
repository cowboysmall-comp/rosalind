import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import math


def main(argv):
    rna = fasta.read_one(argv[0])

    print math.factorial(rna.count('A')) * math.factorial(rna.count('C'))


if __name__ == "__main__":
    main(sys.argv[1:])
