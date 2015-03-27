import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import trie


def main(argv):
    tries = trie.Trie()

    for line in files.read_lines(argv[0]):
        tries.insert(line)

    print '\n'.join('%s->%s:%s' % trie for trie in tries.edges())


if __name__ == "__main__":
    main(sys.argv[1:])
