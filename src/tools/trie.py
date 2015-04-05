

class Trie:

    def __init__(self):
        self._root  = {'': {}}


    def prefix_matching(self, text):
        current = self._root['']
        index   = 0
        symbol  = text[index]

        while True:
            if not current:
                return text[:index]
            elif symbol in current:
                current = current[symbol]
                index  += 1
                if index < len(text):
                    symbol = text[index]
            else:
                return None


    def matching(self, text):
        matches = []
        index   = 0

        while index < len(text):
            match = self.prefix_matching(text[index:])
            if match:
                matches.append((index, match))
            index += 1

        return matches


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


    def edges(self, label = 0):
        labeled = []

        def edges_traversal(current, label):
            current_label = label + 1

            for key in current:
                labeled.append((label, current_label, key))
                current_label = edges_traversal(current[key], current_label)

            return current_label

        edges_traversal(self._root[''], label)

        return labeled

