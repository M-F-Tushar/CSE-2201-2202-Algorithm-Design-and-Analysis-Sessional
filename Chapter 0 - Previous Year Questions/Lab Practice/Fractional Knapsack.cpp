#include <iostream>
#include <algorithm>

using namespace std;

struct Item
{
    int weight;
    int value;
};


bool compare(Item a, Item b)
{
    return (double)a.value / a.weight > (double)b.value / b.weight;
}


int main()
{
    int n, W;
    cin >> n >> W;

    Item item[100];

    for(int i = 0; i < n; i++)
    {
        cin >> item[i].weight >> item[i].value;
    }

    sort(item, item + n, compare);

    double total = 0;

    for(int i = 0; i < n; i++)
    {
        if(item[i].weight <= W)
        {
            W = W - item[i].weight;
            total = total + item[i].value;
        }
        else
        {
            total = total + ((double)item[i].value / item[i].weight) * W;
            break;
        }
    }
    cout << "Maximum value: " << total << endl;

    return 0;
}