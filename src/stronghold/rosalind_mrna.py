import sys

from collections import defaultdict


def reverse_codon_table(file_path):
    table = defaultdict(int)

    with open(file_path) as file:
        for line in file:
            items = line.strip().split()
            for key, value in zip(*[iter(items)] * 2):
                table[value] +=1

    return table


def calculate_total(file_path, table):
    total = 3

    with open(file_path) as file:
        for c in file.readline().strip():
            total *= table[c]
            total %= 1000000

    return total


def main(argv):
    table = reverse_codon_table(argv[0])

    print calculate_total(argv[1], table)


if __name__ == "__main__":
    main(sys.argv[1:])
