import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import tree


def main(argv):
    dna = files.read_line(argv[0])
    st  = tree.SuffixTree(dna)

    print '\n'.join(st.traverse())


if __name__ == "__main__":
    main(sys.argv[1:])
