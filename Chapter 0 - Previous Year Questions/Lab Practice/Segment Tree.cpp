#include <bits/stdc++.h>

using namespace std;

vector<int> tree;

// Build 
void build(int node, int l, int r, vector<int>& arr)
{
    // Base 
    if (l == r)
    {
        tree[node] = arr[l];
        return;
    }

    int mid = (l + r) / 2;

    build(2 * node + 1, l, mid, arr);

    build(2 * node + 2, mid + 1, r, arr);

    tree[node] = tree[2 * node + 1] + tree[2* node + 2];
}

// range sum
int query(int node, int l, int r, int ql, int qr)
{
    // NO overlap
    if (l > qr || r < ql)
    {
        return 0;
    }
    // Complete overlap
    if (l >= ql && r <= qr)
    {
        return tree[node];
    }
    // Partial overlap

    int mid = (l + r) / 2;
    
    int leftsum = query(2 * node + 1, l, mid, ql, qr);

    int rightsum = query(2 * node + 2, mid + 1, r, ql, qr);

    return leftsum + rightsum;
}

//point update

void update(int node, int l, int r, int index, int value)
{
    if (l == r)
    {
        tree[node] = value;
        return;
    }

    int mid = (l + r) / 2;

    if (index <= mid)
    {
        update(2 * node + 1, l, mid, index, value);
    }
    else
    {
        update(2 * node + 2, mid + 1, r, index, value);
    }

    tree[node] = tree[2* node + 1] + tree[2 * node + 2];
}



int main()
{
    vector<int> arr = {2, 1, 5, 3, 4, 7, 6, 8};
    int n = arr.size();

    tree.assign(4 * n, 0);
    build(0, 0, n - 1, arr);

    cout << "Range Sum (0 - 5):" << query(0, 0, n - 1, 0, 5) << "\n";

    update(0, 0, n - 1, 2, 10);

    cout << "Range Sum (0 - 5):" << query(0, 0, n - 1, 0, 5) << "\n";

}