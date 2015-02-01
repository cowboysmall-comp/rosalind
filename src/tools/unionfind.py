

class UnionFind:

    def __init__(self, count):
        self._count = count
        self._data  = []
        for i in xrange(count):
            self._data.append(i + 1)

    def count(self):
        return self._count

    def union(self, p, q):
        p_parent = self._data[p - 1]
        q_parent = self._data[q - 1]
        if p_parent != q_parent:
            for i in xrange(len(self._data)):
                if self._data[i] == p_parent:
                    self._data[i] = q_parent
            self._count -= 1
