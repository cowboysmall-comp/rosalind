import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import fasta
import phylogeny


def main(argv):
    lines   = files.read_lines(argv[0])
    tree    = lines[0]
    strings = fasta.read_from(lines[1:])

    output = []
    for r in phylogeny.reverse_substitutions(tree, strings):
        path        = r[0]
        position    = r[1]
        original    = strings[path[0].name][position]
        substituted = strings[path[1].name][position]
        reverted    = strings[path[-1].name][position]
        output.append('%s %s %s %s->%s->%s' % (path[1].name, path[-1].name, position + 1, original, substituted, reverted))

    print '\n'.join(output)



if __name__ == "__main__":
    main(sys.argv[1:])
