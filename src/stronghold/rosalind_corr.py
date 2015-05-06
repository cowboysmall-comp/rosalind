import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import genetics


def main(argv):
    reads = fasta.read(argv[0]).values()

    print '\n'.join('%s->%s' % correction for correction in genetics.find_corrections_in_reads(reads))


if __name__ == "__main__":
    main(sys.argv[1:])
