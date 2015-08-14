import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import genetics


def main(argv):
    lines = files.read_lines(argv[0])
    text  = lines[0]
    k, d  = [int(i) for i in lines[1].split()]

    table = genetics.kmer_frequency_table_mismatches(text, k, d)
    freq  = genetics.kmer_reverse_frequency_table(table)

    print ' '.join(sorted(freq[max(freq)]))


if __name__ == "__main__":
    main(sys.argv[1:])
