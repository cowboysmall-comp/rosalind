import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from Bio.Align.Applications import ClustalwCommandline


def main(argv):
    results = []
    files   = []

    command = ClustalwCommandline("clustalw2", infile = argv[0])

    for line in command():
        for part in line.split():
            if part[0] == '[' and part[-1] == ']':
                files.append(part[1:-1])

    with open(files[1]) as file:
        for line in file:
            if 'Rosalind' in line:
                results.append(line.split()[0])

    os.remove(files[0])
    os.remove(files[1])

    print results[-1]


if __name__ == "__main__":
    main(sys.argv[1:])
