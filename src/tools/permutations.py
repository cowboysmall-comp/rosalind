

IDENTITY = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def inverse(a):
    return [value[1] for value in sorted([(n - 1, i + 1) for i, n in enumerate(a)])]


def composition(a, b):
    return [a[v - 1] for v in b]

