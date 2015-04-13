#include <vector>
#include <iostream>

using namespace std;


void update_table(vector< vector<int> > &D, string &s, string t, int k) {

    int m = s.length();
    int n = t.length();

    for(int i = 1; i <= m; i++) {

        for(int j = max(1, i - k); j <= min(n, i + k); j++) {

            int mis = (s[i - 1] == t[j - 1]) ? D[i - 1][j - 1] : (D[i - 1][j - 1] - 1);
            int gap = max(D[i - 1][j] - 1, D[i][j - 1] - 1);

            D[i][j] = max(mis, gap);
        }
    }
}


vector< vector<int> > create_matrix(int m, int k) {

    vector< vector<int> > D(m + 1, vector<int>(m + k + 1));

    for(int i = 1; i <= m; i++) {

        fill(D[i].begin(), D[i].end(), -99999);
        D[i][0] = D[i - 1][0] - 1;
    }

    for(int j = 1; j <= m + k; j++) {

        D[0][j] = D[0][j - 1] - 1;
    }

    return D;
}


vector< pair<int, int> > similar_motifs(string &s, string t, int k) {

    int m = s.length();
    int n = t.length();

    vector< vector<int> > D = create_matrix(m, k);

    vector< pair<int, int> > F;

    for(int i = 0; i <= n - (m + k); i++) {

        update_table(D, s, t.substr(i, m + k), k);

        for(int j = m - k; j <= m + k; j++) {

            if (D[m][j] >= -k) {

                F.push_back(make_pair(i + 1, j));
            }
        }
    }

    return F;
}


int main() {

    int    k;
    string s;
    string t;

    cin >> k;
    cin >> s;
    cin >> t;

    vector< pair<int, int> > F = similar_motifs(s, t, k);

    for(int i = 0; i < F.size(); i++) {

        cout << F[i].first << ' ' << F[i].second << endl;
    }
}

