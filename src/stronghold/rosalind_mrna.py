import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import tables
import files


def calculate_total(string, table):
    total = 3

    for c in string:
        total *= table[c]
        total %= 1000000

    return total


def main(argv):
    table  = tables.reverse_codon(argv[0])
    string = files.read_line(argv[1])

    print calculate_total(string, table)


if __name__ == "__main__":
    main(sys.argv[1:])
