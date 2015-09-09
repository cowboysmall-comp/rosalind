import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import sorts


def main(argv):
    line   = files.read_line(argv[0])
    edges  = [tuple(int(node) for node in edge.split(', ')) for edge in line[1:-1].split('), (')]
    genome = sorts.graph_to_genome(edges)

    print ''.join('(%s)' % (' '.join('+%s' % p if p > 0 else '%s' % p for p in g)) for g in genome)


if __name__ == "__main__":
    main(sys.argv[1:])
