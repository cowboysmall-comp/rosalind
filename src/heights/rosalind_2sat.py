import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    k, Gs       = files.read_graphs(argv[0])
    assignments = []

    for G in Gs:
        n, m  = G[:2]
        edges = G[2]
        nodes = [n for n in xrange(1, n + 1)]
        assignments.append(graphs.two_satisfiable(nodes, edges))

    print '\n'.join('1 %s' % ' '.join(str(a) for a in assignment) if assignment else '0' for assignment in assignments)


if __name__ == "__main__":
    sys.setrecursionlimit(1048576)
    main(sys.argv[1:])
