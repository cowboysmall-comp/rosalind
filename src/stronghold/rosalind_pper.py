import sys
import math


def permutations(n, k):
    return math.factorial(n) / math.factorial(n - k)


def main(argv):
    with open(argv[0]) as file:
        n, k = file.readline().strip().split()

        print permutations(int(n), int(k)) % 1000000


if __name__ == "__main__":
    main(sys.argv[1:])
