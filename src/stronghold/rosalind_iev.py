import sys


def main(argv):
    with open(argv[0]) as file:
        numbers = [int(i) for i in file.readline().split()]

        p = 2 * numbers[0] + 2 * numbers[1] + 2 * numbers[2] + 1.5 * numbers[3] + 1 * numbers[4]

        print '%0.1f' % (p)


if __name__ == "__main__":
    main(sys.argv[1:])
