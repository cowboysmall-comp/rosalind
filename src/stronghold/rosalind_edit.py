import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import distance


def main(argv):
    s, t = fasta.read(argv[0]).values()

    print distance.edit(s, t)


if __name__ == "__main__":
    main(sys.argv[1:])
