import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from collections import defaultdict

import files


def indexed_text_array(text):
    indexed = []
    counter = defaultdict(int)

    for c in text:
        counter[c] += 1
        indexed.append((c, counter[c]))

    return indexed


def inverse_burrows_wheeler_transform(text):
    first = indexed_text_array(sorted(text))
    last  = indexed_text_array(text)
    row   = [first[0]]

    while len(row) < len(first):
        row.append(first[last.index(row[-1])])

    return ''.join(r[0] for r in row[1:] + row[:1])


def main(argv):
    text = files.read_line(argv[0])

    print inverse_burrows_wheeler_transform(text)


if __name__ == "__main__":
    main(sys.argv[1:])
