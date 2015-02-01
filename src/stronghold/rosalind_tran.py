import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import distance


def main(argv):
    s1, s2 = fasta.read(argv[0]).values()

    print distance.tt_ratio(s1, s2)


if __name__ == "__main__":
    main(sys.argv[1:])
