import sys
import re
import urllib2

from collections import defaultdict


def read_data(file_path):
    data = []

    with open(file_path) as file:
        for line in file:
            label       = line.strip()
            remote      = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.fasta' % (label))
            string      = read_remote(remote)
            data.append((label, string))

    return data


def read_remote(remote):
    string = ''

    for line in remote:
        line = line.strip()
        if not line.startswith('>'):
            string += line

    return string


def main(argv):
    data = read_data(argv[0])

    for value in data:
        locations = [match.start() + 1 for match in re.compile(r'(?=(N[^P][ST][^P]))').finditer(value[1])]
        if locations:
            print value[0]
            print ' '.join([str(location) for location in locations])


if __name__ == "__main__":
    main(sys.argv[1:])
