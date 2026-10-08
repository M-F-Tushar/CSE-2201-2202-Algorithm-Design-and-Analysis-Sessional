#include <iostream>
#include <vector>

using namespace std;

vector<int> graph[100]; // Store the neighbors of vertex i. Also called adjacencey list.
bool visited[100];

void dfs(int node)
{
    visited[node] = true;

    for(int next : graph[node])
    {
        if (!visited[next])
        {
            dfs(next);
        }
    }
}


int main()
{
    int v, e;
    cout << "Number of Verticees and Number of Edges: ";
    cin >> v >> e;

    for(int i = 0; i < e; i++)
    {
        int u, w;
        cout << "\nEnter the endpoint of edges: ";
        cin >> u >> w;

        graph[u].push_back(w);
        graph[w].push_back(u);
    }

    int components = 0;

    for(int i = 0; i < v; i++)
    {
        if(!visited[i])
        {
            dfs(i);
            components++;
        }
    }

    cout << "Connected Components: " << components << endl;

    return 0;
}