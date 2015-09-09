import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs

from collections import defaultdict


def main(argv):
    lines = files.read_lines(argv[0])
    edges = graphs.edges_from_adjacency_list(lines)

    # print graphs.maximal_non_branching_paths(edges)

    print '\n'.join(' -> '.join(path) for path in graphs.maximal_non_branching_paths(edges))


if __name__ == "__main__":
    # sys.setrecursionlimit(1048576)
    main(sys.argv[1:])
