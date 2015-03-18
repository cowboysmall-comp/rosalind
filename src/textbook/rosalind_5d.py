import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    lines  = files.read_lines(argv[0])

    source = lines[0]
    sink   = lines[1]

    edges  = graphs.weighted_edges(lines[2:])
    nodes  = graphs.nodes_from_edges(edges)
    D, P   = graphs.longest_path(source, nodes, edges)

    print D[sink]
    print '->'.join(graphs.construct_path_from_predecessors(source, sink, P))


if __name__ == "__main__":
    main(sys.argv[1:])
