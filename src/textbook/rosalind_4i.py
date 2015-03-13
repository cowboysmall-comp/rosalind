import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import graphs


def main(argv):
    lines  = files.read_lines(argv[0])
    k, d   = [int(i) for i in lines[0].split()]

    pairs  = genetics.paired_kmers(lines[1:])
    edges  = graphs.debruijn_paired_graph(pairs)
    path   = graphs.eulerian_paired_path(edges, k, d)

    print genetics.reconstruct_string_from_paired_path(path, k, d)


if __name__ == "__main__":
    sys.setrecursionlimit(1048576)
    main(sys.argv[1:])
