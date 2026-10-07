#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    string X, Y;
    cout << "Enter the strings: ";
    cin >> X >> Y;

    int m = X.length();
    int n = Y.length();

    int dp[101][101] = {0};

    // Build DP table
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (X[i - 1] == Y[j - 1])
            {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            }
            else
            {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // Find the actual LCS
    string lcs = "";

    int i = m;
    int j = n;

    while (i > 0 && j > 0)
    {
        if (X[i - 1] == Y[j - 1])
        {
            lcs = X[i - 1] + lcs;
            i--;
            j--;
        }
        else if (dp[i - 1][j] > dp[i][j - 1])
        {
            i--;
        }
        else
        {
            j--;
        }
    }

    cout << "Length: " << dp[m][n] << endl;
    cout << "LCS: " << lcs << endl;

    return 0;
}