import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import combs
import files


def probability(n, r):
    return combs.combinations(n, r) * (0.25 ** r) * (0.75 ** (n - r))


def main(argv):
    k, N  = files.read_line_of_ints(argv[0])
    total = 2 ** k

    print '%0.3f' % (sum([probability(total, n) for n in xrange(N, total + 1)]))


if __name__ == "__main__":
    main(sys.argv[1:])
