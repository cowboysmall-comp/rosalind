import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


def create_row(col, char, strings):
    row = []

    for string in strings:
        row.append(1 if char == string[col] else 0)

    return row


def create_table(strings):
    string = strings[0]
    length = len(strings)
    table  = []

    for col, char in enumerate(string):
        row = create_row(col, char, strings)
        if 1 < sum(row) < length - 1:
            table.append(row)

    return table


def main(argv):
    table = create_table(files.read_lines(argv[0]))

    print '\n'.join(''.join(str(r) for r in row) for row in table)


if __name__ == "__main__":
    main(sys.argv[1:])
