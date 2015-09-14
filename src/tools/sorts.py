import permutations
import arrays
import graphs

from collections import defaultdict


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


def partition3(A, lower, upper):
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

    return lt, gt


'''
    not sure which version I prefer - Sedgewick or the modified 
    version found on Wikipedia. Below is the Wikipedia version - 
    I retain Sedgewick's to be consistent with the three-way 
    partition implementation above.

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

'''

def partition(A, lower, upper):
    i = lower + 1

    for j in xrange(lower + 1, upper + 1):
        if A[j] < A[lower]:
            A[j], A[i] = A[i], A[j]
            i += 1

    A[lower], A[i - 1] = A[i - 1], A[lower]

    return i - 1


def quick_sort(A, lower, higher):
    if lower < higher:
        p = partition(A, lower, higher)
        quick_sort(A, lower, p - 1)
        quick_sort(A, p + 1, higher)

    return A


def partial_sort(A, k):
    length    = len(A)
    heapified = arrays.min_heap(A)

    for i in xrange(length - 1, length - k - 1, -1):
        heapified[i], heapified[0] = heapified[0], heapified[i]
        length -= 1
        arrays.min_heapify(heapified, 0, length)

    return heapified[-k:][::-1]


def insertion_sort(A):
    swaps = 0

    for i in xrange(1, len(A)):
        k = i
        while k > 0 and A[k] < A[k - 1]:
            A[k], A[k - 1] = A[k - 1], A[k]
            swaps += 1
            k     -= 1

    return swaps, A


def greedy_reversal_sort(perm):
    distance = 0
    perms    = []

    for k in xrange(len(perm)):
        if abs(perm[k]) != k + 1:
            l         = perm.index(k + 1) if (k + 1) in perm else perm.index(-(k + 1))
            perm      = perm[:k] + [-p for p in perm[k:l + 1][::-1]] + perm[l + 1:]
            distance += 1
            perms.append(perm)
        if perm[k] == -(k + 1):
            perm      = perm[:k] + [-perm[k]] + perm[k + 1:]
            distance += 1
            perms.append(perm)

    return distance, perms


def breakpoints(perm):
    perm  = [0] + perm + [len(perm) + 1]
    count = 0

    for i in xrange(len(perm) - 1):
        if perm[i + 1] - perm[i] != 1:
            count += 1

    return count


def chromosome_to_cycle(chromosome):
    nodes = [None] * (2 * len(chromosome))

    for j in xrange(1, len(chromosome) + 1):
        i = chromosome[j - 1]
        if i > 0:
            nodes[(2 * j) - 2] =  (2 * i) - 1
            nodes[(2 * j) - 1] =  (2 * i)
        else:
            nodes[(2 * j) - 2] = -(2 * i)
            nodes[(2 * j) - 1] = -(2 * i) - 1

    return nodes


def cycle_to_chromosome(nodes):
    chromosome = [None] * (len(nodes) // 2)

    for j in xrange(1, (len(nodes) // 2) + 1):
        if nodes[(2 * j) - 2] < nodes[(2 * j) - 1]:
            chromosome[j - 1] = nodes[(2 * j) - 1] / 2
        else:
            chromosome[j - 1] = -nodes[(2 * j) - 2] / 2

    return chromosome


def colored_edges(genome):
    edges = []

    for chromosome in genome:
        nodes  = chromosome_to_cycle(chromosome)
        length = len(nodes)
        for j in xrange(1, len(chromosome) + 1):
            edges.append((nodes[((2 * j) - 1) % length], nodes[(2 * j) % length]))

    return edges


def ordered_edges(length):
    return [((2 * i) - 1, 2 * i) for i in xrange(1, length + 1)]


def get_cycles(edges):
    cycles = []
    cycle  = []

    for pair in zip(ordered_edges(len(edges)), edges):
        if pair[0][0] in pair[1]:
            if pair[0][1] not in cycle:
                cycle.append(pair[0][1])
            cycle.append(pair[0][0])
        else:
            if pair[0][0] not in cycle:
                cycle.append(pair[0][0])
            cycle.append(pair[0][1])

        if pair[1][1] in cycle:
            cycles.append(cycle)
            cycle = []
        else:
            cycle.append(pair[1][1])

    return cycles


def graph_to_genome(edges):
    chromosomes = []

    nodes      = graphs.nodes_from_edges(edges)
    components = graphs.connected_components(nodes, edges)

    for cycle in get_cycles(edges):
        chromosomes.append(cycle_to_chromosome(cycle))

    return chromosomes


'''
    a version that doesn't use cycle_to_chromosome

    def graph_to_genome(edges):
        chromosomes = []
        chromosome  = []
        seen        = set()

        for i, pair in enumerate(zip(black_edges(len(edges)), edges)):
            if pair[0][1] in pair[1]:
                chromosome.append(i + 1)
            else:
                chromosome.append(-(i + 1))

            if pair[1][1] in seen:
                chromosomes.append(chromosome)
                chromosome = []
            else:
                seen.add(pair[0][0])
                seen.add(pair[0][1])

        return chromosomes

'''

def two_break_distance(P, Q):
    edges      = set()

    for genome in [P, Q]:
        for edge in colored_edges(genome):
            edges.add(edge)

    # nodes      = graphs.nodes_from_edges(edges)
    # components = graphs.connected_components(nodes, edges, False)

    adjacency  = graphs.adjacency_table(edges, False)
    components = graphs.connected_components_iterative(adjacency)

    return sum(len(g) for g in P) - len(components)


def two_break_on_genome_graph(edges, i1, i2, j1, j2):
    if (i1, i2) in edges:
        edges.remove((i1, i2))
        edges.append((i1, j1))
    else:
        edges.remove((i2, i1))
        edges.append((j1, i1))

    if (j1, j2) in edges:
        edges.remove((j1, j2))
        edges.append((i2, j2))
    else:
        edges.remove((j2, j1))
        edges.append((i2, j2))

    return edges








def black_edges_from_genome(genome):
    edges = []

    for chromosome in genome:
        nodes  = chromosome_to_cycle(chromosome)
        length = len(nodes)
        for j in xrange(len(chromosome)):
            edges.append((nodes[(2 * j)], nodes[(2 * j) + 1]))

    return edges


def black_edges_from_coloured_edges(edges):
    length = len(edges)
    black  = []

    for i in xrange(length):
        black.append((edges[(length - 1 + i) % length][1], edges[(length + i) % length][0]))

    return black








def full_graph_to_genome(edges):
    chromosomes = []

    nodes       = sorted(graphs.nodes_from_edges(edges))
    for cycle in graphs.connected_components(nodes, edges):
        chromosomes.append(cycle_to_chromosome(cycle))

    # adjacency  = graphs.adjacency_table(edges, False)
    # for cycle in graphs.connected_components_iterative(adjacency):
    #     chromosomes.append(cycle_to_chromosome(list(cycle)))

    return chromosomes


def two_break_on_genome(P, i1, i2, j1, j2):
    edges = black_edges_from_genome([P]) + colored_edges([P])
    edges = two_break_on_genome_graph(edges, i1, i2, j1, j2)

    return full_graph_to_genome(edges)








def count_breaks(perm):
    perm  = [0] + perm + [len(perm) + 1]
    count = 0

    for i in xrange(len(perm) - 1):
        if abs(perm[i + 1] - perm[i]) > 1:
            count += 1

    return count


def prune_perms(perms):
    pruned = []
    breaks = [count_breaks(perm[1]) for perm in perms]

    if breaks:
        minimum = min(breaks)

        for index, value in enumerate(breaks):
            if value == minimum:
                pruned.append(perms[index])

    return pruned


def generate_reversals(perm):
    for j in xrange(len(perm[1]) - 1, 1, -1):
        for i in xrange(j):
            yield perm[0] + [(i + 1, j + 1)], perm[1][:i] + perm[1][i:j + 1][::-1] + perm[1][j + 1:]


def reversal_sort(perm):
    visited = set()
    visited.add(tuple(perm))

    queue   = []
    queue.append(([], perm))

    count   = 0

    while permutations.IDENTITY not in visited:
        count += 1

        temp   = []
        for perm in queue:
            for reversal in generate_reversals(perm):
                rev = tuple(reversal[1])

                if rev == permutations.IDENTITY:
                    return count, reversal[0]

                if rev not in visited:
                    visited.add(rev)
                    temp.append(reversal)

        queue  = prune_perms(temp)

    return count, []

