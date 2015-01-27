import sys
import re


COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def dna_complement(string):
    dna = []

    for character in string:
        dna.append(COMPLEMENT[character])

    return ''.join(dna[::-1])


def dna_to_rna(string):
    rna_string = []

    for character in string:
        if character == 'T':
            rna_string.append('U')
        else:
            rna_string.append(character)

    return ''.join(rna_string)


def codon_table(file_path):
    table = {}

    with open(file_path) as file:
        for line in file:
            items = line.strip().split()
            for key, value in zip(*[iter(items)] * 2):
                table[key] = value

    return table


def read_fasta(file_path):
    dna = ''

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                dna += line

    return dna


def encode_protein(rna, table):
    encoded = []

    for match in re.compile(r'(?=(AUG))').finditer(rna):
        sub    = rna[match.start():]
        encode = ''
        for chunk in [sub[i:i + 3] for i in xrange(0, len(sub), 3)]:
            amino = table[chunk]
            if amino != 'Stop':
                encode += amino
            else:
                encoded.append(encode)
                break

    return encoded


def main(argv):
    table   = codon_table(argv[0])
    dna     = read_fasta(argv[1])

    rna1    = dna_to_rna(dna)
    rna2    = dna_to_rna(dna_complement(dna))

    encoded = set()

    encoded.update(encode_protein(rna1, table))
    encoded.update(encode_protein(rna2, table))

    print '\n'.join(list(encoded))


if __name__ == "__main__":
    main(sys.argv[1:])
