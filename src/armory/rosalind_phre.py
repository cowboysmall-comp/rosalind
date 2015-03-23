import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from Bio import SeqIO


def main(argv):
    with open(argv[0]) as file:
        threshold = int(file.readline().strip())
        averages  = [sum(scores) / len(scores) for scores in [record.letter_annotations['phred_quality'] for record in SeqIO.parse(file, 'fastq')]]
        below     = filter(lambda x: x < threshold, averages)

        print len(below)


if __name__ == "__main__":
    main(sys.argv[1:])
