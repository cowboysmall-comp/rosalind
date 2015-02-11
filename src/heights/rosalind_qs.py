import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import sorts


def main(argv):
    data = files.read_lines_of_ints(argv[0])
    n    = data[0][0]
    A    = data[1]

    print ' '.join(str(item) for item in sorts.quick_sort(A, 0, n - 1))


if __name__ == "__main__":
    main(sys.argv[1:])
