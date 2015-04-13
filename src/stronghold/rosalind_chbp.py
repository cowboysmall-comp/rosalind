import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from ete2 import Tree


def construct_tree(species, table):
    print


def main(argv):
    lines   = files.read_lines(argv[0])
    species = lines[0].split()
    length  = len(species)
    table   = ['1' * length] + lines[1:] + ['0' * length]
    table   = sorted(table, reverse = True)

    # unfinished - to be completed...

    print ' '.join(s for s in species)
    print '\n'.join(str(row) for row in table)


if __name__ == "__main__":
    main(sys.argv[1:])




    # tree = Tree('(dog,(cat,rabbit),(rat,(elephant,mouse)));', format = 1)
    # print tree
    # print 

    # cand    = []
    # for i in xrange(1, len(table)):
    #     row = []
    #     for j in xrange(length):
    #         if table[i - 1][j] != table[i][j]:
    #             row.append((i, j, species[j]))
    #     cand.append(row)

    # print cand
    # print 

    # output = '('
    # for i in xrange(len(cand)):
    #     if len(cand[i]) == 1:
    #         output += cand[i][0][2]
    #     else:
    #         output += '('
    #         output += ','.join(c[2] for c in cand[i])
    #         output += ')'
    #     if i != len(cand) - 1:
    #         output += ','
    # output += ');'

    # print output
    # print 

    # tree = Tree(output, format = 1)
    # print tree
    # print 

