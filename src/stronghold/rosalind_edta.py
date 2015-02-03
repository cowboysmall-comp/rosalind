import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings


def main(argv):
    s, t = fasta.read_ordered(argv[0])

    print '%s\n%s\n%s' % strings.optimal_alignment(s, t)


if __name__ == "__main__":
    main(sys.argv[1:])
