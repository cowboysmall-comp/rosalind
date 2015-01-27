import sys

from collections import defaultdict


def read_fasta(file_path):
    strings = defaultdict(str)
    labels  = []

    with open(file_path) as file:
        label = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                label = line[1:]
                labels.append(label)
            else:
                strings[label] += line

    return strings[labels[0]], [strings[label] for label in labels[1:]]


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


def encode_protein(rna, table):
    encode = ''

    for chunk in [rna[i:i + 3] for i in xrange(0, len(rna), 3)]:
        amino = table[chunk]
        if amino != 'Stop':
            encode += amino
        else:
            break

    return encode


def main(argv):
    table        = codon_table(argv[0])
    dna, introns = read_fasta(argv[1])

    for intron in introns:
        dna = dna.replace(intron, '')
    rna = dna_to_rna(dna)

    print encode_protein(rna, table)


if __name__ == "__main__":
    main(sys.argv[1:])
