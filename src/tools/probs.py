import math
import combs


def gc(string, gc):
    count_gc = string.count('G') + string.count('C')
    count_at = string.count('A') + string.count('T')

    return ((gc / 2.0) ** count_gc) * (((1 - gc) / 2.0) ** count_at)


def gc_log(string, gc):
    total = 0

    for char in string:
        if char in ['G', 'C']:
            total += math.log10(gc) - math.log10(2)
        else:
            total += math.log10(1 - gc) - math.log10(2)

    return total


def mendel1(k, m, n):
    t = k + m + n

    return 1 - ((n * (n - 1)) + (n * m) + (0.25 * m * (m - 1))) / (t * (t - 1))


def mendel2(k, N, p):
    count = 2 ** k
    total = 0

    for r in xrange(N, count + 1):
        total += combs.combinations(count, r) * (p ** r) * ((1 - p) ** (count - r))

    return total
