import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import combinatorics


def main(argv):
    print combinatorics.fibonacci(files.read_int(argv[0]))


if __name__ == "__main__":
    main(sys.argv[1:])
