import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from collections import defaultdict


def main(argv):
    words = files.read_line_of_words(argv[0])
    freq  = defaultdict(int)

    for word in words:
        freq[word] += 1



    print '\n'.join('%s %s' % (key, value) for key, value in freq.items())


if __name__ == "__main__":
    main(sys.argv[1:])
