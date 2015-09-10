import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import table
import genetics


def main(argv):
    int_mass    = table.integer_mass(argv[0])
    lines       = files.read_lines(argv[1])
    leaderboard = [([int_mass[p] for p in peptide], peptide) for peptide in lines[0].split()]
    spectrum    = [int(m) for m in lines[1].split()]
    N           = int(lines[2])

    print ' '.join(leader[1] for leader in genetics.trim_leaderboard(leaderboard, spectrum, N))


if __name__ == "__main__":
    main(sys.argv[1:])
