import sys


def main(argv):
    with open(argv[0]) as file:
        print int(file.readline().strip()) - 2


if __name__ == "__main__":
    main(sys.argv[1:])
