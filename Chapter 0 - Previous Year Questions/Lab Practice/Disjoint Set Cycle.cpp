#include <iostream>
#include <vector>

using namespace std;

vector<int> parent;

int find_op(int u)
{
    if(parent[u] == -1)
    {
        return u;
    }
    return find_op(parent[u]);
}

void union_op(int root1, int root2)
{
    parent[root2] = root1;
}

bool is_cycle(vector<pair<int, int>> edges)
{
    for(auto edge : edges)
    {
        int src = edge.first;
        int des = edge.second;

        int src_root = find_op(src);
        int des_root = find_op(des);

        if(src_root == des_root)
        {
            return true;
        }

        union_op(src_root, des_root);
    }
    return false;
}

int main()
{
    int v = 5;

    vector<pair<int, int>> edges = 
    {
        {0, 1},
        {0, 2},
        {1, 3},
        {2, 4},
        {1, 4}
    };

    parent.resize(v, -1);

    if(is_cycle(edges))
    {
        cout << "Cycle exist" << endl;
    }
    else
    {
        cout << "No Cycle" << endl;
    }

    return 0;
}