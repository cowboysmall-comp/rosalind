import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import unionfind


def main(argv):
    n, edges = files.read_graph(argv[0])
    uf       = unionfind.QuickFind(n)

    for edge in edges:
        uf.union(edge[0], edge[1])

    print uf.count() - 1


if __name__ == "__main__":
    main(sys.argv[1:])
