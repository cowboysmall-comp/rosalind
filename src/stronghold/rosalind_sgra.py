import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from collections import defaultdict

import files
import tables


def longest_protein(nodes, edges):
    proteins = defaultdict(str)

    for node in nodes:
        for edge in filter(lambda x: x[1] == node, edges):
            if len(proteins[edge[0]]) + 1 > len(proteins[node]):
                proteins[node] = proteins[edge[0]] + edge[2]

    return max(proteins.values(), key = len)


def spectrum_graph(L, table):
    edges = []

    for i in xrange(len(L) - 1):
        for j in xrange(i, len(L)):
            found = filter(lambda x: abs(x[0] - (L[j] - L[i])) < 0.0001, table)
            if found:
                edges.append((L[i], L[j], found[0][1]))

    return edges


def main(argv):
    table = tables.reverse_mass(argv[0])
    nodes = sorted(files.read_floats(argv[1]))
    edges = spectrum_graph(nodes, table)

    print longest_protein(nodes, edges)


if __name__ == "__main__":
    main(sys.argv[1:])
