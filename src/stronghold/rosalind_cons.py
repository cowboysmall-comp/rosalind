import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta


def statistics(matrix):
    rows  = len(matrix)
    cols  = len(matrix[0])

    stats = []

    for i in xrange(cols):
        col_stats = defaultdict(int)
        for j in xrange(rows):
            col_stats[matrix[j][i]] += 1
        stats.append(col_stats)

    return stats


def main(argv):
    strings = fasta.read(argv[0])
    stats   = statistics(strings.values())

    print ''.join([max(s, key = s.get) for s in stats])

    for row in ['A', 'C', 'G', 'T']:
        vals = []
        for col in stats:
            vals.append(col[row])
        print '%s: %s' % (row, ' '.join([str(val) for val in vals]))


if __name__ == "__main__":
    main(sys.argv[1:])
