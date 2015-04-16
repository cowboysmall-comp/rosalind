import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import phylogeny


def main(argv):
    lines  = files.read_lines(argv[0])
    taxa   = lines[0].split()

    print phylogeny.split_distance(taxa, lines[1:])


if __name__ == "__main__":
    main(sys.argv[1:])
