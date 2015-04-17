import re

from collections import defaultdict
from itertools   import combinations, product
from ete2        import Tree


def create_table_from_strings(strings):
    string = strings[0]
    length = len(strings)
    table  = []

    def create_row(col, char, strings):
        row = []

        for string in strings:
            row.append(1 if char == string[col] else 0)

        return row

    for col, char in enumerate(string):
        row = create_row(col, char, strings)
        if 1 < sum(row) < length - 1:
            table.append(''.join(str(r) for r in row))

    return table



def create_table_from_tree(string):
    tree  = Tree(string, format = 1)
    names = sorted(tree.get_leaf_names())
    table = []

    def create_row(node, names):
        split = [0] * len(names)

        for leaf in node:
            split[names.index(leaf.name)] = 1

        return split

    for node in tree.get_descendants():
        if not node.is_leaf():
            split = create_row(node, names)
            table.append(''.join(str(s) for s in split))

    return table


def quartets(taxa, table):
    quartets = set()

    for row in table:
        A = [taxa[i] for i in xrange(len(row)) if row[i] == '1']
        B = [taxa[i] for i in xrange(len(row)) if row[i] == '0']

        for p in product(combinations(A, 2), combinations(B, 2)):
            quartets.add(frozenset(p))

    return quartets



def count_common_quartets(table1, table2):
    count = defaultdict(int)

    for row in table1:
        A = [i for i in xrange(len(row)) if row[i] == '1']
        B = [i for i in xrange(len(row)) if row[i] == '0']

        for p in product(combinations(A, 2), combinations(B, 2)):
            count[p] += 1

    for row in table2:
        A = [i for i in xrange(len(row)) if row[i] == '1']
        B = [i for i in xrange(len(row)) if row[i] == '0']

        for p in product(combinations(A, 2), combinations(B, 2)):
            count[p] += 1

    return len([0 for key in count if count[key] > 1])



'''
    the below split_distance can be implemented using the ete2 library:

    def split_distance(taxa, strings):
        tree1 = Tree(lines[1])
        tree2 = Tree(lines[2])

        return tree1.robinson_foulds(tree2, unrooted_trees = True)[0]

    but it is really quite slow.

'''

def split_distance(taxa, strings):
    splits1 = set(create_table_from_tree(strings[0]))
    splits2 = set(create_table_from_tree(strings[1]))

    return (2 * (len(taxa) - 3)) - (2 * (len(splits1 & splits2)))



def invert(string):
    return ''.join('1' if b == '0' else '0' for b in string) if string.count('1') > string.count('0') else string



def tree_from_character_table(species, table):
    leaves  = []
    tree    = Tree()
    root    = tree.get_tree_root()

    table   = sorted([invert(row) for row in table], key = lambda x: x.count('1'))

    for specie in species:
        leaves.append(root.add_child(name = specie))

    while table:
        for row in table:
            if row.count('1') == 2:
                i1, i2     = [i.start() for i in re.finditer('1', row)]
                n1, n2     = leaves[i1], leaves[i2]

                leaves[i1] = root.add_child()
                leaves[i1].add_child(n1.detach())
                leaves[i1].add_child(n2.detach())

                table.remove(row)
                leaves     = leaves[:i2] + leaves[i2 + 1:]
                table      = [row[:i2] + row[i2 + 1:] for row in table]
                break
            else:
                return None

    return tree



def consistent_character_table(table):
    table = sorted([invert(row) for row in table], key = lambda x: x.count('1'))

    while table:
        for row in table:
            if row.count('1') == 2:
                i1, i2 = [i.start() for i in re.finditer('1', row)]

                table.remove(row)
                table  = [row[:i2] + row[i2 + 1:] for row in table]
                break
            else:
                return False

    return True



def find_consistent_character_table(table):
    for i in xrange(len(table)):
        temp = table[:i] + table[i + 1:]

        if consistent_character_table(temp):
            return sorted(table[:i] + table[i + 1:], key = lambda x: x.count('1'))

    return None

