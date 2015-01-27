import sys


COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def dna_complement(string):
    dna = []

    for character in string:
        dna.append(COMPLEMENT[character])

    return ''.join(dna[::-1])


def read_fasta(file_path):
    dna = ''

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                dna += line

    return dna


def find_rcs(dna):
    rps  = []

    for i in xrange(4, 13):
        for j in xrange(len(dna) - i + 1):
            c = dna[j:j + i]
            if c == dna_complement(c):
                rps.append((j + 1, i))

    return sorted(rps)


def main(argv):
    dna = read_fasta(argv[0])
    rps = find_rcs(dna)

    print '\n'.join(['%s %s' % rp for rp in rps])


if __name__ == "__main__":
    main(sys.argv[1:])
