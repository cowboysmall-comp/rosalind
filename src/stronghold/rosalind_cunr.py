import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import combinatorics


def main(argv):
    n   = files.read_int(argv[0])

    print combinatorics.double_factorial(2 * n - 5) % 1000000


if __name__ == "__main__":
    main(sys.argv[1:])
