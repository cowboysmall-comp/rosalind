import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from Bio.Seq import translate, CodonTable

import files


def main(argv):
    lines = files.read_lines(argv[0])
    index = -1

    for i in CodonTable.ambiguous_generic_by_id.keys():
        if translate(lines[0], table = i, to_stop = True) == lines[1]:
            index = i
            break

    print index


if __name__ == "__main__":
    main(sys.argv[1:])
