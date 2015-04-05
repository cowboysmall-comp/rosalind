import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import arrays
import strings


def main(argv):
    lines    = files.read_lines_of_words(argv[0])

    text     = lines[0][0]
    patterns = lines[1]

    cm       = arrays.count_matrix(text)
    fo       = arrays.first_occurrence(''.join(sorted(text)))

    matches  = []
    for pattern in patterns:
        matches.append(strings.better_burrows_wheeler_matching(pattern, text, cm, fo))

    print ' '.join(str(match) for match in matches)


if __name__ == "__main__":
    main(sys.argv[1:])
