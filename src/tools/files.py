

def read_line(file_path):
    with open(file_path) as file:
        return file.readline().strip()


def read_lines(file_path):
    lines = []

    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())

    return lines


def read_float(file_path):
    with open(file_path) as file:
        return float(file.readline().strip())


def read_floats(file_path):
    floats = []

    with open(file_path) as file:
        for line in file:
            floats.append(float(line.strip()))

    return floats


def read_int(file_path):
    with open(file_path) as file:
        return int(file.readline().strip())


def read_ints(file_path):
    ints = []

    with open(file_path) as file:
        for line in file:
            ints.append(int(line.strip()))

    return ints


def read_line_of_floats(file_path):
    with open(file_path) as file:
        return [float(i) for i in file.readline().split()]


def read_lines_of_floats(file_path):
    lines = []

    with open(file_path) as file:
        for line in file:
            lines.append([float(i) for i in line.split()])

    return lines


def read_line_of_ints(file_path):
    with open(file_path) as file:
        return [int(i) for i in file.readline().split()]


def read_lines_of_ints(file_path):
    lines = []

    with open(file_path) as file:
        for line in file:
            lines.append([int(i) for i in line.split()])

    return lines


def read_graph(file_path):
    with open(file_path) as file:
        n     = int(file.readline().strip())
        edges = []

        for line in file:
            tail, head = line.strip().split()
            edges.append((int(tail), int(head)))

    return n, edges

