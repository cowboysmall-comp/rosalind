import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import arrays


def shortest_non_shared_substring(s1, s2):
    for i in xrange(len(s1)):
        for j in xrange(len(s1)):
            s = s1[j:j + i + 1]
            if not s in s2:
                return s

    return None


def main(argv):
    lines = files.read_lines(argv[0])

    print shortest_non_shared_substring(lines[0], lines[1])


if __name__ == "__main__":
    main(sys.argv[1:])
