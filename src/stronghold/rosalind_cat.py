import sys


COMPLEMENT = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

def read_fasta(file_path):
    dna = ''

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                dna += line

    return dna


def check_occurences(rna):
    return rna.count('A') == rna.count('U') and rna.count('C') == rna.count('G')


def matchings(rna, start, end, A):
    if end < start:
        return 1

    if A[start][end] != -1:
        return A[start][end]
    else:
        A[start][end] = 0

        if check_occurences(rna[start:end + 1]):
            for i in xrange(start + 1, end + 1):
                if rna[start] == COMPLEMENT[rna[i]]:
                    A[start][end] += matchings(rna, start + 1, i - 1, A) * matchings(rna, i + 1, end, A) 
                    A[start][end] %= 1000000

        return A[start][end]


def main(argv):
    rna = read_fasta(argv[0])
    A   = [[-1 for _ in xrange(len(rna) + 1)] for _ in xrange(len(rna) + 1)]

    print matchings(rna, 0, len(rna) - 1, A)


if __name__ == "__main__":
    main(sys.argv[1:])
