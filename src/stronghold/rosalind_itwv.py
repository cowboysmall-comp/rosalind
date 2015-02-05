import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import strings


def main(argv):
    dna_strings = files.read_lines(argv[0])
    matrix      = strings.interwoven_matrix(dna_strings[0], dna_strings[1:])

    print '\n'.join(' '.join(str(z) for z in y) for y in matrix)


if __name__ == "__main__":
    main(sys.argv[1:])
