import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    n, m, edges = files.read_weighted_graph(argv[0])
    nodes       = [n for n in xrange(1, n + 1)]
    D, P        = graphs.shortest_path(1, nodes, edges)

    print ' '.join(str(D[node]) if D[node] != float('inf') else 'x' for node in nodes)


if __name__ == "__main__":
    main(sys.argv[1:])
