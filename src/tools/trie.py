from collections import defaultdict


class Trie:

    def __init__(self):
        self._root  = {'': {}}


    def insert(self, string):
        node  = self._root['']
        index = 0
        n     = len(string)

        while index < n:
            if string[index] in node:
                node   = node[string[index]]
                index += 1
            else:
                break

        while index < n:
            node[string[index]] = {}
            node   = node[string[index]]
            index += 1


    def edges(self):
        labeled = []

        def edges_traversal(current, label):
            current_label = label + 1

            for key in current:
                labeled.append((label, current_label, key))
                current_label = edges_traversal(current[key], current_label)

            return current_label

        edges_traversal(self._root[''], 1)

        return labeled

