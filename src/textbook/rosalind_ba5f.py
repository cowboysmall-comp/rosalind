import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import strings
import table


def main(argv):
    pam250 = table.scoring(argv[0])
    lines  = files.read_lines(argv[1])
    result = strings.local_alignment(lines[0], lines[1], pam250)

    print result[0]
    print '\n'.join(result[1:])


if __name__ == "__main__":
    main(sys.argv[1:])
