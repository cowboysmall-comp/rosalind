import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def percentile(values, percent):
    total = sum(values)
    sigma = 0

    for i in xrange(len(values) - 1, -1, -1):
        sigma += values[i]
        if sigma >= total * percent:
            return values[i]

    return 0


def main(argv):
    lines   = files.read_lines(argv[0])
    contigs = sorted([len(line) for line in lines])

    print percentile(contigs, 0.5), percentile(contigs, 0.75)


if __name__ == "__main__":
    main(sys.argv[1:])
