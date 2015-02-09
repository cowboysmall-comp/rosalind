import sys
import heapq

import numpy as np

from collections import defaultdict, deque


def create_nodes(strings):
    nodes = []

    for label, string in strings.iteritems():
        nodes.append((label, string[:3], string[-3:], string))

    return nodes


def create_edges(nodes):
    edges = []

    for node in nodes:
        for tail in filter(lambda x: x[1] == node[2] and x != node, nodes):
            edges.append((node[0], tail[0]))

    return edges


def degree_table(edges):
    degree = defaultdict(int)

    for edge in edges:
        degree[edge[0]] += 1
        degree[edge[1]] += 1

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


def depth_first_search(nodes, edges):
    explored  = defaultdict(int)
    count     = 0

    def explore(node):
        explored[node] += 1

        for edge in edges:
            if node == edge[0] and explored[edge[1]] == 0:
                explore(edge[1])
            elif node == edge[1] and explored[edge[0]] == 0:
                explore(edge[0])

    for node in nodes:
        if explored[node] == 0:
            explore(node)
            count += 1

    return count


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
                    return -1

            if not directed:
                if u == edge[1]:
                    if C[edge[0]] == -1:
                        Q.append(edge[0])
                        C[edge[0]] = 1 - C[u]
                    elif C[edge[0]] == C[u]:
                        return -1

    return 1


def cyclic(nodes, edges):
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
            return -1

    return 1


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
                if distance[edge[0]] + edge[2] < distance[edge[1]]:
                    distance[edge[1]] = distance[edge[0]] + edge[2]
                    if (edge[2], edge[1]) in heap:
                        heap.remove((edge[2], edge[1]))
                        heapq.heapify(heap)
                    heapq.heappush(heap, (distance[edge[1]], edge[1]))

    return distance


def bellman_ford(s, nodes, edges):
    distances = {}
    updated   = False

    for node in nodes:
        distances[node] = float('inf')

    distances[s] = 0

    for _ in xrange(len(nodes) - 1):
        for u, v, w in edges:
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                updated      = True

        if not updated:
            break

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


