import sys


def fibonacci(n, m):
    fib = [1, 1, 1]

    for _ in xrange(2, n):
        if len(fib) - 1 < m:
            fib.append(fib[-1] + fib[-2])
        else:
            fib.append(fib[-1] + fib[-2] - fib[-m - 1])

    return fib[n]


def main(argv):
    with open(argv[0]) as file:
        n, k = [int(item) for item in file.readline().split()]

        print fibonacci(n, k)


if __name__ == "__main__":
    main(sys.argv[1:])
