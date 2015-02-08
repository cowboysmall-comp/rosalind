import permutations
import arrays


'''
    the recursive version of merge fails on larger arrays, so I 
    replaced it with an iterative version. The recursive version 
    is kept here for reference.

    def merge(A, B):
        C = []

        if A and B:
            if A[0] > B[0]:
                C.append(B[0])
                C.extend(merge(A, B[1:]))
            else:
                C.append(A[0])
                C.extend(merge(A[1:], B))
        else:
            C.extend(A + B)

        return C

    the original version of merge_sort and merge, which did not 
    include facility to keep track of inversions, is below for 
    comparison. It was proving to be slow on large data so I re-
    wrote it to use indexing rather than list operations 
    (specifically A.pop()). Much faster!

    def merge(A, B):
        C = []

        while A and B:
            if A[0] > B[0]:
                C.append(B.pop(0))
            else:
                C.append(A.pop(0))

        return C + A + B


    def merge_sort(A):
        l = len(A)

        if l > 1:
            return merge(merge_sort(A[:l / 2]), merge_sort(A[l / 2:]))
        else:
            return A

'''

def merge(A, B):
    lengthA    = len(A)
    lengthB    = len(B)
    merged     = []
    inversions = 0

    i = 0
    j = 0

    while i < lengthA and j < lengthB:
        if A[i] > B[j]:
            merged.append(B[j])
            inversions += lengthA - i
            j += 1
        else:
            merged.append(A[i])
            i += 1

    return merged + A[i:] + B[j:], inversions


def merge_sort(A):
    lengthA = len(A)

    if lengthA > 1:
        A1, I1 = merge_sort(A[:lengthA / 2])
        A2, I2 = merge_sort(A[lengthA / 2:])
        AM, IM = merge(A1, A2)
        return AM, I1 + I2 + IM
    else:
        return A, 0


def heap_sort(A):
    length    = len(A)
    heapified = arrays.max_heap(A)

    for i in xrange(length - 1, 0, -1):
        heapified[i], heapified[0] = heapified[0], heapified[i]
        length -= 1
        arrays.max_heapify(heapified, 0, length)

    return heapified


def three_way_partition(A, lower, upper):
    gt = upper
    lt = lower
    i  = lower + 1

    p  = A[lower]
    while i <= gt:
        if A[i] < p:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i  += 1
        elif A[i] > p:
            A[gt], A[i] = A[i], A[gt]
            gt -= 1
        else:
            i  += 1

    return A

'''
    not sure which version I prefer - Sedgewick or the modified 
    version found on Wikipedia. Below is the Wikipedia version - 
    I retain Sedgewick's to be consistent with the three-way 
    partition implementation above.

    def partition(A, lower, upper):
        i = lower + 1

        for j in xrange(lower + 1, upper + 1):
            if A[j] < A[lower]:
                A[j], A[i] = A[i], A[j]
                i += 1

        A[lower], A[i - 1] = A[i - 1], A[lower]

        return i

'''

def partition(A, lower, upper):
    i = lower + 1
    j = upper

    p = A[lower]
    while True:
        while A[i] < p and i < upper:
            i += 1

        while p < A[j] and lower < j:
            j -= 1

        if j <= i:
            break

        A[i], A[j] = A[j], A[i]

    A[lower], A[j] = A[j], A[lower]
    return j


def insertion_sort(A):
    swaps = 0

    for i in xrange(1, len(A)):
        k = i
        while k > 0 and A[k] < A[k - 1]:
            A[k], A[k - 1] = A[k - 1], A[k]
            swaps += 1
            k     -= 1

    return swaps, A


def count_breaks(perm):
    perm  = [min(perm) - 1] + perm + [max(perm) + 1]
    count = 0

    for i in xrange(len(perm) - 1):
        if abs(perm[i + 1] - perm[i]) > 1:
            count += 1

    return count


def get_breaks(perms):
    return [count_breaks(perm[1]) for perm in perms]


def prune_perms(perms, breaks):
    pruned = []

    if breaks:
        minimum = min(breaks)

        for index, value in enumerate(breaks):
            if value == minimum:
                pruned.append(perms[index])

    return pruned


def generate_reversals(perm):
    revs = perm[0]
    perm = perm[1]
    for j in xrange(len(perm) - 1, 1, -1):
        for i in xrange(j):
            yield (revs + [(i + 1, j + 1)], perm[:i] + perm[i:j + 1][::-1] + perm[j + 1:])


def reversal_sort(perm):
    visited  = set()
    visited.add(tuple(perm))

    queue    = []
    queue.append(([], perm))

    count    = 0

    while permutations.IDENTITY not in visited:
        count += 1

        temp = []
        for perm in queue:
            for reversal in generate_reversals(perm):
                rev = tuple(reversal[1])

                if rev == permutations.IDENTITY:
                    return count, reversal[0]

                if rev not in visited:
                    visited.add(rev)
                    temp.append(reversal)

        breaks = get_breaks(temp)
        queue  = prune_perms(temp, breaks)

    return count, []

