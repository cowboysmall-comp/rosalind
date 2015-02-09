import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    k, Gs = files.read_weighted_graphs(argv[0])
    C     = []

    for G in Gs:
        n, m    = G[:2]
        edges   = G[2]
        nodes   = [n for n in xrange(1, n + 1)]
        t, h, w = edges[0]
        C.append(graphs.dijkstra(h, nodes, edges)[t] + w)

    print ' '.join(str(d) if d != float('inf') else '-1' for d in C)



if __name__ == "__main__":
    main(sys.argv[1:])
