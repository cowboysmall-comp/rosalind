import sys
import math


def gc_probabilty(string, gc):
    count_gc = string.count('G') + string.count('C')
    count_at = string.count('A') + string.count('T')

    return ((gc / 2.0) ** count_gc) * (((1 - gc) / 2.0) ** count_at)


def main(argv):
    with open(argv[0]) as file:
        items = file.readline().split()
        N, gc = int(items[0]), float(items[1])
        dna   = file.readline().strip()

        print '%0.3f' % (1 - ((1 - gc_probabilty(dna, gc)) ** N))


if __name__ == "__main__":
    main(sys.argv[1:])
