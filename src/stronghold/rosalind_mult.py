import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import fasta
import strings


def main(argv):
    dna_strings = fasta.read_ordered(argv[0])
    # results     = multiple_alignment(dna_strings)
    results     = strings.quadruple_alignment(dna_strings[0], dna_strings[1], dna_strings[2], dna_strings[3])

    # unfinished - to be completed...

    print results[0]
    # print '\n'.join(results[1])
    print '\n'.join(results[1:])


if __name__ == "__main__":
    main(sys.argv[1:])






def pairwise_scores(dna_strings):
    scores = []

    for i in xrange(len(dna_strings) - 1):
        for j in xrange(i + 1, len(dna_strings)):
            s, t   = dna_strings[i], dna_strings[j]
            l1, l2 = len(s), len(t)
            table  = basic_alignment_table(s, t)
            scores.append((table[l1][l2], s, t))

    return sorted(scores, reverse = True)


def centre_scores(dna_strings, scores):
    centres = []

    for i in xrange(len(dna_strings)):
        sigma = sum(v[0] for v in filter(lambda x: x[1] == dna_strings[i] or x[2] == dna_strings[i], scores))
        centres.append((sigma, dna_strings[i]))

    return sorted(centres, key = lambda x: (-x[0], x[1]))


def closest_aligned(dna_string, aligned):
    C = []
    n = len(dna_string)

    for s in aligned:
        m = len(s)
        T = basic_alignment_table(s, dna_string)
        C.append((T[m][n], s, T))

    return sorted(C, reverse = True)[0][1:]


def scoring(dna_strings):
    score = 0

    for i in xrange(len(dna_strings) - 1):
        for j in xrange(i + 1, len(dna_strings)):
            score += distance.edit(dna_strings[i], dna_strings[j])

    return score


def multiple_alignment(dna_strings):
    scores  = pairwise_scores(dna_strings)
    centres = centre_scores(dna_strings, scores)
    ordered = [c[1] for c in centres]

    stringc = ordered[0]
    aligned = [stringc]

    for stringi in ordered[1:]:
        stringc, T = closest_aligned(stringi, aligned)
        # T          = basic_alignment_table(stringc, stringi)
        m          = len(stringc)
        n          = len(stringi)

        while m + n > 0:
            if T[m][n] == T[m - 1][n - 1] + (MATCH if stringc[m - 1] == stringi[n - 1] else MISMATCH):
                m -= 1
                n -= 1
            elif T[m][n] == T[m - 1][n] + GAP:
                stringi = stringi[:n] + '-' + stringi[n:]
                m -= 1
            elif T[m][n] == T[m][n - 1] + GAP:
                aligned = [s[:m] + '-' + s[m:] for s in aligned]
                n -= 1


        aligned.append(stringi)

    return -scoring(aligned), aligned
    # return sum(v[0] for v in scores), aligned
