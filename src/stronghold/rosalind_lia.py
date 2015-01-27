import sys
import math


def combinations(r, n):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def probability(r, n):
    return combinations(r, n) * (0.25 ** r) * (0.75 ** (n - r))


def main(argv):
    with open(argv[0]) as file:
        k, N = [int(i) for i in file.readline().split()]

        total = 2 ** k

        print '%0.3f' % (sum([probability(n, total) for n in xrange(N, total + 1)]))


if __name__ == "__main__":
    main(sys.argv[1:])
