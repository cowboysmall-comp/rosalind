import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    k, Gs = files.read_graphs(argv[0])
    sinks = []

    for G in Gs:
        n, m  = G[:2]
        edges = G[2]
        nodes = [n for n in xrange(1, n + 1)]
        sinks.append(graphs.general_sink(nodes, edges))

    print ' '.join(str(sink) for sink in sinks)


if __name__ == "__main__":
    sys.setrecursionlimit(1048576)
    main(sys.argv[1:])
