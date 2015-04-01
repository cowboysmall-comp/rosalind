import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from Bio import SeqIO


def main(argv):
    with open(argv[0]) as file:
        count     = 0
        threshold = int(file.readline().strip())
        matrix    = [record.letter_annotations['phred_quality'] for record in SeqIO.parse(file, 'fastq')]

        for j in xrange(len(matrix[0])):
            length  = len(matrix)
            average = sum(matrix[i][j] for i in xrange(length)) / length
            if average < threshold:
                count += 1

        print count


if __name__ == "__main__":
    main(sys.argv[1:])
