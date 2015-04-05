import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings


def main(argv):
    lines  = fasta.read_ordered(argv[0])
    result = strings.overlap_alignment(lines[0], lines[1])

    # unfinished - to be completed...

    print result[0]
    print '\n'.join(result[1:])


if __name__ == "__main__":
    main(sys.argv[1:])
