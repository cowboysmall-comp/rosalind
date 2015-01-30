import sys
import math


def read_fasta(file_path):
    rna = ''

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                rna += line

    return rna


def permutations(n, k):
    return math.factorial(n) / math.factorial(n - k)


def main(argv):
    rna = read_fasta(argv[0])

    au_max = max(rna.count('A'), rna.count('U'))
    au_min = min(rna.count('A'), rna.count('U'))

    cg_max = max(rna.count('C'), rna.count('G'))
    cg_min = min(rna.count('C'), rna.count('G'))

    print permutations(au_max, au_min) * permutations(cg_max, cg_min)


if __name__ == "__main__":
    main(sys.argv[1:])
