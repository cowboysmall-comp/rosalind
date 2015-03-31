import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import arrays
import tree


def main(argv):
    text  = files.read_line(argv[0])
    st    = tree.SuffixTree(text)

    print st.longest_repeat()


    sa    = arrays.suffix_array(text + '$')
    ha    = arrays.lcp_array(sa)
    index = max(ha, key = lambda x: x[1])

    print text[sa[index[0]][0]:sa[index[0]][0] + index[1]]


if __name__ == "__main__":
    main(sys.argv[1:])
