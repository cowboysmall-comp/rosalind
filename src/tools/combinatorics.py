import math


def combinations(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def permutations(n, r):
    return math.factorial(n) / math.factorial(n - r)


def fibonacci(n):
    fib = [0, 1]
    for _ in xrange(2, n + 1):
        fib.append(fib[-1] + fib[-2])

    return fib[n]


def fibonacci_with_reproduction(n, k):
    fib = [1, 1]

    for _ in xrange(2, n):
        fib.append(fib[-1] + (fib[-2] * k))

    return fib[n - 1]


def fibonacci_with_mortality(n, m):
    fib = [1, 1, 1]

    for _ in xrange(2, n):
        if len(fib) - 1 < m:
            fib.append(fib[-1] + fib[-2])
        else:
            fib.append(fib[-1] + fib[-2] - fib[-m - 1])

    return fib[n]


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

