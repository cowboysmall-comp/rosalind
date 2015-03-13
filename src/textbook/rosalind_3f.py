import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines = files.read_lines(argv[0])
    k, t  = [int(i) for i in lines[0].split()]
    dna   = lines[1:]

    print '\n'.join(genetics.randomized_motif_search_with_iterations(dna, k, 1000, pseudocounts = True))


if __name__ == "__main__":
    main(sys.argv[1:])
