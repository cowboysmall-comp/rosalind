
TRANS = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}


def hamming(s, t):
    return sum(x != y for x, y in zip(s, t))


def p(s, t):
    return sum(x != y for x, y in zip(s, t)) / float(len(s))


def edit(s, t):
    m = len(s)
    n = len(t)

    D = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]

    for i in xrange(1, m + 1):
        D[i][0] = i

    for j in xrange(1, n + 1):
        D[0][j] = j

    for j in xrange(1, n + 1):
        for i in xrange(1, m + 1):
            if s[i - 1] == t[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                D[i][j] = min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1]) + 1

    return D[m][n]


def tt_ratio(s, t):
    transition   = 0.0
    transversion = 0.0

    for x, y in zip(s, t):
        if x != y:
            if TRANS[x] == y:
                transition += 1
            else:
                transversion += 1

    return transition / transversion


def p_matrix(strings):
    N   = len(strings)
    D   = [[0.0 for _ in xrange(N)] for _ in xrange(N)]

    for i in xrange(N):
        for j in xrange(i + 1, N):
            D[i][j] = p(strings[i], strings[j])
            D[j][i] = D[i][j]

    return D
