import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import probs


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    N, m  = lines[0]
    A     = lines[1]
    B     = probs.founder_effect(A, N, m)

    print '\n'.join(' '.join(str(col) for col in row) for row in B)


if __name__ == "__main__":
    main(sys.argv[1:])
