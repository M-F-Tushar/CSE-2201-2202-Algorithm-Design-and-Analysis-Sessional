#include <iostream>
#include <algorithm>

using namespace std;

const int INF = 1e9; // Sentinel value representing infinity / no edge

int main()
{
    int n;
    cout << "Number of Vertices: ";
    cin >> n;

    int dist[101][101];

    cout << "Enter the adjacency matrix row by row.\n";
    cout << "For each row, enter " << n << " values (use " << INF << " for no edge / infinity).\n";

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cin >> dist[i][j];
        }
    }

    for(int k = 0; k < n; k++)
    {
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                // Guard against integer overflow and false relaxation of unreachable vertices
                if(dist[i][k] < INF && dist[k][j] < INF)
                {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    cout << "\nShortest Distance Matrix:\n";

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if (dist[i][j] >= INF / 2)
            {
                cout << "INF ";
            }
            else
            {
                cout << dist[i][j] << " ";
            }
        }
        cout << endl;
    }

    return 0;
}