import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import combs


def main(argv):
    rna    = fasta.read_one(argv[0])

    au_max = max(rna.count('A'), rna.count('U'))
    au_min = min(rna.count('A'), rna.count('U'))

    cg_max = max(rna.count('C'), rna.count('G'))
    cg_min = min(rna.count('C'), rna.count('G'))

    print combs.permutations(au_max, au_min) * combs.permutations(cg_max, cg_min)


if __name__ == "__main__":
    main(sys.argv[1:])
