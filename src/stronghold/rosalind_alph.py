import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import fasta
import phylogeny


def main(argv):
    lines   = files.read_lines(argv[0])
    tree    = lines[0]
    strings = fasta.read_from(lines[1:])

    z, L    = phylogeny.small_parsimony(tree, strings)

    print z
    print '\n'.join('>%s\n%s' % (key, value) for key, value in L.iteritems())


if __name__ == "__main__":
    main(sys.argv[1:])
