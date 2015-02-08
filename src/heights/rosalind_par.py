import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import sorts


def main(argv):
    n, A = files.read_lines_of_ints(argv[0])
    A    = sorts.partition(A, 0, n[0] - 1)

    print ' '.join(str(item) for item in A)


if __name__ == "__main__":
    main(sys.argv[1:])
