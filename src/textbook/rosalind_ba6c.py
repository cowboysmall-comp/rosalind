import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import sorts


def main(argv):
    lines = files.read_lines(argv[0])
    P, Q  = [[[int(val) for val in chromosome.split(' ')] for chromosome in line[1:-1].split(')(')] for line in lines]

    print sorts.two_break_distance(P, Q)


if __name__ == "__main__":
    main(sys.argv[1:])
