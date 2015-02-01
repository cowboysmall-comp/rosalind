import math


def combinations(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def permutations(n, r):
    return math.factorial(n) / math.factorial(n - r)


def enumerate_signed_permutations(values):
    if values:
        perms = []
        done  = []

        for value in values:

            if -value not in done:
                temp = values[:]
                temp.remove(value)

                for perm in enumerate_signed_permutations(temp):
                    perms.append([-value] + perm)

            done.append(-value)

            if value not in done:
                temp = values[:]
                temp.remove(value)

                for perm in enumerate_signed_permutations(temp):
                    perms.append([value] + perm)

            done.append(value)

        return perms
    else:
        return [[]]

