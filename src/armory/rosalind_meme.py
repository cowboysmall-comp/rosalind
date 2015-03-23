import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from subprocess import call


def best_scoring_motif(file_path):
    motif = None

    call('meme %s -text -protein -minw 20 -nostatus > meme_out.txt' % file_path, shell = True)

    with open('meme_out.txt') as file:
        while not motif:
            line = file.readline()
            if 'regular expression' in line:
                file.readline()
                motif = file.readline().strip()

    os.remove('meme_out.txt')

    return motif


def main(argv):
    print best_scoring_motif(argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
