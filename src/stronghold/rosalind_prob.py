import sys
import math


def probability(dna, a):
    total = 0

    for char in dna:
        if char in ['G', 'C']:
            total += math.log10(a) - math.log10(2)
        else:
            total += math.log10(1 - a) - math.log10(2)

    return total


def main(argv):
    with open(argv[0]) as file:
        dna = file.readline().strip()
        A   = [float(item) for item in file.readline().split()]
        B   = [probability(dna, a) for a in A]

        print ' '.join('%0.3f' % b for b in B)


if __name__ == "__main__":
    main(sys.argv[1:])
