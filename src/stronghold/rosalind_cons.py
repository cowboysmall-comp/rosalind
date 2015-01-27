import sys

from collections import defaultdict


def read_fasta(file_path):
    strings = defaultdict(str)

    with open(file_path) as file:
        label = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                label = line[1:]
            else:
                strings[label] += line

    return strings


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
    strings = read_fasta(argv[0])
    stats   = statistics(strings.values())

    print ''.join([max(s, key = s.get) for s in stats])

    for row in ['A', 'C', 'G', 'T']:
        vals = []
        for col in stats:
            vals.append(col[row])
        print '%s: %s' % (row, ' '.join([str(val) for val in vals]))


if __name__ == "__main__":
    main(sys.argv[1:])
