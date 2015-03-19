import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    spectrum = files.read_line_of_ints(argv[0])
    counts   = genetics.convolution_counts(spectrum)

    print ' '.join(str(c) for c in genetics.convolution_list(counts))


if __name__ == "__main__":
    main(sys.argv[1:])
