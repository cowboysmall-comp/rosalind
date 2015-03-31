import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from subprocess import call

from Bio import ExPASy
from Bio import SwissProt
from Bio import SeqIO

import files


def pairwise_local_alignment(id1, id2):
    score = 0

    call('water -asequence %s.txt -bsequence %s.txt -datafile EBLOSUM62 -gapopen 10.0 -gapextend 1.0 -aformat pair -outfile water_out.txt' % (id1, id2), shell = True)

    with open('water_out.txt') as file:
        while not score:
            line = file.readline()
            if 'Score' in line:
                score = int(line.split(':')[1].strip().split('.')[0])

    os.remove('water_out.txt')

    return score


def write_to_file(identifier):
    handle = ExPASy.get_sprot_raw(identifier)
    record = SeqIO.read(handle, 'swiss')

    with open('%s.txt' % identifier, 'w') as file:
        SeqIO.write(record, file, 'fasta')

    handle.close()


def main(argv):
    identifiers = files.read_line_of_words(argv[0])

    for identifier in identifiers:
        write_to_file(identifier)

    print pairwise_local_alignment(identifiers[0], identifiers[1])


if __name__ == "__main__":
    main(sys.argv[1:])
