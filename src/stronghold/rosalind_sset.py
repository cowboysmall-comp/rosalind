import sys


def main(argv):
    with open(argv[0]) as file:
        N = int(file.readline().strip())

        print (2 ** N) % 1000000


if __name__ == "__main__":
    main(sys.argv[1:])
