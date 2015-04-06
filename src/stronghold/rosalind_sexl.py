import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import math


def main(argv):
    A = files.read_line_of_floats(argv[0])
    B = [2 * a * (1 - a) for a in A]

    print ' '.join('%0.3g' % b for b in B)


if __name__ == "__main__":
    main(sys.argv[1:])
