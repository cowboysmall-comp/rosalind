import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines   = files.read_lines(argv[0])

    pattern = lines[0]
    text    = lines[1]
    d       = int(lines[2])

    print ' '.join(str(i) for i in genetics.approximate_pattern_matching(pattern, text, d))


if __name__ == "__main__":
    main(sys.argv[1:])
