import sorts


def quick_select(A, k):
    while True:
        lt, gt = sorts.partition3(A, 0, len(A) - 1)

        if k < lt:
            A = A[:lt]
        elif k > gt:
            A  = A[gt + 1:]
            k -= gt + 1
        else:
            return A[lt]

