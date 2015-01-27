import sys


def fibonacci(n, k):
    fib = [1, 1]

    for _ in xrange(2, n):
        fib.append(fib[-1] + (fib[-2] * k))

    return fib[n - 1]


def main(argv):
    with open(argv[0]) as file:
        n, k = file.readline().strip().split()

        print fibonacci(int(n), int(k))


if __name__ == "__main__":
    main(sys.argv[1:])
