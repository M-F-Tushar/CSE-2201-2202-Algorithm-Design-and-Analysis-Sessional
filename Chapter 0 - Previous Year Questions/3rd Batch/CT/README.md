# CSE 2201 Class Tests 01–03: Complete Answers

[Previous: 2nd Batch Theory](../../2nd%20Batch/Theory/README.md) | [Chapter 0 - Previous Year Questions](../../README.md) | [Home](../../../README.md)

This document restores the three class-test answer sets in sequence: **Class Test 1** (the earlier dynamic-programming paper), **Class Test 2** (`Class Test_02`, graph algorithms), and **Class Test 3** (the attached file `CSE 2201 - CT - 3.pdf`). The CT3 filename identifies it as the third test; its internal header incorrectly says “Class Test: 01.”

> [!IMPORTANT]
> **Source notes and assumptions:** CT1 Q4 did not include item data in the scan, so its knapsack instance is illustrative. CT2 Q3 has two hard-to-read diagonal edge labels; the answer states its reading. CT3 Q2 uses a labelled example array because none is supplied. In CT3 Q3, the code comment says query `[1, 4]`, but task (c) asks for `[2, 6]`; the answer follows the explicit task.

Every question has a diagram preview and editable Excalidraw scene in the [diagram index](diagrams/README.md). The answers use simple words, show the working, and end with a memory trick.

| Test | Questions | Topics | Marks |
|------|-----------|--------|-------|
| Class Test 1 | Q1–Q4 | Principle of Optimality, Fibonacci DP, LCS, 0/1 knapsack | 20 |
| Class Test 2 | Q1–Q3 | Topological sort, Bellman–Ford, Floyd–Warshall | 20 |
| Class Test 3 | Q1–Q3 | Union by rank, maximum subarray, segment tree | 20 |

---

## Class Test 1: Dynamic Programming

### Q1. Principle of Optimality

**Question (transcribed):** State the Principle of Optimality and explain it with an example. (5 marks)

**Answer.** The Principle of Optimality says that every part of an optimal solution is optimal for its own smaller problem. For a shortest route, every sub-route between two points on the best route must itself be shortest; otherwise replacing it would make the whole route shorter.

For example, use the weighted directed graph shown below. The best route from S to T is **S→A→B→T**, cost 2+1+3=6. Its suffix **A→B→T** costs 4, which is better than direct A→T (7). If a cheaper A-to-T route existed, replacing the suffix would improve the whole route, contradicting that the original route was optimal.

![Principle of optimality illustrated with a shortest-route graph](diagrams/ct1-01-principle-optimality.svg)

> Memory trick: best whole = best parts.

### Q2. Elements of Dynamic Programming: Fibonacci

**Question (transcribed):** Explain the elements of dynamic programming by illustrating the nth Fibonacci number. (5 marks)

**Answer.** DP is useful when a problem has **optimal substructure** (a solution is built from smaller solutions) and **overlapping subproblems** (the same smaller answers are needed more than once). Fibonacci has both: $F(n)=F(n-1)+F(n-2)$, with $F(0)=0$ and $F(1)=1$.

Naive recursion for $F(5)$ makes 15 calls: it computes $F(3)$ twice, $F(2)$ three times, $F(1)$ five times, and $F(0)$ three times. Dynamic programming stores each answer once. Top-down storage is **memoization**; filling $F(0),F(1),\ldots,F(n)$ in order is **tabulation**. The table for $F(5)$ is 0, 1, 1, 2, 3, 5. Tabulation takes $\Theta(n)$ time and space; retaining only the previous two values takes $\Theta(1)$ space.

![Repeated calls in naive F(5) recursion](diagrams/ct1-02-fib-recursion.svg)

![Bottom-up Fibonacci table](diagrams/ct1-03-fib-table.svg)

> Memory trick: store each repeated subproblem once.

### Q3. Longest Common Subsequence

**Question (transcribed):** Find the LCS of AGGTAB and GXTXAYB and write the subsequence. (5 marks)

**Answer.** Let $L[i][j]$ be the LCS length for the first $i$ letters of AGGTAB and first $j$ letters of GXTXAYB. A match uses the diagonal value plus one; a mismatch uses the larger of the value above and the value to the left.

| | | G | X | T | X | A | Y | B |
|--|--|--|--|--|--|--|--|--|
| | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | 0 | 0 | 0 | 0 | 0 | **1** | 1 | 1 |
| G | 0 | **1** | 1 | 1 | 1 | 1 | 1 | 1 |
| G | 0 | **1** | 1 | 1 | 1 | 1 | 1 | 1 |
| T | 0 | 1 | 1 | **2** | 2 | 2 | 2 | 2 |
| A | 0 | 1 | 1 | 2 | 2 | **3** | 3 | 3 |
| B | 0 | 1 | 1 | 2 | 2 | 3 | 3 | **4** |

Traceback from the lower-right cell takes B, A, T, G; reverse them to get **GTAB**. The LCS has length **4**.

![LCS table for the two strings](diagrams/ct1-04-lcs.svg)

> Memory trick: match = diagonal + 1; mismatch = max(up, left).

### Q4. 0/1 Knapsack by Dynamic Programming

**Question (transcribed):** Solve a 0/1 knapsack problem using DP. Show the table and give the maximum profit and selected items. (5 marks)

> **Illustrative data:** The scan does not show the item table. Use capacity $W=8$, weights $[3,4,5,6]$, and profits $[2,3,1,4]$. Replace these numbers if the original paper has different data.

**Answer.** Let $V[i][c]$ be the best profit using the first $i$ items and capacity $c$. If item $i$ is too heavy, keep the previous value; otherwise take the larger of skipping it and taking it:

$$V[i][c]=\max\big(V[i-1][c],\ V[i-1][c-w_i]+p_i\big)$$

when $w_i\le c$, and $V[i][c]=V[i-1][c]$ otherwise.

The table is:

| Items used / capacity | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-----------------------|---|---|---|---|---|---|---|---|---|
| None | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Item 1 (w=3, p=2) | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2 | 2 |
| Item 2 (w=4, p=3) | 0 | 0 | 0 | 2 | 3 | 3 | 3 | 5 | 5 |
| Item 3 (w=5, p=1) | 0 | 0 | 0 | 2 | 3 | 3 | 3 | 5 | 5 |
| Item 4 (w=6, p=4) | 0 | 0 | 0 | 2 | 3 | 3 | 4 | 5 | 5 |

The last value is $V[4][8]=5$. Traceback selects items **1 and 2**: weight $3+4=7\le8$, profit $2+3=5$. The diagram highlights this traceback.

![Illustrative 0/1 knapsack DP table and selected items](diagrams/ct1-05-knapsack.svg)

> Memory trick: select an item when its row improves the value.

---

## Class Test 2: Graph Algorithms

### Q1. Topological Sort

**Question (transcribed):** Perform a topological sort of the given DAG. (4 marks)

**Answer.** The edges read from the scan are 5→6, 4→6, 5→2, 4→1, 2→3, and 3→1. Use Kahn’s algorithm: repeatedly remove a vertex whose in-degree is zero. Starting with 4 and 5 gives one valid order: **4, 5, 6, 2, 3, 1**. Checking each edge shows its source appears before its destination.

![DAG with one valid topological order](diagrams/ct2-01-topological.svg)

> Memory trick: repeatedly remove a vertex with no incoming edge.

### Q2. Bellman–Ford from S to T

**Question (transcribed):** Use Bellman–Ford to find the shortest path from S to T in the weighted graph. (8 marks)

**Answer.** The edges read from the scan are S→A=5, S→C=−2, A→B=1, C→A=2, C→B=4, C→D=4, B→D=−1, B→T=3, and D→T=1. Initialize $d(S)=0$ and all other distances to infinity. Relax all nine edges in that order, in place, for $V-1=5$ passes.

| After | S | A | B | C | D | T |
|-------|---|---|---|---|---|---|
| Start | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| Pass 1 | 0 | 0 | 2 | -2 | 1 | 2 |
| Pass 2 | 0 | 0 | 1 | -2 | 0 | 1 |
| Pass 3 | 0 | 0 | 1 | -2 | 0 | 1 |
| Pass 4 | 0 | 0 | 1 | -2 | 0 | 1 |
| Pass 5 | 0 | 0 | 1 | -2 | 0 | 1 |

Following parent links gives **S→C→A→B→D→T**, with cost $-2+2+1-1+1=1$. No further relaxation improves a distance, so there is no reachable negative cycle.

![Bellman–Ford graph with shortest route highlighted](diagrams/ct2-02-bellman-ford.svg)

> Memory trick: relax every edge V−1 times; then check once more for a negative cycle.

### Q3. Floyd–Warshall

**Question (transcribed):** Use Floyd–Warshall to find all-pairs shortest paths in the weighted graph. (8 marks)

> **Graph reading:** the edges are 1→2=2, 2→3=3, 3→4=1, 4→3=12, 4→1=4, 1→4=5, and the diagonals 3→1=6 and 4→2=7. Those two diagonal labels are hard to read; verify them against the paper.

**Answer.** Start with direct-edge matrix $D_0$ (zero diagonal, infinity when no direct edge). For each intermediate vertex $k$, update $d(i,j)=\min(d(i,j),d(i,k)+d(k,j))$.

**$D_0$**

| | 1 | 2 | 3 | 4 |
|--|--|--|--|--|
| 1 | 0 | 2 | ∞ | 5 |
| 2 | ∞ | 0 | 3 | ∞ |
| 3 | 6 | ∞ | 0 | 1 |
| 4 | 4 | 7 | 12 | 0 |

**After allowing vertex 1 ($D_1$):** $d(3,2)=8$ and $d(4,2)=6$.

| | 1 | 2 | 3 | 4 |
|--|--|--|--|--|
| 1 | 0 | 2 | ∞ | 5 |
| 2 | ∞ | 0 | 3 | ∞ |
| 3 | 6 | 8 | 0 | 1 |
| 4 | 4 | 6 | 12 | 0 |

**After allowing vertex 2 ($D_2$):** $d(1,3)=5$ and $d(4,3)=9$.

| | 1 | 2 | 3 | 4 |
|--|--|--|--|--|
| 1 | 0 | 2 | 5 | 5 |
| 2 | ∞ | 0 | 3 | ∞ |
| 3 | 6 | 8 | 0 | 1 |
| 4 | 4 | 6 | 9 | 0 |

**After allowing vertex 3 ($D_3$):** $d(2,1)=9$ and $d(2,4)=4$.

| | 1 | 2 | 3 | 4 |
|--|--|--|--|--|
| 1 | 0 | 2 | 5 | 5 |
| 2 | 9 | 0 | 3 | 4 |
| 3 | 6 | 8 | 0 | 1 |
| 4 | 4 | 6 | 9 | 0 |

**Final matrix ($D_4$):** allowing vertex 4 improves $d(2,1)=8$, $d(3,1)=5$, and $d(3,2)=7$.

| | 1 | 2 | 3 | 4 |
|--|--|--|--|--|
| 1 | 0 | 2 | 5 | 5 |
| 2 | 8 | 0 | 3 | 4 |
| 3 | 5 | 7 | 0 | 1 |
| 4 | 4 | 6 | 9 | 0 |

Floyd–Warshall takes $O(n^3)$ time and $O(n^2)$ space.

![Four-vertex graph used for Floyd–Warshall](diagrams/ct2-03-floyd-warshall.svg)

> Memory trick: for each k, ask whether going through k is shorter.

---

## Class Test 3: CSE 2201 - CT - 3 PDF

The filename identifies this as CT3. The PDF header says “Class Test: 01”; that internal label is treated as a typo, as requested.

### Q1. Union by Rank

**Question (transcribed):** Explain how union by rank helps reduce the height of a DSU tree. Illustrate your answer with an example. (5 marks)

**Answer.**

A **disjoint-set union (DSU)** keeps each set as a tree. The root represents the set. `find(x)` follows parent links to get the root; `union(a, b)` joins the two sets.

**Union by rank** stores a small rank at each root as an estimate of its tree height. When joining two roots:

1. Attach the root with the **smaller rank** below the root with the larger rank.
2. If the ranks are equal, attach either root below the other and increase the new root's rank by 1.

This avoids attaching a tall tree under a shorter one. For example, with elements 1–8, join the pairs `(1,2)`, `(3,4)`, `(5,6)`, `(7,8)`, then join the resulting pairs `(1,3)`, `(5,7)`, and finally `(1,5)`. Equal-rank roots are joined at each step. The final tree has height **3**. A poor sequence of unions without rank can make a chain of height **7**.

A rank-r root represents at least $2^r$ elements, because its rank only increases when two roots of the same rank are joined. Therefore rank is at most $\log_2 n$, and union by rank alone keeps the height logarithmic. With path compression as well, the amortized cost per operation is nearly constant, $O(\alpha(n))$.

![A naive DSU chain compared with a shallow tree built by union by rank](diagrams/ct3-01-union-by-rank.svg)

> Memory trick: attach the shorter tree below the taller one; raise rank only on a tie.

---

### Q2. Divide-and-Conquer Maximum Subarray Sum

**Question (transcribed):** Illustrate with an example construction of the divide-and-conquer solution for Maximum Subarray Sum problem to find in using a suitable test-case. (5 marks)

**Answer.**

> **Illustrative test case:** the paper does not give an array. Use `[-2, 1, -3, 4, -1, 2, 1, -5]` below. Indices are zero-based.

Split the array into two halves until each part contains one value. For every interval, compute:

- the best subarray entirely in the **left half**;
- the best subarray entirely in the **right half**;
- the best **crossing** subarray, which is the largest suffix of the left half plus the largest prefix of the right half.

Return the largest of those three values. A one-element interval is the base case: its best sum is that element.

| Interval | Best left | Best right | Best crossing | Best for interval |
|----------|-----------|------------|---------------|-------------------|
| `[0,1]` | -2 | 1 | -1 | 1 at `[1,1]` |
| `[2,3]` | -3 | 4 | 1 | 4 at `[3,3]` |
| `[0,3]` | 1 | 4 | 2 | 4 at `[3,3]` |
| `[4,5]` | -1 | 2 | 1 | 2 at `[5,5]` |
| `[6,7]` | 1 | -5 | -4 | 1 at `[6,6]` |
| `[4,7]` | 2 | 1 | 3 | 3 at `[5,6]` |
| `[0,7]` | 4 | 3 | **6** | **6 at `[3,6]`** |

At the final split, the best left-half sum is 4, the best right-half sum is 3, and the best crossing sum is 4 + (−1 + 2 + 1) = **6**. Therefore the maximum-sum subarray is `[4, -1, 2, 1]`, at indices 3 through 6.

Each recursion level does $\Theta(n)$ work to find crossing sums, and there are $\Theta(\log n)$ levels. Thus $T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)$.

![Divide-and-conquer recursion tree with left, right, and crossing sums](diagrams/ct3-02-maximum-subarray.svg)

> Memory trick: split; compare left, right, and crossing.

---

### Q3. Segment Tree and Range-Sum Query

**Question (transcribed):** Consider the following C++ function for constructing a Segment Tree and performing a Range Sum Query. Complete all the sections marked TODO.

```cpp
#include <bits/stdc++.h>
using namespace std;
vector<int> tree;
// Build Segment Tree
void build(int node, int l, int r, vector<int> &arr)
{
    // TODO 1: Write the base case
    // TODO 2: Calculate the middle position
    // TODO 3: Recursively build the left half
    // TODO 4: Recursively build the right half
    // TODO 5: Combine the results of the two children
}
// Range Sum Query
int query(int node, int l, int r, int ql, int qr)
{
    // TODO 6: Handle the No Overlap case
    // TODO 7: Handle the Complete Overlap case
    // TODO 8: Calculate the middle position
    // TODO 9: Perform query on the left child
    // TODO 10: Perform query on the right child
    // TODO 11: Return the combined result
}
int main()
{
    vector<int> arr = {2, 1, 5, 3, 4, 7, 6, 8};
    int n = arr.size();
    // Allocate memory for Segment Tree
    tree.resize(4 * n);
    // Root = tree[0]
    build(0, 0, n - 1, arr);
    // TODO 12: Perform a range sum query for [1, 4]
    return 0;
}
```

**Tasks (transcribed):**

- a) Complete TODO 1-5 to implement the `build()` function. (3 marks)
- b) Complete TODO 6-11 to implement the `query()` function. (3 marks)
- c) Complete TODO 12 to perform the range-sum query `[2, 6]`. (1 mark)
- d) Draw the Segment Tree corresponding to the given array. (3 marks)

#### Q3(a) and Q3(b). Complete the functions

**Answer.** The tree stores the sum of each interval. With zero-based indexing, node `node` has children `2 * node + 1` and `2 * node + 2`.

- **TODO 1:** If the interval is a single index, store that array value.
- **TODO 2:** Find the midpoint.
- **TODO 3–4:** Build both halves recursively.
- **TODO 5:** Add the children's sums.
- **TODO 6:** If the query interval and current interval do not overlap, return 0 (the identity for sum).
- **TODO 7:** If the current interval is fully inside the query, return its stored sum.
- **TODO 8–10:** Otherwise, query both children.
- **TODO 11:** Add the two partial answers.

```cpp
void build(int node, int l, int r, vector<int> &arr)
{
    if (l == r) {
        tree[node] = arr[l];
        return;
    }

    int mid = l + (r - l) / 2;
    build(2 * node + 1, l, mid, arr);
    build(2 * node + 2, mid + 1, r, arr);
    tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
}

int query(int node, int l, int r, int ql, int qr)
{
    if (qr < l || r < ql) return 0;           // No overlap
    if (ql <= l && r <= qr) return tree[node]; // Complete overlap

    int mid = l + (r - l) / 2;
    int leftSum = query(2 * node + 1, l, mid, ql, qr);
    int rightSum = query(2 * node + 2, mid + 1, r, ql, qr);
    return leftSum + rightSum;
}
```

> Memory trick: no overlap returns 0; full overlap returns the stored sum; otherwise split.

#### Q3(c). Query `[2, 6]`

**Answer.** The source code comment says `[1, 4]`, but task (c) explicitly requests `[2, 6]`. Follow the task's range:

```cpp
cout << query(0, 0, n - 1, 2, 6) << '\n';
```

The array entries at indices 2 through 6 are `5, 3, 4, 7, 6`, so the sum is **25**.

> Memory trick: the query endpoints are inclusive, so `[2,6]` has five entries.

#### Q3(d). Draw the Segment Tree

**Answer.** The root represents the full interval `[0,7]`. Each internal node stores the sum of its two child intervals; each leaf stores one array value.

| Tree node | Interval | Stored sum |
|-----------|----------|------------|
| 0 | `[0,7]` | 36 |
| 1 | `[0,3]` | 11 |
| 2 | `[4,7]` | 25 |
| 3 | `[0,1]` | 3 |
| 4 | `[2,3]` | 8 |
| 5 | `[4,5]` | 11 |
| 6 | `[6,7]` | 14 |
| 7 | `[0,0]` | 2 |
| 8 | `[1,1]` | 1 |
| 9 | `[2,2]` | 5 |
| 10 | `[3,3]` | 3 |
| 11 | `[4,4]` | 4 |
| 12 | `[5,5]` | 7 |
| 13 | `[6,6]` | 6 |
| 14 | `[7,7]` | 8 |

For the `[2,6]` query, the green nodes cover `[2,3]`, `[4,5]`, and `[6,6]`. Their sums are 8, 11, and 6, giving 8 + 11 + 6 = **25**.

![Segment tree for the given array, with the range-query cover highlighted](diagrams/ct3-03-segment-tree.svg)

> Memory trick: each parent stores left sum + right sum; query only the covered pieces.

---

## Verification

Run `python tools/verify_ct3.py` from the repository root. It checks the CT1 LCS and knapsack tables, Fibonacci call counts, CT2 shortest-path tables and topological order, the CT3 DSU and maximum-subarray examples, the segment tree and query result, and every local link and diagram pair. These checks verify the worked examples; they cannot verify uncertain scan labels or the transcribed wording.

## Quick Revision

| Test / topic | One-line memory |
|--------------|-----------------|
| CT1 — Principle of Optimality | A part of an optimal solution is optimal for its own subproblem |
| CT1 — Fibonacci DP | Optimal substructure + overlapping subproblems; store each state once |
| CT1 — LCS | Match = diagonal + 1; otherwise max(up, left); answer GTAB, length 4 |
| CT1 — 0/1 knapsack | For the illustrative data, items 1 and 2 give profit 5 |
| CT2 — Topological sort | Repeatedly remove zero-in-degree vertices; 4, 5, 6, 2, 3, 1 is valid |
| CT2 — Bellman–Ford | Relax all edges V−1 times; shortest S-to-T distance is 1 |
| CT2 — Floyd–Warshall | Try each vertex as an intermediate; update with min(d(i,j), d(i,k)+d(k,j)) |
| CT3 — Union by rank | Attach smaller rank below larger; raise the rank only on a tie |
| CT3 — Maximum subarray | `max(best-left, best-right, best-crossing)`; example answer 6 at `[3,6]` |
| CT3 — Segment tree | Parent sum = left child + right child; no-overlap query contributes 0 |
| CT3 — Range `[2,6]` | Inclusive range sum is 25; task (c) takes precedence over the `[1,4]` comment |
