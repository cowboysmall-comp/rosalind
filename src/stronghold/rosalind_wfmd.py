import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import probs


def main(argv):
    N, m, g, k = files.read_line_of_ints(argv[0])

    state      = probs.genetic_drift(N, m, g)
    length     = len(state)

    print '%0.3f' % sum(state[:length - k])
    print '%0.3f' % (1 - sum(state[length - k:]))


if __name__ == "__main__":
    main(sys.argv[1:])
