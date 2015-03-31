import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import arrays
import tree


def shortest_non_shared_substring(s1, s2):
    length   = len(s1)
    shortest = []

    for i in xrange(1, length):
        for j in xrange(length - i + 1):
            s = s1[j:j + i]
            if not s in s2 and not s in shortest:
                shortest.append(s)
        if shortest: break

    return sorted(shortest)[0]


def main(argv):
    lines = files.read_lines(argv[0])

    print shortest_non_shared_substring(lines[0], lines[1])


if __name__ == "__main__":
    main(sys.argv[1:])
