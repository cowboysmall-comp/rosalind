import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import algorithms


def main(argv):
    lines = files.read_lines(argv[0])
    n, m  = [int(i) for i in lines[0].split()]

    down  = []
    for i in xrange(1, n + 1):
        down.append([int(v) for v in  lines[i].split()])

    right = []
    for j in xrange(n + 2, (2 * n) + 3):
        right.append([int(v) for v in lines[j].split()])

    print algorithms.manhattan_tourist(n, m, down, right)


if __name__ == "__main__":
    main(sys.argv[1:])
