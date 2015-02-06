import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def main(argv):
    s, ints    = files.read_lines(argv[0])
    a, b, c, d = [int(i) for i in ints.split()]

    print '%s %s' % (s[a:b + 1], s[c:d + 1])


if __name__ == "__main__":
    main(sys.argv[1:])
