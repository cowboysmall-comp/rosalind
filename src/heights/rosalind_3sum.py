import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import sorts
import searches

from collections import defaultdict


def three_sum(A):
    H = defaultdict(list)

    for i, e in enumerate(A):
        H[e].append(i)

    for i in xrange(len(A)):
        for j in xrange(len(A)):
            h = (A[i] + A[j])
            if -h in H:
                return sorted([H[A[i]][-1] + 1, H[A[j]][-1] + 1, H[-h][-1] + 1])

    return []


def main(argv):
    data    = files.read_lines_of_ints(argv[0])
    k, n    = data[0]
    As      = data[1:]

    results = [three_sum(A) for A in As]

    print '\n'.join('%s %s %s' % (result[0], result[1], result[2]) if result else '-1' for result in results)


if __name__ == "__main__":
    main(sys.argv[1:])
