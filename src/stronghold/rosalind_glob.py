import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import tables
import strings


def main(argv):
    blosom62 = tables.blosom62_scoring(argv[0])
    s, t     = fasta.read_ordered(argv[1])
    m, n     = len(s), len(t)

    print strings.alignment_table(s, t, blosom62)[m][n]


if __name__ == "__main__":
    main(sys.argv[1:])
