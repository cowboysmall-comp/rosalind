import re

from collections import defaultdict
from itertools   import combinations, product
from ete2        import Tree


def create_table_from_strings(strings):
    string = strings[0]
    length = len(strings)
    table  = []

    def create_row(col, char):
        row = []

        for string in strings:
            row.append(1 if char == string[col] else 0)

        return row

    for col, char in enumerate(string):
        row = create_row(col, char)
        if 1 < sum(row) < length - 1:
            table.append(''.join(str(r) for r in row))

    return table



def create_table_from_tree(string):
    tree   = Tree(string, format = 1)
    names  = sorted(tree.get_leaf_names())
    length = len(names)
    table  = []

    def create_row(node):
        split = [0] * length

        for leaf in node:
            split[names.index(leaf.name)] = 1

        return split

    for node in tree.get_descendants():
        if not node.is_leaf():
            split = create_row(node)
            table.append(''.join(str(s) for s in split))

    return table


def create_table_from_tree_and_leaves(string, leaves):
    tree   = Tree(string, format = 1)
    names  = sorted(leaves)
    length = len(leaves)
    table  = set()

    def create_row(node):
        split = [0] * length

        for leaf in node:
            split[names.index(leaf.name)] = 1

        return split

    for node in tree.iter_descendants():
        if not node.is_leaf():
            split = create_row(node)
            table.add(''.join(str(s) for s in split))

    return table


def quartets(taxa, table):
    quartets = set()

    for row in table:
        A = [taxa[i] for i in xrange(len(row)) if row[i] == '1']
        B = [taxa[i] for i in xrange(len(row)) if row[i] == '0']

        for p in product(combinations(A, 2), combinations(B, 2)):
            quartets.add(frozenset(p))

    return quartets


'''
    I need to work on this - the algorithm is sound, but the amount of memory 
    it uses is prohibitive. Until I can implement my own sub-quartic algorithm, 
    I'm going to park this and make use of another tool entitled qdist:

        http://birc.au.dk/Software/QDist

    here are the existing implementations:


    def count_common_quartets(table1, table2):
        count = 0
        seen  = set()

        for row in table1:
            A = [i for i in xrange(len(row)) if row[i] == '1']
            B = [i for i in xrange(len(row)) if row[i] == '0']

            for p in product(combinations(A, 2), combinations(B, 2)):
                val = '{0:016b}{1:016b}{2:016b}{3:016b}'.format(int(p[0][0]), int(p[0][1]), int(p[1][0]), int(p[1][1]))
                seen.add(int(val, 2))

        for row in table2:
            A = [i for i in xrange(len(row)) if row[i] == '1']
            B = [i for i in xrange(len(row)) if row[i] == '0']

            for p in product(combinations(A, 2), combinations(B, 2)):
                val = '{0:016b}{1:016b}{2:016b}{3:016b}'.format(int(p[0][0]), int(p[0][1]), int(p[1][0]), int(p[1][1]))
                if int(val, 2) in seen:
                    count += 1

        return count



    def count_common_quartets(table1, table2):
        count = defaultdict(int)

        for row in table1:
            for i in xrange(len(row) - 1):
                if row[i] == '1':
                    for j in xrange(i + 1, len(row)):
                        if row[j] == '1':
                            for k in xrange(len(row) - 1):
                                if row[k] == '0':
                                    for l in xrange(k + 1, len(row)):
                                        if row[l] == '0':
                                            count[((i, j), (k, l))] += 1

        for row in table2:
            for i in xrange(len(row) - 1):
                if row[i] == '1':
                    for j in xrange(i + 1, len(row)):
                        if row[j] == '1':
                            for k in xrange(len(row) - 1):
                                if row[k] == '0':
                                    for l in xrange(k + 1, len(row)):
                                        if row[l] == '0':
                                            count[((i, j), (k, l))] += 1

        return len([count[key] for key in count if count[key] > 1])


'''

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

    return len([count[key] for key in count if count[key] > 1])




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



def small_parsimony(tree, strings):
    tree   = Tree(tree, format = 1)
    length = len(strings.values()[0])

    S      = defaultdict(dict)
    L      = defaultdict(str)
    Z      = [0]

    def forward_pass():
        for i in xrange(length):
            for node in tree.traverse('postorder'):
                if node.is_leaf():
                    S[node.name][i] = {strings[node.name][i]}
                else:
                    children = node.get_children()
                    s1 = S[children[0].name][i] & S[children[1].name][i]
                    if s1:
                        S[node.name][i] = s1
                    else:
                        S[node.name][i] = S[children[0].name][i] | S[children[1].name][i]
                        Z[0] += 1

    def backward_pass():
        for i in xrange(length):
            for node in tree.traverse('preorder'):
                if not node.up:
                    L[node.name] += S[node.name][i].pop()
                else:
                    if L[node.up.name][i] in S[node.name][i]:
                        L[node.name] += L[node.up.name][i]
                    else:
                        L[node.name] += S[node.name][i].pop()

    forward_pass()
    backward_pass()

    return Z[0], {key: value for key, value in L.iteritems() if key not in strings}




def reverse_substitutions(tree, strings):
    length = len(strings.values()[0])
    tree   = Tree(tree, format = 1)
    found  = []

    def find_reversing_substitutions(node, position, orig = None, subs = None):
        paths = []
        char  = strings[node.name][position]

        if not orig:
            for child in node.get_children():
                for path in find_reversing_substitutions(child, position, orig = char):
                    paths.append([node] + path)

        elif not subs:
            if strings[node.name][position] != orig:
                for child in node.get_children():
                    for path in find_reversing_substitutions(child, position, orig, subs = char):
                        paths.append([node] + path)

        elif strings[node.name][position] == subs:
            for child in node.get_children():
                for path in find_reversing_substitutions(child, position, orig, subs):
                    paths.append([node] + path)

        elif strings[node.name][position] == orig:
            paths.append([node])

        return paths

    for node in tree.traverse('preorder'):
        for i in xrange(length):
            for path in find_reversing_substitutions(node, i):
                found.append((path, i))

    return found


