import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    n, m, edges = files.read_graph(argv[0])
    adjacency   = graphs.adjacency_table(edges)
    D           = []

    for i in xrange(1, n + 1):
        D.append(sum(len(adjacency[node]) for node in adjacency[i]))

    print ' '.join(str(d) for d in D)


if __name__ == "__main__":
    main(sys.argv[1:])
