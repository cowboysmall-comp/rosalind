import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import sorts
import searches

from collections import defaultdict


def two_sum(A):
    H = defaultdict(list)

    for i, e in enumerate(A):
        H[e].append(i)

    if 0 in H and len(H[0]) > 1:
        return sorted([H[0][-1] + 1, H[0][-2] + 1])

    for h in A:
        if -h in H:
            if h != -h:
                return sorted([H[h][-1] + 1, H[-h][-1] + 1])

    return []


def main(argv):
    data    = files.read_lines_of_ints(argv[0])
    k, n    = data[0]
    As      = data[1:]

    results = [two_sum(A) for A in As]

    print '\n'.join('-1' if len(result) == 0 else '%s %s' % (result[0], result[1]) for result in results)


if __name__ == "__main__":
    main(sys.argv[1:])
