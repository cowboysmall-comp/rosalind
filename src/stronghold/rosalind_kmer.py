import sys
import re

from itertools import product


def read_fasta(file_path):
    dna = ''

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                dna += line

    return dna


def main(argv):
    dna   = read_fasta(argv[0])
    kmers = [''.join(p) for p in product(*[['A', 'C', 'G', 'T']] * 4)]

    A = []
    for kmer in kmers:
        A.append(len(re.findall(r'(?=(%s))' % kmer, dna)))

    print ' '.join(str(a) for a in A)


if __name__ == "__main__":
    main(sys.argv[1:])
