import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings


def main(argv):
    dna = fasta.read_one(argv[0])

    print ' '.join(str(entry) for entry in strings.failure_array(dna))


if __name__ == "__main__":
    main(sys.argv[1:])
