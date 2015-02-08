import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import permutations
import sorts


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    D = []

    for i in xrange(0, len(lines), 2):
        perm1, perm2 = lines[i:i + 2]

        final_perm   = permutations.composition(permutations.inverse(perm2), perm1)
        D.append(sorts.reversal_sort(final_perm))

    print ' '.join(str(d[0]) for d in D)


if __name__ == "__main__":
    main(sys.argv[1:])
