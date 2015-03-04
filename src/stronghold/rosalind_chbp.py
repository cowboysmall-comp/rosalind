import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def main(argv):
    lines   = files.read_lines(argv[0])
    species = lines[0].split()
    table   = lines[1:]
    count   = [0] * len(species)

    # unfinished - to be completed...

    print ' '.join(s for s in species)
    print '\n'.join(row for row in table)


if __name__ == "__main__":
    main(sys.argv[1:])
