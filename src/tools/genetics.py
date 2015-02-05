import re

from collections import defaultdict
from itertools   import product


DNA_COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

RNA_COMPLEMENT = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}


def dna_count(string):
    symbols = defaultdict(int)

    for character in string:
        symbols[character] += 1    

    return symbols


def dna_complement(string):
    dna = []

    for character in string:
        dna.append(DNA_COMPLEMENT[character])

    return ''.join(dna[::-1])


def dna_to_rna(string):
    rna_string = []

    for character in string:
        if character == 'T':
            rna_string.append('U')
        else:
            rna_string.append(character)

    return ''.join(rna_string)


def gc_content(string):
    return 100 * float(string.count('G') + string.count('C')) / len(string)


def gc_contents(strings):
    contents = []

    for label, string in strings.iteritems():
        contents.append((label, gc_content(string)))

    return contents


def kmer_composition(string, alpha, k):
    kmers = [''.join(p) for p in product(*[alpha] * k)]

    A = []
    for kmer in kmers:
        A.append(len(re.findall(r'(?=(%s))' % kmer, string)))

    return A


def check_occurences(rna):
    return rna.count('A') == rna.count('U') and rna.count('C') == rna.count('G')


"""
    Here are some earlier (and alternative) versions of the perfect 
    matcher:

    1) this was the original. It's a little nasty, but pretty 
    simple. Perhaps the start and end indexes are a little 
    confusing - especially around the recursive calls. I decided 
    I needed to at least think about making it a little easier 
    on the eyes and brain.

        def perfect_matchings(rna, start, end, A):
            if end < start:
                return 1
            elif A[start, end] == -1:
                A[start, end] = 0

                if check_occurences(rna[start:end + 1]):
                    for i in xrange(start + 1, end + 1, 2):
                        if rna[start] == COMPLEMENT[rna[i]]:
                            A[start, end] += matchings(rna, start + 1, i - 1, A) * matchings(rna, i + 1, end, A)
                            A[start, end] %= 1000000

            return A[start, end]


    2) here is a slightly altered version of 1 above - it is 
    constructed to hide the creation of the numpy array - called 
    A - used for sub-problem caching. The recursion step is also 
    hidden from view. It's still not perfect, but a step in the 
    right direction maybe. 

        import numpy as np

        def perfect_matchings(rna):
            N = len(rna)
            A = np.empty((N, N), dtype = int)
            A.fill(-1)

            def match(rna, start, end):
                if end < start:
                    return 1
                elif A[start, end] == -1:
                    A[start, end] = 0
                    if check_occurences(rna[start:end + 1]):
                        for i in xrange(start + 1, end + 1, 2):
                            if rna[start] == COMPLEMENT[rna[i]]:
                                A[start, end] += match(rna, start + 1, i - 1) * match(rna, i + 1, end)
                                A[start, end] %= 1000000
                return A[start, end]

            return match(rna, 0, N - 1)


    3) this was a version I wrote soon after - it seemed cleaner 
    to me because it used split strings, and no indexes were passed
    around. Also, it used a Python dictionary, rather than a numpy 
    array (not that I object to numpy in the slightest - on the 
    contrary, I love it - but I set myself the task of using standard 
    Python as much as possible on these solutions). The final version 
    is the one used below - it's same as this version, but as above 
    the sub-problem cache and recursion steps are now hidden.

        def perfect_matchings(rna, A):
            if len(rna) == 0:
                return 1
            elif rna not in A:
                A[rna] = 0
                if check_occurences(rna):
                    for i in xrange(1, len(rna), 2):
                        if rna[0] == COMPLEMENT[rna[i]]:
                            A[rna] += matchings(rna[1:i], A) * matchings(rna[i + 1:], A)
                            A[rna] %= 1000000
            return A[rna]


    4) and just out of interest, here is a version, based on a 
    version written in Ruby that I found in the forums, and 
    translated into Python. It is much slower, but I find it 
    fascinating. For some reason, examples of Dynamic Programming 
    always tend to turn my brain inside out, and this example is no 
    different in that respect.

        def perfect_matchings(rna):
            A = np.zeros((len(rna), len(rna)), dtype = int)

            for i in xrange(len(rna)):
                for j in xrange(i - 1, -1, -1):
                    if rna[i] == COMPLEMENT[rna[j]]:
                        A[i, j] = A[i - 1, j + 1] if j + 1 <= i - 1 else 1

                for j in xrange(i):
                    for k in xrange(j):
                        A[i, k] += A[i, j] * A[j - 1, k]
                        A[i, k] %= 1000000

            return A


    I have no idea what's going on here :-)

"""

def perfect_matchings(rna):
    A = {}

    def match(rna):
        if len(rna) == 0:
            return 1
        elif rna not in A:
            A[rna] = 0
            if check_occurences(rna):
                for i in xrange(1, len(rna), 2):
                    if rna[0] == RNA_COMPLEMENT[rna[i]]:
                        A[rna] += match(rna[1:i]) * match(rna[i + 1:])
                        A[rna] %= 1000000

        return A[rna]

    return match(rna)


def matchings(rna):
    A = {}

    def match(rna):
        if len(rna) == 0 or len(rna) == 1:
            return 1
        elif rna not in A:
            A[rna]  = match(rna[1:])
            A[rna] %= 1000000
            for i in xrange(1, len(rna)):
                if rna[0] == RNA_COMPLEMENT[rna[i]]:
                    A[rna] += match(rna[1:i]) * match(rna[i + 1:])
                    A[rna] %= 1000000

        return A[rna]

    return match(rna)


def encode_protein(rna, table):
    encode = ''

    for chunk in [rna[i:i + 3] for i in xrange(0, len(rna), 3)]:
        amino = table[chunk]
        if amino != 'Stop':
            encode += amino
        else:
            break

    return encode


def protein_weight(protein, table):
    total = 0.0

    for p in protein:
        total += table[p]

    return total


def count_rnas_from_protein(protein, table):
    total = 3

    for c in protein:
        total *= table[c]
        total %= 1000000

    return total


def find_locations_in_protein(protein, motif):
    return [match.start() + 1 for match in re.compile(motif).finditer(protein)]


def find_locations_in_protein_data(data, motif):
    locations = []

    for protein in data:
        found = find_locations_in_protein(protein[1], motif)
        if found:
            locations.append((protein[0], found))

    return locations


