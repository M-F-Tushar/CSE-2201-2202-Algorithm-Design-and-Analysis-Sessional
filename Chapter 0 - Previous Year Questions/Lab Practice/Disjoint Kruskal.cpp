#include <bits/stdc++.h>
using namespace std;

vector<int> parent;
vector<int> ranki;

// Sort edges by weight
bool sortbywt(const tuple<int, int, int>& a, const tuple<int, int, int>& b)
{
    return get<2>(a) < get<2>(b);
}

// Find the root of a vertex
int findop(int u)
{
    if(parent[u] == -1)
    {
        return u;
    }

    return parent[u] = findop(parent[u]);
}

// Union two sets
void unionop(int u, int v)
{
    if(ranki[u] > ranki[v])
    {
        parent[v] = u;
    }
    else if(ranki[v] > ranki[u])
    {
        parent[u] = v;
    }
    else
    {
        parent[u] = v;
        ranki[v]++;
    }
}

int main()
{
    int v, e;
    cin >> v >> e;

    // Store edges: source, destination, weight
    vector<tuple<int, int, int>> edges;

    for(int i = 0; i < e; i++)
    {
        int sc, des, wt;

        cin >> sc >> des >> wt;

        edges.push_back(make_tuple(sc, des, wt));
    }

    // Sort edges by increasing weight
    sort(edges.begin(), edges.end(), sortbywt);

    // Initially, every vertex is a separate set
    parent.assign(v, -1);
    ranki.assign(v, 0);

    // Store MST edges
    vector<tuple<int, int, int>> mst;

    long long totalWeight = 0;

    // Go through edges from smallest weight to largest
    for(const auto& edge : edges)
    {
        int sc = get<0>(edge);
        int des = get<1>(edge);
        int wt = get<2>(edge);

        // Find roots
        int rootsc = findop(sc);
        int rootdes = findop(des);

        // If roots are different, adding this edge will not create a cycle
        if(rootsc != rootdes)
        {
            unionop(rootsc, rootdes);

            mst.push_back(edge);

            totalWeight += wt;

            // MST of v vertices always has v - 1 edges
            if((int)mst.size() == v - 1)
            {
                break;
            }
        }
    }

    // Check whether an MST was successfully created
    if(v > 0 && (int)mst.size() == v - 1)
    {
        cout << "Edges in the MST:" << endl;

        for(const auto& edge : mst)
        {
            cout << get<0>(edge) << " "
                 << get<1>(edge) << " "
                 << get<2>(edge) << endl;
        }

        cout << "Total Weight: " << totalWeight << endl;
    }
    else
    {
        cout << "The graph is disconnected: No MST exists" << endl;
    }

    return 0;
}