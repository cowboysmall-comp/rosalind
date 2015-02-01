import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import genetics


def main(argv):
    strings = fasta.read(argv[0])
    highest = max(genetics.gc_contents(strings), key = lambda x: x[1])

    print highest[0]
    print '%0.6f' % (highest[1])


if __name__ == "__main__":
    main(sys.argv[1:])
