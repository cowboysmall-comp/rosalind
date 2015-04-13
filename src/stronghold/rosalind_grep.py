import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    reads   = files.read_lines(argv[0])
    strings = genetics.assemble_genome_from_reads_with_repeats(reads)

    print '\n'.join(sorted(strings))


if __name__ == "__main__":
    main(sys.argv[1:])
