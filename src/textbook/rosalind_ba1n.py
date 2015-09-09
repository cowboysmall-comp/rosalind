import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines = files.read_lines(argv[0])
    dna   = lines[0]
    d     = int(lines[1])

    print '\n'.join(genetics.neighbourhood(dna, d))


if __name__ == "__main__":
    main(sys.argv[1:])
