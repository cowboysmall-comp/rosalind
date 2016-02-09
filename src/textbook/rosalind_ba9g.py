import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import arrays


def main(argv):
    text = files.read_line(argv[0])
    sa   = arrays.suffix_array(text)

    print ', '.join(str(v[0]) for v in sa)


if __name__ == "__main__":
    main(sys.argv[1:])
