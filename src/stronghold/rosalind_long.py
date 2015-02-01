import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings


def main(argv):
    print strings.shortest_superstring(fasta.read(argv[0]).values())


if __name__ == "__main__":
    main(sys.argv[1:])
