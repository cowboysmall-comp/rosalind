from collections import defaultdict


def minkowski_difference(S1, S2):
    m_difference = []

    for i in xrange(len(S1)):
        for j in xrange(len(S2)):
            m_difference.append(S1[i] - S2[j])

    return m_difference


def minkowski_sum(S1, S2):
    m_sum = []

    for i in xrange(len(S1)):
        for j in xrange(len(S2)):
            m_sum.append(S1[i] + S2[j])

    return m_sum


def multiplicity(S):
    multip = defaultdict(int)

    for s in S:
        multip[str(s)] += 1

    return multip
