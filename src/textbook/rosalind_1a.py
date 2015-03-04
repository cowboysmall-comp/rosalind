import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines = files.read_lines(argv[0])
    dna   = lines[0]
    k     = int(lines[1])

    table = genetics.kmer_frequency_table(dna, k)
    freq  = genetics.kmer_reverse_frequency_table(table)

    print ' '.join(sorted(freq[max(freq)]))


if __name__ == "__main__":
    main(sys.argv[1:])
