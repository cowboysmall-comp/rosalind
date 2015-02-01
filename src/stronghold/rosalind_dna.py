import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    symbols = genetics.dna_count(files.read_line(argv[0]))

    print '%s %s %s %s' % (symbols['A'], symbols['C'], symbols['G'], symbols['T'])


if __name__ == "__main__":
    main(sys.argv[1:])
