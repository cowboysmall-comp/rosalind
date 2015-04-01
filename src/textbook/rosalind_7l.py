import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from collections import defaultdict

import files


def count_matrix(last):
    row = {c: 0 for c in last}
    c   = [row.copy()]

    for l in last:
        row[l] += 1
        c.append(row.copy())

    return c


def first_occurrence_dict(first):
    fa = {}

    for f in first:
        if f not in fa:
            fa[f] = first.index(f)

    return fa


def better_burrows_wheeler_matching(pattern, last, count, first_occurrence):
    top    = 0
    bottom = len(last) - 1

    while top <= bottom:
        if pattern:
            symbol   = pattern[-1]
            pattern  = pattern[:-1]
            if symbol in last[top:bottom + 1]:
                top    = first_occurrence[symbol] + count[top][symbol]
                bottom = first_occurrence[symbol] + count[bottom + 1][symbol] - 1
            else:
                return 0
        else:
            return bottom - top + 1


def main(argv):
    lines    = files.read_lines_of_words(argv[0])

    last     = lines[0][0]
    first    = ''.join(sorted(last))
    patterns = lines[1]

    count    = count_matrix(last)
    fo       = first_occurrence_dict(first)

    matches  = []
    for pattern in patterns:
        matches.append(better_burrows_wheeler_matching(pattern, last, count, fo))

    print ' '.join(str(match) for match in matches)


if __name__ == "__main__":
    main(sys.argv[1:])
