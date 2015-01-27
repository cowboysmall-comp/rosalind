import sys

from itertools import permutations


def main(argv):
    with open(argv[0]) as file:
        number = int(file.readline().strip())
        perms  = list(permutations([i + 1 for i in xrange(number)]))

        print len(perms)
        for perm in perms:
            print ' '.join([str(i) for i in perm])


if __name__ == "__main__":
    main(sys.argv[1:])
