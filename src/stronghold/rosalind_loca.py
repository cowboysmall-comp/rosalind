import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import table
import strings


def main(argv):
    pam250 = table.scoring(argv[0])
    lines  = fasta.read_ordered(argv[1])
    result = strings.local_alignment(lines[0], lines[1], pam250)

    print result[0]
    print '\n'.join(r.translate(None, '-') for r in result[1:])


if __name__ == "__main__":
    main(sys.argv[1:])
