#include <iostream>
#include <vector>

using namespace std;

int n;
vector<vector<int>> board;

bool isSafe(int row, int col)
{
    //column check
    for(int i = 0; i < row; i++)
    {
        if(board[i][col] == 1)
        {
            return false;
        }
    }

    // Right diagonal check
    for(int i = row -1, j = col + 1; i >=0 && j < n; i--, j++)
    {
        if(board[i][j] == 1)
        {
            return false;
        }
    }

    // Left diagonal check
    for(int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
    {
        if(board[i][j] == 1)
        {
            return false;
        }
    }

    return true;
}

bool placeQueen(int row)
{
    if(row == n)
    {
        return true;
    }

    for(int col = 0; col < n; col++)
    {
        if(isSafe(row, col))
        {
            board[row][col] = 1;

            if(placeQueen(row + 1))
            {
                return true;
            }

            board[row][col] = 0;
        }
        
    }

    return false;
}



int main()
{
    
    cout << "Enter the queen number: "<< endl;
    cin >> n;
    board.resize(n, vector<int>(n, 0));

    bool result = placeQueen(0);

    if(result)
    {
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
    }
    else
    {
        cout << "NO Solution";
    }

    return 0;
}