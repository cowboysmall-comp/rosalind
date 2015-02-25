import sys
import heapq

import numpy as np

from collections import defaultdict, deque


def create_overlap_nodes(strings, k):
    nodes = []

    for label, string in strings.iteritems():
        nodes.append((label, string[:k], string[-k:], string))

    return nodes


def create_overlap_edges(nodes):
    edges = []

    for node in nodes:
        for tail in filter(lambda x: x[1] == node[2] and x != node, nodes):
            edges.append((node[0], tail[0]))

    return edges


def degree_table(edges, directed = True):
    degree = defaultdict(int)

    for edge in edges:
        degree[edge[1]] += 1
        if not directed:
            degree[edge[0]] += 1

    return degree


def adjacency_table(edges, directed = True):
    adjacency = defaultdict(list)

    for edge in edges:
        adjacency[edge[0]].append(edge[1])
        if not directed:
            adjacency[edge[1]].append(edge[0])

    return adjacency


def weighted_adjacency_table(edges, directed = True):
    adjacency = defaultdict(dict)

    for edge in edges:
        adjacency[edge[0]][edge[1]] = edge[2]
        if not directed:
            adjacency[edge[1]][edge[0]] = edge[2]

    return adjacency


'''
    I've decided to use numpy for my matrix needs. This means 
    all matrix operations will henceforth be implemented with 
    numpy. Python matrix operations are blazingly slow, and 
    numpy is insanely fast.

    For comparison, I've incuded some pure Python code I was 
    using, till I decided I needed the speedup:


    def matrix_multiply(A, B):
        rowsA = len(A)
        colsA = len(A[0])
        rowsB = len(B)
        colsB = len(B[0])

        if colsA != rowsB:
            return

        C = [[0 for _ in xrange(colsB)] for _ in xrange(rowsA)]

        for i in xrange(rowsA):
            for j in xrange(colsB):
                C[i][j] = sum(A[i][k] * B[k][j] for k in xrange(colsA))

        return C


    def adjacency_matrix(n, edges, directed = True):
        A = [[0 for _ in xrange(n)] for _ in xrange(n)]

        for edge in edges:
            A[edge[0] - 1][edge[1] - 1] = 1
            if not directed:
                A[edge[1] - 1][edge[0] - 1] = 1

        return A


    def has_4cycles(A):
        length = len(A)
        cycles = 0

        A2     = matrix_multiply(A, A)
        A4     = matrix_multiply(matrix_multiply(A2, A), A)

        for i in xrange(length):
            cycles += A4[i][i] + A2[i][i] - sum(2 * A2[i][j] for j in xrange(length))

        return cycles / 8

'''

def adjacency_matrix(n, edges, directed = True):
    A = np.zeros((n, n), dtype = int)

    for edge in edges:
        A[edge[0] - 1, edge[1] - 1] = 1
        if not directed:
            A[edge[1] - 1, edge[0] - 1] = 1

    return A


def has_4cycles(A):
    length = len(A)
    cycles = 0

    A2     = A.dot(A)
    A4     = A2.dot(A).dot(A)

    for i in xrange(length):
        cycles += A4[i, i] + A2[i, i] - sum(2 * A2[i, j] for j in xrange(length))

    return cycles / 8 != 0


def breadth_first_search(s, nodes, edges):
    D = {}

    for node in nodes:
        D[node] = -1

    D[s] = 0
    Q    = deque([s])

    while Q:
        node = Q.popleft()
        for edge in edges:
            if node == edge[0] and D[edge[1]] == -1:
                Q.append(edge[1])
                D[edge[1]] = D[node] + 1

    return D


def depth_first_search(s, edges, directed = True):
    explored  = defaultdict(int)
    traversal = []

    def explore(node):
        explored[node] += 1

        for edge in edges:
            if node == edge[0] and explored[edge[1]] == 0:
                explore(edge[1])
            if not directed:
                if node == edge[1] and explored[edge[0]] == 0:
                    explore(edge[0])

        traversal.append(node)

    explore(s)

    return traversal


def connected_components(nodes, edges, directed = True):
    explored   = set()
    components = []

    for node in nodes:
        if node not in explored:
            component = depth_first_search(node, edges, directed)
            explored |= set(component)
            components.append(component)

    return components


def bipartite(s, nodes, edges, directed = True):
    C = {}

    for node in nodes:
        C[node] = -1

    C[s] = 1
    Q    = deque([s])

    while Q:
        u = Q.popleft()
        for edge in edges:
            if u == edge[0]:
                if C[edge[1]] == -1:
                    Q.append(edge[1])
                    C[edge[1]] = 1 - C[u]
                elif C[edge[1]] == C[u]:
                    return False

            if not directed:
                if u == edge[1]:
                    if C[edge[0]] == -1:
                        Q.append(edge[0])
                        C[edge[0]] = 1 - C[u]
                    elif C[edge[0]] == C[u]:
                        return False

    return True


def acyclic(nodes, edges):
    explored  = defaultdict(int)
    colour    = defaultdict(int)

    def detect_cycles(node):
        if explored[node] == 0:
            explored[node] += 1
            colour[node]   += 1

            for edge in edges:
                if node == edge[0]:
                    if explored[edge[1]] == 0 and detect_cycles(edge[1]):
                        return True
                    elif colour[edge[1]] == 1:
                        return True

        colour[node] -= 1
        return False

    for node in nodes:
        if detect_cycles(node):
            return False

    return True


def dijkstra(s, nodes, edges):
    distance = {}
    heap     = []

    for node in nodes:
        distance[node] = float('inf')

    distance[s] = 0
    heapq.heappush(heap, (0, s))

    while len(heap) != 0:
        weighted = heapq.heappop(heap)
        for edge in edges:
            if weighted[1] == edge[0]:
                if distance[edge[1]] > distance[edge[0]] + edge[2]:
                    distance[edge[1]] = distance[edge[0]] + edge[2]
                    if (edge[2], edge[1]) in heap:
                        heap.remove((edge[2], edge[1]))
                        heapq.heapify(heap)
                    heapq.heappush(heap, (distance[edge[1]], edge[1]))

    return distance


def bellman_ford(s, nodes, edges):
    distances = {}

    for node in nodes:
        distances[node] = float('inf')

    distances[s] = 0

    for _ in xrange(len(nodes) - 1):
        updated = False
        for u, v, w in edges:
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                updated      = True

        if not updated:
            break

    for u, v, w in edges:
        if distances[v] > distances[u] + w:
            return None

    return distances


def topological_sort(nodes, edges):
    ordering = []
    explored = defaultdict(int)

    def topological(node):
        explored[node] += 1

        for edge in edges:
            if node == edge[0] and explored[edge[1]] == 0:
                topological(edge[1])

        ordering.append(node)

    for node in nodes:
        if explored[node] == 0:
            topological(node)

    return ordering[::-1]


def hamiltonian_path(nodes, edges):
    ordering = topological_sort(nodes, edges)

    for i in xrange(len(ordering) - 1):
        if (ordering[i], ordering[i + 1]) not in edges:
            return []

    return ordering


def negative_weight_cycle(nodes, edges):
    visited = set()

    for node in nodes:
        if node not in visited:
            distances = bellman_ford(node, nodes, edges)
            if distances:
                for d in distances:
                    if distances[d] != float('inf'):
                        visited.add(d)
            else:
                return True

    return False


def tarjan(nodes, edges):
    index      = {}
    lowlink    = {}
    stack      = []
    components = []

    counter    = [0]

    def scc(node):
        index[node]   = counter[0]
        lowlink[node] = counter[0]
        counter[0]   += 1

        stack.append(node)

        for edge in edges:
            if node == edge[0]:
                head = edge[1]
                if head not in index:
                    scc(head)
                    lowlink[node] = min(lowlink[node], lowlink[head])
                elif head in stack:
                    lowlink[node] = min(lowlink[node], index[head])

        if lowlink[node] == index[node]:
            component  = []
            while node not in component:
                component.append(stack.pop())
            components.append(component)

    for node in nodes:
        if node not in index:
            scc(node)

    return components


def kosaraju(nodes, edges):
    transpose  = [(edge[1], edge[0]) for edge in edges]
    explored   = defaultdict(int)
    stack      = []
    component  = []
    components = []

    def ordering(node):
        explored[node] += 1

        for edge in edges:
            if node == edge[0] and explored[edge[1]] == 0:
                ordering(edge[1])

        stack.append(node)

    def scc(node):
        explored[node] += 1

        for edge in transpose:
            if node == edge[0] and explored[edge[1]] == 0:
                scc(edge[1])

        component.append(node)


    for node in nodes:
        if explored[node] == 0:
            ordering(node)

    explored  = defaultdict(int)

    while stack:
        node = stack.pop()

        if explored[node] == 0:
            scc(node)

        if component:
            components.append(component)
            component = []

    return components


def two_satisfiable(nodes, edges):
    variables   = nodes + [-n for n in nodes]
    clauses     = [(-a, b) for a, b in edges] + [(-b, a) for a, b in edges]
    components  = tarjan(variables, clauses)

    assigned    = set()

    for component in components:
        for node in component:
            if -node in component:
                return []
            if abs(node) not in assigned:
                nodes[abs(node) - 1] = node
                assigned.add(abs(node))

    return nodes


def component_graph(components, edges):
    length     = len(components)

    cnodes     = [i + 1 for i in xrange(length)]
    cedges     = set()

    for edge in edges:
        ctail = filter(lambda x: edge[0] in x and edge[1] not in x, components)
        chead = filter(lambda x: edge[1] in x and edge[0] not in x, components)
        if ctail and chead:
            cedges.add((components.index(ctail[0]) + 1, components.index(chead[0]) + 1))

    return cnodes, cedges


'''
    here is the recommended way to find a general sink, or 
    mother vertex. I came up with my own algorithm that is 
    much quicker:

    1) topological sort graph
    2) choose first node - with in degree 0
    3) get distance from this node to others in graph - bfs 
    4) if any node unreachable, node not a general sink
    5) if all nodes reachable, node a general sink

    I retain this version for reference.

    def general_sink(nodes, edges):
        components     = tarjan(nodes, edges)
        cnodes, cedges = component_graph(components, edges)
        degrees        = degree_table(cedges)

        candidates = [n for n in cnodes if degrees[n] == 0]
        if len(candidates) == 1:
            return components[candidates[0] - 1][0]
        else:
            return -1

'''

def general_sink(nodes, edges):
    topological = topological_sort(nodes, edges)
    source      = topological[0]
    distances   = breadth_first_search(source, nodes, edges)

    if filter(lambda x: distances[x] == -1, distances):
        return -1
    else:
        return source


def semi_connected(nodes, edges):
    components     = tarjan(nodes, edges)
    cnodes, cedges = component_graph(components, edges)
    cnodes         = topological_sort(cnodes, cedges)

    for i in xrange(len(cnodes) - 1):
        if (cnodes[i], cnodes[i + 1]) not in cedges:
            return False

    return True


def shortest_path(s, nodes, edges):
    distances = {}
    nodes     = topological_sort(nodes, edges)

    for node in nodes:
        distances[node] = float('inf')

    distances[s] = 0

    for node in nodes:
        for u, v, w in edges:
            if node == u:
                if distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w

    return distances



def floyd_warshall(nodes, edges):
    n = len(nodes)

    D = [[float('inf') for _ in xrange(n)] for _ in xrange(n)]

    for node in nodes:
        D[node - 1][node - 1] = float('inf')

    for edge in edges:
        D[edge[0] - 1][edge[1] - 1] = edge[2]

    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]

    return D

