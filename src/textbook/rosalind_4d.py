import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    kmers = files.read_lines(argv[0])

    edges = graphs.debruijn_graph(kmers)
    adj   = graphs.adjacency_table(edges)

    print '\n'.join('%s -> %s' % (head, ','.join(sorted(adj[head]))) for head in sorted(adj))


if __name__ == "__main__":
    main(sys.argv[1:])
