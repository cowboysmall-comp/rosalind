import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from subprocess import call

import files


def main(argv):
    call('meme %s -text -nostatus -protein -minw 20 > out.txt' % argv[0], shell = True)

    with open('out.txt') as file:
        while True:
            line = file.readline()
            if 'Motif 1 regular expression' in line:
                file.readline()
                print file.readline().strip()
                break

    os.remove('out.txt')


if __name__ == "__main__":
    main(sys.argv[1:])
