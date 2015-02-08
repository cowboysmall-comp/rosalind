import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import arrays


def main(argv):
    data     = files.read_lines_of_ints(argv[0])
    k        = data[0][0]
    n        = data[0][1]
    As       = data[1:]
    majority = []

    for A in As:
        candidates = [(value, key) for key, value in arrays.frequency_table(A).iteritems() if value > n / 2]
        if candidates:
            majority.append(max(candidates)[1])
        else:
            majority.append(-1)

    print ' '.join(str(majority[i]) for i in xrange(k))


if __name__ == "__main__":
    main(sys.argv[1:])
