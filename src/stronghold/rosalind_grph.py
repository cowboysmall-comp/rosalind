import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import graphs


def main(argv):
    strings = fasta.read(argv[0])
    nodes   = graphs.create_nodes(strings)
    edges   = graphs.create_edges(nodes)

    print '\n'.join(['%s %s' % (edge) for edge in edges])


if __name__ == "__main__":
    main(sys.argv[1:])
