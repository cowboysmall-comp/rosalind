import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import arrays


def main(argv):
    lines = files.read_lines(argv[0])

    text  = lines[0]
    k     = int(lines[1])
    psa   = arrays.partial_suffix_array(text, k)

    print '\n'.join('%s,%s' % v for v in psa)


if __name__ == "__main__":
    main(sys.argv[1:])
