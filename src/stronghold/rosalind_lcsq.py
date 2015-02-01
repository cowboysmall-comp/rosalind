import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings


def main(argv):
    s, t = fasta.read(argv[0]).values()

    print strings.longest_common_subsequence(s, t)


if __name__ == "__main__":
    main(sys.argv[1:])
