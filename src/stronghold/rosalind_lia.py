import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import probs


def main(argv):
    k, N  = files.read_line_of_ints(argv[0])

    print '%0.3f' % probs.mendel2(k, N, 0.25)


if __name__ == "__main__":
    main(sys.argv[1:])
