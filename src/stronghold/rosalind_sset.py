import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def main(argv):
    N = files.read_int(argv[0])

    print pow(2, N, 1000000)


if __name__ == "__main__":
    main(sys.argv[1:])
