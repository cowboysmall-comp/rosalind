import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import sorts


def main(argv):
    data = files.read_lines_of_ints(argv[0])

    print ' '.join(str(item) for item in sorts.merge_sort(data[1])[0])


if __name__ == "__main__":
    main(sys.argv[1:])
