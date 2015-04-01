import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from Bio.Seq      import translate, CodonTable, Seq
from Bio.Alphabet import IUPAC

import re

import files


def main(argv):
    line     = files.read_line(argv[0])
    length   = len(line)
    orfs     = []

    sequence = Seq(line, IUPAC.unambiguous_dna)
    string   = str(sequence)
    for pos in re.finditer('ATG', string):
        start = pos.start()
        end   = length - ((length - start) % 3)
        orfs.append(translate(string[start:end], to_stop = True))

    sequence = sequence.reverse_complement()
    string   = str(sequence)
    for pos in re.finditer('ATG', string):
        start = pos.start()
        end   = length - ((length - start) % 3)
        orfs.append(translate(string[start:end], to_stop = True))

    print max(orfs, key = len)


if __name__ == "__main__":
    main(sys.argv[1:])
