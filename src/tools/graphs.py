

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
