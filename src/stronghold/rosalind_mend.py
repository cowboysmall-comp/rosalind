import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from ete2 import Tree


def main(argv):
    line = files.read_line(argv[0])
    tree = Tree(line, format = 1)

    # unfinished - to be completed...

    print tree


if __name__ == "__main__":
    main(sys.argv[1:])
