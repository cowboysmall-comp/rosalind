from collections import defaultdict


def read_ordered(file_path):
    strings = defaultdict(str)
    labels  = []

    with open(file_path) as file:
        label = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                label = line[1:]
                labels.append(label)
            else:
                strings[label] += line

    return [strings[label] for label in labels]


def read(file_path):
    strings = defaultdict(str)

    with open(file_path) as file:
        label = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                label = line[1:]
            else:
                strings[label] += line

    return strings


def read_one(file_path):
    string = ''

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                string += line

    return string


def read_one_from(obj):
    string = ''

    for line in obj:
        line = line.strip()
        if not line.startswith('>'):
            string += line

    return string

