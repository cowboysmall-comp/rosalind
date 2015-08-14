import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    adjacency = files.read_lines(argv[0])

    edges     = graphs.edges_from_adjacency_list(adjacency)
    path      = graphs.eulerian_path(edges)

    print '->'.join(path)


if __name__ == "__main__":
    main(sys.argv[1:])
