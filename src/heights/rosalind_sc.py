import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    k, Gs = files.read_graphs(argv[0])
    sc    = []

    for G in Gs:
        n, m  = G[:2]
        edges = G[2]
        nodes = [n for n in xrange(1, n + 1)]
        sc.append(graphs.semi_connected(nodes, edges))

    print ' '.join('1' if s else '-1' for s in sc)


if __name__ == "__main__":
    sys.setrecursionlimit(1048576)
    main(sys.argv[1:])
