import sys

from collections import defaultdict


def read_fasta(file_path):
    strings = defaultdict(str)
    labels  = []

    with open(file_path) as file:
        label = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                label = line[1:]
                labels.append(label)
            else:
                strings[label] += line

    return strings[labels[0]], strings[labels[1]]


def main(argv):
    s, t = read_fasta(argv[0])

    indices  = []
    position = 0

    for c in t:
        position = s.find(c, position) + 1
        indices.append(position)

    print ' '.join([str(i) for i in indices])


if __name__ == "__main__":
    main(sys.argv[1:])
