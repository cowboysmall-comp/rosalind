import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import sorts


def main(argv):
    data = files.read_lines_of_ints(argv[0])

    print ' '.join(str(item) for item in sorts.merge(data[1], data[3]))


if __name__ == "__main__":
    main(sys.argv[1:])
