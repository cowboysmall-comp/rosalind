import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import graphs


def main(argv):
    lines = files.read_lines(argv[0])
    k     = int(lines[0])
    kmers = lines[1:]

    edges = graphs.debruijn_graph(kmers)
    path  = graphs.eulerian_path(edges)

    print genetics.reconstruct_string_from_path(path)


if __name__ == "__main__":
    main(sys.argv[1:])
