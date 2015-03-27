import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import trie


def main(argv):
    lines = files.read_lines(argv[0])

    tries = trie.Trie()
    for line in lines[1:]:
        tries.insert(line)

    matches = tries.matching(lines[0])

    print ' '.join(str(match[0]) for match in matches)


if __name__ == "__main__":
    main(sys.argv[1:])
