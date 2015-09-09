import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    pattern, genome = files.read_lines(argv[0])

    print ' '.join(str(i) for i in genetics.kmer_occurences(genome, pattern))


if __name__ == "__main__":
    main(sys.argv[1:])
