from itertools import combinations


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


def failure_array(string):
    N   = len(string)
    T   = [0] * N

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

        if s[m - 1] == t[n - 1]:
            sequence.insert(0, s[m - 1])
            m -= 1
            n -= 1

    return ''.join(sequence)



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

