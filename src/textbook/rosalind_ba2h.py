import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines   = files.read_lines(argv[0])
    pattern = lines[0]
    dnas    = lines[1].split()

    print genetics.sigma_distance(pattern, dnas)


if __name__ == "__main__":
    main(sys.argv[1:])
