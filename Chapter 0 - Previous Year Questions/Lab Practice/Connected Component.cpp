#include <iostream>
#include <vector>

using namespace std;

void dfs(int node, const vector<vector<int>>& graph, vector<bool>& visited)
{
    visited[node] = true;

    for(int next : graph[node])
    {
        if (!visited[next])
        {
            dfs(next, graph, visited);
        }
    }
}

int main()
{
    int v, e;
    cout << "Number of Vertices and Number of Edges: ";
    cin >> v >> e;

    // Dynamically sized adjacency list and visited array (0-based: 0 to v-1)
    vector<vector<int>> graph(v + 1);
    vector<bool> visited(v + 1, false);

    cout << "Enter endpoints for " << e << " edges (vertices 0 to " << v - 1 << "):\n";
    for(int i = 0; i < e; i++)
    {
        int u, w;
        cin >> u >> w;

        if (u >= 0 && u <= v && w >= 0 && w <= v)
        {
            graph[u].push_back(w);
            graph[w].push_back(u);
        }
    }

    int components = 0;

    for(int i = 0; i < v; i++)
    {
        if(!visited[i])
        {
            dfs(i, graph, visited);
            components++;
        }
    }

    cout << "Connected Components: " << components << endl;

    return 0;
}