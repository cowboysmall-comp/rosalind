import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def main(argv):
    a, b = files.read_line_of_ints(argv[0])

    print sum(i for i in xrange(a, b + 1) if i % 2 == 1)


if __name__ == "__main__":
    main(sys.argv[1:])
