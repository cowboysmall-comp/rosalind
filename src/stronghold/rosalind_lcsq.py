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


def sequence_table(s, t):
    m = len(s)
    n = len(t)

    C = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            if s[i - 1] == t[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])

    return C


def read_sequence(C, s, t):
    m = len(s)
    n = len(t)

    sequence = []

    while m != 0 and n != 0:
        if C[m][n] == C[m - 1][n]:
            m -= 1
        elif C[m][n] == C[m][n - 1]:
            n -= 1

        if s[m - 1] == t[n - 1]:
            sequence.insert(0, s[m - 1])
            m -= 1
            n -= 1

    return ''.join(sequence)


def main(argv):
    s, t = read_fasta(argv[0]).values()
    C    = sequence_table(s, t)

    print read_sequence(C, s, t)


if __name__ == "__main__":
    main(sys.argv[1:])
