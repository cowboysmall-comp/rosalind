import sys


def hamming_distance(s, t):
    return sum(x != y for x, y in zip(s, t))


def main(argv):
    with open(argv[0]) as file:
        s = file.readline().strip()
        t = file.readline().strip()

        print hamming_distance(s, t)


if __name__ == "__main__":
    main(sys.argv[1:])
