import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines   = files.read_lines(argv[0])
    text    = lines[0]
    k       = int(lines[1])
    profile = {c:[float(value) for value in line.split()] for c, line in zip('ACGT', lines[2:])}

    print genetics.profile_most_kmer(text, profile, k)


if __name__ == "__main__":
    main(sys.argv[1:])
