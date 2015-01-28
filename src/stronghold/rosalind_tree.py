import sys

from tools import unionfind


def read_graph(file_path):
    with open(file_path) as file:
        n     = int(file.readline().strip())
        edges = []

        for line in file:
            tail, head = line.strip().split()
            edges.append((int(tail), int(head)))

        return n, edges


def main(argv):
    n, edges  = read_graph(argv[0])
    uf        = unionfind.UnionFind(n)

    for edge in edges:
        uf.union(edge[0], edge[1])

    print uf.count() - 1


if __name__ == "__main__":
    main(sys.argv[1:])
