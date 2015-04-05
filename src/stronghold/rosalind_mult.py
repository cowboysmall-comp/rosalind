import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings
import table


def main(argv):
    lines  = fasta.read_ordered(argv[0])
    result = strings.multiple_alignment4(lines[0], lines[1], lines[2], lines[3])

    # unfinished - to be completed...

    print result[0]
    print '\n'.join(result[1:])


if __name__ == "__main__":
    main(sys.argv[1:])
