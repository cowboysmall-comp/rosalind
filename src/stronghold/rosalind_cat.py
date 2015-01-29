import sys


"""
    Here are some earlier (and alternative) versions of the matcher:

    1) this was the original. It's a little nasty, but pretty 
    simple. Perhaps the start and end indexes are a little 
    confusing - especially around the recursive calls. I decided 
    I needed to at least think about making it a little easier 
    on the eyes and brain.

        def matchings(rna, start, end, A):
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

        def matchings(rna):
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

        def matchings(rna, A):
            if len(rna) == 0:
                return 1
            if rna not in A:
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

        def matchings(rna):
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

COMPLEMENT = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

def read_fasta(file_path):
    dna = ''

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                dna += line

    return dna


def check_occurences(rna):
    return rna.count('A') == rna.count('U') and rna.count('C') == rna.count('G')


def matchings(rna):
    A = {}
    def match(rna):
        if len(rna) == 0:
            return 1
        if rna not in A:
            A[rna] = 0
            if check_occurences(rna):
                for i in xrange(1, len(rna), 2):
                    if rna[0] == COMPLEMENT[rna[i]]:
                        A[rna] += match(rna[1:i]) * match(rna[i + 1:])
                        A[rna] %= 1000000
        return A[rna]
    return match(rna)


def main(argv):
    print matchings(read_fasta(argv[0]))


if __name__ == "__main__":
    main(sys.argv[1:])
