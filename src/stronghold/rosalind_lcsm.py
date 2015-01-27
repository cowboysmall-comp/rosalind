import sys

from collections import defaultdict


def read_fasta(file_path):
    strings = defaultdict(str)

    with open(file_path) as file:
        label = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                label = line[1:]
            else:
                strings[label] += line

    return strings


def longest_common_substring(strings):
    longest = ''
    string  = strings[0]

    for i in xrange(len(string)):
        for j in xrange(i, len(string) + 1):
            current = string[i:j]
            if len(longest) < len(current) and all(current in s for s in strings):
                longest = current

    return longest


def main(argv):
    strings = read_fasta(argv[0])

    print longest_common_substring(strings.values())


if __name__ == "__main__":
    main(sys.argv[1:])
