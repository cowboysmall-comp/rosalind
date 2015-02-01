import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta


def find_indices(s, t):
    indices = []
    index   = 0

    for c in t:
        index = s.find(c, index) + 1
        indices.append(index)

    return indices


def main(argv):
    s, t = fasta.read_ordered(argv[0])

    print ' '.join([str(i) for i in find_indices(s, t)])


if __name__ == "__main__":
    main(sys.argv[1:])
