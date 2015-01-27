import sys


def codon_table(file_path):
    table = {}

    with open(file_path) as file:
        for line in file:
            items = line.strip().split()
            for key, value in zip(*[iter(items)] * 2):
                table[key] = value

    return table


def encode_protein(file_path, table):
    encode = ''

    with open(file_path) as file:
        line = file.readline().strip()
        for chunk in [line[i:i + 3] for i in xrange(0, len(line), 3)]:
            amino = table[chunk]
            if amino != 'Stop':
                encode += amino
            else:
                break

    return encode


def main(argv):
    table = codon_table(argv[0])

    print encode_protein(argv[1], table)


if __name__ == "__main__":
    main(sys.argv[1:])
