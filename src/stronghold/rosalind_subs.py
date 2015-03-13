import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import strings


def main(argv):
    s, t = files.read_lines(argv[0])

    print ' '.join(str(i) for i in strings.find_indices_of_substrings(s, t))


if __name__ == "__main__":
    main(sys.argv[1:])
