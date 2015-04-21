import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    S     = files.read_lines(argv[0])
    nodes = set()
    edges = set()

    for s in S:
        nodes.add(s[:-1])
        nodes.add(s[1:])
        edges.add((s[:-1], s[1:]))

    print ''.join(node[-1] for node in graphs.topological_sort(nodes, edges))


if __name__ == "__main__":
    sys.setrecursionlimit(1048576)
    main(sys.argv[1:])
