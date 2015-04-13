import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def update_table(D, s, t, k):
    m = len(s)
    n = len(t)

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            D[i][j] = max(D[i - 1][j - 1] + (0 if s[i - 1] == t[j - 1] else -1), D[i - 1][j] - 1, D[i][j - 1] - 1)


def create_matrix(m, k):
    D = [[0 for _ in xrange(m + k + 1)] for _ in xrange(m + 1)]

    for i in xrange(1, m + 1):
        D[i][0] = -i

    for j in xrange(1, m + k + 1):
        D[0][j] = -j

    return D


def similar_motifs(s, t, k):
    m = len(s)
    n = len(t)

    D = create_matrix(m, k)
    F = []

    for i in xrange(0, n - (m + k) + 1):
        update_table(D, s, t[i:i + (m + k)], k)
        for j in xrange(m - k, m + k + 1):
            if D[m][j] >= -k:
                F.append((i + 1, j))

    return F


def main(argv):
    lines = files.read_lines(argv[0])
    k     = int(lines[0])
    s, t  = lines[1:]

    # unfinished - to be completed...

    print '\n'.join('%s %s' % f for f in similar_motifs(s, t, k))


if __name__ == "__main__":
    main(sys.argv[1:])
