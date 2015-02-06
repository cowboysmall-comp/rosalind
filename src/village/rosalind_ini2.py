import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def main(argv):
    p, q = files.read_line_of_ints(argv[0])

    print p ** 2 + q ** 2


if __name__ == "__main__":
    main(sys.argv[1:])
