import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    line  = files.read_line(argv[0])
    cycle = [int(val) for val in line[1:-1].split(' ')]

    print '(%s)' % ' '.join('+%s' % c if c > 0 else '%s' % c for c in genetics.cycle_to_chromosome(cycle))


if __name__ == "__main__":
    main(sys.argv[1:])
