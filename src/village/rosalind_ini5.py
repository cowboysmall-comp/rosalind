import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def main(argv):
    lines = files.read_lines(argv[0])

    files.write_lines(argv[1], [lines[i] for i in xrange(1, len(lines), 2)])


if __name__ == "__main__":
    main(sys.argv[1:])
