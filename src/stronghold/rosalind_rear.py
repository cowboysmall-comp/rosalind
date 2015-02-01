import sys


IDENTITY = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def read_perms(file_path):
    perms = []

    with open(file_path) as file:
        pair = []

        for line in file:
            line = line.strip()

            if line:
                pair.append([int(i) for i in line.split()])

            if len(pair) == 2:
                perms.append(composition(inverse(pair[1]), pair[0]))
                pair = []

    return perms


def inverse(a):
    return [value[1] for value in sorted([(n - 1, i + 1) for i, n in enumerate(a)])]


def composition(a, b):
    return [a[v - 1] for v in b]


def count_breaks(perm):
    perm  = [min(perm) - 1] + perm + [max(perm) + 1]
    count = 0

    for i in xrange(len(perm) - 1):
        if abs(perm[i + 1] - perm[i]) > 1:
            count += 1

    return count


def get_breaks(perms):
    return [count_breaks(perm) for perm in perms]


def prune_perms(perms, breaks):
    pruned = []

    if breaks:
        minimum = min(breaks)

        for index, value in enumerate(breaks):
            if value == minimum:
                pruned.append(perms[index])

    return pruned


def generate_reversals(perm):
    for j in xrange(len(perm) - 1, 1, -1):
        for i in xrange(j):
            yield perm[:i] + perm[i:j + 1][::-1] + perm[j + 1:]


def reversal_sort(perm):
    visited  = set()
    visited.add(tuple(perm))

    queue    = []
    queue.append(perm)

    count    = 0

    while IDENTITY not in visited:
        count += 1

        temp   = []
        for perm in queue:
            for reversal in generate_reversals(perm):
                rev = tuple(reversal)

                if rev == IDENTITY:
                    return count

                if rev not in visited:
                    visited.add(rev)
                    temp.append(reversal)

        breaks = get_breaks(temp)
        queue  = prune_perms(temp, breaks)

    return count


def main(argv):
    perms = read_perms(argv[0])
    D     = []

    for perm in perms:
        D.append(reversal_sort(perm))

    print ' '.join(str(d) for d in D)


if __name__ == "__main__":
    main(sys.argv[1:])
