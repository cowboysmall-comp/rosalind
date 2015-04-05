import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from Bio import Entrez, SeqIO

import files


def main(argv):
    ids          = files.read_line_of_words(argv[0])

    Entrez.email = "jerry@cowboysmall.com"

    handle       = Entrez.efetch(db = 'nucleotide', id = ids, rettype = 'fasta')
    records      = SeqIO.parse(handle, 'fasta')
    shortest     = min(records, key = len)

    print shortest.format('fasta')


if __name__ == "__main__":
    main(sys.argv[1:])
