import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines = files.read_lines(argv[0])
    k, d  = [int(i) for i in lines[0].split()]
    dna   = lines[1:]

    print ' '.join(genetics.implanted_motifs(dna, k, d))


if __name__ == "__main__":
    main(sys.argv[1:])
