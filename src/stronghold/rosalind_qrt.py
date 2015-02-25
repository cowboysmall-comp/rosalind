import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from itertools import combinations, product

import files
import multisets


def main(argv):
    lines = files.read_lines(argv[0])
    taxa  = lines[0].split()
    table = lines[1:]
    Q     = set()

    for t in table:
        A     = [taxa[i] for i in xrange(len(t)) if t[i] == '1']
        B     = [taxa[i] for i in xrange(len(t)) if t[i] == '0']

        for p in product(combinations(A, 2), combinations(B, 2)):
            Q.add(frozenset(p))

    print '\n'.join('{%s, %s} {%s, %s}' % (a1, a2, b1, b2) for ((a1, a2), (b1, b2)) in Q)


if __name__ == "__main__":
    main(sys.argv[1:])
