#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cout << "Number of Element: "<< endl;
    cin >> n;

    int a[100];
    int dp[100];

    for(int i = 0; i < n; i++)
    {
        cout << "Element "<< i << endl;
        cin >> a[i];
        dp[i] = 1;
    }

    for(int i = 1; i < n; i++)
    {
        for(int j = 0; j < i; j++)
        {
            if(a[j] < a[i])
            {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    int answer = 0;

    for(int i = 0; i < n; i++)
    {
        answer = max(answer, dp[i]);
    }

    cout<< "LIS length: "<< answer << endl;

    return 0;
}