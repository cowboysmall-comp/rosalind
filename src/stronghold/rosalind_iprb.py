import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def main(argv):
    k, m, n = files.read_line_of_ints(argv[0])

    t = k + m + n
    p = 1 - ((n * (n - 1)) + (n * m) + (0.25 * m * (m - 1))) / (t * (t - 1))

    print '%0.6f' % (p)


if __name__ == "__main__":
    main(sys.argv[1:])
