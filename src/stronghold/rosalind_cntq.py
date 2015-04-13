import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import combinatorics


def main(argv):
    lines = files.read_lines(argv[0])
    n     = int(lines[0])

    print combinatorics.combinations(n, 4) % 1000000


if __name__ == "__main__":
    main(sys.argv[1:])
