

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


    def has_leaf_children(self):
        for child in self.children:
            if child.is_leaf():
                return True
        return False


    def child_count(self):
        return len(self.children)


    def descendent_count(self):
        return 1 if self.is_leaf() else sum(child.descendent_count() for child in self.children)


    def depth(self):
        return 1 + self.parent.depth() if self.parent else 0


    def add_child(self, node):
        node.parent = self
        self.children.append(node)


    def remove_child(self, node):
        node.parent = None
        self.children.remove(node)


    def clear_children(self):
        self.children = []


    def __str__(self):
        return '%s - depth:%s' % (self.label, self.depth())


    def __repr__(self):
        return self.__str__()




class BaseSuffixTree:

    def add_child(self, parent, node):
        if not self.split(parent, node):
            node.label = node.label[len(parent.label):]

            for child in parent.children:
                if child.label[0] == node.label[0]:
                    return self.add_child(child, node)

            parent.add_child(node)


    def split(self, parent, node):
        for i in xrange(min(len(node.label), len(parent.label))):
            if node.label[i] != parent.label[i]:
                new_node        = Node(parent.label[i:])
                node.label      = node.label[i:]

                for child in parent.children:
                    new_node.add_child(child)

                parent.label    = parent.label[:i]
                parent.children = []

                parent.add_child(new_node)
                parent.add_child(node)

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


    def __str__(self):
        string = []

        def traverse_for_printing(node, space):
            string.append(space + str(node))

            for child in node.children:
                traverse_for_printing(child, space + '  ')

        traverse_for_printing(self.root, '  ')

        return '\n'.join(string)




class SuffixTree(BaseSuffixTree):

    def __init__(self, string):
        if string[-1] != '$':
            string += '$'

        self.root = Node('')
        for i in xrange(len(string)):
            self.add_child(self.root, Node(string[i:]))


    def repeats(self, length = 1):
        repeats = []

        def to_string(node):
            string = ''

            while node:
                string = node.label + string
                node   = node.parent

            return string

        def traverse_from(node):
            if node.label and node.child_count() > 1:
                string = to_string(node)
                if len(string) >= length:
                    repeats.append(string)

            for child in node.children:
                traverse_from(child)

        traverse_from(self.root)

        return repeats


    def longest_repeat(self):
        return max(self.repeats(), key = len)




class GeneralizedSuffixTree(BaseSuffixTree):

    def __init__(self, strings):
        self.root = Node('')
        for index, string in enumerate(strings):
            string += '$%s' % index + 1
            for i in xrange(len(string)):
                self.add_child(self.root, Node(string[i:]))




def reconstruct_suffix_tree(word, sa, lcp):
    nodes     = [Node('')]
    traversal = []

    def descent(node):
        length = 0

        while node:
            length += len(node.label)
            node    = node.parent

        return length

    def insert(index):
        current = nodes[-1]
        dist    = descent(current)

        while dist > lcp[index + 1]:
            current = current.parent
            dist    = descent(current)

        if dist == lcp[index + 1]:
            start   = sa[index + 1] + lcp[index + 1]
            node    = Node(word[start:])
            current.add_child(node)
            nodes.append(node)
        else:
            w       = current.children[-1]
            distw   = descent(w)
            current.remove_child(w)

            start   = sa[index] + dist
            end     = sa[index] + lcp[index + 1]
            y       = Node(word[start:end])
            current.add_child(y)
            nodes.append(y)

            start   = sa[index] + lcp[index + 1]
            end     = sa[index] + distw
            w.label = word[start:end]
            y.add_child(w)

            start   = sa[index + 1] + lcp[index + 1]
            x       = Node(word[start:])
            y.add_child(x)
            nodes.append(x)

    def traverse_from(node):
        if node.label:
            traversal.append(node.label)

        for child in node.children:
            traverse_from(child)

    start = sa[0]
    node  = Node(word[start:])
    nodes[0].add_child(node)
    nodes.append(node)

    for index in xrange(len(sa) - 1):
        insert(index)

    traverse_from(nodes[0])

    return traversal






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
        child.label  = string[start:start + end]

        parent.add_child(child)

    return nodes.values()[0].get_root()



def longest_substring(node, k):
    strings = []

    for child in node.children:
        string = child.label
        if child.descendent_count() >= k:
            substrings = longest_substring(child, k)
            if substrings:
                for substring in substrings:
                    strings.append(string + substring)
            else:
                strings.append(string)

    return sorted(strings)

