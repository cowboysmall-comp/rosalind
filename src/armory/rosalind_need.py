import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from subprocess import call

import files


def pairwise_global_alignment(id1, id2):
    score = 0

    call('needle -asequence embl:%s -bsequence embl:%s -datafile EDNAFULL -gapopen 10.0 -gapextend 1.0 -endweight -endopen 10.0 -endextend 1.0 -aformat pair -outfile needle_out.txt' % (id1, id2), shell = True)

    with open('needle_out.txt') as file:
        while not score:
            line = file.readline()
            if 'Score' in line:
                score = int(line.split(':')[1].strip().split('.')[0])

    os.remove('needle_out.txt')

    return score


def main(argv):
    id1, id2 = files.read_line_of_words(argv[0])

    print pairwise_global_alignment(id1, id2)


if __name__ == "__main__":
    main(sys.argv[1:])
