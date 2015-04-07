import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings


def main(argv):
    s, t = fasta.read_ordered(argv[0])
    m, n = len(s), len(t)
    C    = strings.longest_common_subsequence_table(s, t)

    print m + n - (2 * C[m][n])


if __name__ == "__main__":
    main(sys.argv[1:])
