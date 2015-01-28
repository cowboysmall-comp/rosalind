import sys


def find_indexes(s, t):
    indexes = []
    index   = 0

    while index < len(s):
        index = s.find(t, index)
        if index == -1:
            break
        indexes.append(index + 1)
        index += 1

    return indexes


def main(argv):
    with open(argv[0]) as file:
        s = file.readline().strip()
        t = file.readline().strip()

        print ' '.join([str(index) for index in find_indexes(s, t)])


if __name__ == "__main__":
    main(sys.argv[1:])