

class QuickFind:

    def __init__(self, length, offset = 1):
        self.length = length
        self.offset = offset
        self.array  = [i for i in xrange(length)]


    def __str__(self):
        return ' '.join([str(element) for element in self.array])


    def count(self):
        return self.length


    def connected(self, p, q):
        return self.array[p - self.offset] == self.array[q - self.offset]


    def union(self, p, q):
        pid = self.array[p - self.offset]
        qid = self.array[q - self.offset]
        if pid != qid:
            for i in xrange(self.length):
                if self.array[i] == pid:
                    self.array[i] = qid
        self.length -= 1


    def get_array(self):
        return self.array



class QuickUnion:
    
    def __init__(self, length, offset = 1):
        self.length = length
        self.offset = offset
        self.array  = [i for i in xrange(length)]


    def __str__(self):
        return ' '.join([str(element) for element in self.array])


    def _root(self, i):
        while i != self.array[i]:
            i = self.array[i]
        return i


    def count(self):
        return self.length


    def connected(self, p, q):
        return self._root(p - self.offset) == self._root(q - self.offset)


    def union(self, p, q):
        proot = self._root(p - self.offset)
        qroot = self._root(q - self.offset)
        self.array[proot] = qroot
        self.length -= 1


    def get_array(self):
        return self.array



class WeightedQuickUnion:
    
    def __init__(self, length, offset = 1):
        self.length = length
        self.offset = offset
        self.array  = [i for i in xrange(length)]
        self.sizes  = [1 for _ in xrange(length)]


    def __str__(self):
        return ' '.join([str(element) for element in self.array])


    def _root(self, i):
        while i != self.array[i]:
            i = self.array[i]
        return i


    def count(self):
        return self.length


    def connected(self, p, q):
        return self._root(p - self.offset) == self._root(q - self.offset)


    def union(self, p, q):
        proot = self._root(p - self.offset)
        qroot = self._root(q - self.offset)
        if proot != qroot:
            if self.sizes[proot] < self.sizes[qroot]:
                self.array[proot] = qroot
                self.sizes[qroot] += self.sizes[proot]
            else:
                self.array[qroot] = proot
                self.sizes[proot] += self.sizes[qroot]
        self.length -= 1


    def get_array(self):
        return self.array


    def get_sizes(self):
        return self.sizes
