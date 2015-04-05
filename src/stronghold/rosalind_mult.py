import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings
import table


# def align(s1, s2):
#     strings.


def main(argv):
    lines  = fasta.read_ordered(argv[0])
    # result = strings.multiple_alignment4(lines[0], lines[1], lines[2], lines[3])

    # unfinished - to be completed...

    for i in xrange(len(lines) - 1):
        for j in xrange(i + 1, len(lines)):
            print strings.optimal_basic_alignment(lines[i], lines[j])

    # print result[0]
    # print '\n'.join(result[1:])


if __name__ == "__main__":
    main(sys.argv[1:])
