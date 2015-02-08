import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    n, m, edges = files.read_graph(argv[0])
    nodes       = [n for n in xrange(1, n + 1)]
    D           = graphs.breadth_first_search(1, nodes, edges)

    print ' '.join(str(D[n]) for n in nodes)


if __name__ == "__main__":
    main(sys.argv[1:])
