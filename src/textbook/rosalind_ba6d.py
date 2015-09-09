import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import permutations
import sorts


def two_break_sort(P, Q):
    D = 0
    L = [P]

    for k in xrange(len(P)):
        if abs(P[k]) != Q[k]:
            l  = P.index(Q[k]) if Q[k] in P else P.index(-Q[k])
            P  = P[:k] + [-p for p in P[k:l + 1][::-1]] + P[l + 1:]
            D += 1
            L.append(P)
        if P[k] == -Q[k]:
            P  = P[:k] + [-P[k]] + P[k + 1:]
            D += 1
            L.append(P)

    return D, L


def main(argv):
    lines = files.read_lines(argv[0])

    P     = [int(val) for val in lines[0][1:-1].split(' ')]
    Q     = [int(val) for val in lines[1][1:-1].split(' ')]

    D, L  = two_break_sort(P, Q)

    print '\n'.join('(%s)' % ' '.join('+%s' % c if c > 0 else '%s' % c for c in m) for m in L)


if __name__ == "__main__":
    main(sys.argv[1:])
