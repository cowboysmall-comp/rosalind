import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import distance
import genetics


def split_strings(strings):
    correct   = []
    incorrect = []

    for string in strings:
        comp = genetics.dna_complement(string)
        if strings.count(string) + strings.count(comp) > 1:
            correct.append(string)
        else:
            incorrect.append(string)

    return correct, incorrect


def find_corrections(correct, incorrect):
    corrections = set()

    for c in correct:
        comp = genetics.dna_complement(c)
        for i in incorrect:
            if distance.hamming(c, i) == 1:
                corrections.add((i, c))
            elif distance.hamming(comp, i) == 1:
                corrections.add((i, comp))

    return list(corrections)


def main(argv):
    correct, incorrect = split_strings(fasta.read(argv[0]).values())

    print '\n'.join('%s->%s' % correction for correction in find_corrections(correct, incorrect))


if __name__ == "__main__":
    main(sys.argv[1:])
