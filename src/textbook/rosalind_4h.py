import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from itertools import product

import files
import genetics
import graphs


def main(argv):
    k     = files.read_int(argv[0])

    kmers = [''.join(p) for p in product('01', repeat = k)]
    edges = graphs.debruijn_graph(kmers)
    path  = graphs.eulerian_cycle(edges[0][0], edges)

    print genetics.reconstruct_circular_string_from_path(path)


if __name__ == "__main__":
    main(sys.argv[1:])
