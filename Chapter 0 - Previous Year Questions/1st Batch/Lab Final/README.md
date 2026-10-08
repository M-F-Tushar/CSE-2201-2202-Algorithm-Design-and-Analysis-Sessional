# CSE 2202 Lab Final — Questions and Answers

- **Course:** Algorithm Design and Analysis Sessional
- **Exam:** B.Sc. Engineering, 2nd Year, 2nd Semester Final Examination, 2024
- **Time:** 2 hours
- **Full marks:** 120

> The paper says to answer one tick-marked question. This guide gives an exam-style
> answer for all ten questions so each topic can be revised. The explanations use
> simple English. The C++ programs are separate; compile and run one program at a
> time.

The answers follow the repository's notes on [searching](../../../Chapter%204%20-%20Searching%20and%20Basic%20Traversal/README.md), [greedy algorithms](../../../Chapter%207%20-%20Greedy%20Algorithms/README.md), [dynamic programming](../../../Chapter%208%20-%20Dynamic%20Programming/README.md), and [0/1 knapsack](../../Lab%20Practice/0_1_knapsack.cpp).

## Contents

1. [Linear and Binary Search](#1-linear-and-binary-search)
2. [Iterative and Recursive Merge Sort](#2-iterative-and-recursive-merge-sort)
3. [Iterative and Recursive Quick Sort](#3-iterative-and-recursive-quick-sort)
4. [Greedy Change-Making](#4-greedy-change-making)
5. [Greedy Fractional Knapsack](#5-greedy-fractional-knapsack)
6. [Fibonacci by Recursion and Dynamic Programming](#6-fibonacci-by-recursion-and-dynamic-programming)
7. [Coin-Row Problem by Dynamic Programming](#7-coin-row-problem-by-dynamic-programming)
8. [Change-Making by Dynamic Programming](#8-change-making-by-dynamic-programming)
9. [Coin-Collecting Problem by Dynamic Programming](#9-coin-collecting-problem-by-dynamic-programming)
10. [0/1 Knapsack by Dynamic Programming](#10-01-knapsack-by-dynamic-programming)

---

## 1. Linear and Binary Search

### Question

Implement linear search and binary search. Explain their time complexity and
compare the two algorithms.

### Answer

Searching means finding the position of a required value in a collection.

**Linear search** checks the elements one by one from the beginning. It works on
both sorted and unsorted arrays. If the target is present, it returns its index;
otherwise, it returns `-1`.

**Binary search** compares the target with the middle element. It then discards
the half that cannot contain the target. The array **must be sorted** before
binary search is used.

#### Algorithm

```text
LINEAR-SEARCH(A, n, key)
1. for i = 0 to n - 1:
2.     if A[i] == key:
3.         return i
4. return -1

BINARY-SEARCH(A, n, key)       // A must be sorted
1. low = 0, high = n - 1
2. while low <= high:
3.     mid = low + (high - low) / 2
4.     if A[mid] == key: return mid
5.     if A[mid] < key: low = mid + 1
6.     else: high = mid - 1
7. return -1
```

#### C++ implementation

**Input:** `n`, then `n` array values, then the target. For binary search, enter
the array in increasing order. Indices are zero-based.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int linearSearch(const vector<int>& a, int key) {
    for (int i = 0; i < static_cast<int>(a.size()); ++i) {
        if (a[i] == key) return i;
    }
    return -1;
}

int binarySearch(const vector<int>& a, int key) {
    int low = 0;
    int high = static_cast<int>(a.size()) - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == key) return mid;
        if (a[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

int main() {
    int n, key;
    cin >> n;
    vector<int> a(n);
    for (int& x : a) cin >> x;
    cin >> key;

    cout << "Linear search index: " << linearSearch(a, key) << '\n';
    cout << "Binary search index: " << binarySearch(a, key) << '\n';
}
```

#### Sample input and output

```text
Input
6
2 5 8 12 16 23
12

Output
Linear search index: 3
Binary search index: 3
```

#### Result analysis and comparison

For six values, linear search may check all six values. Binary search cuts the
remaining range approximately in half at each step: 6, 3, 1. Both return index
`3` for the target `12` in this example.

| Feature | Linear search | Binary search |
| :--- | :--- | :--- |
| Required order | Any order | Sorted array required |
| Best-case time | `O(1)` | `O(1)` |
| Average/worst-case time | `O(n)` | `O(log n)` |
| Extra space, iterative | `O(1)` | `O(1)` |
| Suitable use | Small or unsorted data | Large, sorted data |

**Conclusion:** Use linear search when the data is unsorted or small. Use binary
search for a sorted array when fast repeated searches are needed.

---

## 2. Iterative and Recursive Merge Sort

### Question

Implement merge sort using both recursive and iterative approaches, and compare
their time complexities.

### Answer

Merge sort is a divide-and-conquer sorting algorithm. It divides an array into
two halves, sorts each half, and merges the two sorted halves. The merge step
keeps the final values in order.

The recursive version divides until each part has one value. The iterative
version starts with sorted runs of length one, then merges runs of length two,
four, eight, and so on.

#### Algorithm and recurrence

```text
RECURSIVE-MERGE-SORT(A, left, right)
1. if left >= right: return
2. mid = left + (right - left) / 2
3. sort A[left ... mid]
4. sort A[mid + 1 ... right]
5. merge the two sorted parts

ITERATIVE-MERGE-SORT(A)
1. runLength = 1
2. while runLength < n:
3.     merge each adjacent pair of runs of runLength
4.     double runLength
```

The recurrence for recursive merge sort is

\[
T(n)=2T(n/2)+\Theta(n),\qquad T(1)=\Theta(1).
\]

There are `log n` levels, and each level does `Theta(n)` merge work. Therefore,
`T(n) = Theta(n log n)`.

#### C++ implementation

This program runs both versions on the same input.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void mergeRanges(vector<int>& a, int left, int mid, int right) {
    vector<int> temp;
    int i = left, j = mid + 1;
    while (i <= mid && j <= right) {
        if (a[i] <= a[j]) temp.push_back(a[i++]);
        else temp.push_back(a[j++]);
    }
    while (i <= mid) temp.push_back(a[i++]);
    while (j <= right) temp.push_back(a[j++]);
    for (int k = 0; k < static_cast<int>(temp.size()); ++k) {
        a[left + k] = temp[k];
    }
}

void recursiveMergeSort(vector<int>& a, int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    recursiveMergeSort(a, left, mid);
    recursiveMergeSort(a, mid + 1, right);
    mergeRanges(a, left, mid, right);
}

void iterativeMergeSort(vector<int>& a) {
    int n = static_cast<int>(a.size());
    for (int width = 1; width < n; width *= 2) {
        for (int left = 0; left < n; left += 2 * width) {
            int mid = min(left + width, n);
            int right = min(left + 2 * width, n);
            if (mid < right) mergeRanges(a, left, mid - 1, right - 1);
        }
    }
}

void printArray(const vector<int>& a) {
    for (int x : a) cout << x << ' ';
    cout << '\n';
}

int main() {
    int n;
    cin >> n;
    vector<int> original(n);
    for (int& x : original) cin >> x;

    vector<int> recursive = original;
    vector<int> iterative = original;
    recursiveMergeSort(recursive, 0, n - 1);
    iterativeMergeSort(iterative);

    cout << "Recursive: ";
    printArray(recursive);
    cout << "Iterative: ";
    printArray(iterative);
}
```

#### Sample input and output

```text
Input
8
8 3 5 1 7 2 6 4

Output
Recursive: 1 2 3 4 5 6 7 8
Iterative: 1 2 3 4 5 6 7 8
```

#### Result analysis and comparison

Both approaches produce the same sorted array. In either approach, there are
about `log2(n)` merge levels and each level processes `n` values.

| Feature | Recursive merge sort | Iterative merge sort |
| :--- | :--- | :--- |
| Time, best/average/worst | `O(n log n)` | `O(n log n)` |
| Temporary array space | `O(n)` | `O(n)` |
| Call-stack space | `O(log n)` | `O(1)` |
| Main method | Recursively split, then merge | Repeatedly merge wider runs |

Merge sort is stable when equal values are taken from the left run first. Its
worst-case time remains `O(n log n)`.

---

## 3. Iterative and Recursive Quick Sort

### Question

Implement quick sort using both iterative and recursive approaches, and compare
their time complexities.

### Answer

Quick sort chooses a **pivot**, partitions the array so values on one side are
smaller and values on the other side are larger, and then sorts the parts. This
answer uses the last element as the pivot (Lomuto partition).

The recursive version calls itself for the two parts. The iterative version
stores the parts that still need sorting in an explicit stack.

#### Algorithm and recurrence

```text
QUICK-SORT(A, low, high)
1. if low < high:
2.     p = PARTITION(A, low, high)
3.     QUICK-SORT(A, low, p - 1)
4.     QUICK-SORT(A, p + 1, high)

PARTITION moves values <= pivot left of the pivot
and returns the pivot's final index.
```

If the partition divides the array evenly,

\[
T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n).
\]

If the pivot is always the smallest or largest value,

\[
T(n)=T(n-1)+\Theta(n)=\Theta(n^2).
\]

#### C++ implementation

```cpp
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

int partitionArray(vector<int>& a, int low, int high) {
    int pivot = a[high];
    int smallerEnd = low;
    for (int i = low; i < high; ++i) {
        if (a[i] <= pivot) {
            swap(a[i], a[smallerEnd]);
            ++smallerEnd;
        }
    }
    swap(a[smallerEnd], a[high]);
    return smallerEnd;
}

void recursiveQuickSort(vector<int>& a, int low, int high) {
    if (low >= high) return;
    int p = partitionArray(a, low, high);
    recursiveQuickSort(a, low, p - 1);
    recursiveQuickSort(a, p + 1, high);
}

void iterativeQuickSort(vector<int>& a) {
    if (a.empty()) return;
    vector<pair<int, int>> pending;
    pending.push_back({0, static_cast<int>(a.size()) - 1});

    while (!pending.empty()) {
        auto [low, high] = pending.back();
        pending.pop_back();
        if (low >= high) continue;

        int p = partitionArray(a, low, high);
        if (low < p - 1) pending.push_back({low, p - 1});
        if (p + 1 < high) pending.push_back({p + 1, high});
    }
}

void printArray(const vector<int>& a) {
    for (int x : a) cout << x << ' ';
    cout << '\n';
}

int main() {
    int n;
    cin >> n;
    vector<int> original(n);
    for (int& x : original) cin >> x;

    vector<int> recursive = original;
    vector<int> iterative = original;
    recursiveQuickSort(recursive, 0, n - 1);
    iterativeQuickSort(iterative);

    cout << "Recursive: ";
    printArray(recursive);
    cout << "Iterative: ";
    printArray(iterative);
}
```

#### Sample input and output

```text
Input
7
9 4 8 3 1 2 5

Output
Recursive: 1 2 3 4 5 8 9
Iterative: 1 2 3 4 5 8 9
```

#### Result analysis and comparison

Both versions perform the same partition operations and return the sorted input.
Their time complexity depends on how balanced the partitions are.

| Case | Recursive calls | Time complexity |
| :--- | :--- | :--- |
| Best / balanced partitions | Two parts of about `n/2` | `O(n log n)` |
| Average | Usually reasonably balanced | `O(n log n)` expected |
| Worst / highly unbalanced | One part has `n - 1` values | `O(n^2)` |

The recursive version uses call-stack space: normally `O(log n)`, but `O(n)` in
the worst case. The iterative version avoids recursive calls but stores ranges
on an explicit stack; its worst-case extra space is also `O(n)`. Choosing a
random or median-like pivot reduces the chance of consistently poor partitions.

---

## 4. Greedy Change-Making

### Question

Implement the change-making problem using a greedy approach and evaluate its
correctness.

### Answer

Given coin denominations and an amount, the goal is to make the amount using as
few coins as possible. The greedy method repeatedly chooses the largest coin
that does not exceed the remaining amount.

#### Greedy algorithm

```text
GREEDY-CHANGE(coins, amount)
1. sort denominations from largest to smallest
2. remaining = amount
3. for each denomination c:
4.     while c <= remaining:
5.         take coin c
6.         remaining = remaining - c
7. if remaining == 0, return the coins
8. otherwise report that exact change could not be made
```

#### C++ implementation

**Input:** number of denominations `k`, the `k` denominations, then the amount.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int k, amount;
    cin >> k;
    vector<int> coins(k);
    for (int& coin : coins) cin >> coin;
    cin >> amount;

    sort(coins.rbegin(), coins.rend());
    vector<int> answer;
    int remaining = amount;

    for (int coin : coins) {
        if (coin <= 0) continue;
        while (coin <= remaining) {
            answer.push_back(coin);
            remaining -= coin;
        }
    }

    if (remaining != 0) {
        cout << "Exact change is not possible with these denominations.\n";
        return 0;
    }
    cout << "Coins used: ";
    for (int coin : answer) cout << coin << ' ';
    cout << "\nNumber of coins: " << answer.size() << '\n';
}
```

#### Sample input and output

```text
Input
5
50 20 10 5 1
87

Output
Coins used: 50 20 10 5 1 1
Number of coins: 6
```

#### Correctness evaluation

For the denomination system `50, 20, 10, 5, 1`, choosing the largest possible
coin at each step gives an optimal result for this example. This type of system
is called a **canonical coin system** when the greedy method gives a minimum
number of coins for every amount.

However, greedy change-making is **not correct for every set of denominations**.
For coins `4, 3, 1` and amount `6`, greedy chooses `4 + 1 + 1` (three coins),
but the optimal answer is `3 + 3` (two coins). Thus, the greedy choice is only
proven correct for a suitable coin system; it must not be claimed to work for
all denominations.

If denominations are already sorted, scanning the denomination list takes
`O(k)` in addition to the number of coins written. Sorting first takes
`O(k log k)`. The output list may use `O(q)` space for `q` selected coins.

---

## 5. Greedy Fractional Knapsack

### Question

Implement the knapsack problem using a greedy approach and evaluate its
correctness.

### Answer

In the **fractional knapsack** problem, an item may be divided. For each item,
calculate its value per unit of weight:

\[
r_i=\frac{v_i}{w_i}.
\]

Sort items by decreasing `r_i`. Take each item in that order. If the whole item
does not fit, take only the fraction that fills the remaining capacity.

#### Algorithm

```text
FRACTIONAL-KNAPSACK(items, W)
1. calculate value/weight for each item
2. sort items by decreasing value/weight
3. totalValue = 0
4. for each item in sorted order:
5.     take as much as fits
6.     add the same fraction of the item's value
7.     stop when capacity is full
8. return totalValue
```

#### C++ implementation

**Input:** `n`, capacity `W`, then one `weight value` pair per item.

```cpp
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

struct Item {
    double weight;
    double value;
};

int main() {
    int n;
    double capacity;
    cin >> n >> capacity;
    vector<Item> items(n);
    for (Item& item : items) cin >> item.weight >> item.value;

    sort(items.begin(), items.end(), [](const Item& a, const Item& b) {
        return a.value / a.weight > b.value / b.weight;
    });

    double totalValue = 0.0;
    double remaining = capacity;
    for (const Item& item : items) {
        if (remaining <= 0) break;
        double fraction = min(1.0, remaining / item.weight);
        totalValue += fraction * item.value;
        remaining -= fraction * item.weight;
    }

    cout << fixed << setprecision(2) << "Maximum value: " << totalValue << '\n';
}
```

#### Sample input and output

```text
Input
3 50
10 60
20 100
30 120

Output
Maximum value: 240.00
```

#### Result analysis and correctness

The value-to-weight ratios are `6`, `5`, and `4`. Take all of item 1 and item
2, which use 30 units of capacity. The remaining capacity is 20, so take
`20/30` of item 3. The total value is

\[
60+100+\frac{20}{30}(120)=240.
\]

This greedy method is correct for fractional knapsack. If a solution uses some
weight from a lower-ratio item while a higher-ratio item is still available,
replace that weight with the higher-ratio item. The total value does not decrease.
Repeating this exchange gives the ratio-sorted greedy solution.

The method is **not** for 0/1 knapsack, where items cannot be divided. Sorting
takes `O(n log n)` time and the scan takes `O(n)`, so total time is `O(n log n)`.

---

## 6. Fibonacci by Recursion and Dynamic Programming

### Question

Implement the Fibonacci series using recursion and dynamic programming. Analyze
the time complexity of both methods.

### Answer

The Fibonacci sequence is

\[
F(0)=0,\quad F(1)=1,\quad F(n)=F(n-1)+F(n-2)\quad(n\ge2).
\]

A direct recursive function follows this definition, but it calculates many
values repeatedly. Dynamic programming stores results and reuses them.

#### C++ implementation

The recursive version below is intended for small `n`; the memoized version
stores every result and is safe for much larger practical inputs (up to the
range of `long long`).

```cpp
#include <iostream>
#include <vector>
using namespace std;

long long fibonacciRecursive(int n) {
    if (n <= 1) return n;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

long long fibonacciMemo(int n, vector<long long>& memo) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo);
    return memo[n];
}

long long fibonacciDP(int n) {
    if (n <= 1) return n;
    vector<long long> dp(n + 1, 0);
    dp[1] = 1;
    for (int i = 2; i <= n; ++i) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

int main() {
    int n;
    cin >> n;
    vector<long long> memo(n + 1, -1);
    cout << "Recursive: " << fibonacciRecursive(n) << '\n';
    cout << "Memoized DP: " << fibonacciMemo(n, memo) << '\n';
    cout << "Bottom-up DP: " << fibonacciDP(n) << '\n';
}
```

#### Sample input and output

```text
Input
7

Output
Recursive: 13
Memoized DP: 13
Bottom-up DP: 13
```

#### Result analysis

All methods return `13` for `F(7)`. Direct recursion repeats the same
subproblems, such as `F(3)`, many times. Memoization computes each value once;
bottom-up DP fills values from `F(0)` to `F(n)`.

| Method | Time | Extra space |
| :--- | :--- | :--- |
| Direct recursion | `O(2^n)` (more tightly, `Theta(phi^n)`) | `O(n)` call stack |
| Memoization | `O(n)` | `O(n)` table and call stack |
| Bottom-up DP | `O(n)` | `O(n)` table; can be reduced to `O(1)` |

The direct recursive method is simple, but dynamic programming is much faster
because it stores and reuses earlier answers.

---

## 7. Coin-Row Problem by Dynamic Programming

### Question

Given a row of coins with different values, select coins with the maximum total
value. Two neighboring coins cannot both be selected. Solve the problem using
dynamic programming.

### Answer

Let `value[i]` be the value of coin `i`. For the first `i` coins, there are two
choices:

1. Do not take coin `i`; the best value is `dp[i - 1]`.
2. Take coin `i`; coin `i - 1` cannot be taken, so the value is
   `value[i] + dp[i - 2]`.

Therefore,

\[
dp[0]=0,\qquad dp[1]=value[1],
\]
\[
dp[i]=\max(dp[i-1],\ value[i]+dp[i-2]).
\]

#### Algorithm

```text
COIN-ROW(value, n)
1. dp[0] = 0
2. dp[1] = value[1]
3. for i = 2 to n:
4.     dp[i] = max(dp[i - 1], value[i] + dp[i - 2])
5. return dp[n]
```

#### C++ implementation

**Input:** `n`, then the values of the coins from left to right.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> value(n + 1), dp(n + 1, 0);
    for (int i = 1; i <= n; ++i) cin >> value[i];

    if (n >= 1) dp[1] = value[1];
    for (int i = 2; i <= n; ++i) {
        dp[i] = max(dp[i - 1], value[i] + dp[i - 2]);
    }

    cout << "Maximum value: " << dp[n] << '\n';
    cout << "Selected coin values: ";
    int i = n;
    while (i >= 1) {
        if (i == 1 || dp[i] != dp[i - 1]) {
            cout << value[i] << ' ';
            i -= 2;
        } else {
            --i;
        }
    }
    cout << '\n';
}
```

#### Sample input and output

```text
Input
6
5 1 2 10 6 2

Output
Maximum value: 17
Selected coin values: 2 10 5
```

The selected coins are from positions 1, 4, and 6: `5 + 10 + 2 = 17`. No two
selected positions are neighbors. The program prints the selected values in
reverse order because traceback moves from right to left.

#### Result analysis

The DP table for this input is `0, 5, 5, 7, 15, 15, 17`. At every position it
keeps the better of taking the current coin or skipping it. The algorithm uses
`O(n)` time and `O(n)` space. Since only the last two states are needed to
calculate the next state, the maximum value alone can also be computed in
`O(1)` extra space.

---

## 8. Change-Making by Dynamic Programming

### Question

Given coin denominations and an amount, find the minimum number of coins needed
to make the amount. Solve the problem using dynamic programming.

### Answer

Unlike greedy change-making, dynamic programming checks all possible last
coins. Coin denominations can be used any number of times.

Let `dp[x]` be the minimum number of coins needed to make amount `x`. Set
`dp[0]=0`. For every coin `c` that is no larger than `x`, using it last gives
`dp[x-c]+1` coins. Thus,

\[
dp[x]=1+\min_{c\le x} dp[x-c].
\]

If no denomination can make an amount, its value remains infinity.

#### Algorithm

```text
MIN-COINS(coins, amount)
1. dp[0] = 0; all other dp values = infinity
2. for x = 1 to amount:
3.     for each coin c:
4.         if c <= x and dp[x - c] is possible:
5.             dp[x] = min(dp[x], dp[x - c] + 1)
6. if dp[amount] is infinity, report impossible
7. otherwise return dp[amount]
```

#### C++ implementation

**Input:** `k`, the `k` denominations, then the target amount.

```cpp
#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;

int main() {
    int k, amount;
    cin >> k;
    vector<int> coins(k);
    for (int& coin : coins) cin >> coin;
    cin >> amount;

    const int INF = numeric_limits<int>::max() / 2;
    vector<int> dp(amount + 1, INF), lastCoin(amount + 1, -1);
    dp[0] = 0;

    for (int x = 1; x <= amount; ++x) {
        for (int coin : coins) {
            if (coin > 0 && coin <= x && dp[x - coin] + 1 < dp[x]) {
                dp[x] = dp[x - coin] + 1;
                lastCoin[x] = coin;
            }
        }
    }

    if (dp[amount] == INF) {
        cout << "Amount cannot be made.\n";
        return 0;
    }
    cout << "Minimum number of coins: " << dp[amount] << '\n';
    cout << "Coins used: ";
    for (int x = amount; x > 0; x -= lastCoin[x]) cout << lastCoin[x] << ' ';
    cout << '\n';
}
```

#### Sample input and output

```text
Input
3
1 3 4
6

Output
Minimum number of coins: 2
Coins used: 3 3
```

#### Result analysis

Greedy would select `4 + 1 + 1`, which uses three coins. The DP table compares
every possible last coin and finds `3 + 3`, which uses two coins. The DP answer
is optimal because any solution must finish with some coin `c`; before that
last coin, it must make amount `x-c` optimally.

If there are `k` denominations and the target is `A`, time is `O(kA)` and space
is `O(A)`. This version allows unlimited use of each denomination.

---

## 9. Coin-Collecting Problem by Dynamic Programming

### Question

A collector starts at the top-left cell of a grid and can move only right or
down. Each cell contains a coin value. Find the maximum number of coins that
can be collected on the way to the bottom-right cell.

### Answer

Let `coins[i][j]` be the value in row `i`, column `j`. Let `dp[i][j]` be the
maximum value collected on a path from the top-left cell to `(i,j)`.

A path can enter a cell only from above or from the left. Therefore,

\[
dp[i][j]=coins[i][j]+\max(dp[i-1][j],dp[i][j-1]).
\]

For the top-left cell, `dp[0][0]=coins[0][0]`. For the first row, the only
possible move is from the left. For the first column, the only possible move
is from above.

#### Algorithm

```text
COIN-COLLECT(coins, rows, columns)
1. dp[0][0] = coins[0][0]
2. fill the first row using the cell to the left
3. fill the first column using the cell above
4. for every other cell (i, j):
5.     dp[i][j] = coins[i][j] + max(dp[i - 1][j], dp[i][j - 1])
6. return dp[rows - 1][columns - 1]
```

#### C++ implementation

**Input:** row count, column count, then the grid values row by row.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int rows, columns;
    cin >> rows >> columns;
    vector<vector<long long>> coins(rows, vector<long long>(columns));
    for (auto& row : coins) {
        for (long long& value : row) cin >> value;
    }

    vector<vector<long long>> dp(rows, vector<long long>(columns, 0));
    dp[0][0] = coins[0][0];
    for (int j = 1; j < columns; ++j) {
        dp[0][j] = coins[0][j] + dp[0][j - 1];
    }
    for (int i = 1; i < rows; ++i) {
        dp[i][0] = coins[i][0] + dp[i - 1][0];
    }
    for (int i = 1; i < rows; ++i) {
        for (int j = 1; j < columns; ++j) {
            dp[i][j] = coins[i][j] + max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    cout << "Maximum coins collected: " << dp[rows - 1][columns - 1] << '\n';
}
```

#### Sample input and output

```text
Input
3 3
1 2 3
4 8 2
1 5 3

Output
Maximum coins collected: 21
```

#### Result analysis

One maximum path is `1 -> 4 -> 8 -> 5 -> 3`, with total
`1 + 4 + 8 + 5 + 3 = 21`. At each cell, the algorithm keeps the better path
from above and from the left. It calculates every cell once, so the time and
space complexities are both `O(rows * columns)`.

---

## 10. 0/1 Knapsack by Dynamic Programming

### Question

Given `n` items, each with a weight and a value, and a knapsack of capacity `W`,
find the greatest total value that fits. Each item may be taken once or not at
all; fractions are not allowed.

### Answer

Let `dp[i][j]` be the maximum value obtainable using the first `i` items and
capacity `j`. For item `i`, either skip it or take it if it fits:

\[
dp[i][j]=
\begin{cases}
dp[i-1][j], & w_i>j,\\
\max(dp[i-1][j],\ v_i+dp[i-1][j-w_i]), & w_i\le j.
\end{cases}
\]

The base cases are `dp[0][j]=0` and `dp[i][0]=0`. Taking the item uses the
previous row, which ensures that the same item is not used more than once.

#### Algorithm

```text
KNAPSACK-01(weight, value, n, W)
1. set dp[0][j] = 0 for every capacity j
2. for i = 1 to n:
3.     for j = 0 to W:
4.         dp[i][j] = dp[i - 1][j]
5.         if weight[i] <= j:
6.             dp[i][j] = max(dp[i][j], value[i] + dp[i - 1][j - weight[i]])
7. return dp[n][W]
```

#### C++ implementation

**Input:** `n W`, followed by one `weight value` pair for each item.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, capacity;
    cin >> n >> capacity;
    vector<int> weight(n + 1), value(n + 1);
    for (int i = 1; i <= n; ++i) cin >> weight[i] >> value[i];

    vector<vector<long long>> dp(n + 1, vector<long long>(capacity + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int w = 0; w <= capacity; ++w) {
            dp[i][w] = dp[i - 1][w];
            if (weight[i] <= w) {
                dp[i][w] = max(dp[i][w],
                               value[i] + dp[i - 1][w - weight[i]]);
            }
        }
    }

    cout << "Maximum value: " << dp[n][capacity] << '\n';
    cout << "Selected item numbers: ";
    int w = capacity;
    for (int i = n; i >= 1; --i) {
        if (dp[i][w] != dp[i - 1][w]) {
            cout << i << ' ';
            w -= weight[i];
        }
    }
    cout << '\n';
}
```

#### Sample input and output

```text
Input
3 50
10 60
20 100
30 120

Output
Maximum value: 220
Selected item numbers: 3 2
```

#### Result analysis

Items 2 and 3 have total weight `20 + 30 = 50` and total value
`100 + 120 = 220`. This is better than taking items 1 and 2 (value 160), or
items 1 and 3 (value 180). The DP table checks both choices for every item and
capacity, so its final cell gives the best feasible value.

Time complexity is `O(nW)` and space complexity is `O(nW)`. The running time is
pseudo-polynomial because it depends on the numeric capacity `W`. The table can
be reduced to `O(W)` space by updating capacities from right to left.

---

## Quick revision table

| Question | Main technique | Time complexity |
| :---: | :--- | :---: |
| 1 | Linear search / binary search | `O(n)` / `O(log n)` |
| 2 | Merge sort | `O(n log n)` in both approaches |
| 3 | Quick sort | Average `O(n log n)`, worst `O(n^2)` |
| 4 | Greedy change-making | `O(k log k + q)` with sorting and `q` selected coins |
| 5 | Fractional knapsack | `O(n log n)` |
| 6 | Fibonacci recursion / DP | `O(2^n)` / `O(n)` |
| 7 | Coin-row DP | `O(n)` |
| 8 | Minimum-coin DP | `O(kA)` |
| 9 | Coin-collecting DP | `O(rows * columns)` |
| 10 | 0/1 knapsack DP | `O(nW)` |

**Exam writing order:** state the idea, define the recurrence or greedy choice,
write the algorithm, show a sample run, analyze time and space, and state any
important condition (for example, binary search needs sorted input and greedy
change-making is not always optimal).
