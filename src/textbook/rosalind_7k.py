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


def last_to_first(first, last):
    ltof  = {}

    for index in xrange(len(last)):
        ltof[index] = first.index(last[index])

    return ltof


def burrows_wheeler_matching(pattern, first, last, ltof):
    top    = 0
    bottom = len(last) - 1

    while top <= bottom:
        if pattern:
            symbol   = pattern[-1]
            pattern  = pattern[:-1]

            itop     = top
            ibottom  = bottom

            if symbol in [s[0] for s in last[top:bottom + 1]]:

                for i in xrange(top, bottom + 1):
                    if last[i][0] == symbol:
                        itop = i
                        break

                for i in xrange(bottom, top - 1, -1):
                    if last[i][0] == symbol:
                        ibottom = i
                        break

                top    = ltof[itop]
                bottom = ltof[ibottom]
            else:
                return 0
        else:
            return bottom - top + 1


def main(argv):
    lines    = files.read_lines_of_words(argv[0])
    text     = lines[0][0]
    patterns = lines[1]

    first    = indexed_text_array(sorted(text))
    last     = indexed_text_array(text)
    ltof     = last_to_first(first, last)

    matches  = []
    for pattern in patterns:
        matches.append(burrows_wheeler_matching(pattern, first, last, ltof))

    print ' '.join(str(match) for match in matches)


if __name__ == "__main__":
    main(sys.argv[1:])
