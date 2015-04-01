import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from subprocess import call

import files


def base_filtration_by_quality(q):
    lines = []

    call('java -jar libs/trimmomatic-0.33.jar SE -phred33 in.fastq out.fastq LEADING:%s TRAILING:%s' % (q, q), shell = True)

    with open('out.fastq') as file:
        for line in file:
            lines.append(line.strip())

    os.remove('in.fastq')
    os.remove('out.fastq')

    return lines



def main(argv):
    lines = files.read_lines(argv[0])
    q     = lines[0]
    files.write_lines('in.fastq', lines[1:])

    lines = base_filtration_by_quality(q)

    print
    print '\n'.join(lines)


if __name__ == "__main__":
    main(sys.argv[1:])
