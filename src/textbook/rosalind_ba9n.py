import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import arrays
import strings


def main(argv):
    lines    = files.read_lines(argv[0])

    text     = lines[0] + '$'
    patterns = lines[1:]

    bwt      = strings.burrows_wheeler_transform(text)
    first    = ''.join(sorted(text))
    k        = len(patterns[0]) + 1

    cm       = arrays.checkpoint_matrix(bwt, k)
    fo       = arrays.first_occurrence(first)
    psa      = {i:v for i, v in arrays.partial_suffix_array(text, k)}

    ifirst   = arrays.indexed_text_array(first)
    ilast    = arrays.indexed_text_array(bwt)

    matches  = []
    for pattern in patterns:
        matches.extend(strings.lighter_burrows_wheeler_matching(pattern, bwt, cm, fo, psa, ifirst, ilast, k))

    print ' '.join(str(match) for match in sorted(matches))


if __name__ == "__main__":
    main(sys.argv[1:])
