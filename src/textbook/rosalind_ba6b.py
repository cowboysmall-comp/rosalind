import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import sorts


def main(argv):
    line  = files.read_line(argv[0])
    perm  = [int(val) for val in line[1:-1].split(' ')]

    print sorts.count_signed_breaks(perm)


if __name__ == "__main__":
    main(sys.argv[1:])
