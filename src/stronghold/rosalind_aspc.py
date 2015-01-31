import sys
import math


def combinations(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def main(argv):
    with open(argv[0]) as file:
        n, m = [int(i) for i in file.readline().split()]

        print sum(combinations(n, i) for i in xrange(m, n + 1)) % 1000000


if __name__ == "__main__":
    main(sys.argv[1:])
