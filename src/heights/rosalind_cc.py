import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    n, m, edges = files.read_graph(argv[0])
    nodes       = [n for n in xrange(1, n + 1)]

    print len(graphs.connected_components(nodes, edges, directed = False))


if __name__ == "__main__":
    main(sys.argv[1:])
