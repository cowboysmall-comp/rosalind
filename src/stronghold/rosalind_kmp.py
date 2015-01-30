import sys


def read_fasta(file_path):
    dna = ''

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                dna += line

    return dna


def compute_kmp(dna):
    N   = len(dna)
    T   = [0] * N

    pos = 1
    idx = 0
    while pos < N:
        if dna[pos] == dna[idx]:
            idx   += 1
            T[pos] = idx
            pos   += 1
        elif idx > 0:
            idx    = T[idx - 1]
        else:
            pos   += 1

    return T


def main(argv):
    dna = read_fasta(argv[0])

    print ' '.join(str(entry) for entry in compute_kmp(dna))


if __name__ == "__main__":
    main(sys.argv[1:])
