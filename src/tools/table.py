from collections import defaultdict


def codon(file_path):
    table = {}

    with open(file_path) as file:
        for line in file:
            items = line.strip().split()
            for key, value in zip(*[iter(items)] * 2):
                table[key] = value

    return table


def reverse_codon(file_path):
    table = defaultdict(int)

    with open(file_path) as file:
        for line in file:
            items = line.strip().split()
            for key, value in zip(*[iter(items)] * 2):
                table[value] +=1

    return table


def mass(file_path):
    table = {}

    with open(file_path) as file:
        for line in file:
            key, value = line.strip().split()
            table[key] = float(value)

    return table


def integer_mass(file_path):
    table = {}

    with open(file_path) as file:
        for line in file:
            key, value = line.strip().split()
            table[key] = int(float(value))

    return table


def reverse_mass(file_path):
    lookup = []

    with open(file_path) as file:
        for line in file:
            key, value = line.strip().split()
            lookup.append((float(value), key))

    return lookup


def reverse_integer_mass(file_path):
    lookup = []

    with open(file_path) as file:
        for line in file:
            key, value = line.strip().split()
            lookup.append((int(float(value)), key))

    return lookup


def scoring(file_path):
    matrix = defaultdict(dict)

    with open(file_path) as file:
        cols = file.readline().strip().split()
        for line in file:
            items = line.strip().split()
            row   = items[0]
            for i, value in enumerate(items[1:]):
                matrix[row][cols[i]] = int(value)

    return matrix
            
