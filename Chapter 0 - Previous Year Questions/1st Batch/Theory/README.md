# 1st Batch Theory: Answers

[Previous: Chapter 0 - Previous Year Questions](../../README.md) | [Home](../../../README.md) | [Next: 2nd Batch Theory](../../2nd%20Batch/Theory/README.md)

This study guide covers **Section A, Q1–Q4 (all parts)** and **Section B, Q5–Q8 (all parts)** of the paper identified in these notes as CSE 2201, 1st Batch, 2023. The recorded instruction is to answer any 3 questions from each section; all 27 subquestions are answered here.

> [!IMPORTANT]
> **Source and reconstruction:** no original paper scan or original question figures accompany this Theory subtree. The wording, year, marks, and instructions below are retained from the existing notes, not independently authenticated. Arrays, graphs, loop snippets, boards, grids, and numerical examples are specified here as **reconstructed/illustrative working inputs**, not claimed to be historical originals. Answers and diagrams apply to exactly these stated inputs. A supplied original could require different numerical answers.

**Conventions:** $\log$ means $\log_2$ unless stated otherwise. Complexity counts unit-cost operations under the stated model; arbitrary-precision arithmetic can cost more. Graphs are finite, with no unlisted edges. All 27 parts include a suitable SVG with a matching editable source in the [diagram index](diagrams/README.md).

| Question | Topic | a | b | c | d |
|----------|-------|---|---|---|---|
| Q1 | Algorithm design and analysis basics | 10 | 10 | 15 | - |
| Q2 | Recurrences and loop analysis | 10 | 10 | 15 | - |
| Q3 | Divide and conquer, merge sort, quick sort, heap sort | 5 | 10 | 10 | 10 |
| Q4 | Greedy, memoization vs tabulation, MST | 10 | 10 | 15 | - |
| Q5 | Backtracking: N-Queen, subset sum, Hamiltonian circuit | 5 | 10 | 10 | 10 |
| Q6 | Dynamic programming: knapsack, grid, coin change | 5 | 10 | 10 | 10 |
| Q7 | Bellman-Ford, optimality, 0/1 knapsack | 10 | 10 | 15 | - |
| Q8 | P, NP, decision vs optimization, Dijkstra | 10 | 10 | 15 | - |

### Visual Map: Full-Paper Roadmap

Foundations support the later topics; the roadmap groups all eight questions without claiming that one paradigm requires another.

![Full-paper roadmap for Q1 through Q8](diagrams/b1-theory-01-question-escalator.svg)

---

## Section A

### Q1. Algorithm Design, Analysis, and Complexity

#### Q1(a) Design and analysis of an algorithm. What makes a good algorithm?

- **Design** means deciding how the algorithm will solve the problem. It is the method or plan (for example: divide the problem, or sort first, or try all choices).
- **Analysis** means deriving time and space bounds under a stated computation model and establishing correctness. Mathematical analysis complements, but is not replaced by, timing experiments.

An algorithm must have precise, effective steps and terminate for every valid input. Specify its input domain and required output; efficiency matters only after correctness.

![Design, correctness, and resource analysis](diagrams/b1-theory-09-design-analysis.svg)

A good algorithm has these qualities:

1. **Correct**: it gives the right output for every valid input.
2. **Time efficient**: it runs fast as $n$ grows.
3. **Space efficient**: it uses little extra memory.
4. **Simple**: it is easy to understand, write, and debug.
5. **Handles all valid inputs**: it works for edge cases such as an empty array or one element.

#### Q1(b) Best, worst, and average case. Give examples.

For a deterministic algorithm, let $t(x)$ be its cost on input $x$ of size $n$.

- **Best-case time**: $B(n)=\min_{|x|=n}t(x)$, the least work on any size-$n$ input.
- **Worst-case time**: $W(n)=\max_{|x|=n}t(x)$, the greatest work on any size-$n$ input.
- **Average-case time**: $A(n)=\mathbb{E}_{X\sim D_n}[t(X)]$, under an **explicit probability distribution** $D_n$ over size-$n$ inputs, not necessarily uniform. This differs from expected time over an algorithm's random choices.

![Linear-search best, worst, and average comparisons](diagrams/b1-theory-10-case-analysis.svg)

| Algorithm | Best case | Worst case | Average case |
|-----------|-----------|------------|--------------|
| Linear search | $\Theta(1)$: the item is the first element | $\Theta(n)$: the item is last or not present | $(n+1)/2$ comparisons, hence $\Theta(n)$, if the target occurs once and each position is equally likely |
| Insertion sort | $\Theta(n)$: input is already sorted | $\Theta(n^2)$: input is reverse sorted | $\Theta(n^2)$ for a uniformly random permutation of distinct keys |

#### Q1(c) Two algorithms: A takes $n^2$ time, B takes $n \log n$ time. Which one is better? Why?

**Answer: B is asymptotically faster**, assuming runtimes $\Theta(n^2)$ and $\Theta(n\log n)$ with positive fixed leading constants. Merely knowing upper bounds $O(n^2)$ and $O(n\log n)$ would not establish a strict comparison. The illustrative counts below use unit coefficients.

![Growth comparison under unit coefficients](diagrams/b1-theory-11-growth.svg)

| $n$ | $n^2$ (Algorithm A) | $n \log_2 n$ (Algorithm B) |
|-----|---------------------|----------------------------|
| 10 | 100 | about 33 |
| 1,000 | 1,000,000 | about 9,966 |
| 1,000,000 | $10^{12}$ | about $2 \times 10^7$ |

At $n = 10^6$, Algorithm B does about 50,000 times less work.

> [!NOTE]
> For very small $n$, Algorithm A may still be faster in practice, because its constant factors can be smaller. Asymptotic analysis is about what happens as $n$ becomes large.

---

### Q2. Recurrences and Loop Analysis

#### Q2(a) What is a recurrence? How do we solve one?

A **recurrence** defines a sequence or function in terms of smaller arguments, together with base cases. In algorithm analysis, it often expresses running time $T(n)$ using the running times on smaller inputs.

Example: $T(n)=2T(n/2)+n$ for $n\ge2$, $T(1)=1$, with $n$ a power of two. A recurrence needs base cases and an input-size/rounding convention.

![Recurrence and work per level](diagrams/b1-theory-02-recursion-tree.svg)

We solve recurrences in three common ways:

1. **Substitution method**: guess the answer and prove it with induction.
2. **Recursion tree method**: draw the calls as a tree, add the work per level, and sum all levels.
3. **Master Theorem**: compare $f(n)$ with $n^{\log_b a}$ for $T(n)=aT(n/b)+f(n)$, where $a\ge1$ and $b>1$ are constants. Apply it only when the chosen case's growth/regularity conditions hold; not every recurrence fits.

#### Q2(b) Analyze the loops (count the inner work).

**Illustrative snippets:** let $n\ge1$ be an integer, initialize `sum = 0`, and assume unit-cost arithmetic with no overflow (including `i * 2`). Each inner loop body takes constant time, so we count iterations.

![Loop iteration counts for n equals 8](diagrams/b1-theory-12-loop-counts.svg)

**(i)**

```text
for (i = 1; i <= n; i = i * 2)
    for (j = 1; j <= n; j++)
        sum = sum + i * j;
```

- The outer loop runs for $i = 1, 2, 4, \dots$ up to $n$. That is $\lfloor \log_2 n \rfloor + 1$ times.
- For each outer iteration, the inner loop runs $n$ times.
- Total iterations: $(\lfloor \log_2 n \rfloor + 1) \cdot n$.

**Result: $\Theta(n \log n)$.** For $n = 8$: outer runs 4 times, inner runs 8 times, so total = 32.

**(ii)**

```text
for (i = 1; i <= n; i = i * 2)
    for (j = 1; j <= i; j++)
        sum = sum + 1;
```

- The inner loop runs $i$ times, for $i = 1, 2, 4, \dots, 2^K$, where $2^K \le n < 2^{K+1}$.
- Total: $1 + 2 + 4 + \dots + 2^K = 2^{K+1} - 1$.
- Since $n \le 2^{K+1} - 1 \le 2n - 1$, the total is between $n$ and $2n - 1$.

**Result: $\Theta(n)$.** For $n = 8$: $K = 3$, total = $1+2+4+8 = 15$.

#### Q2(c) Solve $T(n) = 2T(n/2) + n$ with $T(1) = 1$. Show the steps.

**Domain:** $n=2^k$ for integer $k\ge0$; the recurrence applies only when $n>1$.

**Method 1: Substitution (prove $T(n) = O(n \log n)$)**

Guess $T(n) \le c\,n \log_2 n$ for some constant $c$ and all $n \ge 2$.

- **Base case** ($n = 2$): $T(2) = 2T(1) + 2 = 4$. And $c \cdot 2 \cdot \log_2 2 = 2c$. With $c = 2$, $4 \le 4$. ✓
- **Inductive step** ($n\ge4$, a power of two): assume the guess is true for $n/2$. Handle $n=2$ separately because $cn\log n$ is zero at $n=1$.

$$T(n) = 2T(n/2) + n \le 2 \cdot c\,\frac{n}{2}\log_2\frac{n}{2} + n = cn\log_2 n - cn + n$$

Since $c \ge 1$, we have $-cn + n \le 0$, so $T(n) \le c\,n \log_2 n$. ✓

So $T(n) = O(n \log n)$.

**Method 2: Recursion tree**

| Level | Number of nodes | Size of each node | Work per level |
|-------|-----------------|-------------------|----------------|
| 0 | 1 | $n$ | $n$ |
| 1 | 2 | $n/2$ | $2 \cdot n/2 = n$ |
| 2 | 4 | $n/4$ | $4 \cdot n/4 = n$ |
| ... | ... | ... | $n$ |
| $\log_2 n$ | $n$ | 1 | $n$ |

![Recursion tree for T(n) = 2T(n/2) + n](diagrams/b1-theory-02-recursion-tree.svg)

There are $\log_2 n + 1$ levels, each doing $n$ work. Total: $n(\log_2 n + 1)$.

**Method 3: Master Theorem**

Here $a = 2$, $b = 2$, $f(n) = n$. Then $n^{\log_b a} = n^{\log_2 2} = n^1 = n$. Since $f(n) = \Theta(n^{\log_b a})$, this is **Case 2**, so $T(n) = \Theta(n \log n)$.

**Final answer:** $T(n) = \Theta(n \log n)$. (Exact solution for powers of 2: $T(n) = n\log_2 n + n$. Check: $T(4) = 12$, $T(8) = 32$.)

---

### Q3. Divide and Conquer, Merge Sort, Quick Sort, Heap Sort

#### Q3(a) Explain the three steps of divide and conquer. Give an example.

1. **Divide**: split the problem into smaller subproblems.
2. **Conquer**: solve each subproblem (recursively). When a subproblem is small enough, solve it directly (the base case).
3. **Combine**: join the subproblem solutions into the final answer.

**Illustrative example: merge sort on $[5, 2, 4, 7]$**

![Divide, conquer, and combine in merge sort](diagrams/b1-theory-13-merge-sort.svg)

```text
[5, 2, 4, 7]          divide
[5, 2]   [4, 7]       divide
[2, 5]   [4, 7]       conquer (sort each half)
[2, 4, 5, 7]          combine (merge)
```

#### Q3(b) Write the merge sort recurrence and show that its complexity is $\Theta(n \log n)$.

**Algorithm idea:** split the array into two halves, sort each half recursively, then merge the two sorted halves.

**Recurrence:**

$$T(n) = 2T(n/2) + \Theta(n), \qquad T(1) = \Theta(1)$$

This balanced form assumes powers of two. For arbitrary $n>1$, use $T(\lfloor n/2\rfloor)+T(\lceil n/2\rceil)+\Theta(n)$, with $T(0),T(1)=\Theta(1)$; the same asymptotic bound holds.

![Balanced merge-sort recursion and level costs](diagrams/b1-theory-02-recursion-tree.svg)

- Divide: $\Theta(1)$ (find the middle).
- Conquer: two recursive calls on $n/2$ each.
- Combine (merge): $\Theta(n)$ to scan both halves.

**Recursion tree:** for powers of two, each internal level does $\Theta(n)$ work; the leaves also total $\Theta(n)$. There are $\log_2 n+1$ levels, so $T(n)=\Theta(n\log n)$. The linked tree uses unit coefficients to illustrate these level costs.

**Master Theorem:** $a = 2$, $b = 2$, $f(n) = n = \Theta(n^{\log_2 2})$, which is **Case 2**. So $T(n) = \Theta(n \log n)$.

**Space:** standard array merge sort needs a $\Theta(n)$ auxiliary merge buffer plus $O(\log n)$ stack space, hence $\Theta(n)$ auxiliary space overall; this implementation is **not in-place**.

#### Q3(c) What is an in-place sorting algorithm? Is quick sort in-place?

Under the **strict definition**, an in-place sort uses $O(1)$ total auxiliary space. Some textbooks exclude the recursion stack when calling a sort in-place; state the convention.

**Standard array quicksort has in-place partitioning**, using swaps and $O(1)$ partition workspace. Ordinary two-recursive-call quicksort uses $O(\log n)$ expected stack space under random pivots (or suitable random-input assumptions), but $O(n)$ worst-case stack space. It is conventionally called in-place when the stack is excluded, not under the strict total-space definition. Recursing only on the smaller side and iterating over the larger side guarantees $O(\log n)$ stack space; worst-case time can still be $\Theta(n^2)$.

![Quicksort partition workspace versus recursion stack](diagrams/b1-theory-14-quicksort-space.svg)

> [!NOTE]
> Quick sort is **not stable**: equal elements may change their relative order.

#### Q3(d) Heap sort on $A = [7, 2, 5, 3, 4, 6, 1]$. Show the steps.

**Illustrative input:** the array in the heading is the working example, not an authenticated original. Indices start at 0. For index $i$, the children are at $2i+1$ and $2i+2$ when within the active heap. We build a **max-heap** first, then repeatedly move the largest element to the end.

**Step 1: Build the max-heap** (call heapify from index 2 down to 0)

- $i = 2$ (value 5): children are 6 and 1. Largest child is 6, so swap 5 and 6. Array: $[7, 2, 6, 3, 4, 5, 1]$
- $i = 1$ (value 2): children are 3 and 4. Largest child is 4, so swap 2 and 4. Array: $[7, 4, 6, 3, 2, 5, 1]$
- $i = 0$ (value 7): 7 is already larger than both children (4 and 6). No swap.

Heap as a tree:

![Max-heap after the build step](diagrams/b1-theory-03-heap-build-tree.svg)

**Step 2: Sort (repeat until size is 1)**

Each round: swap the root (largest) with the last element in the heap, shrink the heap by 1, then heapify the root.

| Round | Swap root with | Array after the round |
|-------|----------------|-----------------------|
| 1 | last element | $[6, 4, 5, 3, 2, 1, 7]$ |
| 2 | last heap element | $[5, 4, 1, 3, 2, 6, 7]$ |
| 3 | last heap element | $[4, 3, 1, 2, 5, 6, 7]$ |
| 4 | last heap element | $[3, 2, 1, 4, 5, 6, 7]$ |
| 5 | last heap element | $[2, 1, 3, 4, 5, 6, 7]$ |
| 6 | last heap element | $[1, 2, 3, 4, 5, 6, 7]$ |

**Final sorted array:** $[1, 2, 3, 4, 5, 6, 7]$

**Complexity:** bottom-up heap construction is $\Theta(n)$ (summing work by node height), followed by $n-1$ root-removal rounds taking at most $O(\log n)$ each. Worst-case sorting time is $\Theta(n\log n)$. With iterative sift-down, heapsort uses $O(1)$ auxiliary space and is strictly in-place, but **not stable**.

---

### Q4. Greedy Algorithms, Memoization vs Tabulation, and MST

#### Q4(a) What is a greedy algorithm? Give a counterexample where it fails.

A **greedy algorithm** builds the solution step by step. At each step it picks the locally best choice and never goes back to change it.

**Illustrative counterexample: coin change.** Unlimited coins of denominations $\{1,3,4\}$, amount $6$; minimize the number of coins making exactly that amount.

![Greedy versus optimal coin change](diagrams/b1-theory-15-coin-change.svg)

- Greedy picks the largest coin first: $4 + 1 + 1$. That is **3 coins**.
- Optimal is $3 + 3$. That is **2 coins**.

Greedy is not always optimal for every problem. It works for problems with the greedy-choice property (such as Kruskal's and Prim's MST algorithms).

#### Q4(b) Memoization vs tabulation. Explain the difference with an example.

Both are techniques for **dynamic programming**: they store answers to subproblems so that each subproblem is solved only once.

- **Memoization (top-down)**: write the recursive solution, and store each result in a cache the first time it is computed.
- **Tabulation (bottom-up)**: fill a table with answers for the smallest subproblems first, using a loop, then build up to the answer.

**Illustrative example: Fibonacci**, $F_0=0$, $F_1=1$, $F_n=F_{n-1}+F_{n-2}$ for integer $n\ge2$. Both functions accept nonnegative integers.

![Top-down memoization versus bottom-up tabulation](diagrams/b1-theory-16-memo-tab.svg)

```python
# Memoization (top-down)
memo = {}
def fib_memo(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

# Tabulation (bottom-up)
def fib_tab(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
```

| Point | Memoization | Tabulation |
|-------|-------------|------------|
| Direction | Top-down (start from the big problem) | Bottom-up (start from the small problems) |
| Implementation | Recursion plus a cache | Loop plus a table |
| Recursion overhead | Yes (can hit recursion limits) | No |
| Subproblems computed | Only the ones actually reached | All states selected by the iteration order |

Both implementations use $O(n)$ arithmetic operations and $O(n)$ stored values; memoization also has $O(n)$ recursion depth. Fibonacci needs all preceding states in either version, so this example does not save states top-down. Tabulation can keep just two previous values for $O(1)$ stored values. These are unit-cost arithmetic bounds; Fibonacci integers grow in bit length.

#### Q4(c) Find the MST of the graph, using Prim's and Kruskal's algorithms.

A **minimum spanning tree (MST)** is a connected, acyclic subgraph covering every vertex with minimum total edge weight; it has $|V|-1$ edges.

**Reconstructed working graph:** connected, simple, undirected, with $V=\{A,B,C,D,E\}$ and exactly these weighted edges. This list defines the example; no original figure is available.

| Edge | Weight |
|------|--------|
| A-B | 2 |
| A-C | 3 |
| B-C | 1 |
| B-D | 4 |
| C-D | 5 |
| C-E | 6 |
| D-E | 7 |

![Reconstructed graph and its unique MST](diagrams/b1-theory-17-mst.svg)

**Prim's algorithm (start from A)**

1. Start with $\{A\}$. Candidate edges: A-B (2), A-C (3). Pick **A-B (2)**.
2. Tree is $\{A, B\}$. Candidates: A-C (3), B-C (1), B-D (4). Pick **B-C (1)**.
3. Tree is $\{A, B, C\}$. Candidates: B-D (4), C-D (5), C-E (6). Pick **B-D (4)**.
4. Tree is $\{A, B, C, D\}$. Candidates: C-E (6), D-E (7). Pick **C-E (6)**.

**Kruskal's algorithm (sort edges by weight)**

| Edge | Weight | Decision |
|------|--------|----------|
| B-C | 1 | Take (no cycle) |
| A-B | 2 | Take (no cycle) |
| A-C | 3 | Skip (A, B, C would form a cycle) |
| B-D | 4 | Take (no cycle) |
| C-D | 5 | Skip (C and D already connected) |
| C-E | 6 | Take (no cycle). We now have 4 edges for 5 vertices, so stop. |
| D-E | 7 | Not needed |

**MST edges:** B-C, A-B, B-D, C-E

**Total MST weight:** $1 + 2 + 4 + 6 = 13$

Both algorithms give the same MST. Distinct edge weights make it unique. The cut property justifies Prim's lightest crossing edge; Kruskal maintains a forest using disjoint sets to avoid cycles. With adjacency lists and a binary heap, Prim takes $O((V+E)\log V)$; Kruskal takes $O(E\log E)$ for sorting plus near-linear disjoint-set work.

---

## Section B

### Q5. Backtracking

#### Q5(a) What is backtracking? Explain briefly.

**Backtracking** solves a problem by building a solution one step at a time. At each step it:

1. Makes a choice.
2. Checks whether the partial solution still satisfies the constraints.
3. If the choice leads to a **dead end**, it **undoes** the choice (backtracks) and tries the next option.

It is a depth-first search over a **state-space tree**. Branches that cannot lead to a valid solution are cut early (**pruning**). A pruning test must be sound: it must never discard a branch containing a required solution. Backtracking may still take exponential time.

![Choose, reject, undo, and find a four-queen solution](diagrams/b1-theory-18-queens-backtracking.svg)

#### Q5(b) Explain the N-Queen problem using backtracking. Place 4 queens on a $4 \times 4$ board.

**Illustrative instance:** $N=4$, with zero-based rows and columns. In general, place $N$ queens on an $N \times N$ board so that no two queens attack each other. Queens attack along the same row, same column, or same diagonal.

![Four-queen search branches and the first solution board](diagrams/b1-theory-18-queens-backtracking.svg)

**Idea:** place one queen per row. To place the $k$-th queen (in row $k$):

1. Try columns $0, 1, \dots, N-1$ in order.
2. A column is safe if no earlier queen (rows $0$ to $k-1$) is in the same column or on the same diagonal.
3. If a safe column is found, place the queen and move to row $k+1$.
4. If no column is safe, **backtrack**: go back to queen $k-1$ and move it to its next column.

**Pseudocode**

```text
SOLVE(row):
    if row == N:
        print the board          // found a solution
        return

    for col = 0 to N-1:
        if IS-SAFE(row, col):
            board[row] = col     // place queen
            SOLVE(row + 1)
            // if we get here, backtrack: the loop tries the next column

IS-SAFE(row, col):
    for r = 0 to row-1:
        if board[r] == col:                    // same column
            return false
        if |board[r] - col| == row - r:        // same diagonal
            return false
    return true
```

**Backtrack conditions**

- **Column conflict**: a queen already sits in the same column.
- **Diagonal conflict**: a queen already sits on the same diagonal.
- **No safe column**: no column in row $k$ is safe, so go back to row $k-1$.

**Trace for 4 queens** (rows and columns start at 0, shown as (row, col))

1. Place (0, 0).
2. Row 1: columns 0 and 1 conflict (column and diagonal). Place (1, 2).
3. Row 2: every column conflicts. **Backtrack** to row 1.
4. Row 1: try column 3. Place (1, 3).
5. Row 2: column 0 conflicts. Place (2, 1).
6. Row 3: every column conflicts. **Backtrack** to row 2.
7. Row 2: columns 2 and 3 conflict. **Backtrack** to row 1.
8. Row 1 has no more options. **Backtrack** to row 0.
9. Row 0: try column 1. Place (0, 1). Continue: (1, 3), (2, 0), (3, 2).

**First solution:**

```text
. Q . .
. . . Q
Q . . .
. . Q .
```

Call `SOLVE(0)` with a length-$N$ array `board`; only entries before `row` are consulted, so stale later entries are ignored after backtracking. For $N=4$ there are exactly two solutions, encoded by column per row: $[1,3,0,2]$ and $[2,0,3,1]$. The first is shown above. With this $O(N)$ safety scan and distinct-column branching, a coarse upper bound is $O(N^2N!)$ time and $O(N)$ auxiliary space (excluding output); pruning improves many instances.

#### Q5(c) Subset sum with $A = \{3, 5, 6, 7\}$ and $d = 15$. Use backtracking.

**Illustrative input:** four distinct positive integers, each usable at most once; find all subsets summing exactly to $d=15$. Go through items in the stated order; try **take** before **skip**. The trace and diagram show only the prefix through the first solution, not the entire tree.

- If the sum goes above $d$, **prune** that branch; this is safe here because all remaining values are positive (not generally safe with negative values).
- If the sum equals $d$, we found a solution.
- If no items are left and the sum is not $d$, it is a **dead end**.

**Trace**

1. Take 3: sum = 3.
2. Take 5: sum = 8.
3. Take 6: sum = 14.
4. Take 7: sum = 21. This is more than 15, so **prune**.
5. Skip 7: sum = 14. No items left, so **dead end**. Backtrack.
6. Skip 6: sum = 8.
7. Take 7: sum = 15. **Solution found.**

![Backtracking trace for subset sum with d = 15](diagrams/b1-theory-04-subset-sum-tree.svg)

**Answer: $\{3,5,7\}$**, because $3+5+7=15$. It is unique: 0- or 1-item sums are below 15, 2-item sums are at most 13, the other 3-item sums are 14, 16, 18, and all four sum to 21.

```text
SUBSETS(i, total, chosen):
    if total == d: output chosen; return
    if total > d or i == length(A): return
    SUBSETS(i + 1, total + A[i], chosen followed by A[i])
    SUBSETS(i + 1, total, chosen)
```

Call `SUBSETS(0, 0, [])`. Positivity makes returning at the target sound for enumerating all solutions. There are $O(2^n)$ search nodes and $O(n)$ recursion depth. Mutable push/pop choices use $O(n)$ auxiliary space; literally copying the lists in this pseudocode can use $O(n^2)$ live space and add an $O(n)$ factor to time. Output storage is additional.

#### Q5(d) Find a Hamiltonian circuit starting from vertex $a$.

A **Hamiltonian circuit** visits every vertex exactly once and returns to the start.

**Reconstructed working graph:** simple and undirected, $V=\{a,b,c,d,e,f\}$, with exactly the symmetric adjacency list below. It defines this example; the unavailable original figure is not being inferred.

| Vertex | Neighbours |
|--------|------------|
| a | b, c, d |
| b | a, c, f |
| c | a, b, d, e, f |
| d | a, c, e |
| e | c, d, f |
| f | b, c, e |

**Idea:** start at $a$. Go to an unvisited neighbour (try them in alphabetical order). If we get stuck, backtrack.

**Trace**

1. $a \to b \to c \to d \to e \to f$. All 6 vertices are visited, but $f$ is not adjacent to $a$. **Dead end.**
2. Back to $c$, try $e$: $a \to b \to c \to e \to d$. From $d$, the only unvisited vertex is $f$, and $d$-$f$ is not an edge. **Dead end.**
3. Back to $c$, try $e$ then $f$: $a \to b \to c \to e \to f$. From $f$, the only unvisited vertex is $d$, and $f$-$d$ is not an edge. **Dead end.**
4. Back to $c$, try $f$: $a \to b \to c \to f \to e \to d$. All 6 vertices are visited, and $d$ is adjacent to $a$. **Circuit found.**

![Backtracking search tree for a Hamiltonian circuit from a](diagrams/b1-theory-05-hamiltonian-tree.svg)

**Answer:** $a-b-c-f-e-d-a$. Another valid circuit is $a-b-f-e-d-c-a$. Every consecutive pair, including the closing edge to $a$, occurs in the adjacency list.

```text
EXTEND(path, used):
    if length(path) == |V|:
        if edge(last(path), a): output path followed by a
        return
    for v in neighbours(last(path)) in alphabetical order:
        if v not in used:
            EXTEND(path followed by v, used union {v})
```

Call `EXTEND([a], {a})`; stop after the first output for the trace shown, or continue for all circuits (including reversed duplicates in an undirected graph). Only unused vertices may be appended; a full path must also close. A coarse bound is $O(V\cdot V!)$ time including candidate scans and $O(V)$ search space with mutable path/visited state. Literal copied paths/sets can use $O(V^2)$ live auxiliary space; graph and output storage are separate.

---

### Q6. Dynamic Programming

#### Q6(a) Two properties that a problem needs for dynamic programming.

1. **Optimal substructure**: the best answer to the big problem is built from the best answers to smaller subproblems.
2. **Overlapping subproblems**: the same smaller subproblem is needed many times. DP stores its answer, so it is computed only once.

For **optimization DP**, optimal substructure makes the recurrence valid, and overlapping subproblems makes reuse beneficial. More generally DP also handles counting and feasibility: Fibonacci has repeated subproblems and a recurrence, but no best/worst objective, so calling its structure *optimal* is unnecessary. Merge sort works on disjoint subarrays, without repeated identical subproblems.

![Overlapping knapsack states and optimal substructure](diagrams/b1-theory-19-dp-properties.svg)

#### Q6(b) 0/1 knapsack using DP. Write the recurrence.

**Problem:** $n\ge1$ items with positive integer weights $w_i$, nonnegative profits $p_i$, and nonnegative integer capacity $W$. Each item is taken whole at most once; total weight must be **at most** $W$. The empty selection is allowed. Maximize profit.

![Knapsack skip/take dependencies and worked DP table](diagrams/b1-theory-20-knapsack.svg)

**Table:** $DP[i][w]$ = maximum profit using the first $i$ items with capacity $w$.

**Recurrence:**

$$DP[i][w] = \begin{cases} DP[i-1][w] & \text{if } w_i > w \\ \max\big(DP[i-1][w],\; p_i + DP[i-1][w - w_i]\big) & \text{if } w_i \le w \end{cases}$$

- If item $i$ does not fit, we cannot take it.
- Otherwise, take the better of two choices: skip item $i$, or take it and add its profit to the best answer for the remaining capacity.

**Base cases:** $DP[0][w]=0$ for $0\le w\le W$ and $DP[i][0]=0$. Fill rows $i=1,\ldots,n$ and capacities $w=0,\ldots,W$ using only the previous row.

**Answer:** $DP[n][W]$. Time and table space are $O(nW)$ (more precisely $O(n(W+1))$, including $W=0$). Value-only space can be $O(W+1)$ by scanning capacities **downward** for each item; upward updates could reuse an item. The time is **pseudo-polynomial** because binary encoding of $W$ needs only $\Theta(\log(W+2))$ bits. For reconstruction, walk backward through the full table, skipping ties or taking item $i$ when its row improves the value; then subtract $w_i$. See Q7(c) for a complete example.

#### Q6(c) Coins on a grid: maximum coins from top-left to bottom-right.

**Illustrative grid:** find the maximum coins collected from $(0,0)$ to $(3,2)$ using **right or down** moves only, with no blocked cells. A cell's 0 or 1 coin is collected upon visiting, including both endpoints.

![Grid values, DP values, and an optimal path](diagrams/b1-theory-21-grid.svg)

| | col 0 | col 1 | col 2 |
|---|---|---|---|
| row 0 | 1 | 0 | 1 |
| row 1 | 0 | 1 | 0 |
| row 2 | 1 | 1 | 1 |
| row 3 | 0 | 0 | 1 |

**Base:** $dp[0][0]=\text{grid}[0][0]$. Fill row-major using $dp[r][c]=\text{grid}[r][c]+\max(dp[r-1][c],dp[r][c-1])$, using only predecessors that exist. Equivalently, accumulate the first row and column, then use the recurrence inside. This follows because the last move enters from above or left. For an $R\times C$ grid, time is $O(RC)$, full-table space is $O(RC)$, and value-only space can be $O(C)$.

| | col 0 | col 1 | col 2 |
|---|---|---|---|
| row 0 | 1 | 1 | 2 |
| row 1 | 1 | 2 | 2 |
| row 2 | 2 | 3 | 4 |
| row 3 | 2 | 3 | **5** |

**Answer: 5 coins.** One optimal path: $(0,0) \to (0,1) \to (1,1) \to (2,1) \to (2,2) \to (3,2)$, which collects $1+0+1+1+1+1 = 5$. Another path, $(0,0) \to (1,0) \to (2,0) \to (2,1) \to (2,2) \to (3,2)$, also gives 5, so there is a tie.

#### Q6(d) Coin change with coins $\{1, 3, 4\}$ and $n = 6$. Find the minimum number of coins.

**Illustrative instance:** unlimited coins of each stated positive integer denomination; make amount 6 exactly. Let $D=\{1,3,4\}$.

**Recurrence:** $C[x]=1+\min_{c\in D,\ c\le x}C[x-c]$, with $C[0]=0$. Treat an empty minimum as $\infty$, meaning unreachable. Fill amounts in increasing order. The last coin of an optimal solution leaves an optimally solved smaller amount.

![Minimum-coin DP table and greedy counterexample](diagrams/b1-theory-15-coin-change.svg)

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $C[x]$ | 0 | 1 | 2 | 1 | 1 | 2 | 2 |

**Answer: 2 coins** ($3+3$); traceback uses $6\to3\to0$, subtracting 3 twice. Greedy gives $4+1+1$ (3 coins), as in Q4(a). DP is a correct method here, not the only possible method. For amount $M$, it takes $O(|D|M)$ time and $O(M)$ space, pseudo-polynomial in binary-encoded $M$.

---

### Q7. Shortest Paths, Optimality, and Knapsack

#### Q7(a) Why does Dijkstra fail with negative edge weights? How does Bellman-Ford handle them?

**Standard label-setting Dijkstra** settles the minimum-tentative-distance unsettled vertex and never revises a settled label. Nonnegative weights guarantee this is safe; negative edges invalidate the guarantee (though not every such instance fails).

**Illustrative directed counterexample:** $V=\{A,B,C\}$ with exactly $A\to B=1$, $A\to C=4$, $C\to B=-5$, source $A$.

![Negative-edge failure of label-setting Dijkstra](diagrams/b1-theory-22-negative-edge.svg)

- Dijkstra takes $B$ first (distance 1) and fixes it.
- Then $C$ (distance 4) gives $4 + (-5) = -1$ for $B$. This is shorter, but $B$ is already fixed, so Dijkstra keeps $B = 1$. The true answer is $-1$.

**Bellman–Ford** initializes the source to 0 and other labels to $\infty$, then relaxes every edge for up to $|V|-1$ passes. Relax $(u,v)$ only if $dist[u]\ne\infty$ and $dist[u]+w(u,v)<dist[v]$. With no source-reachable negative cycle, a shortest path can be chosen simple, with at most $|V|-1$ edges. After pass $k$, all shortest paths using at most $k$ edges have been accounted for (in-place updates may propagate farther). This proves correctness after $|V|-1$ passes. An unchanged full pass permits early stopping. Time is $O(VE+V)$ including initialization, usually written $O(VE)$; label space is $O(V)$.

**Negative-cycle check:** after the passes, a still-relaxable edge with finite tail distance implies a **source-reachable** negative cycle. Vertices reachable from such a cycle have no finite minimum distance. An unreachable negative cycle does not affect this single-source computation.

#### Q7(b) Apply Bellman-Ford from A on the directed graph.

**Reconstructed working graph:** directed, $V=\{A,B,C,D,E\}$, source A, with exactly these edges **in scan order**: A to B = 6, A to C = 7, B to D = 5, B to E = -4, C to B = -3, C to D = 8, D to E = -2, E to A = 2. These givens are not authenticated against an original figure.

Use **in-place relaxation**: an improvement is available to later edges in the same pass. Each pass scans the edges in the order above. For example, in pass 1, B first becomes 6 (from A), then C to B gives $7 + (-3) = 4$, so B becomes 4.

| Pass | A | B | C | D | E |
|------|---|---|---|---|---|
| Start | 0 | $\infty$ | $\infty$ | $\infty$ | $\infty$ |
| 1 | 0 | 4 | 7 | 11 | 2 |
| 2 | 0 | 4 | 7 | 9 | 0 |
| 3 | 0 | 4 | 7 | 9 | 0 |

Pass 3 changes nothing, so we stop early.

**Final distances from A:** A = 0, B = 4 (A to C to B), C = 7 (A to C), D = 9 (A to C to B to D), E = 0 (A to C to B to E).

**Negative cycle:** none. Every cycle goes through A, since E to A is the only edge back. The smallest cycle total is 2 (A to C to B to E to A: $7 - 3 - 4 + 2 = 2$), which is positive.

![Bellman-Ford directed graph with shortest distances from A](diagrams/b1-theory-06-bellman-ford-graph.svg)

#### Q7(c) What is algorithm optimality? Is the 0/1 knapsack DP optimal? Solve the example.

**Two meanings of optimality:** (1) **solution optimality** means attaining the best feasible objective value; (2) **algorithmic/resource optimality** means matching a lower bound on time or space in a stated computation model. A correct exact optimization algorithm guarantees the first, not automatically the second.

**0/1 knapsack DP guarantees an optimal solution.** Any feasible selection either excludes item $i$, or includes it and leaves capacity $w-w_i$ for the first $i-1$ items. Those exhaustive cases and optimal substructure prove the recurrence by induction from row 0. This does **not** prove resource optimality. Its $O(nW)$ time is pseudo-polynomial, not polynomial in the binary input length.

![Knapsack recurrence, full table, and optimal item choice](diagrams/b1-theory-20-knapsack.svg)

**Illustrative instance:** capacity $W=8$, at-most-capacity 0/1 knapsack, empty selection allowed, with the four items below.

| Item | 1 | 2 | 3 | 4 |
|------|---|---|---|---|
| Weight | 3 | 4 | 5 | 6 |
| Profit | 2 | 3 | 1 | 4 |

**DP table** (rows: first $i$ items; columns: capacity $w = 0$ to $8$):

| $i$ \ $w$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2 | 2 |
| 2 | 0 | 0 | 0 | 2 | 3 | 3 | 3 | 5 | 5 |
| 3 | 0 | 0 | 0 | 2 | 3 | 3 | 3 | 5 | 5 |
| 4 | 0 | 0 | 0 | 2 | 3 | 3 | 4 | 5 | 5 |

**Answer: profit 5**, using items 1 and 2 (weight $3 + 4 = 7 \le 8$, profit $2 + 3 = 5$).

**Traceback:** $DP[4][8] = DP[3][8] = 5$, so item 4 is not taken. Likewise item 3 is not taken. $DP[2][8] = 5 \ne DP[1][8] = 2$, so item 2 is taken, and the capacity becomes $8 - 4 = 4$. $DP[1][4] = 2 \ne DP[0][4] = 0$, so item 1 is taken.

---

### Q8. P, NP, Decision vs Optimization, and Dijkstra

#### Q8(a) Define P, NP, NP-hard, and NP-complete. Show their relation.

These classes are defined for **decision problems** (languages), measured against input **bit length**, using polynomial-time many-one reductions unless stated otherwise.

- **P**: decision problems solvable by a deterministic algorithm in polynomial time. Example: in a nonnegative integer-weighted graph, is there an $s$–$t$ path of cost at most $K$? Sorting itself is not a decision problem.
- **NP**: decision problems whose yes-instances have **polynomial-length certificates** verified deterministically in polynomial time; no certificate may make a no-instance pass. Example: a Hamiltonian cycle is a certificate for the Hamiltonian-cycle decision problem. NP does not mean “not polynomial.”
- **NP-hard**: every problem in NP has a polynomial-time reduction to the problem: for each language $L\in NP$, $L\le_p H$. It need not belong to NP or even be decidable. Optimization problems can also be called NP-hard under a specified appropriate reduction, but are not themselves languages in NP.
- **NP-complete**: decision problems both in NP and NP-hard. Examples: SAT and Hamiltonian-cycle decision.

**Known relations:** $P\subseteq NP$ and $NP\text{-complete}=NP\cap NP\text{-hard}$. Whether $P=NP$ is **open**. If any NP-complete problem is in P, then $P=NP$; if $P\ne NP$, none is in P. The relation diagram shows only known inclusions, not an unconditional strict Venn separation.

![How P, NP, NP-hard, and NP-complete relate](diagrams/b1-theory-07-classes-venn.svg)

#### Q8(b) Decision problem vs optimization problem. Why does this matter?

For the **traveling salesperson problem (TSP)**, a tour visits every vertex exactly once and returns to its start; its cost is the sum of its edge weights.

- **Decision problem**: the answer is yes or no. Example: "Is there a tour with cost at most $k$?"
- **Optimization problem**: find the best solution. Example: "Find the cheapest tour."

NP-completeness applies to decision problems; optimization problems may be NP-hard. An exact optimization solver answers the associated threshold question by comparing its optimum with $k$ (and handling infeasibility).

**Converse, with conditions:** for a minimization problem with integer objective values in a known range $[L,U]$ whose endpoints have polynomial bit length, a threshold oracle “is some feasible solution worth at most $k$?” lets us find the **optimal value** by binary search using $O(\log(U-L+1))$ calls (plus a constant number for boundary/feasibility checks). Include polynomial work per call and monotonicity of the threshold predicate. This does not, for an arbitrary problem, automatically recover an optimal **solution**.

For nonnegative integer-weight TSP on a complete $n$-vertex graph with maximum edge cost $M$, the range is $[0,nM]$. Tour recovery additionally uses self-reduction: delete edges one at a time whenever the threshold answer at the optimum remains yes, allowing missing edges in oracle instances. At most $O(n^2)$ such queries leave the edges of an optimal tour. These properties justify polynomial equivalence for this example, not for all possible optimization problems.

![Threshold decision, value search, and conditional witness recovery](diagrams/b1-theory-23-decision-optimization.svg)

#### Q8(c) Run Dijkstra's algorithm from A.

**Reconstructed working graph:** simple, **undirected**, nonnegative-weighted, $V=\{A,B,C,D,E,F\}$, source A, with exactly A-B 2, A-D 8, B-E 6, B-D 5, E-D 3, E-F 1, E-C 9, F-C 3, D-F 2. Undirectedness is a declared working assumption, not verified against an original figure.

Initialize $dist[A]=0$, all others $\infty$, and no predecessors. Repeatedly settle an unsettled vertex of minimum tentative distance. For each unsettled neighbour $v$, if $dist[u]+w(u,v)<dist[v]$, set that distance and `pred[v] = u`. Keep the first predecessor on equal-distance ties; a heap implementation discards stale entries. Stop when no finite unsettled distance remains.

| Step | Visit | Distances updated |
|------|-------|-------------------|
| 1 | A (0) | B = 2, D = 8 |
| 2 | B (2) | E = 8, D = 7 |
| 3 | D (7) | F = 9 |
| 4 | E (8) | C = 17. (F: 8 + 1 = 9, no change) |
| 5 | F (9) | C = 12 |
| 6 | C (12) | none |

**Final distances:** A = 0, B = 2, D = 7, E = 8, F = 9, C = 12.

**Shortest path to C:** A to B to D to F to C = $2 + 5 + 2 + 3 = 12$.

F also has distance 9 through A to B to E to F ($2+6+1=9$), a tie. Either path is valid; strict-improvement updates keep D as F's predecessor here. Thus C also has two shortest routes, via D–F or E–F. The displayed tree uses predecessors B←A, D←B, E←B, F←D, C←F. Binary-heap time is $O((V+E)\log V)$ with $O(V+E)$ graph storage; a simple array implementation takes $O(V^2+E)$.

![Dijkstra shortest path tree from A](diagrams/b1-theory-08-dijkstra-graph.svg)

---

## Verification

Run `python tools/verify_b1_theory.py` from the repository root to recheck the published numerical tables, graph/search results, local links, all 27 subquestion visual references, and all 23 SVG/Excalidraw pairs. The checks are read-only and use Python's standard library. They supplement the mathematical review; they do not authenticate the missing original paper or automatically prove every prose statement.

## Quick Revision

| Topic | One-line memory |
|-------|-----------------|
| Design vs analysis | Design = make the method; analysis = predict time and space |
| Recurrence methods | Substitution, recursion tree, Master Theorem |
| Merge sort | $T(n) = 2T(n/2) + n$, so $\Theta(n \log n)$, not in-place |
| Quick sort | In-place partition; count stack separately; not stable; expected $\Theta(n\log n)$ with random pivots |
| Heap sort | Build max-heap in $\Theta(n)$, then $n-1$ removal rounds; worst-case $\Theta(n\log n)$ |
| Greedy | Local best choice, no going back, not always optimal |
| Memo vs tab | Memo = top-down with cache; tab = bottom-up with table |
| MST | Prim grows one tree; Kruskal adds the smallest safe edge |
| Backtracking | Choose, check, undo on dead end |
| Subset sum | Take or skip; pruning sum > $d$ is safe for nonnegative remaining items |
| Hamiltonian circuit | Visit every vertex once, return to start, backtrack on dead end |
| DP properties | Valid recurrence + reuse; optimal substructure for optimization |
| 0/1 knapsack | Max of skip and (if it fits) take using the previous row; $O(nW)$ is pseudo-polynomial |
| Grid max coins | Cell value + max(up, left) |
| Coin change DP | $C[x] = 1 + \min C[x - c]$; greedy can fail |
| Bellman-Ford | Up to $V-1$ passes; finite shortest paths require no reachable negative cycle |
| Dijkstra vs Bellman-Ford | Nonnegative weights guarantee Dijkstra; Bellman–Ford handles negatives and detects reachable negative cycles |
| Optimality | Best feasible objective is distinct from matching a resource lower bound |
| P, NP, NP-hard, NP-complete | Decision classes; $P\subseteq NP$, NP-complete = NP ∩ NP-hard; P vs NP open |
| Decision vs optimization | Yes/no vs best answer; value search needs bounded integer thresholds, recovery needs more |
| Dijkstra | Repeatedly settle the nearest unsettled vertex and relax its edges |

---

[Previous: Chapter 0 - Previous Year Questions](../../README.md) | [Home](../../../README.md) | [Next: 2nd Batch Theory](../../2nd%20Batch/Theory/README.md)
