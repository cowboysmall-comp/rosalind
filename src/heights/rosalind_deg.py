import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import graphs


def main(argv):
    n, m, edges = files.read_graph(argv[0])
    degree      = graphs.degree_table(edges)

    print ' '.join(str(degree[i + 1]) for i in xrange(n))


if __name__ == "__main__":
    main(sys.argv[1:])
