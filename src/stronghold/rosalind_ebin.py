import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def main(argv):
    lines = files.read_lines(argv[0])
    n     = int(lines[0])
    P     = [float(p) for p in lines[1].split()]

    print ' '.join(str(n * p) for p in P)


if __name__ == "__main__":
    main(sys.argv[1:])
