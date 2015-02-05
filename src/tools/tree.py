

class Node:

    def __init__(self, label):
        self.label    = label
        self.data     = None
        self.parent   = None
        self.children = []


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
        self.children.append(node)


    def __str__(self):
        return '%s (%s)' % (self.data, self.depth())


    def __repr__(self):
        return self.__str__()



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

        child.parent = parent
        parent.add_child(child)

    return child.get_root()

