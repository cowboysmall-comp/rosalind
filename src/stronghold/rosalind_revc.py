import sys


COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def dna_complement(string):
    dna = []

    for character in string:
        dna.append(COMPLEMENT[character])

    return ''.join(dna[::-1])


def main(argv):
    with open(argv[0]) as file:
        print dna_complement(file.readline().strip())


if __name__ == "__main__":
    main(sys.argv[1:])
