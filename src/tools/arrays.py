from collections import defaultdict


def frequency_table(A):
    freq  = defaultdict(int)

    for a in A:
        freq[a] += 1

    return freq


def reverse_frequency_table(A):
    return [(value, key) for key, value in frequency_table(A).iteritems()]


def majority_element(A):
    l        = len(A)
    elements = filter(lambda x: x[0] > l / 2, reverse_frequency_table(A))

    return max(elements)[1] if elements else -1


def max_heapify(A, i, l):
    left    = 2 * i + 1
    right   = 2 * i + 2
    largest = i

    if left < l and A[largest] < A[left]:
        largest = left

    if right < l and A[largest] < A[right]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, l)


def max_heap(A):
    l = len(A)

    for i in xrange(l // 2, -1, -1):
        max_heapify(A, i, l)

    return A


def min_heapify(A, i, l):
    left     = 2 * i + 1
    right    = 2 * i + 2
    smallest = i

    if left < l and A[smallest] > A[left]:
        smallest = left

    if right < l and A[smallest] > A[right]:
        smallest = right

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest, l)


def min_heap(A):
    l = len(A)

    for i in xrange(l // 2, -1, -1):
        min_heapify(A, i, l)

    return A


def count_inversions(A):
    l = len(A)
    c = 0

    for i in xrange(len(A) - 1):
        for j in xrange(i + 1, len(A)):
            if A[i] > A[j]:
                c += 1

    return c



def indexed_text_array(text):
    indexed = []
    counter = defaultdict(int)

    for c in text:
        counter[c] += 1
        indexed.append((c, counter[c]))

    return indexed


def last_to_first(first, last):
    ltof  = {}

    for index in xrange(len(last)):
        ltof[index] = first.index(last[index])

    return ltof


def count_matrix(last):
    row = {c: 0 for c in last}
    c   = [row.copy()]

    for l in last:
        row[l] += 1
        c.append(row.copy())

    return c


def checkpoint_matrix(last, k):
    row = {c: 0 for c in last}
    i   = 0
    c   = {i:row.copy()}

    for l in last:
        i      += 1
        row[l] += 1
        if i % k == 0:
            c[i] = row.copy()

    return c


def first_occurrence(first):
    fo = {}

    for f in first:
        if f not in fo:
            fo[f] = first.index(f)

    return fo







def suffix_array(string):
    if string[-1] != '$':
        string += '$'

    sa = []

    for i in xrange(len(string)):
        sa.append((i, string[i:]))

    return sorted(sa, key = lambda x: x[1])


def partial_suffix_array(string, k):
    psa = []

    for index, value in enumerate(suffix_array(string)):
        if value[0] % k == 0:
            psa.append((index, value[0]))

    return psa


def lcp_array(suffix_array):
    lcp = [(0, -1)]

    for i in xrange(1, len(suffix_array)):
        string1 = suffix_array[i - 1][1]
        string2 = suffix_array[i][1]
        for j in xrange(min(len(string1), len(string2))):
            if string1[j] != string2[j]:
                lcp.append((i, j))
                break

    return lcp

