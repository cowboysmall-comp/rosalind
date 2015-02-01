import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta


def gc_content(strings):
    max_count = 0
    max_label = None

    for label, string in strings.iteritems():
        count = 100 * float(string.count('G') + string.count('C')) / len(string)
        if max_count < count:
            max_count = count
            max_label = label

    return max_count, max_label


def main(argv):
    strings      = fasta.read(argv[0])
    count, label = gc_content(strings)

    print label
    print '%0.6f' % (count)


if __name__ == "__main__":
    main(sys.argv[1:])
