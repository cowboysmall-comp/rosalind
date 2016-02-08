import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import graphs


def main(argv):
    kmers   = files.read_lines(argv[0])
    edges   = graphs.debruijn_graph(kmers)
    maximal = graphs.maximal_non_branching_paths(edges)

    print ' '.join(genetics.reconstruct_strings_from_maximal_paths(maximal))


if __name__ == "__main__":
    main(sys.argv[1:])
