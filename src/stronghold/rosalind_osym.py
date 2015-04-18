import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings


def main(argv):
    s, t  = fasta.read_ordered(argv[0])
    m, n  = len(s), len(t)

    T1    = strings.mismatch_alignment_table(s, t)
    T2    = strings.mismatch_alignment_table(s[::-1], t[::-1])

    total = 0

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            total += T1[i - 1][j - 1] + T2[m - i][n - j] + (1 if s[i - 1] == t[j - 1] else -1)

    print T1[m][n]
    print total


if __name__ == "__main__":
    main(sys.argv[1:])
