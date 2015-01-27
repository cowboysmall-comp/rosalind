import sys


def mass_table(file_path):
    table = {}

    with open(file_path) as file:
        for line in file:
            key, value = line.strip().split()
            table[key] = float(value)

    return table


def calculate_weight(file_path, table):
    total = 0.0

    with open(file_path) as file:
        line = file.readline().strip()
        for c in line:
            total += table[c]

    return total



def main(argv):
    table = mass_table(argv[0])

    print '%0.3f' % (calculate_weight(argv[1], table))


if __name__ == "__main__":
    main(sys.argv[1:])
