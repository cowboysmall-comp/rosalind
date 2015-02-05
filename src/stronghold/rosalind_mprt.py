import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import uniprot
import genetics
import re


def main(argv):
    labels    = files.read_lines(argv[0])
    data      = uniprot.read(labels)
    locations = genetics.find_locations_in_protein_data(data, r'(?=(N[^P][ST][^P]))')

    for location in locations:
        print location[0]
        print ' '.join([str(loc) for loc in location[1]])


if __name__ == "__main__":
    main(sys.argv[1:])
