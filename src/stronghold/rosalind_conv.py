import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import multisets


def main(argv):
    S1, S2  = files.read_lines_of_floats(argv[0])

    diff    = multisets.minkowski_difference(S1, S2)
    mult    = multisets.multiplicity(diff)
    maximum = max(mult, key = mult.get)

    print mult[maximum]
    print abs(float(maximum))



if __name__ == "__main__":
    main(sys.argv[1:])
