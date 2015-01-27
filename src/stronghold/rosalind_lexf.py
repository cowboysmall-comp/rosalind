import sys

from itertools import product


def main(argv):
    with open(argv[0]) as file:
        ab   = file.readline().split()
        n    = int(file.readline().strip())

        args = [ab] * n

        print '\n'.join([''.join(p) for p in product(*args)])


if __name__ == "__main__":
    main(sys.argv[1:])
