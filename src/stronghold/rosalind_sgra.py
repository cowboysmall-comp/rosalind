import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import tables


def main(argv):
    table = tables.reverse_mass(argv[0])
    nodes = sorted(files.read_floats(argv[1]))
    edges = genetics.spectrum_graph(nodes, table)

    print genetics.longest_protein(nodes, edges)


if __name__ == "__main__":
    main(sys.argv[1:])
