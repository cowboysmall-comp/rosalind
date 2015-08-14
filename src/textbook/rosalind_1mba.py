import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines = files.read_ints(argv[0])
    index = lines[0]
    k     = lines[1]

    print genetics.number_to_pattern(index, k)


if __name__ == "__main__":
    main(sys.argv[1:])
