import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import tree


def main(argv):
    data  = files.read_lines(argv[0])

    s     = data[0]
    k     = int(data[1])
    edges = data[2:]

    root  = tree.build_suffix_tree(s, edges)

    print max(tree.longest_substring(root, k), key = len)


if __name__ == "__main__":
    main(sys.argv[1:])
