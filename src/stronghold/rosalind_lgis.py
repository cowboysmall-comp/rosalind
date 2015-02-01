import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import strings


def main(argv):
    with open(argv[0]) as file:
        n    = int(file.readline().strip())
        seq  = [int(item) for item in file.readline().split()]

        print ' '.join([str(item) for item in strings.longest_subsequence(seq)])
        print ' '.join([str(item) for item in strings.longest_subsequence(seq, False)])


if __name__ == "__main__":
    main(sys.argv[1:])
