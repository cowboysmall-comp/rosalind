import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    S    = files.read_lines(argv[0])
    S_rc = [genetics.dna_complement(s) for s in S]
    S_u  = set(S + S_rc)

    B_k  = []

    for s in S_u:
        B_k.append((s[:-1], s[1:]))

    print '\n'.join('(%s, %s)' % b for b in sorted(B_k))


if __name__ == "__main__":
    main(sys.argv[1:])
