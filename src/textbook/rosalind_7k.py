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

    last     = arrays.indexed_text_array(text)
    first    = arrays.indexed_text_array(''.join(sorted(text)))
    ltof     = arrays.last_to_first(first, last)

    matches  = []
    for pattern in patterns:
        matches.append(strings.burrows_wheeler_matching(pattern, first, last, ltof))

    print ' '.join(str(match) for match in matches)


if __name__ == "__main__":
    main(sys.argv[1:])
