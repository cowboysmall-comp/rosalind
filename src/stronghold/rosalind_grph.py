import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta


def create_nodes(strings):
    nodes = []

    for label, string in strings.iteritems():
        nodes.append((label, string[:3], string[-3:], string))

    return nodes


def create_edges(nodes):
    edges = []

    for node in nodes:
        for tail in filter(lambda x: x[1] == node[2] and x != node, nodes):
            edges.append((node[0], tail[0]))

    return edges


def main(argv):
    strings = fasta.read(argv[0])
    nodes   = create_nodes(strings)
    edges   = create_edges(nodes)

    print '\n'.join(['%s %s' % (edge) for edge in edges])


if __name__ == "__main__":
    main(sys.argv[1:])
