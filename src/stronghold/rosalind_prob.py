import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import probs


def main(argv):
    with open(argv[0]) as file:
        dna = file.readline().strip()
        A   = [float(item) for item in file.readline().split()]

        B   = [probs.gc_probability_cl(dna, a) for a in A]

        print ' '.join('%0.3f' % b for b in B)


if __name__ == "__main__":
    main(sys.argv[1:])
