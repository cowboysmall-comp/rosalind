import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import searches


def main(argv):
    with open(argv[0]) as file:
        n     = int(file.readline().strip())
        m     = int(file.readline().strip())
        A     = [int(a) for a in file.readline().split()]
        ids   = [int(i) for i in file.readline().split()]

        found = [searches.binary_search(A, i, 1, n) for i in ids]

        print ' '.join(str(f) for f in found)



if __name__ == "__main__":
    main(sys.argv[1:])
