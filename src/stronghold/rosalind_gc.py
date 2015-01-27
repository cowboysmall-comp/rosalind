import sys

from collections import defaultdict


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


def gc_content(dna_strings):
    max_count = 0
    max_label = None

    for label, string in dna_strings.iteritems():
        count = 100 * float(string.count('G') + string.count('C')) / len(string)
        if max_count < count:
            max_count = count
            max_label = label

    return max_count, max_label


def main(argv):
    dna_strings  = read_fasta(argv[0])
    count, label = gc_content(dna_strings)

    print label
    print '%0.6f' % (count)


if __name__ == "__main__":
    main(sys.argv[1:])
