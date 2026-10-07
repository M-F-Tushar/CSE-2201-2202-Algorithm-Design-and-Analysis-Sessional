#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int divideConquer(vector<int> a, int b, int e)
{
    // Base Case
    if (b == e)
    {
        return a[b];
    }

    int mid = (b + e) / 2;

    // Left half

    int leftsum = divideConquer(a, b, mid);

    // Righ half
    int rightsum = divideConquer(a, mid + 1, e);

    // Cross Sum

    int leftMax = a[mid];
    int total = 0;

    for(int i = mid; i >=b; i--)
    {
        total = total + a[i];

        if (total > leftMax)
        {
            leftMax = total;
        }
    }

    int rightMax = a[mid + 1];
    total = 0;

    for (int i = mid + 1; i <= e; i++)
    {
        total = total + a[i];

        if(total > rightMax)
        {
            rightMax = total;
        }
    }

    int crossSum = leftMax + rightMax;

    return max({leftsum, rightsum, crossSum});

}

int main()
{
    vector<int> a = {2, 3, -8, 7, 2, -1, 3};

    int n = a.size();

    cout << "Array: ";
    for (int x: a)
    {
        cout << x << " ";
    }
    cout << endl;

    cout << "Maximum Sum: "<< divideConquer(a, 0, n - 1);

    return 0;
}