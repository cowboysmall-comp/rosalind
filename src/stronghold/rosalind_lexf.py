import sys

from itertools import product


def main(argv):
    with open(argv[0]) as file:
        alpha = file.readline().split()
        n     = int(file.readline().strip())

        print '\n'.join(''.join(p) for p in product(alpha, repeat = n))


if __name__ == "__main__":
    main(sys.argv[1:])
