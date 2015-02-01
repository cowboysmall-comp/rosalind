import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import probs


def main(argv):
    with open(argv[0]) as file:
        items = file.readline().split()
        N, gc = int(items[0]), float(items[1])
        dna   = file.readline().strip()

        print '%0.3f' % ( 1 - ( ( 1 - probs.gc(dna, gc) ) ** N ) )


if __name__ == "__main__":
    main(sys.argv[1:])
