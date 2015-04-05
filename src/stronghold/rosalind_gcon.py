import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import table
import strings


def main(argv):
    blosom62 = table.scoring(argv[0])
    s, t     = fasta.read_ordered(argv[1])
    m, n     = len(s), len(t)

    print strings.constant_gap_penalty_alignment_table(s, t, blosom62)[1][m][n]


if __name__ == "__main__":
    main(sys.argv[1:])
