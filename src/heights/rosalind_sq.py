import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    k, Gs  = files.read_graphs(argv[0])
    cycles = []

    for G in Gs:
        n, m  = G[:2]
        edges = G[2]
        A     = graphs.adjacency_matrix(n, edges, directed = False)
        cycles.append(graphs.has_4cycles(A))

    print ' '.join('1' if cycles[n] else '-1' for n in xrange(k))


if __name__ == "__main__":
    main(sys.argv[1:])
