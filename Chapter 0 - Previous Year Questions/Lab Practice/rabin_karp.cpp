/**
 * CSE 2202 - Algorithm Sessional Lab Practice
 * Problem: String Pattern Matching using Rabin-Karp Algorithm (Polynomial Rolling Hash)
 * 
 * Input:
 *   Two lines: text and pattern
 * Output:
 *   Starting index of the first occurrence (or all occurrences)
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

const long long P = 31;
const long long MOD = 1000000007LL;

long long val(char c)
{
    return c - 'a' + 1;
}

int main()
{
    string text, pattern;
    if (!(cin >> text >> pattern))
    {
        text = "ababcabab";
        pattern = "cab";
    }

    int n = text.size();
    int m = pattern.size();

    if (m > n || m == 0)
    {
        cout << "Pattern not found" << endl;
        return 0;
    }

    // Step 1: Precompute power array pw[i] = P^i mod MOD
    vector<long long> pw(n);
    pw[0] = 1;
    for (int i = 1; i < n; i++)
    {
        pw[i] = (pw[i - 1] * P) % MOD;
    }

    // Step 2: Precompute prefix hash array hs[i]
    vector<long long> hs(n);
    hs[0] = val(text[0]);
    for (int i = 1; i < n; i++)
    {
        hs[i] = (hs[i - 1] + val(text[i]) * pw[i]) % MOD;
    }

    // Step 3: Compute pattern hash patHash
    long long patHash = 0;
    for (int i = 0; i < m; i++)
    {
        patHash = (patHash + val(pattern[i]) * pw[i]) % MOD;
    }

    // Step 4: Slide the window over the text
    vector<int> matches;
    for (int i = 0; i + m <= n; i++)
    {
        int r = i + m - 1;
        long long winHash = hs[r];
        if (i > 0)
        {
            winHash = (winHash - hs[i - 1] + MOD) % MOD;
        }

        // Compare winHash against patHash * P^i (multiply, never divide)
        if (winHash == (patHash * pw[i]) % MOD)
        {
            matches.push_back(i);
        }
    }

    if (matches.empty())
    {
        cout << "Pattern not found" << endl;
    }
    else
    {
        cout << "Pattern found at indices:";
        for (int idx : matches)
        {
            cout << " " << idx;
        }
        cout << endl;
    }

    return 0;
}
