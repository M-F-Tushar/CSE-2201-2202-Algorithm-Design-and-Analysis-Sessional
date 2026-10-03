#include <iostream>
#include <vector>

using namespace std;

vector<long long> build_prefix(const vector<long long>& values)
{
    vector<long long> prefix(values.size());
    if (values.empty())
        return prefix;

    prefix[0] = values[0];
    for (int i = 1; i < static_cast<int>(values.size()); ++i)
        prefix[i] = prefix[i - 1] + values[i];

    return prefix;
}

long long range_sum_prefix(const vector<long long>& prefix, int left, int right)
{
    return prefix[right] - (left == 0 ? 0 : prefix[left - 1]);
}

void update_prefix(vector<long long>& prefix, vector<long long>& values,
                   int index, long long value)
{
    const long long delta = value - values[index];
    values[index] = value;
    for (int i = index; i < static_cast<int>(prefix.size()); ++i)
        prefix[i] += delta;
}

vector<long long> segment_tree;

void build_segment_tree(int node, int left, int right,
                        const vector<long long>& values)
{
    if (left == right)
    {
        segment_tree[node] = values[left];
        return;
    }

    const int middle = left + (right - left) / 2;
    build_segment_tree(2 * node + 1, left, middle, values);
    build_segment_tree(2 * node + 2, middle + 1, right, values);
    segment_tree[node] = segment_tree[2 * node + 1]
                       + segment_tree[2 * node + 2];
}

long long range_sum_segment_tree(int node, int left, int right,
                                 int query_left, int query_right)
{
    if (right < query_left || query_right < left)
        return 0;

    if (query_left <= left && right <= query_right)
        return segment_tree[node];

    const int middle = left + (right - left) / 2;
    return range_sum_segment_tree(2 * node + 1, left, middle,
                                  query_left, query_right)
         + range_sum_segment_tree(2 * node + 2, middle + 1, right,
                                  query_left, query_right);
}

void update_segment_tree(int node, int left, int right,
                         int index, long long value)
{
    if (left == right)
    {
        segment_tree[node] = value;
        return;
    }

    const int middle = left + (right - left) / 2;
    if (index <= middle)
        update_segment_tree(2 * node + 1, left, middle, index, value);
    else
        update_segment_tree(2 * node + 2, middle + 1, right, index, value);

    segment_tree[node] = segment_tree[2 * node + 1]
                       + segment_tree[2 * node + 2];
}

int main()
{
    const vector<long long> original = {2, 1, 5, 3, 4, 7, 6, 8};
    const int size = static_cast<int>(original.size());

    vector<long long> prefix_values = original;
    vector<long long> prefix = build_prefix(prefix_values);
    cout << "Prefix sum, [0,5]: "
         << range_sum_prefix(prefix, 0, 5) << '\n';
    update_prefix(prefix, prefix_values, 2, 10);
    cout << "Prefix sum after update, [0,5]: "
         << range_sum_prefix(prefix, 0, 5) << '\n';

    vector<long long> tree_values = original;
    segment_tree.assign(4 * size, 0);
    build_segment_tree(0, 0, size - 1, tree_values);
    cout << "Segment tree, [0,5]: "
         << range_sum_segment_tree(0, 0, size - 1, 0, 5) << '\n';
    update_segment_tree(0, 0, size - 1, 2, 10);
    cout << "Segment tree after update, [0,5]: "
         << range_sum_segment_tree(0, 0, size - 1, 0, 5) << '\n';
}
