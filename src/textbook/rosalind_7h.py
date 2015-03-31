import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import tree


def main(argv):
    lines = files.read_lines(argv[0])

    text  = lines[0]
    sa    = [int(v) for v in lines[1].split(', ')]
    lcp   = [int(v) for v in lines[2].split(', ')]

    # text = 'banana$'
    # sa   = [6, 5, 3, 1, 0, 4, 2]
    # lcp  = [0, 0, 1, 3, 0, 0, 2]

    print '\n'.join(tree.reconstruct_suffix_tree(text, sa, lcp))


if __name__ == "__main__":
    main(sys.argv[1:])
