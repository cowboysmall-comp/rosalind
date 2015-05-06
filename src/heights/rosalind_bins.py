import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import searches


def main(argv):
    data  = files.read_lines_of_ints(argv[0])
    n     = data[0][0]
    m     = data[1][0]
    A     = data[2]
    ids   = data[3]
    found = [searches.binary_search(A, i, 0, n - 1) for i in ids]

    print ' '.join(str(f + 1) if f != -1 else '-1' for f in found)



if __name__ == "__main__":
    main(sys.argv[1:])
