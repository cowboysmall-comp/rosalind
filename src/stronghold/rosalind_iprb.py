import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import probs


def main(argv):
    k, m, n = files.read_line_of_ints(argv[0])

    print '%0.6f' % probs.mendel1(k, m, n)


if __name__ == "__main__":
    main(sys.argv[1:])
