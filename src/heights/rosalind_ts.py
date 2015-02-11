import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    n, m, edges = files.read_graph(argv[0])
    nodes       = [n for n in xrange(1, n + 1)]
    topological = graphs.topological_sort(nodes, edges)

    print ' '.join(str(node) for node in topological)


if __name__ == "__main__":
    main(sys.argv[1:])
