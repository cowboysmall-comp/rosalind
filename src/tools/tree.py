

class Node:

    def __init__(self, label, parent = None, children = None):
        self.label    = label
        self.data     = None
        self.parent   = parent
        self.children = children if children else []


    def get_root(self):
        return self if self.is_root() else self.parent.get_root()


    def is_root(self):
        return self.parent == None


    def is_leaf(self):
        return len(self.children) == 0


    def child_count(self):
        return len(self.children)


    def descendent_count(self):
        return 1 if self.is_leaf() else sum(child.descendent_count() for child in self.children)


    def depth(self):
        return 1 + self.parent.depth() if self.parent else 0


    def add_child(self, node):
        node.parent = self
        self.children.append(node)


    def __str__(self):
        return '%s (%s)' % (self.label, self.depth())


    def __repr__(self):
        return self.__str__()



class SuffixTree:

    def __init__(self, string):
        self.root = Node(string)
        for i in xrange(1, len(string)):
            self.add_child(self.root, Node(string[i:]))


    def add_child(self, parent, node):
        if not self.split(parent, node):
            node.label = node.label[len(parent.label):]
            for child in parent.children:
                if child.label[0] == node.label[0]:
                    return self.add_child(child, node)
            parent.add_child(node)

            
    def split(self, parent, node):
        length = min(len(parent.label), len(node.label))
        for i in xrange(length):
            if parent.label[i] != node.label[i]:
                node.parent     = parent
                node.label      = node.label[i:]
                parent.children = [Node(parent.label[i:], parent, parent.children), node]
                parent.label    = parent.label[:i]
                return True
        return False


    def traverse(self):
        traversal = []

        def traverse_from(node):
            if node.label:
                traversal.append(node.label)

            for child in node.children:
                traverse_from(child)

        traverse_from(self.root)

        return traversal


    def longest_repeat(self):
        repeats = []

        def to_string(node):
            string = ''

            while node:
                string = node.label + string
                node   = node.parent

            return string

        def traverse_from(node):
            if node.label and node.child_count() > 1:
                repeats.append(to_string(node))

            for child in node.children:
                traverse_from(child)

        traverse_from(self.root)

        return max(repeats, key = len)


    def __str__(self):
        string = []

        def traverse_for_printing(node, space):
            if node.label:
                string.append(space + node.label)
            else:
                string.append('root')

            for child in node.children:
                traverse_for_printing(child, space + '  ')

        traverse_for_printing(self.root, '  ')

        return '\n'.join(string)


def build_suffix_tree(string, edges):
    nodes = {}

    for edge in edges:
        values       = edge.split()

        if values[0] not in nodes:
            nodes[values[0]] = Node(values[0])

        if values[1] not in nodes:
            nodes[values[1]] = Node(values[1])

        parent       = nodes[values[0]]
        child        = nodes[values[1]]

        start        = int(values[2]) - 1
        end          = int(values[3])
        child.data   = string[start:start + end]

        parent.add_child(child)

    return nodes.values()[0].get_root()

