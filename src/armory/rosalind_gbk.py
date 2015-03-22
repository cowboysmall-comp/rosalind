import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from Bio import Entrez

import files


def main(argv):
    lines        = files.read_lines(argv[0])

    Entrez.email = "jerry@cowboysmall.com"

    search       = '(%s[Organism]) AND ("%s"[Publication Date] : "%s"[Publication Date])' % (lines[0], lines[1], lines[2])
    handle       = Entrez.esearch(db = "nucleotide", term = search)
    record       = Entrez.read(handle)

    print record['Count']


if __name__ == "__main__":
    main(sys.argv[1:])
