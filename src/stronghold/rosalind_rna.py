import sys


def dna_to_rna(string):
    rna_string = []

    for character in string:
        if character == 'T':
            rna_string.append('U')
        else:
            rna_string.append(character)

    return ''.join(rna_string)


def main(argv):
    with open(argv[0]) as file:
        print dna_to_rna(file.readline().strip())


if __name__ == "__main__":
    main(sys.argv[1:])
