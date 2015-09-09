import sys
import re
import math
import random
import bisect

from collections import defaultdict
from itertools   import combinations, product

import distance
import graphs


DNA_COMPLEMENT   = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
RNA_COMPLEMENT   = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

SYMBOL_TO_NUMBER = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
NUMBER_TO_SYMBOL = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


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


def reverse_palindromes(string):
    rps  = []

    for i in xrange(4, 13):
        for j in xrange(len(string) - i + 1):
            c = string[j:j + i]
            if c == dna_complement(c):
                rps.append((j + 1, i))

    return sorted(rps)


def gc_content(string):
    return 100 * float(string.count('G') + string.count('C')) / len(string)


def gc_contents(strings):
    contents = []

    for label, string in strings.iteritems():
        contents.append((label, gc_content(string)))

    return contents


def list_kmers(string, k, rc = False):
    length = len(string)
    kmers  = set()

    for i in xrange(length - k + 1):
        kmer = string[i:i + k]
        kmers.add(kmer)
        if rc:
            kmers.add(dna_complement(kmer))

    return sorted(kmers)


def kmer_candidates(strings, k, rc = False):
    candidates = set()

    for string in strings:
        for kmer in list_kmers(string, k, rc):
            candidates.add(kmer)

    return candidates


def paired_kmers(strings):
    kmers = []

    for pairs in strings:
        pair = pairs.split('|')
        kmers.append((pair[0], pair[1]))

    return kmers


def reconstruct_string_from_path(path):
    return path[0][:-1] + ''.join(p[-1] for p in path)


def reconstruct_circular_string_from_path(path):
    return ''.join(p[-1] for p in path[:-1])


def reconstruct_string_from_paired_path(path, k, d):
    string1 = reconstruct_string_from_path([p[0] for p in path])
    string2 = reconstruct_string_from_path([p[1] for p in path])

    for i in xrange(k + d + 1, len(string1)):
        if string1[i] != string2[i - k - d]:
            return None

    return string1 + string2[-(k + d):]


def reconstruct_strings_from_maximal_paths(maximal):
    strings = []

    for path in maximal:
        strings.append(reconstruct_string_from_path(path))

    return sorted(strings)



'''
    original implementation:

    def split_strings(strings):
        correct   = set()
        incorrect = set()

        for string in strings:
            comp = genetics.dna_complement(string)
            if strings.count(string) + strings.count(comp) > 1:
                correct.add(string)
            else:
                incorrect.add(string)

        return correct, incorrect


    def find_corrections(strings):
        corrections        = set()
        correct, incorrect = split_strings(strings)

        for c in correct:
            comp = genetics.dna_complement(c)
            for i in incorrect:
                if distance.hamming(i, c) == 1:
                    corrections.add((i, c))
                elif distance.hamming(i, comp) == 1:
                    corrections.add((i, comp))

        return corrections

'''


def find_corrections_in_reads(reads):
    corrections = set()

    creads      = reads + [dna_complement(r) for r in reads]
    correct     = set([r for r in creads if creads.count(r) > 1])
    incorrect   = set(reads) - correct

    for i in incorrect:
        for c in correct:
            if distance.hamming(i, c) == 1:
                corrections.add((i, c))

    return corrections



def assemble_genome_from_reads(reads):
    length = len(reads[0])

    for i in xrange(length - 1, 1, -1):
        kmers = kmer_candidates(reads, i, rc = True)
        edges = graphs.debruijn_graph(kmers)
        adj   = graphs.adjacency_table(edges)

        if len(graphs.connected_components_iterative(adj)) == 2:
            path = graphs.eulerian_cycle(edges[0][1], edges)
            return reconstruct_circular_string_from_path(path)

    return None


def assemble_genome_from_reads_with_repeats(reads):
    start   = reads[0]
    edges   = graphs.debruijn_graph(reads[1:])

    def list_cycles(start, edges):
        if not edges:
            return [[]]
        else:
            seen   = set()
            cycles = []
            for edge in filter(lambda x: x[0] == start, edges):
                if edge[1] not in seen:
                    seen.add(edge[1])
                    index = edges.index(edge)
                    for cycle in list_cycles(edge[1], edges[:index] + edges[index + 1:]):
                        cycles.append([edge] + cycle)

            return cycles

    strings = set()

    for cycle in list_cycles(start[1:], edges):
        strings.add(start[0] + ''.join(c[0][0] for c in cycle))

    return strings


def kmer_occurences(string, pattern):
    return [i.start() for i in re.finditer(r'(?=(%s))' % pattern, string)]


def kmer_composition(string, k):
    kmers = [''.join(p) for p in product('ACGT', repeat = k)]
    comp  = []

    for kmer in kmers:
        comp.append(len(re.findall(r'(?=(%s))' % kmer, string)))

    return comp


def kmer_frequency_table(string, k):
    stats = {}

    for i in xrange(len(string) - k + 1):
        kmer = string[i:i + k]
        if kmer not in stats:
            stats[kmer] = len(re.findall(r'(?=(%s))' % kmer, string))

    return stats


def kmer_frequency_table_mismatches(string, k, d, complements = False):
    kmers = [''.join(p) for p in product('ACGT', repeat = k)]
    stats = defaultdict(int)

    for kmer in kmers:
        stats[kmer] = len(approximate_pattern_matching(kmer, string, d))
        if complements:
            stats[kmer] += len(approximate_pattern_matching(dna_complement(kmer), string, d))

    return stats


def pattern_to_number(dna):
    if not dna:
        return 0
    return 4 * pattern_to_number(dna[:-1]) + SYMBOL_TO_NUMBER[dna[-1]]


def number_to_pattern(index, k):
    if k == 1:
        return NUMBER_TO_SYMBOL[index]
    return number_to_pattern(index / 4, k - 1) + NUMBER_TO_SYMBOL[index % 4]


def kmer_frequency_array(dna, k):
    freqs = [0 for _ in xrange(4 ** k)]

    for i in xrange(len(dna) - k + 1):
        freqs[pattern_to_number(dna[i:i + k])] += 1

    return freqs


def neighbourhood(pattern, d):
    if d == 0:
        return {pattern}

    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    hood = set()
    for text in neighbourhood(pattern[1:], d):
        if distance.hamming(pattern[1:], text) < d:
            for x in ['A', 'C', 'G', 'T']:
                hood.add(x + text)
        else:
            hood.add(pattern[0] + text)

    return hood



'''
    Here is the original version of the code I wrote - it ran, I 
    thought, quite quickly (around 5 seconds) but then I found this
    version on stack exchange, and was really impressed. I retain 
    both for reference.

    def kmer_clump(dna, k, L, t):
        kmers = []
        seen  = set()

        for i in xrange(len(dna) - k + 1):
            kmer  = dna[i:i + k]
            if kmer not in seen:
                found = [pos.start() for pos in re.finditer(r'(?=(%s))' % kmer, dna)]
                if len(found) >= t and min([found[i + t - 1] + k - found[i] for i in xrange(len(found) - t + 1)]) < L:
                    kmers.append(kmer)
                seen.add(kmer)

        return kmers

'''

def kmer_clump(dna, k, L, t):
    positions = defaultdict(list)
    kmers     = set()

    for i in xrange(len(dna) - k + 1):
        kmer = dna[i:i + k]
        if kmer not in kmers:
            while positions[kmer] and i + k - positions[kmer][0] > L:
                positions[kmer].pop(0)

            positions[kmer].append(i)
            if len(positions[kmer]) == t:
                kmers.add(kmer)

    return kmers


def shared_kmers(s1, s2, k):
    kmers  = set()
    lookup = defaultdict(list)

    for i in xrange(len(s1) - k + 1):
        kmer = s1[i:i + k]
        lookup[kmer].append(i)

    for i in xrange(len(s2) - k + 1):
        kmer = s2[i:i + k]
        for j in lookup[kmer] + lookup[dna_complement(kmer)]:
            kmers.add((j, i))

    return sorted(kmers)


def kmer_reverse_frequency_table(table):
    freq = defaultdict(list)

    for kmer in table:
        freq[table[kmer]].append(kmer)

    return freq


def reverse_skew_table(genome):
    length = len(genome)

    counts = defaultdict(int)
    skew   = defaultdict(list)

    for i in xrange(length):
        counts[genome[i]] += 1
        skew[counts['G'] - counts['C']].append(i + 1)

    return skew


def skew_list(genome):
    length = len(genome)

    counts = defaultdict(int)
    skew   = [0 for _ in xrange(length)]

    for i in xrange(length):
        counts[genome[i]] += 1
        skew[i] = counts['G'] - counts['C']

    return skew


def approximate_pattern_matching(pattern, string, d):
    slength   = len(string)
    plength   = len(pattern)

    positions = []

    for i in xrange(slength - plength + 1):
        if distance.hamming(pattern, string[i:i + plength]) <= d:
            positions.append(i)

    return positions


def implanted_motifs(strings, k, d):
    length    = len(strings)
    motifs    = [''.join(p) for p in product('ACGT', repeat = k)]
    implanted = []

    counter = 0
    for motif in motifs:
        found = []

        for string in strings:
            if approximate_pattern_matching(motif, string, d):
                counter += 1

        if counter == length:
            implanted.append(motif)

        counter = 0

    return implanted


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
        if len(rna) < 2:
            return 1
        elif rna not in A:
            A[rna] = 0
            if check_occurences(rna):
                for i in xrange(1, len(rna), 2):
                    if rna[0] == RNA_COMPLEMENT[rna[i]]:
                        A[rna] += match(rna[1:i]) * match(rna[i + 1:])

        return A[rna]

    return match(rna)


def matchings(rna):
    A = {}

    def match(rna):
        if len(rna) < 2:
            return 1
        elif rna not in A:
            A[rna]  = match(rna[1:])
            A[rna] %= 1000000
            for i in xrange(1, len(rna)):
                if rna[0] == RNA_COMPLEMENT[rna[i]]:
                    A[rna] += match(rna[1:i]) * match(rna[i + 1:])

        return A[rna]

    return match(rna)


def check_wobble(rna1, rna2):
    return (rna1 == 'U' and rna2 == 'G') or (rna1 == 'G' and rna2 == 'U')


def wobble_matchings(rna):
    A = {}

    def match(rna):
        if len(rna) < 4:
            return 1
        elif rna not in A:
            A[rna]  = match(rna[1:])
            for i in xrange(4, len(rna)):
                if rna[0] == RNA_COMPLEMENT[rna[i]] or check_wobble(rna[0], rna[i]):
                    A[rna] += match(rna[1:i]) * match(rna[i + 1:])

        return A[rna]

    return match(rna)


def encode_protein(rna, table):
    encode = ''

    for chunk in [rna[i:i + 3] for i in xrange(0, len(rna), 3)]:
        if len(chunk) == 3:
            amino = table[chunk]
            if amino != 'Stop':
                encode += amino
            else:
                break

    return encode


def encode_protein_from_orf(rna, table):
    encoded = []

    for match in re.compile(r'(?=(AUG))').finditer(rna):
        sub    = rna[match.start():]
        encode = ''

        for chunk in [sub[i:i + 3] for i in xrange(0, len(sub), 3)]:
            if len(chunk) == 3:
                amino = table[chunk]
                if amino != 'Stop':
                    encode += amino
                else:
                    encoded.append(encode)
                    break

    return encoded


def protein_mass(protein, table):
    total = 0.0

    for p in protein:
        total += table[p]

    return total


def spectrum_graph(masses, table):
    edges = []

    for i in xrange(len(masses) - 1):
        for j in xrange(i, len(masses)):
            found = filter(lambda x: abs(x[0] - (masses[j] - masses[i])) < 0.0001, table)
            if found:
                edges.append((masses[i], masses[j], found[0][1]))

    return edges


def longest_protein(nodes, edges):
    proteins = defaultdict(str)

    for node in nodes:
        for edge in filter(lambda x: x[1] == node, edges):
            if len(proteins[node]) < len(proteins[edge[0]]) + 1:
                proteins[node] = proteins[edge[0]] + edge[2]

    return max(proteins.values(), key = len)


def complete_spectrum(protein, table):
    S = []

    for i in xrange(1, len(protein) + 1):
        S.append(protein_mass(protein[:i], table))
        S.append(protein_mass(protein[-i:], table))

    return S


def masses_from_cyclo_spectrum(spectrum):
    length = int((1 + math.sqrt(4 * len(spectrum) - 7)) / 2)
    masses = []

    for i in xrange(1, length + 1):
        masses.append([spectrum[i]])

    return masses


def cyclo_spectrum(masses):
    length   = len(masses)
    spectrum = [0, sum(masses)]
    masses   = masses * 2

    for i in xrange(length):
        for j in xrange(i + 1, i + length):
            spectrum.append(sum(masses[i:j]))

    return sorted(spectrum)


def linear_spectrum(masses):
    length   = len(masses)
    spectrum = [0, sum(masses)]

    for i in xrange(1, length):
        for j in xrange(length - i + 1):
            spectrum.append(sum(masses[j:j + i]))

    return sorted(spectrum)


def matching_peptides(masses, spectrum):
    candidates = masses[:]
    matches    = []

    while candidates:
        for candidate in candidates[:]:
            if set(linear_spectrum(candidate)) < set(spectrum):
                if sum(candidate) == spectrum[-1]:
                    matches.append(candidate)
                    candidates.remove(candidate)
            else:
                candidates.remove(candidate)
        candidates = [c + m for c in candidates for m in masses]

    return matches


def leaderboard_matching_peptides(masses, spectrum, N):
    leader  = (0, [])
    leaders = [leader]

    def score(spectrum1, spectrum2):
        return len(set(spectrum1) & set(spectrum2))

    def expand():
        expanded = []
        for leader in leaders:
            for mass in masses:
                expand = leader[1] + mass
                if sum(expand) <= spectrum[-1]:
                    expanded.append((score(cyclo_spectrum(expand), spectrum), expand))
        return expanded

    def cut(candidates, count):
        if len(candidates) <= count:
            return candidates

        candidates = sorted(candidates, reverse = True)
        value      = candidates[count][0]
        while count < len(candidates) and candidates[count][0] == value:
            count += 1
        return sorted(candidates[:count])

    while leaders:
        candidates = []
        for candidate in expand():
            if sum(candidate[1]) == spectrum[-1]:
                if candidate[0] > leader[0]:
                    leader = candidate
            candidates.append(candidate)
        leaders = cut(candidates, N)

    return leader


def convolution_counts(spectrum):
    counts = defaultdict(int)

    for pair in combinations(sorted(spectrum), 2):
        difference = pair[1] - pair[0]
        if difference != 0:
            counts[difference] += 1

    return counts


def convolution_list(counts):
    convolution = []

    for item in sorted(counts.iteritems(), key = lambda x: x[1], reverse = True):
        convolution.extend([item[0]] * item[1])

    return convolution


def convolution_frequent(counts, M):
    ordered = sorted([(freq, mass) for mass, freq in counts.iteritems() if 57 <= mass <= 200], reverse = True)

    value = ordered[M][0]
    while M < len(ordered) and ordered[M][0] == value:
        M += 1

    return [[item[1]] for item in ordered[:M]]


def sigma_distance(kmer, strings):
    k    = len(kmer)
    dist = 0

    for string in strings:
        hamming = sys.maxint
        length  = len(string)
        for i in xrange(length - k + 1):
            d = distance.hamming(kmer, string[i:i + k])
            if hamming > d:
                hamming = d
        dist += hamming

    return dist


def median_string(strings, k):
    kmers  = kmer_candidates(strings, k)

    dist   = sys.maxint
    median = None

    for kmer in kmers:
        d = sigma_distance(kmer, strings)
        if dist >= d:
            dist   = d
            median = kmer

    return median


def profile_most_kmer(text, profile, k):
    length  = len(text)

    maximum = -float('inf')
    kmer    = None

    for i in xrange(length - k + 1):
        string = text[i:i + k]

        total  = 1.0
        for j, c in enumerate(string):
            total *= profile[c][j]

        if maximum < total:
            maximum = total
            kmer    = string

    return kmer


def profile_most_kmers(strings, profile, k):
    kmers = []

    for string in strings:
        kmers.append(profile_most_kmer(string, profile, k))

    return kmers


def profile_matrix(strings, k, pseudocounts = False):
    length  = len(strings) + 4 if pseudocounts else len(strings)
    profile = {c:[1.0 / float(length) if pseudocounts else 0.0 for _ in xrange(k)] for c in 'ACGT'}

    for string in strings:
        for i in xrange(k):
            profile[string[i]][i] += (1.0 / float(length))

    return profile


def consensus(strings, k):
    kmer = ''

    for i in xrange(k):
        counter = defaultdict(int)

        for string in strings:
            counter[string[i]] += 1

        kmer += max(counter, key = counter.get)

    return kmer


def score(strings, k):
    dist = 0
    kmer = consensus(strings, k)

    for string in strings:
        dist += distance.hamming(string, kmer)

    return dist


def greedy_motif_search(strings, k, pseudocounts = False):
    bmotifs = [string[:k] for string in strings]
    bscore  = score(bmotifs, k)

    first   = strings[0]
    rest    = strings[1:]
    length  = len(first)

    for i in xrange(length - k + 1):
        cmotifs = [first[i:i + k]]

        for string in rest:
            profile = profile_matrix(cmotifs, k, pseudocounts)
            cmotifs.append(profile_most_kmer(string, profile, k))

        cscore = score(cmotifs, k)
        if cscore < bscore:
            bmotifs = cmotifs
            bscore  = cscore

    return bmotifs


def randomized_kmer(string, k):
    length = len(string)
    i      = random.randint(0, length - k)
    return string[i:i + k]


def randomized_kmers(strings, k):
    kmers  = []

    for string in strings:
        kmers.append(randomized_kmer(string, k))

    return kmers


def randomized_motif_search(strings, k, pseudocounts = False):
    motifs  = randomized_kmers(strings, k)

    bmotifs = motifs
    bscore  = score(motifs, k)

    while True:
        profile = profile_matrix(motifs, k, pseudocounts)
        motifs  = profile_most_kmers(strings, profile, k)
        cscore  = score(motifs, k)

        if bscore > cscore:
            bmotifs = motifs
            bscore  = cscore
        else:
            return bmotifs, bscore


def randomized_motif_search_with_iterations(strings, k, iterations, pseudocounts = False):
    bmotifs = None
    bscore  = sys.maxint
    count   = 0

    while count < iterations:
        cmotifs, cscore = randomized_motif_search(strings, k, pseudocounts)

        if bscore > cscore:
            bscore  = cscore
            bmotifs = cmotifs

        count += 1

    return bmotifs


def profile_random_kmer(text, profile, k):
    length  = len(text)
    kmers   = []
    totals  = []
    total   = 0

    for i in xrange(length - k + 1):
        string  = text[i:i + k]

        current = 1.0
        for j, c in enumerate(string):
            current *= profile[c][j]

        total  += current

        kmers.append(string)
        totals.append(total)

    return kmers[bisect.bisect(totals, random.random() * total)]


def profile_random_kmers(text, profile, k):
    kmers  = []

    for string in strings:
        kmers.append(profile_random_kmer(string, profile, k))

    return kmers


def gibbs_sampler(strings, k, t, N, pseudocounts = False):
    motifs  = randomized_kmers(strings, k)

    bmotifs = motifs
    bscore  = score(motifs, k)

    for j in xrange(N):
        i       = random.randrange(t)
        start   = motifs[:i]
        end     = motifs[i + 1:]

        profile = profile_matrix(start + end, k, pseudocounts)
        motif   = profile_random_kmer(strings[i], profile, k)

        motifs  = start + [motif] + end
        cscore  = score(motifs, k)

        if bscore > cscore:
            bmotifs = motifs
            bscore  = cscore

    return bmotifs, bscore


def gibbs_sampler_with_iterations(strings, k, t, N, iterations, pseudocounts = False):
    bmotifs = None
    bscore  = sys.maxint
    count   = 0

    while count < iterations:
        cmotifs, cscore = gibbs_sampler(strings, k, t, N, pseudocounts)

        if bscore > cscore:
            bscore  = cscore
            bmotifs = cmotifs

        count += 1

    return bmotifs


def infer_peptides_from_spectrum(spectrum, table):
    protein = ''

    for i in xrange(1, len(spectrum)):
        protein += filter(lambda x: abs(x[0] - (spectrum[i] - spectrum[i - 1])) < 0.0001, table)[0][1]

    return protein


def infer_peptides_from_masses(masses, table, length):
    peptide = ''
    masses  = [m - masses[0] for m in masses[1:]]

    while len(peptide) < length:
        for i in xrange(len(masses)):
            found = filter(lambda x: abs(x[0] - masses[i]) < 0.0001, table)
            if found:
                peptide += found[0][1]
                masses   = [l - masses[i] for l in masses[i + 1:]]
                break

    return peptide


def count_rnas_from_protein(protein, table):
    total = 3

    for c in protein:
        total *= table[c]
        total %= 1000000

    return total


def count_peptides_with_mass(mass, table):
    M       = [0 for _ in xrange(mass + 1)]
    M[0]    = 1

    masses  = set(table.values())

    for i in xrange(min(masses), mass + 1):
        for m in masses:
            if 0 <= i - m <= mass:
                M[i] += M[i - m]

    return M[mass]


def find_locations_in_protein(protein, motif):
    return [match.start() + 1 for match in re.compile(motif).finditer(protein)]


def find_locations_in_protein_data(data, motif):
    locations = []

    for protein in data:
        found = find_locations_in_protein(protein[1], motif)
        if found:
            locations.append((protein[0], found))

    return locations


def find_peptides_in_dna(dna, amino, table):
    dlength = len(dna)
    alength = len(amino) * 3
    chunks  = []

    for i in xrange(dlength - alength + 1):
        chunk   = dna[i:i + alength]

        rna     = dna_to_rna(chunk)
        protein = encode_protein(rna, table)
        if protein == amino:
            chunks.append(chunk)

        dnac    = dna_complement(chunk)
        rna     = dna_to_rna(dnac)
        protein = encode_protein(rna, table)
        if protein == amino:
            chunks.append(chunk)

    return chunks

