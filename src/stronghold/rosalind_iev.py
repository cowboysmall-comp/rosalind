import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def main(argv):
    nums = files.read_line_of_ints(argv[0])

    print '%0.1f' % (2 * nums[0] + 2 * nums[1] + 2 * nums[2] + 1.5 * nums[3] + 1 * nums[4])


if __name__ == "__main__":
    main(sys.argv[1:])
