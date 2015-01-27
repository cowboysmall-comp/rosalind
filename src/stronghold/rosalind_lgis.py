import sys

from itertools import product


def longest_subsequence(seq, increasing = True):
    sub = []

    for i in xrange(len(seq)):
        if increasing:
            sub.append(max([sub[j] for j in xrange(i) if sub[j][-1] < seq[i]] or [[]], key = len) + [seq[i]])
        else:
            sub.append(max([sub[j] for j in xrange(i) if sub[j][-1] > seq[i]] or [[]], key = len) + [seq[i]])

    return max(sub, key = len)


def main(argv):
    with open(argv[0]) as file:
        n    = int(file.readline().strip())
        seq  = [int(item) for item in file.readline().split()]

        print ' '.join([str(item) for item in longest_subsequence(seq)])
        print ' '.join([str(item) for item in longest_subsequence(seq, False)])


if __name__ == "__main__":
    main(sys.argv[1:])
