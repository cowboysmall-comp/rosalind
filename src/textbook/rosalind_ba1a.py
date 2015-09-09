import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import permutations
import sorts


def pattern_match(text, pattern):
    t = len(text)
    p = len(pattern)
    c = 0

    for i in xrange(t - p + 1):
        if text[i:i + p] == pattern:
            c += 1

    return c


def main(argv):
    lines = files.read_lines(argv[0])

    print pattern_match(lines[0], lines[1])


if __name__ == "__main__":
    main(sys.argv[1:])
