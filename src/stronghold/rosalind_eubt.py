import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import tree


def main(argv):
    leaves = files.read_line_of_words(argv[0])

    print '\n'.join('(%s)%s;' % (enum, leaves[0]) for enum in tree.enumerate_unrooted(leaves[1:]))


if __name__ == "__main__":
    main(sys.argv[1:])
