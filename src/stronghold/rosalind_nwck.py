import sys

from ete2 import Tree


def read_data(file_path):
    data = []

    with open(file_path) as file:
        d = []

        for line in file:
            line = line.strip()

            if line:
                d.append(line)

            if len(d) == 2:
                data.append((Tree(d[0], format = 1), tuple(d[1].split())))
                d = []

    return data


def main(argv):
    D = [d[0].get_distance(*d[1]) for d in read_data(argv[0])]

    print ' '.join('%d' % d for d in D)


if __name__ == "__main__":
    main(sys.argv[1:])
