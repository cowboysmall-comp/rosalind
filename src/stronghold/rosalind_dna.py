import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from collections import defaultdict


def dna_count(string):
    symbols = defaultdict(int)

    for character in string:
        symbols[character] += 1    

    return symbols


def main(argv):
    symbols = dna_count(files.read_line(argv[0]))

    print '%s %s %s %s' % (symbols['A'], symbols['C'], symbols['G'], symbols['T'])


if __name__ == "__main__":
    main(sys.argv[1:])
