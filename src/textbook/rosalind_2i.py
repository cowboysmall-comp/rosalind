import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import algorithms


def main(argv):
    distances = files.read_line_of_ints(argv[0])

    print ' '.join(str(distance) for distance in algorithms.turnpike(distances))


if __name__ == "__main__":
    main(sys.argv[1:])
