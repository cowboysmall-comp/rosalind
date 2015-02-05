import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import combinatorics


def main(argv):
    n, k = files.read_line_of_ints(argv[0])

    print combinatorics.permutations(n, k) % 1000000


if __name__ == "__main__":
    main(sys.argv[1:])
