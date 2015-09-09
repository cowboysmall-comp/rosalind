import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import table


def main(argv):
    int_mass = table.integer_mass(argv[0])
    lines    = files.read_lines_of_ints(argv[1])

    M        = lines[0][0]
    N        = lines[1][0]
    spectrum = sorted(lines[2])

    counts   = genetics.convolution_counts(spectrum)
    masses   = genetics.convolution_frequent(counts, M)
    match    = genetics.leaderboard_matching_peptides(masses, [0] + spectrum, N)

    print '-'.join(str(m) for m in match[1])


if __name__ == "__main__":
    main(sys.argv[1:])
