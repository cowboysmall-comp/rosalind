import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import strings
import tables


def main(argv):
    blosom62 = tables.scoring(argv[0])
    s, t     = files.read_lines(argv[1])

    edge     = strings.middle_edge(s, t, blosom62)

    print edge[0], edge[1]


if __name__ == "__main__":
    main(sys.argv[1:])
