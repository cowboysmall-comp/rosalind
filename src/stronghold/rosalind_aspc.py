import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import combinatorics


def main(argv):
    n, m = files.read_line_of_ints(argv[0])

    print sum(combinatorics.combinations(n, i) for i in xrange(m, n + 1)) % 1000000


if __name__ == "__main__":
    main(sys.argv[1:])
