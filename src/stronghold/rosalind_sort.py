import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import permutations


def main(argv):
    perm1, perm2     = files.read_lines_of_ints(argv[0])

    final_perm       = permutations.composition(permutations.inverse(perm2), perm1)
    count, reversals = permutations.reversal_sort(final_perm)

    print count
    print '\n'.join(' '.join(str(r) for r in reversal) for reversal in reversals)


if __name__ == "__main__":
    main(sys.argv[1:])
