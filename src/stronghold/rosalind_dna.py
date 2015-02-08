import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import arrays


def main(argv):
    freq = arrays.frequency_table(files.read_line(argv[0]))

    print '%s %s %s %s' % (freq['A'], freq['C'], freq['G'], freq['T'])


if __name__ == "__main__":
    main(sys.argv[1:])
