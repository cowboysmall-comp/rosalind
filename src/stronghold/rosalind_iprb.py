import sys


def main(argv):
    with open(argv[0]) as file:
        k, m, n = [int(i) for i in file.readline().split()]

        t = k + m + n
        p = 1 - ((n * (n - 1)) + (n * m) + (0.25 * m * (m - 1))) / (t * (t - 1))

        print '%0.6f' % (p)


if __name__ == "__main__":
    main(sys.argv[1:])