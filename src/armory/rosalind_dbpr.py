import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from Bio import ExPASy
from Bio import SwissProt

import files


def main(argv):
    line   = files.read_line(argv[0])
    handle = ExPASy.get_sprot_raw(line)
    record = SwissProt.read(handle)

    go     = filter(lambda x: x[0] == 'GO' and 'P:' in x[2], record.cross_references)

    print '\n'.join(g[2].split(':')[1] for g in go)


if __name__ == "__main__":
    main(sys.argv[1:])
