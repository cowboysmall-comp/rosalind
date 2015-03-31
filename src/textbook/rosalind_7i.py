import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def burrows_wheeler_transform(text):
    matrix = []

    for i in xrange(len(text)):
        matrix.append(text[-i:] + text[:-i])

    return ''.join(row[-1] for row in sorted(matrix))


def main(argv):
    text = files.read_line(argv[0])

    print burrows_wheeler_transform(text)


if __name__ == "__main__":
    main(sys.argv[1:])
