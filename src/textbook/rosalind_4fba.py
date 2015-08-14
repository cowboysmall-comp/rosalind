import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import table


def main(argv):
    int_mass = table.integer_mass(argv[0])
    lines    = files.read_lines_of_ints(argv[1])
    masses   = [[value] for value in sorted(int_mass.values())]

    N        = lines[0][0]
    spectrum = lines[1]
    match    = genetics.leaderboard_matching_peptides(masses, spectrum, N, int_mass)

    print '-'.join(str(m) for m in match[1])


if __name__ == "__main__":
    main(sys.argv[1:])
