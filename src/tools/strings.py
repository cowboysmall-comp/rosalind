from collections import defaultdict
from itertools import combinations


MATCH    =  0
MISMATCH = -1
GAP      = -1


def basic_alignment_table(s, t):
    m = len(s)
    n = len(t)

    T = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]

    for i in xrange(1, m + 1):
        T[i][0] = GAP * i

    for j in xrange(1, n + 1):
        T[0][j] = GAP * j

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            T[i][j] = max(T[i - 1][j - 1] + (MATCH if s[i - 1] == t[j - 1] else MISMATCH), T[i - 1][j] + GAP, T[i][j - 1] + GAP)

    return T


def optimal_basic_alignment(s, t):
    m   = len(s)
    n   = len(t)

    T   = basic_alignment_table(s, t)
    e_d = -T[m][n]

    s_a = []
    t_a = []

    while m + n > 0:
        if T[m][n] == T[m - 1][n] + GAP:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif T[m][n] == T[m][n - 1] + GAP:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        elif T[m][n] == T[m - 1][n - 1] + (MATCH if s[m - 1] == t[n - 1] else MISMATCH):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            m -= 1
            n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)


def count_basic_alignments(s, t):
    m = len(s)
    n = len(t)

    T = basic_alignment_table(s, t)
    V = defaultdict(int)

    def alignments(m, n):
        if m != 0 and n != 0:
            if (m, n) not in V:
                total = 0
                if T[m][n] == T[m - 1][n] + GAP:
                    total += alignments(m - 1, n)
                if T[m][n] == T[m][n - 1] + GAP:
                    total += alignments(m, n - 1)
                if T[m][n] == T[m - 1][n - 1] + (MATCH if s[m - 1] == t[n - 1] else MISMATCH):
                    total += alignments(m - 1, n - 1)
                V[(m, n)] = total
            return V[(m, n)]
        else:
            return 1

    return alignments(m, n)


def alignment_table(s, t, scoring, gap = -5):
    m = len(s)
    n = len(t)

    T = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]

    for i in xrange(1, m + 1):
        T[i][0] = gap * i

    for j in xrange(1, n + 1):
        T[0][j] = gap * j

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            T[i][j] = max(T[i - 1][j - 1] + scoring[s[i - 1]][t[j - 1]], T[i - 1][j] + gap, T[i][j - 1] + gap)

    return T


def optimal_alignment(s, t, scoring, gap = -5):
    m   = len(s)
    n   = len(t)

    T   = alignment_table(s, t, scoring, gap)
    e_d = T[m][n]

    s_a = []
    t_a = []

    while m + n > 0:
        if T[m][n] == T[m - 1][n] + gap:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif T[m][n] == T[m][n - 1] + gap:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        elif T[m][n] == T[m - 1][n - 1] + scoring[s[m - 1]][t[n - 1]]:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            m -= 1
            n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)


def local_alignment_table(s, t, scoring, gap = -5):
    m       = len(s)
    n       = len(t)

    table   = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]

    maximum = (0, 0, 0)

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            table[i][j] = max(table[i - 1][j - 1] + scoring[s[i - 1]][t[j - 1]], table[i - 1][j] + gap, table[i][j - 1] + gap, 0)
            if maximum[0] < table[i][j]:
                maximum = (table[i][j], i, j)

    return table, maximum


def local_alignment(s, t, scoring, gap = -5):
    T, M = local_alignment_table(s, t, scoring, gap)

    e_d  = M[0]
    m, n = M[1:]

    s_a  = []
    t_a  = []

    while T[m][n] > 0:
        if T[m][n] == T[m - 1][n] + gap:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif T[m][n] == T[m][n - 1] + gap:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        elif T[m][n] == T[m - 1][n - 1] + scoring[s[m - 1]][t[n - 1]]:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            m -= 1
            n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)


def fitting_alignment_table(s, t):
    m       = len(s)
    n       = len(t)

    table   = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]

    maximum = (0, 0, 0)

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            table[i][j] = max(table[i - 1][j - 1] + (1 if s[i - 1] == t[j - 1] else -1), table[i - 1][j] - 1, table[i][j - 1] - 1)
            if i >= n and j >= n and maximum[0] < table[i][j]:
                maximum = (table[i][j], i, j)

    return table, maximum


def fitting_alignment(s, t):
    T, M = fitting_alignment_table(s, t)

    e_d  = M[0]
    m, n = M[1:]

    s_a  = []
    t_a  = []

    while m > 0 and n > 0:
        if T[m][n] == T[m - 1][n] - 1:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif T[m][n] == T[m][n - 1] - 1:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        elif T[m][n] == T[m - 1][n - 1] + (1 if s[m - 1] == t[n - 1] else -1):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            m -= 1
            n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)


def overlap_alignment_table(s, t):
    m       = len(s)
    n       = len(t)

    table   = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]

    maximum = (0, 0, 0)

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            table[i][j] = max(table[i - 1][j - 1] + (1 if s[i - 1] == t[j - 1] else -2), table[i - 1][j] - 2, table[i][j - 1] - 2)

    for j in xrange(n, 0, -1):
        if maximum[0] < table[m][j]:
            maximum = (table[m][j], m, j)

    return table, maximum


def overlap_alignment(s, t):
    T, M = overlap_alignment_table(s, t)

    e_d  = M[0]
    m, n = M[1:]

    s_a  = []
    t_a  = []

    while n > 0:
        if T[m][n] == T[m - 1][n] - 2:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif T[m][n] == T[m][n - 1] - 2:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        elif T[m][n] == T[m - 1][n - 1] + (1 if s[m - 1] == t[n - 1] else -2):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            m -= 1
            n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)


def affine_gap_alignment_table(s, t, scoring, sigma = -11, epsilon = -1):
    m       = len(s)
    n       = len(t)

    table   = [[[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)] for _ in xrange(3)]

    maximum = (0, 0, 0, 0)

    for i in xrange(1, m + 1):
        table[0][i][0] = sigma + (i - 1) * epsilon
        table[1][i][0] = sigma + (i - 1) * epsilon
        table[2][i][0] = sigma + (i - 1) * epsilon

    for j in xrange(1, n + 1):
        table[0][0][j] = sigma + (j - 1) * epsilon
        table[1][0][j] = sigma + (j - 1) * epsilon
        table[2][0][j] = sigma + (j - 1) * epsilon

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            table[0][i][j] = max(table[0][i - 1][j] + epsilon, table[1][i - 1][j] + sigma)
            table[2][i][j] = max(table[2][i][j - 1] + epsilon, table[1][i][j - 1] + sigma)
            table[1][i][j] = max(table[0][i][j], table[1][i - 1][j - 1] + scoring[s[i - 1]][t[j - 1]], table[2][i][j])

    for i in xrange(3):
        if maximum[0] < table[i][m][n]:
            maximum = (table[i][m][n], i, m, n)

    return table, maximum


def affine_gap_alignment(s, t, scoring, sigma = -11, epsilon = -1):
    T, M    = affine_gap_alignment_table(s, t, scoring, sigma, epsilon)

    e_d     = M[0]
    l, m, n = M[1:]

    s_a     = []
    t_a     = []

    while m > 0 and n > 0:
        if l == 0:
            if T[0][m][n] == T[1][m - 1][n] + sigma:
                l = 1
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif l == 2:
            if T[2][m][n] == T[1][m][n - 1] + sigma:
                l = 1
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        else:
            if T[1][m][n] == T[0][m][n]:
                l = 0
            elif T[1][m][n] == T[2][m][n]:
                l = 2
            else:
                s_a.insert(0, s[m - 1])
                t_a.insert(0, t[n - 1])
                m -= 1
                n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)


def failure_array(string):
    N = len(string)
    T = [0] * N

    pos = 1
    idx = 0
    while pos < N:
        if string[pos] == string[idx]:
            idx   += 1
            T[pos] = idx
            pos   += 1
        elif idx > 0:
            idx    = T[idx - 1]
        else:
            pos   += 1

    return T


def longest_subsequence(seq, increasing = True):
    sub = []

    for i in xrange(len(seq)):
        if increasing:
            sub.append(max([sub[j] for j in xrange(i) if sub[j][-1] < seq[i]] or [[]], key = len) + [seq[i]])
        else:
            sub.append(max([sub[j] for j in xrange(i) if sub[j][-1] > seq[i]] or [[]], key = len) + [seq[i]])

    return max(sub, key = len)


def sequence_table(s, t):
    m = len(s)
    n = len(t)

    C = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            if s[i - 1] == t[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])

    return C


def longest_common_subsequence(s, t):
    m = len(s)
    n = len(t)

    C = sequence_table(s, t)

    sequence = []

    while m != 0 and n != 0:
        if C[m][n] == C[m - 1][n]:
            m -= 1
        elif C[m][n] == C[m][n - 1]:
            n -= 1
        elif s[m - 1] == t[n - 1]:
            sequence.insert(0, s[m - 1])
            m -= 1
            n -= 1

    return ''.join(sequence)


'''
    this is a version of the below implementation that uses indexes
    rather than string slicing. Also, I'm going to have to start 
    refactoring code into tools.

    def shortest_supersequence(s, t, lcs):
        scs  = ''

        idxs = 0
        idxt = 0

        for char in lcs:
            while idxs < len(s) and s[idxs] != char:
                scs  += s[idxs]
                idxs += 1

            while idxt < len(t) and t[idxt] != char:
                scs  += t[idxt]
                idxt += 1

            scs  += char
            idxs += 1
            idxt += 1

        if idxs < len(s):
            scs += s[idxs:]

        if idxt < len(t):
            scs += t[idxt:]

        return scs

'''

def shortest_supersequence(s, t):
    lcs = longest_common_subsequence(s, t)
    scs = ''

    for char in lcs:
        while s and s[0] != char:
            scs  += s[0]
            s     = s[1:]

        while t and t[0] != char:
            scs  += t[0]
            t     = t[1:]

        scs  += char
        s, t  = s[1:], t[1:]

    if len(s) > 0:
        scs += s

    if len(t) > 0:
        scs += t

    return scs


def find_overlaps(s, t):
    length = min(len(s), len(t))
    total  = len(s) + len(t)

    for i in xrange(length):
        if s[i - length:] == t[:length - i]:
            combined = s + t[length - i:]
            return (total - len(combined), combined, [s, t])
        elif t[i - length:] == s[:length - i]:
            combined = t + s[length - i:]
            return (total - len(combined), combined, [s, t])

    return None


def shortest_superstring(strings):
    while len(strings) > 1:
        found = []

        for combination in combinations(strings, 2):
            overlap = find_overlaps(*combination)
            if overlap:
                found.append(overlap)

        joined  = max(found)
        strings = filter(lambda x: x not in joined[2], strings)
        strings.append(joined[1])

    return strings[0]


def longest_common_substring(strings):
    longest = ''
    string  = strings[0]

    for i in xrange(len(string)):
        for j in xrange(i, len(string) + 1):
            current = string[i:j]
            if len(longest) < len(current) and all(current in s for s in strings):
                longest = current

    return longest


def interwoven_sequences(string1, string2):
    length1 = len(string1)
    length2 = len(string2)

    if length1 + length2 == 1:
        return string1 if length2 == 0 else string2

    sequences = set()

    if string1:
        for sequence in interwoven_sequences(string1[1:], string2):
            sequences.add(string1[0] + sequence)

    if string2:
        for sequence in interwoven_sequences(string1, string2[1:]):
            sequences.add(string2[0] + sequence)

    return sequences


def sequences_interweave(string, string1, string2):
    if len(string1) == 0:
        return string.startswith(string2)

    if len(string2) == 0:
        return string.startswith(string1)

    return ((string1[0] == string[0] and sequences_interweave(string[1:], string1[1:], string2)) 
        or  (string2[0] == string[0] and sequences_interweave(string[1:], string1, string2[1:])))


def interwoven_matrix(string, strings):
    lstring  = len(string)
    lstrings = len(strings)
    lall     = [len(s) for s in strings]
    M        = [[0 for i in xrange(lstrings)] for _ in xrange(lstrings)]

    for i in xrange(lstrings):
        for j in xrange(i, lstrings):
            for k in xrange(lstring - lall[i] - lall[j] + 1):
                if sequences_interweave(string[k:], strings[i], strings[j]):
                    M[i][j] = 1
                    M[j][i] = 1

    return M


def longest_substring(node, k):
    strings = []

    for child in node.children:
        string = child.data
        if child.descendent_count() >= k:
            substrings = longest_substring(child, k)
            if substrings:
                for substring in substrings:
                    strings.append(string + substring)
            else:
                strings.append(string)

    return sorted(strings)


def find_indices_of_subsequence(s, t):
    indices = []
    index   = 0

    for c in t:
        index = s.find(c, index)
        indices.append(index + 1)

    return indices


def find_indices_of_substrings(s, t):
    indices = []
    index   = 0

    while index < len(s):
        index = s.find(t, index)
        if index == -1:
            break
        indices.append(index + 1)
        index += 1

    return indices

