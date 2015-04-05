import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from subprocess import call

from Bio import SeqIO

import files


def read_filtration_by_quality(p, q):
    count = 0

    call('fastq_quality_filter -q %s -p %s -i in.fastq -o out.fastq' % (p, q), shell = True)

    with open('out.fastq') as file:
        count = len([record for record in SeqIO.parse(file, 'fastq')])

    os.remove('in.fastq')
    os.remove('out.fastq')

    return count


def main(argv):
    lines = files.read_lines(argv[0])
    p, q  = lines[0].split()
    files.write_lines('in.fastq', lines[1:])

    print read_filtration_by_quality(p, q)


if __name__ == "__main__":
    main(sys.argv[1:])
