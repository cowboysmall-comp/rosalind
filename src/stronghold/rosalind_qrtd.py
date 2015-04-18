import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from subprocess import call

import files


'''
    how I would have liked to solve this one:


    import combinatorics
    import phylogeny

    def main(argv):
        lines  = files.read_lines(argv[0])
        taxa   = lines[0].split()
        trees  = lines[1:]

        table1 = phylogeny.create_table_from_tree_and_leaves(trees[0], taxa)
        table2 = phylogeny.create_table_from_tree_and_leaves(trees[1], taxa)
        total  = combinatorics.combinations(len(taxa), 4)
        common = phylogeny.count_common_quartets(table1, table2)

        print (2 * total) - (2 * common)


    but alas, I cannot figure out an algorithm that uses less memory, 
    and takes less time. I'll try again in future.

'''

def quartet_distance(tree1, tree2):
    distance = 0

    files.write_lines('tree1.newick', tree1)
    files.write_lines('tree2.newick', tree2)

    call('qdist tree1.newick tree2.newick > qdist.out', shell = True)

    with open('qdist.out') as file:
        file.readline()
        distance = 2 * int(file.readline().split()[6].strip())

    os.remove('qdist.out')
    os.remove('tree1.newick')
    os.remove('tree2.newick')

    return distance


def main(argv):
    lines  = files.read_lines(argv[0])
    taxa   = lines[0].split()
    trees  = lines[1:]

    print quartet_distance(*trees)


if __name__ == "__main__":
    main(sys.argv[1:])
