import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import strings


def main(argv):
    lines  = files.read_lines(argv[0])
    result = strings.tripple_alignment(*lines)

    print result[0]
    print '\n'.join(result[1:])


if __name__ == "__main__":
    main(sys.argv[1:])
