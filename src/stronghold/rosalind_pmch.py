import sys
import math


def read_fasta(file_path):
    dna = ''

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                dna += line

    return dna


def main(argv):
    rna = read_fasta(argv[0])

    print math.factorial(rna.count('A')) * math.factorial(rna.count('C'))


if __name__ == "__main__":
    main(sys.argv[1:])