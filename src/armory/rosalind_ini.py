import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from Bio.Seq import Seq

import files


def main(argv):
    line = files.read_line(argv[0])
    seq  = Seq(line)

    print seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T') 


if __name__ == "__main__":
    main(sys.argv[1:])
