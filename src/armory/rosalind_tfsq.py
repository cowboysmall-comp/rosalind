import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from StringIO import StringIO

from Bio import SeqIO


def main(argv):
    output = StringIO('')
    SeqIO.convert(argv[0], 'fastq', output, 'fasta')

    print output.getvalue()


if __name__ == "__main__":
    main(sys.argv[1:])
