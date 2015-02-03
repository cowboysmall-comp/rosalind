import sys


def main(argv):
    with open(argv[0]) as file:
        # U    = set(i for i in xrange(1, int(file.readline().strip()) + 1))
        # set1 = set(int(item) for item in file.readline().strip()[1:-1].split(', '))
        # set2 = set(int(item) for item in file.readline().strip()[1:-1].split(', '))

        # print '{%s}' % ', '.join(str(element) for element in set1 | set2)
        # print '{%s}' % ', '.join(str(element) for element in set1 & set2)
        # print '{%s}' % ', '.join(str(element) for element in set1 - set2)
        # print '{%s}' % ', '.join(str(element) for element in set2 - set1)
        # print '{%s}' % ', '.join(str(element) for element in U - set1)
        # print '{%s}' % ', '.join(str(element) for element in U - set2)


        U    = set(str(i) for i in xrange(1, int(file.readline().strip()) + 1))
        set1 = set(file.readline().strip()[1:-1].split(', '))
        set2 = set(file.readline().strip()[1:-1].split(', '))

        print '{%s}' % ', '.join(set1 | set2)
        print '{%s}' % ', '.join(set1 & set2)
        print '{%s}' % ', '.join(set1 - set2)
        print '{%s}' % ', '.join(set2 - set1)
        print '{%s}' % ', '.join(U - set1)
        print '{%s}' % ', '.join(U - set2)


if __name__ == "__main__":
    main(sys.argv[1:])
