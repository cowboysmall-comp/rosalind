import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import graphs


def main(argv):
    lines = files.read_lines(argv[0])
    k     = int(lines[0])
    text  = lines[1]

    kmers = genetics.list_kmers(text, k)
    edges = graphs.debruijn_graph(kmers)
    adj   = graphs.adjacency_table(edges)

    print '\n'.join('%s -> %s' % (head, ','.join(sorted(adj[head]))) for head in sorted(adj))


if __name__ == "__main__":
    main(sys.argv[1:])
