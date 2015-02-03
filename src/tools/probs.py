import math
import combs


def gc(string, gc):
    count_gc = string.count('G') + string.count('C')
    count_at = string.count('A') + string.count('T')

    return ((gc / 2.0) ** count_gc) * (((1 - gc) / 2.0) ** count_at)


def binomial(n, k, p):
    return combs.combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))


def binomial_cumulative(n, k, p):
    return sum(binomial(n, r, p) for r in xrange(k, n + 1))


def mendel1(k, m, n):
    t = k + m + n

    return 1 - ((n * (n - 1)) + (n * m) + (0.25 * m * (m - 1))) / (t * (t - 1))


def mendel2(k, N, p):
    count = 2 ** k

    return sum(binomial(count, r, p) for r in xrange(N, count + 1))

