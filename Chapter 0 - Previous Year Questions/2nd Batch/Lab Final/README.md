# 2nd Batch Lab Test — Questions and Answers

This guide answers the three programming questions on the first page of the
second-batch lab-test paper. Each question is worth 10 marks. The other pages in
the provided PDF are for different subjects, so they are not included here.

The code examples are independent C++17 programs. Each one reads input in the
format shown and prints only the requested answer.

## Contents

1. [Count Distinct Values](#1-count-distinct-values)
2. [Maximum Sum of a Contiguous Subarray](#2-maximum-sum-of-a-contiguous-subarray)
3. [Search for an Element](#3-search-for-an-element)

---

## 1. Count Distinct Values

### Question

You are given a list of `n` integers. Find how many different values are in the
list.

- **Input:** The first line contains `n`. The second line contains `n` integers.
- **Output:** Print one integer: the number of distinct values.
- **Example constraints shown on the paper:** `1 ≤ n ≤ 2 × 10^5` and
  `1 ≤ x_i ≤ 10^9`.

### Idea

Sort the values. Equal values will then be next to each other. The C++ function
`unique` removes repeated neighboring values, so the size of the remaining list
is the number of distinct values.

### Algorithm

```text
COUNT-DISTINCT(A)
1. sort A in increasing order
2. remove repeated neighboring values from A
3. print the size of A
```

### C++ implementation

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<long long> values(n);
    for (long long& value : values) cin >> value;

    sort(values.begin(), values.end());
    values.erase(unique(values.begin(), values.end()), values.end());

    cout << values.size() << '\n';
}
```

### Sample input and output

```text
Input
5
2 3 2 2 3

Output
2
```

### Result analysis

After sorting, the list is `2 2 2 3 3`. Removing repeated values leaves `2 3`,
so there are **2 distinct values**.

Sorting takes `O(n log n)` time. The operations after sorting take `O(n)` time.
The program uses `O(log n)` auxiliary stack space for sorting, in addition to
space for the input list.

---

## 2. Maximum Sum of a Contiguous Subarray

### Question

Given an array of integers, find the maximum sum of any **contiguous, nonempty
subarray**.

- **Input:** The first line contains `n`. The second line contains the `n` array
  values.
- **Output:** Print one integer: the maximum subarray sum.
- **Example constraints shown on the paper:** `1 ≤ n ≤ 2 × 10^5` and
  `−10^9 ≤ x_i ≤ 10^9`.

### Idea: Kadane's algorithm

A contiguous subarray ending at the current value has two choices:

1. Start a new subarray at the current value.
2. Extend the best subarray that ended at the previous value.

Let `endingHere` be the best sum of a subarray that must end at the current
position. For each value `x`, update it as follows:

\[
endingHere = \max(x, endingHere + x).
\]

Keep the largest `endingHere` seen so far as the answer. Initialize both values
from the first array element. This makes the algorithm correct when every value
is negative and the subarray must be nonempty.

### Algorithm

```text
MAX-SUBARRAY-SUM(A, n)
1. endingHere = A[0]
2. answer = A[0]
3. for i = 1 to n - 1:
4.     endingHere = max(A[i], endingHere + A[i])
5.     answer = max(answer, endingHere)
6. print answer
```

### C++ implementation

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<long long> values(n);
    for (long long& value : values) cin >> value;

    long long endingHere = values[0];
    long long answer = values[0];

    for (int i = 1; i < n; ++i) {
        endingHere = max(values[i], endingHere + values[i]);
        answer = max(answer, endingHere);
    }

    cout << answer << '\n';
}
```

### Sample input and output

```text
Input
8
-1 3 -2 5 3 -5 2 2

Output
9
```

### Result analysis

A maximum-sum subarray is `3, -2, 5, 3`. It is contiguous, and its sum is
`3 - 2 + 5 + 3 = 9`.

For each position, the algorithm keeps the best subarray ending there. Any
maximum subarray either starts at that position or extends a subarray ending at
the previous position, so checking these two choices is sufficient.

- **Time complexity:** `O(n)` — each value is processed once.
- **Extra space:** `O(1)` apart from the input array.

The use of `long long` is important because a sum can be much larger than one
input value.

---

## 3. Search for an Element

### Question

Search for a specific element in an array. Print `Yes` if the element is
present; otherwise, print `No`.

- **Input:** The first line contains `n` and the target value `k`. The second
  line contains `n` integers.
- **Output:** Print `Yes` or `No`.

### Idea

Check each array value against `k`. If a match is found, print `Yes`. If all
values have been checked and none matches, print `No`. The array does not need
to be sorted.

### Algorithm

```text
SEARCH(A, n, k)
1. for i = 0 to n - 1:
2.     if A[i] == k:
3.         print "Yes" and stop
4. print "No"
```

### C++ implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    long long target;
    cin >> n >> target;

    vector<long long> values(n);
    for (long long& value : values) cin >> value;

    for (long long value : values) {
        if (value == target) {
            cout << "Yes\n";
            return 0;
        }
    }

    cout << "No\n";
}
```

### Sample input and output

```text
Input
3 4
1 2 3

Output
No
```

### Result analysis

The target is `4`. The array contains `1`, `2`, and `3`, so the target is absent
and the program prints `No`.

- **Best-case time:** `O(1)` if the first value is the target.
- **Worst-case time:** `O(n)` if the target is last or absent.
- **Extra space:** `O(1)` apart from the input array.

---

## Quick revision table

| Question | Main method | Time | Extra space |
| :---: | :--- | :---: | :---: |
| 1 | Sort, then remove duplicates | `O(n log n)` | `O(log n)` auxiliary |
| 2 | Kadane's algorithm | `O(n)` | `O(1)` |
| 3 | Linear search | `O(n)` worst case | `O(1)` |

**Exam answer order:** write the idea, give the algorithm, provide a working
program, show the sample result, and finish with correctness reasoning and
complexity.
