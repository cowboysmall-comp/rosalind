import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from itertools import permutations


def main(argv):
    number = files.read_int(argv[0])
    perms  = list(permutations([i + 1 for i in xrange(number)]))

    print len(perms)
    for perm in perms:
        print ' '.join([str(i) for i in perm])


if __name__ == "__main__":
    main(sys.argv[1:])
