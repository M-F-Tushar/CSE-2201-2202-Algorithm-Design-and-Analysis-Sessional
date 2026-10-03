#include <algorithm>
#include <cstddef>
#include <iostream>
#include <stdexcept>
#include <vector>

using Sum = long long;
using namespace std;

Sum maximum_subarray_brute_force(const vector<Sum>& values)
{
    if (values.empty())
        throw invalid_argument("Array must contain at least one element");

    Sum best = values[0];
    for (size_t start = 0; start < values.size(); ++start)
    {
        Sum current = 0;
        for (size_t end = start; end < values.size(); ++end)
        {
            current += values[end];
            best = max(best, current);
        }
    }
    return best;
}

Sum maximum_crossing_sum(const vector<Sum>& values, int left, int middle, int right)
{
    Sum left_best = values[middle];
    Sum running = 0;
    for (int i = middle; i >= left; --i)
    {
        running += values[i];
        left_best = max(left_best, running);
    }

    Sum right_best = values[middle + 1];
    running = 0;
    for (int i = middle + 1; i <= right; ++i)
    {
        running += values[i];
        right_best = max(right_best, running);
    }

    return left_best + right_best;
}

Sum maximum_subarray_divide_and_conquer_range(
    const vector<Sum>& values, int left, int right)
{
    if (left == right)
        return values[left];

    const int middle = left + (right - left) / 2;
    const Sum left_best =
        maximum_subarray_divide_and_conquer_range(values, left, middle);
    const Sum right_best =
        maximum_subarray_divide_and_conquer_range(values, middle + 1, right);
    const Sum crossing_best =
        maximum_crossing_sum(values, left, middle, right);

    return max({left_best, right_best, crossing_best});
}

Sum maximum_subarray_divide_and_conquer(const vector<Sum>& values)
{
    if (values.empty())
        throw invalid_argument("Array must contain at least one element");

    return maximum_subarray_divide_and_conquer_range(
        values, 0, static_cast<int>(values.size()) - 1);
}

Sum maximum_subarray_kadane(const vector<Sum>& values)
{
    if (values.empty())
        throw invalid_argument("Array must contain at least one element");

    Sum current = values[0];
    Sum best = values[0];
    for (size_t i = 1; i < values.size(); ++i)
    {
        current = max(values[i], current + values[i]);
        best = max(best, current);
    }
    return best;
}

struct SubarrayResult
{
    Sum sum;
    size_t start;
    size_t end; // Inclusive.
};

SubarrayResult maximum_subarray_kadane_with_indices(const vector<Sum>& values)
{
    if (values.empty())
        throw invalid_argument("Array must contain at least one element");

    Sum current = values[0];
    Sum best = values[0];
    size_t current_start = 0;
    size_t best_start = 0;
    size_t best_end = 0;

    for (size_t i = 1; i < values.size(); ++i)
    {
        if (values[i] > current + values[i])
        {
            current = values[i];
            current_start = i;
        }
        else
        {
            current += values[i];
        }

        if (current > best)
        {
            best = current;
            best_start = current_start;
            best_end = i;
        }
    }

    return {best, best_start, best_end};
}

int main()
{
    const vector<Sum> values = {2, 3, -8, 7, 2, -1, 3};
    const SubarrayResult result = maximum_subarray_kadane_with_indices(values);

    cout << "Brute force: " << maximum_subarray_brute_force(values) << '\n';
    cout << "Divide and conquer: "
         << maximum_subarray_divide_and_conquer(values) << '\n';
    cout << "Kadane: " << maximum_subarray_kadane(values) << '\n';
    cout << "Best subarray: [" << result.start << ", " << result.end
         << "] with sum " << result.sum << '\n';
}
