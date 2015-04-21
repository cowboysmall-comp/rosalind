import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from itertools import product


def main(argv):
    with open(argv[0]) as file:
        alpha = file.readline().split()
        n     = int(file.readline().strip())

        perms = []
        for i in xrange(1, n + 1):
            perms.extend(product(alpha, repeat = i))

        words = []
        for p in sorted(perms, key = lambda x: [alpha.index(c) for c in x]):
            words.append(''.join(p))

        print '\n'.join(words)


if __name__ == "__main__":
    main(sys.argv[1:])
