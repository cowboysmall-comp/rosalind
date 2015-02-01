import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def find_indices(s, t):
    indices = []
    index   = 0

    while index < len(s):
        index = s.find(t, index)
        if index == -1:
            break
        indices.append(index + 1)
        index += 1

    return indices


def main(argv):
    s, t = files.read_lines(argv[0])

    print ' '.join([str(index) for index in find_indices(s, t)])


if __name__ == "__main__":
    main(sys.argv[1:])
