import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


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


def main(argv):
    distances = files.read_line_of_ints(argv[0])

    print ' '.join(str(distance) for distance in turnpike(distances))


if __name__ == "__main__":
    main(sys.argv[1:])
