import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import re

import files
import genetics


def main(argv):
    pattern, genome = files.read_lines(argv[0])

    print ' '.join(str(i.start()) for i in re.finditer(r'(?=(%s))' % pattern, genome))


if __name__ == "__main__":
    main(sys.argv[1:])
