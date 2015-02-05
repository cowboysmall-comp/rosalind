import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import probs
import math


def main(argv):
    n   = files.read_int(argv[0])
    N   = 2 * n

    cum = []
    for i in xrange(1, N + 1):
        cum.append(math.log10(probs.binomial_cumulative(N, i, 0.5)))

    print ' '.join('%0.3f' % val for val in cum)


if __name__ == "__main__":
    main(sys.argv[1:])
