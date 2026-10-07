#include <algorithm>
#include <iostream>
using namespace std;
int main()
{
    int n, w;
    cout << "Enter the number of items and the maximum weight: ";
    cin >> n >> w;

    int weight[101], value[101];

    for (int i = 1; i <= n; i++)
    {
        cout << "Enter weight and value for item " << i << ": ";
        cin >> weight[i] >> value[i];
    }

    int dp[101][101] = {0};

    for (int i =  1; i <= n; i++)
    {
        for (int j = 0; j <= w; j++)
        {
            if(weight[i] <= j)
            {
                dp[i][j] = max(dp[i - 1][j], 
                                value[i] + dp[i - 1][j - weight[i]]);
            }
            else
            {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    cout << dp[n][w] << endl;
    int j = w;
    
    for(int i = n; i >= 1; i--)
    {
        if(dp[i][j] != dp[i - 1][j])
        {
            cout << "item" << i << endl;
            j -= weight[i];
        }
    }
}