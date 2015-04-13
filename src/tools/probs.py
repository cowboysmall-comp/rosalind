import math

import numpy as np

import combinatorics


def gc(string, gc):
    count_gc = string.count('G') + string.count('C')
    count_at = string.count('A') + string.count('T')

    return ((gc / 2.0) ** count_gc) * (((1 - gc) / 2.0) ** count_at)


def binomial(n, k, p):
    return combinatorics.combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))


def binomial_cumulative(n, k, p):
    return sum(binomial(n, r, p) for r in xrange(k, n + 1))


def mendel1(k, m, n):
    t = k + m + n

    return 1 - ((n * (n - 1)) + (n * m) + (0.25 * m * (m - 1))) / (t * (t - 1))


def mendel2(k, N, p):
    count = 2 ** k

    return sum(binomial(count, r, p) for r in xrange(N, count + 1))


def genetic_drift(N, m, g):
    T    = np.zeros(((2 * N) + 1, (2 * N) + 1))

    for i in xrange((2 * N) + 1):
        for j in xrange((2 * N) + 1):
            T[j, i] = binomial(2 * N, j, i / (2.0 * N))

    S    = np.zeros(((2 * N) + 1))
    S[m] = 1

    for _ in xrange(g):
        S = T.dot(S)

    return S


def founder_effect(A, N, m):
    T      = np.zeros(((2 * N) + 1, (2 * N) + 1))

    for i in xrange((2 * N) + 1):
        for j in xrange((2 * N) + 1):
            T[j, i] = binomial(2 * N, j, i / (2.0 * N))

    length = len(A)
    B      = [[0 for _ in xrange(length)] for _ in xrange(m)]

    for i in xrange(length):
        c    = A[i]

        S    = np.zeros(((2 * N) + 1))
        S[c] = 1

        for j in xrange(m):
            S       = T.dot(S)
            B[j][i] = math.log10(S[0])

    return B


