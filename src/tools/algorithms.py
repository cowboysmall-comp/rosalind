from collections import defaultdict


def turnpike(distances):
    distances = sorted(filter(lambda x: x > 0, distances))

    def solve(distances, points):
        if not distances:
            return points

        return solve_point(distances, points, distances[-1]) or solve_point(distances, points, points[-1] - distances[-1])

    def solve_point(distances, points, point):
        distances = distances[:]
        points    = points[:]

        for p in points:
            d = abs(p - point)
            if d in distances:
                distances.remove(d)
            else:
                return None

        points.append(point)
        return solve(distances, sorted(points))

    return solve(distances[:-1], [0, distances[-1]])


def minimum_coins(coins, change):
    counts = defaultdict(int)

    for amount in xrange(change + 1):
        counts[amount] = amount
        for coin in coins:
            if coin <= amount:
                counts[amount] = min(counts[amount], counts[amount - coin] + 1)

    return counts[change]


def manhattan_tourist(n, m, down, right):
    S = [[0 for _ in xrange(m + 1)] for _ in xrange(n + 1)]

    for i in xrange(1, n + 1):
        S[i][0] = S[i - 1][0] + down[i - 1][0]

    for j in xrange(1, m + 1):
        S[0][j] = S[0][j - 1] + right[0][j - 1]

    for i in xrange(1, n + 1):
        for j in xrange(1, m + 1):
            S[i][j] = max(S[i - 1][j] + down[i - 1][j], S[i][j - 1] + right[i][j - 1])

    return S[i][j]

