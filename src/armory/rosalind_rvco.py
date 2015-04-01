import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from Bio.Seq      import Seq
from Bio.Alphabet import IUPAC

import fasta


def main(argv):
    strings = fasta.read(argv[0])
    count   = 0

    for string in strings.values():
        if string == Seq(string, IUPAC.unambiguous_dna).reverse_complement():
            count += 1

    print count


if __name__ == "__main__":
    main(sys.argv[1:])
