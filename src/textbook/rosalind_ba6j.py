import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines   = files.read_lines(argv[0])
    edges   = [tuple([int(v) for v in c.split(', ')]) for c in lines[0][1:-1].split('), (')]
    indices = [int(i) for i in lines[1].split(', ')]

    print ', '.join(str(edge) for edge in genetics.two_break_on_genome_graph(edges, *indices))


if __name__ == "__main__":
    main(sys.argv[1:])
