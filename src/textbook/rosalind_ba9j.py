import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import strings


def main(argv):
    text = files.read_line(argv[0])

    print strings.inverse_burrows_wheeler_transform(text)


if __name__ == "__main__":
    main(sys.argv[1:])
