import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    k, Gs = files.read_weighted_graphs(argv[0])
    D     = []

    for G in Gs:
        n, m    = G[:2]
        edges   = G[2]
        nodes   = [n for n in xrange(1, n + 1)]
        t, h, w = edges[0]
        D.append(graphs.negative_weight_cycle(nodes, edges))

    print ' '.join('1' if d else '-1' for d in D)



if __name__ == "__main__":
    main(sys.argv[1:])
