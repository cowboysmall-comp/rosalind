import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import sorts


def main(argv):
    line  = files.read_line(argv[0])
    perm  = [int(val) for val in line[1:-1].split(' ')]
    perms = sorts.greedy_reversal_sort(perm)[1]

    print '\n'.join('(%s)' % (' '.join('+%s' % p if p > 0 else '%s' % p for p in perm)) for perm in perms)


if __name__ == "__main__":
    main(sys.argv[1:])
