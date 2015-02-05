import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from ete2 import Tree


def main(argv):
    lines = files.read_lines(argv[0])
    D     = [Tree(lines[i], format = 1).get_distance(*lines[i + 1].split()) for i in xrange(0, len(lines), 2)]

    print ' '.join('%d' % d for d in D)


if __name__ == "__main__":
    main(sys.argv[1:])
