import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import selects


def main(argv):
    data = files.read_lines_of_ints(argv[0])
    n    = data[0][0]
    A    = data[1]
    k    = data[2][0]

    print selects.quick_select(A, k - 1)


if __name__ == "__main__":
    main(sys.argv[1:])
