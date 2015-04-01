import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from Bio import SeqIO

from subprocess import call

import distance
import files


def best_local_alignments():
    alignments = []

    call('lalign36 -n -r "+5/-4" -E 3.0 seq_1.txt seq_2.txt > lalign_out.txt', shell = True)

    with open('lalign_out.txt') as file:
        line = file.readline()
        while line:
            if '100.0%' in line:
                file.readline()
                file.readline()
                r = file.readline().strip().split()[1]
                if 32 <= len(r) <= 40:
                    alignments.append(r)

            line = file.readline()

    os.remove('lalign_out.txt')
    os.remove('seq_1.txt')
    os.remove('seq_2.txt')

    return alignments


def sub_optimal_occurences(strings, alignments, threshold = 3):
    totals = []

    for r in alignments:
        counts  = []
        for string in strings:
            length_s = len(string)
            length_r = len(r)
            count    = 0

            for i in xrange(length_s - length_r + 1):
                if distance.hamming(string[i:i + length_r], r) <= threshold:
                    count += 1

            counts.append(count)
        totals.append(tuple(counts))

    return max(totals)


def main(argv):
    strings   = []
    sequences = SeqIO.parse(argv[0], 'fasta')

    for index, sequence in enumerate(sequences):
        strings.append(sequence.seq)
        with open('seq_%s.txt' % (index + 1), 'w') as file:
            SeqIO.write(sequence, file, 'fasta')

    alignments = best_local_alignments()
    counts     = sub_optimal_occurences(strings, alignments)

    print ' '.join(str(count) for count in counts)


if __name__ == "__main__":
    main(sys.argv[1:])
