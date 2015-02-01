import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import combs
import files


def main(argv):
    n     = files.read_int(argv[0])
    perms = combs.enumerate_signed_permutations([i for i in xrange(1, n + 1)])

    print len(perms)
    print '\n'.join(' '.join([str(p) for p in perm]) for perm in perms)


if __name__ == "__main__":
    main(sys.argv[1:])
