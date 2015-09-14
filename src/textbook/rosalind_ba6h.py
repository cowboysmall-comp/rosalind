import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import sorts


def main(argv):
    line   = files.read_line(argv[0])
    genome = [[int(val) for val in chromosome.split(' ')] for chromosome in line[1:-1].split(')(')]

    print ', '.join(str(c) for c in sorts.colored_edges(genome))
    print ', '.join(str(c) for c in sorts.black_edges(genome))


if __name__ == "__main__":
    main(sys.argv[1:])
