import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from ete2 import Tree


'''
    my original implementation. I changed it to use
    add_features and a postorder traversal - much cleaner

    def genotype_probs(node):

        def child_probs(child):
            if child.is_leaf():
                return leaf_probs(''.join(sorted(child.name)))
            else:
                return genotype_probs(child)

        def leaf_probs(v):
            values     = {'AA': 0.0, 'Aa': 0.0, 'aa': 0.0}
            values[v] += 1.0
            return values

        def calculate_probs(p1, p2):
            AA  =        (p1['AA'] * p2['AA']) 
            AA += 0.5  * (p1['AA'] * p2['Aa']) 
            AA += 0.5  * (p1['Aa'] * p2['AA'])
            AA += 0.25 * (p1['Aa'] * p2['Aa'])

            Aa  =        (p1['AA'] * p2['aa'])
            Aa +=        (p1['aa'] * p2['AA'])
            Aa += 0.5  * (p1['AA'] * p2['Aa']) 
            Aa += 0.5  * (p1['Aa'] * p2['AA']) 
            Aa += 0.5  * (p1['Aa'] * p2['Aa']) 
            Aa += 0.5  * (p1['aa'] * p2['Aa']) 
            Aa += 0.5  * (p1['Aa'] * p2['aa'])

            aa  =        (p1['aa'] * p2['aa']) 
            aa += 0.5  * (p1['aa'] * p2['Aa']) 
            aa += 0.5  * (p1['Aa'] * p2['aa'])
            aa += 0.25 * (p1['Aa'] * p2['Aa'])

            return {'AA': AA, 'Aa': Aa, 'aa': aa}

        children = node.get_children()
        probs1   = child_probs(children[0])
        probs2   = child_probs(children[1])

        return calculate_probs(probs1, probs2)

'''


def genotype_probs(root):

    def leaf_probs(v):
        values     = {'AA': 0.0, 'Aa': 0.0, 'aa': 0.0}
        values[v] += 1.0
        return values

    def calculate_probs(p1, p2):
        AA  =        (p1.AA * p2.AA) 
        AA += 0.5  * (p1.AA * p2.Aa) 
        AA += 0.5  * (p1.Aa * p2.AA)
        AA += 0.25 * (p1.Aa * p2.Aa)

        Aa  =        (p1.AA * p2.aa)
        Aa +=        (p1.aa * p2.AA)
        Aa += 0.5  * (p1.AA * p2.Aa) 
        Aa += 0.5  * (p1.Aa * p2.AA) 
        Aa += 0.5  * (p1.Aa * p2.Aa) 
        Aa += 0.5  * (p1.aa * p2.Aa) 
        Aa += 0.5  * (p1.Aa * p2.aa)

        aa  =        (p1.aa * p2.aa) 
        aa += 0.5  * (p1.aa * p2.Aa) 
        aa += 0.5  * (p1.Aa * p2.aa)
        aa += 0.25 * (p1.Aa * p2.Aa)

        return {'AA': AA, 'Aa': Aa, 'aa': aa}

    for node in root.traverse(strategy = 'postorder'):
        if node.is_leaf():
            node.add_features(**leaf_probs(''.join(sorted(node.name))))
        else:
            children = node.get_children()
            node.add_features(**calculate_probs(children[0], children[1]))

    return root


def main(argv):
    line = files.read_line(argv[0])
    tree = genotype_probs(Tree(line, format = 1))

    print '%0.3g %0.3g %0.3g' % (tree.AA, tree.Aa, tree.aa)


if __name__ == "__main__":
    main(sys.argv[1:])
