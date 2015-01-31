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


def edit_distance(s, t):
    m = len(s)
    n = len(t)

    D = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]

    for i in xrange(1, m + 1):
        D[i][0] = i

    for j in xrange(1, n + 1):
        D[0][j] = j

    for j in xrange(1, n + 1):
        for i in xrange(1, m + 1):
            if s[i - 1] == t[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                D[i][j] = min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1]) + 1

    return D[m][n]


def main(argv):
    s, t = read_fasta(argv[0]).values()

    print edit_distance(s, t)
    


if __name__ == "__main__":
    main(sys.argv[1:])
