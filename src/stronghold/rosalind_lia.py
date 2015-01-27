import sys
import math


def combinations(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def probability(n, r):
    return combinations(n, r) * (0.25 ** r) * (0.75 ** (n - r))


def main(argv):
    with open(argv[0]) as file:
        k, N = [int(i) for i in file.readline().split()]

        total = 2 ** k

        print '%0.3f' % (sum([probability(total, n) for n in xrange(N, total + 1)]))


if __name__ == "__main__":
    main(sys.argv[1:])
