import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    kmers = files.read_lines(argv[0])

    nodes = graphs.overlap_nodes(kmers)
    edges = graphs.overlap_edges(nodes)

    print '\n'.join('%s -> %s' % edge for edge in edges)


if __name__ == "__main__":
    main(sys.argv[1:])
