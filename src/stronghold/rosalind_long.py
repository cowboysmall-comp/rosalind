import sys

from collections import defaultdict
from itertools   import combinations


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


def find_overlaps(dna1, dna2):
    length = min(len(dna1), len(dna2))
    total  = len(dna1) + len(dna2)

    for i in xrange(length):
        if dna1[i - length:] == dna2[:length - i]:
            combined = dna1 + dna2[length - i:]
            return (total - len(combined), combined, [dna1, dna2])
        elif dna2[i - length:] == dna1[:length - i]:
            combined = dna2 + dna1[length - i:]
            return (total - len(combined), combined, [dna1, dna2])

    return None


def main(argv):
    strings = read_fasta(argv[0]).values()

    while len(strings) > 1:
        found = []

        for combination in combinations(strings, 2):
            overlap = find_overlaps(*combination)
            if overlap:
                found.append(overlap)

        joined  = max(found)
        strings = filter(lambda x: x not in joined[2], strings)
        strings.append(joined[1])

    print '\n'.join(strings)


if __name__ == "__main__":
    main(sys.argv[1:])
