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

    return [strings[label] for label in labels]


def p_distance(s, t):
    return sum(x != y for x, y in zip(s, t)) / float(len(s))


def create_matrix(strings):
    N   = len(strings)
    D   = [[0.0 for _ in xrange(N)] for _ in xrange(N)]

    for i in xrange(N):
        for j in xrange(i + 1, N):
            D[i][j] = p_distance(strings[i], strings[j])
            D[j][i] = D[i][j]

    return D


def main(argv):
    dna = read_fasta(argv[0])

    print '\n'.join([' '.join(['%0.5f' % col for col in row]) for row in create_matrix(dna)])


if __name__ == "__main__":
    main(sys.argv[1:])
