import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import arrays
import tree


def main(argv):
    text  = files.read_line(argv[0])

    st1   = tree.SuffixTree(text)
    st2   = tree.SuffixTree(text[::-1])
    reps  = set(st1.repeats(length = 20)) & set([repeat[::-1] for repeat in st2.repeats(length = 20)])

    print '\n'.join(reps)


if __name__ == "__main__":
    main(sys.argv[1:])
