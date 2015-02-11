import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    k, Gs = files.read_graphs(argv[0])
    paths = []

    for G in Gs:
        n, m  = G[:2]
        edges = G[2]
        nodes = [n for n in xrange(1, n + 1)]
        paths.append(graphs.hamiltonian_path(nodes, edges))

    print '\n'.join('1 %s' % ' '.join(str(p) for p in path) if path else '-1' for path in paths)


if __name__ == "__main__":
    main(sys.argv[1:])
