import sys

from collections import defaultdict


def dna_count(string):
    symbols = defaultdict(int)

    for character in string:
        symbols[character] += 1    

    return symbols


def main(argv):
    with open(argv[0]) as file:
        symbols = dna_count(file.readline().strip())

        print '%s %s %s %s' % (symbols['A'], symbols['C'], symbols['G'], symbols['T'])


if __name__ == "__main__":
    main(sys.argv[1:])
