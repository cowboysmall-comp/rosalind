import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics
import tables


def main(argv):
    table    = tables.integer_mass(argv[0])
    lines    = files.read_lines_of_ints(argv[1])
    masses   = [[value] for value in sorted(table.values())]

    N        = lines[0][0]
    spectrum = lines[1]
    match    = genetics.leaderboard_matching_peptides(masses, spectrum, N, table)

    print '-'.join(str(m) for m in match[1])


if __name__ == "__main__":
    main(sys.argv[1:])
