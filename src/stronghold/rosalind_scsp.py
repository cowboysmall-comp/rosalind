import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import strings
import files



def main(argv):
    s, t = files.read_lines(argv[0])

    print strings.shortest_supersequence(s, t)


if __name__ == "__main__":
    main(sys.argv[1:])