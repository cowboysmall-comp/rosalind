import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    genome = files.read_line(argv[0])
    skew   = genetics.reverse_skew_table(genome)

    print ' '.join(str(i) for i in skew[min(skew)])


if __name__ == "__main__":
    main(sys.argv[1:])
