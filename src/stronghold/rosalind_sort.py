import sys


IDENTITY = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def read_perms(file_path):
    with open(file_path) as file:
        p1 = [int(i) for i in file.readline().split()]
        p2 = [int(i) for i in file.readline().split()]

        return composition(inverse(p2), p1)


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
    return [count_breaks(perm[1]) for perm in perms]


def prune_perms(perms, breaks):
    pruned = []

    if breaks:
        minimum = min(breaks)

        for index, value in enumerate(breaks):
            if value == minimum:
                pruned.append(perms[index])

    return pruned


def generate_reversals(perm):
    revs = perm[0]
    perm = perm[1]
    for j in xrange(len(perm) - 1, 1, -1):
        for i in xrange(j):
            yield (revs + [(i + 1, j + 1)], perm[:i] + perm[i:j + 1][::-1] + perm[j + 1:])


def reversal_sort(perm):
    visited  = set()
    visited.add(tuple(perm))

    queue    = []
    queue.append(([], perm))

    count    = 0

    while IDENTITY not in visited:
        count += 1

        temp = []
        for perm in queue:
            for reversal in generate_reversals(perm):
                rev = tuple(reversal[1])

                if rev == IDENTITY:
                    return count, reversal[0]

                if rev not in visited:
                    visited.add(rev)
                    temp.append(reversal)

        breaks = get_breaks(temp)
        queue  = prune_perms(temp, breaks)

    return count, []


def main(argv):
    count, reversals = reversal_sort(read_perms(argv[0]))

    print count
    print '\n'.join(' '.join(str(r) for r in reversal) for reversal in reversals)


if __name__ == "__main__":
    main(sys.argv[1:])
