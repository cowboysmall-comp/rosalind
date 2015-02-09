

def write_lines(file_path, lines):
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')


def read_line(file_path):
    with open(file_path) as file:
        return file.readline().strip()


def read_lines(file_path):
    lines = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                lines.append(line)

    return lines


def read_float(file_path):
    with open(file_path) as file:
        return float(file.readline().strip())


def read_floats(file_path):
    floats = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                floats.append(float(line))

    return floats


def read_int(file_path):
    with open(file_path) as file:
        return int(file.readline().strip())


def read_ints(file_path):
    ints = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                ints.append(int(line))

    return ints


def read_line_of_words(file_path):
    with open(file_path) as file:
        return [word for word in file.readline().split()]


def read_lines_of_words(file_path):
    lines = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                lines.append([word for word in line.split()])

    return lines


def read_line_of_floats(file_path):
    with open(file_path) as file:
        return [float(i) for i in file.readline().split()]


def read_lines_of_floats(file_path):
    lines = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                lines.append([float(i) for i in line.split()])

    return lines


def read_line_of_ints(file_path):
    with open(file_path) as file:
        return [int(i) for i in file.readline().split()]


def read_lines_of_ints(file_path):
    lines = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                lines.append([int(i) for i in line.split()])

    return lines


def read_graph(file_path):
    with open(file_path) as file:
        graph = [int(i) for i in file.readline().split()]
        edges = []

        for line in file:
            tail, head = line.strip().split()
            edges.append((int(tail), int(head)))

        graph.append(edges)

    return graph


def read_weighted_graph(file_path):
    with open(file_path) as file:
        graph = [int(i) for i in file.readline().split()]
        edges = []

        for line in file:
            tail, head, weight = line.strip().split()
            edges.append((int(tail), int(head), int(weight)))

        graph.append(edges)

    return graph


def read_graphs(file_path):
    with open(file_path) as file:
        k = int(file.readline().strip())

        graph_count = 0
        graphs      = []
        while graph_count < k:
            line = file.readline().strip()
            while not line:
                line = file.readline().strip()

            graph = [int(i) for i in line.split()]

            edge_count = 0
            edges      = []
            while edge_count < graph[1]:
                tail, head = file.readline().strip().split()
                edges.append((int(tail), int(head)))
                edge_count += 1

            graph.append(edges)
            graphs.append(graph)
            graph_count += 1

    return k, graphs


def read_weighted_graphs(file_path):
    with open(file_path) as file:
        k = int(file.readline().strip())

        graph_count = 0
        graphs      = []
        while graph_count < k:
            line = file.readline().strip()
            while not line:
                line = file.readline().strip()

            graph = [int(i) for i in line.split()]

            edge_count = 0
            edges      = []
            while edge_count < graph[1]:
                tail, head, weight = file.readline().strip().split()
                edges.append((int(tail), int(head), int(weight)))
                edge_count += 1

            graph.append(edges)
            graphs.append(graph)
            graph_count += 1

    return k, graphs
