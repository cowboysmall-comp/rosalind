import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import arrays
import tree


def main(argv):
    dna  = files.read_line(argv[0])
    N    = len(dna)


    sa   = arrays.suffix_array(dna)
    lcp  = arrays.lcp_array(sa)
    sub1 = sum(len(sa[i][1][:-1]) - lcp[i][1] for i in xrange(1, N + 1))


    st   = tree.SuffixTree(dna)
    sub2 = sum(len(s) - 1 if s[-1] == '$' else len(s) for s in st.traverse())


    m    = sum([min(4 ** i, N - i + 1) for i in xrange(N)])


    print
    print 'suffix tree  - lc: %0.4f' % (sub1 / float(m))
    print
    print 'suffix array - lc: %0.4f' % (sub2 / float(m))
    print


if __name__ == "__main__":
    main(sys.argv[1:])
