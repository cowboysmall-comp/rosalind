import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    line       = files.read_line(argv[0])
    chromosome = [int(val) for val in line[1:-1].split(' ')]

    print '(%s)' % ' '.join(str(c) for c in genetics.chromosome_to_cycle(chromosome))


if __name__ == "__main__":
    main(sys.argv[1:])
