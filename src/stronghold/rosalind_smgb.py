import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings


def main(argv):
    s, t   = fasta.read_ordered(argv[0])
    result = strings.semi_global_alignment(s, t)

    print result[0]
    print '\n'.join(r for r in result[1:])


if __name__ == "__main__":
    main(sys.argv[1:])
