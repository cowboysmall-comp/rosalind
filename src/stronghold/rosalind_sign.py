import sys
import math

from itertools import product


def permutations(values):
    if values:
        perms = []
        done  = []

        for value in values:

            if -value not in done:
                temp = values[:]
                temp.remove(value)

                for perm in permutations(temp):
                    perms.append([-value] + perm)

            done.append(-value)

            if value not in done:
                temp = values[:]
                temp.remove(value)

                for perm in permutations(temp):
                    perms.append([value] + perm)

            done.append(value)

        return perms
    else:
        return [[]]


def main(argv):
    with open(argv[0]) as file:
        n     = list(xrange(1, int(file.readline().strip()) + 1))
        perms = permutations(n)

        print len(perms)
        print '\n'.join(' '.join([str(p) for p in perm]) for perm in perms)


if __name__ == "__main__":
    main(sys.argv[1:])
