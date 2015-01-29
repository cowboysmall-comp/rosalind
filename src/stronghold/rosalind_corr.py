import sys

from collections import defaultdict


COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def complement(string):
    dna = []

    for character in string:
        dna.append(COMPLEMENT[character])

    return ''.join(dna[::-1])


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


def hamming_distance(s, t):
    return sum(x != y for x, y in zip(s, t))


def split_strings(strings):
    correct   = []
    incorrect = []

    for string in strings:
        comp = complement(string)
        if strings.count(string) + strings.count(comp) > 1:
            correct.append(string)
        else:
            incorrect.append(string)

    return correct, incorrect


def find_corrections(correct, incorrect):
    corrections = set()

    for c in correct:
        comp = complement(c)
        for i in incorrect:
            if hamming_distance(c, i) == 1:
                corrections.add((i, c))
            elif hamming_distance(comp, i) == 1:
                corrections.add((i, comp))

    return list(corrections)


def main(argv):
    correct, incorrect = split_strings(read_fasta(argv[0]).values())

    print '\n'.join('%s->%s' % correction for correction in find_corrections(correct, incorrect))


if __name__ == "__main__":
    main(sys.argv[1:])
