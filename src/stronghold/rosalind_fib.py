import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import combs
import files


def main(argv):
    n, k = files.read_line_of_ints(argv[0])

    print combs.fibonacci_with_reproduction(n, k)


if __name__ == "__main__":
    main(sys.argv[1:])
