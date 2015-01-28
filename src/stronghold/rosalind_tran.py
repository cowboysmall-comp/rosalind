import sys

from collections import defaultdict


TRANS = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}

def read_fasta(file_path):
    strings = defaultdict(str)

    with open(file_path) as file:
        label = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                label = line[1:]
            else:
                strings[label] += line

    return strings


def calculate_ratio(s, t):
    transition   = 0.0
    transversion = 0.0

    for x, y in zip(s, t):
        if x != y:
            if TRANS[x] == y:
                transition += 1
            else:
                transversion += 1

    return transition / transversion


def main(argv):
    strings = read_fasta(argv[0]).values()

    print calculate_ratio(strings[0], strings[1])


if __name__ == "__main__":
    main(sys.argv[1:])
