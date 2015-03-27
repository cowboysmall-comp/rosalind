import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines  = files.read_lines(argv[0])
    k      = int(lines[0])
    s1, s2 = lines[1:]

    print '\n'.join(str(kmer) for kmer in genetics.shared_kmers(s1, s2, k))


if __name__ == "__main__":
    main(sys.argv[1:])
