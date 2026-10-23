# 1st Batch Theory: Answers

[Previous: Chapter 0 - Previous Year Questions](../../README.md) | [Home](../../../README.md) | [Next: 2nd Batch Theory](../../2nd%20Batch/Theory/README.md)

This guide answers all 27 subquestions in the supplied CSE 2201 final-examination paper for 2023. The paper says to answer any 3 questions from each section. The question text and marks below were checked against the supplied scan; line breaks are normalized.

> [!IMPORTANT]
> **Source:** the supplied scan identifies the paper as the 2023 CSE 2201 final examination. Question wording, year, marks, instructions, and printed numerical data were checked against that scan. Line breaks and spacing are normalized. Any extra example used to explain a question that gives no data is marked as illustrative.

**Language:** Answers use short explanations and show the working. Necessary course terms are kept and explained in simple words.

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

#### Q1(a)

**Question (transcribed):** What do you mean by the terms Design and Analysis of algorithm? What are the properties of a good algorithm?

**Answer.**

- **Design** means choosing the steps or method that will solve the problem.
- **Analysis** means estimating how an algorithm's running time and memory use grow as the input gets larger.

An algorithm needs clear steps that can be carried out and that stop for every valid input. State what input it accepts and what output it must produce. Also check that it gives the right answer before judging its speed or memory use.

![Design, correctness, and resource analysis](diagrams/b1-theory-09-design-analysis.svg)

A good algorithm has these qualities:

1. **Correct**: it gives the right answer for every valid input.
2. **Fast**: its running time grows slowly as the input size $n$ grows.
3. **Memory efficient**: it uses little extra memory.
4. **Simple**: it is easy to understand, write, and check.
5. **Works on all valid inputs**: it also handles cases such as an empty array or a one-item array.

#### Q1(b)

**Question (transcribed):** Distinguish between best-case, worst-case, and average-case analysis for an algorithm. When is each most relevant?

**Answer.**

For inputs of the same size $n$:

- **Best-case time** is the least work on any such input.
- **Worst-case time** is the most work on any such input.
- **Average-case time** is the average work, assuming a stated chance for each kind of input. The average depends on that assumption.

![Linear-search best, worst, and average comparisons](diagrams/b1-theory-10-case-analysis.svg)

| Algorithm | Best case | Worst case | Average case |
|-----------|-----------|------------|--------------|
| Linear search | $\Theta(1)$: the item is the first element | $\Theta(n)$: the item is last or not present | $(n+1)/2$ comparisons, hence $\Theta(n)$, if the target occurs once and each position is equally likely |
| Insertion sort | $\Theta(n)$: input is already sorted | $\Theta(n^2)$: input is reverse sorted | $\Theta(n^2)$ for a uniformly random order of distinct items |

**When each case is useful:** use the best case to describe the fastest situation, the worst case to give a guarantee for every input, and the average case when you know how likely each kind of input is. State the assumption used for an average case.

#### Q1(c)

**Question (transcribed):** Given two algorithms, Algorithm A with time complexity O(n^2) and Algorithm B with time complexity O(n log n), which one would you prefer for large input sizes and why? Justify your answer.

**Answer.**

Assuming the given bounds are the algorithms' actual growth rates, prefer **Algorithm B** for large inputs because $n\log n$ grows more slowly than $n^2$. The table uses coefficient 1 to compare them. Strictly, $O(\cdot)$ gives only an upper bound, so these bounds alone do not prove which algorithm is faster. Fixed costs can also make Algorithm A faster on small inputs.

![Growth comparison under unit coefficients](diagrams/b1-theory-11-growth.svg)

| $n$ | $n^2$ (Algorithm A) | $n \log_2 n$ (Algorithm B) |
|-----|---------------------|----------------------------|
| 10 | 100 | about 33 |
| 1,000 | 1,000,000 | about 9,966 |
| 1,000,000 | $10^{12}$ | about $2 \times 10^7$ |

At $n = 10^6$, Algorithm B does about 50,000 times less work. For very small inputs, Algorithm A may still be faster because its fixed costs can be smaller. Asymptotic analysis compares growth as $n$ becomes large.

---

### Q2. Recurrences and Loop Analysis

#### Q2(a)

**Question (transcribed):** Explain the significance of recurrence relations.

**Answer.**

A **recurrence** defines a value using values for smaller inputs, along with a base case. In algorithm analysis, it often describes running time $T(n)$ using the running times of smaller problems. This is useful because solving the recurrence tells us how the running time grows.

For example, $T(n)=2T(n/2)+n$ for $n\ge2$, with $T(1)=1$. Here $n$ is a power of two. A recurrence must state its base case and how input sizes are handled.

![Recurrence and work per level](diagrams/b1-theory-02-recursion-tree.svg)

Three common ways to solve a recurrence are:

1. **Substitution**: guess a bound, then prove it by induction (check a base case, then show the bound follows for larger inputs).
2. **Recursion tree**: draw the recursive calls, add the work at each level, and total it.
3. **Master Theorem**: for $T(n)=aT(n/b)+f(n)$, compare $f(n)$ with $n^{\log_b a}$. Use it only when the recurrence meets its conditions.

#### Q2(b)

**Question (transcribed):** Determine the time complexity for the following algorithms:

**(i)**

```text
sum = 0;
for (i = 1; i <= n; i = i * 2)
    for (j = 1; j <= n; j++)
        sum += i * j;
```

**(ii)**

```text
sum = 0;
for (i = 1; i <= n; i = i * 2)
    for (j = 1; j <= i; j++)
        sum += i * j;
```

**Answer.**

Assume integer $n\ge1$, no arithmetic overflow, and constant-time arithmetic. Each loop body takes a constant amount of time, so count how many times it runs.

![Loop iteration counts for n equals 8](diagrams/b1-theory-12-loop-counts.svg)

**(i)** The outer loop doubles $i$: $1,2,4,\dots$ up to $n$. It runs $\lfloor\log_2 n\rfloor+1$ times. The inner loop runs $n$ times each time, for a total of $n(\lfloor\log_2 n\rfloor+1)$ iterations. The time is **$\Theta(n\log n)$**. For $n = 8$: total = 32 iterations.

**(ii)** The outer loop again doubles $i$, and the inner loop runs $i$ times. If $2^K\le n<2^{K+1}$, the total is $1+2+4+\dots+2^K=2^{K+1}-1$. This total is between $n$ and $2n-1$, so the time is **$\Theta(n)$**. For $n = 8$: total = $1+2+4+8 = 15$.

#### Q2(c)

**Question (transcribed):** Prove that $T(n)=O(n\log n)$ for the recurrence relation:

$$T(n)=\begin{cases}2T(n/2)+n,&n>1,\\n,&n=1.\end{cases}$$

**Answer.**

**Domain:** $n=2^k$ for an integer $k\ge0$. The recursive rule applies when $n>1$.

**Method 1: Substitution**

We prove the bound $T(n)=O(n\log n)$ by guessing $T(n)\le c n\log_2 n$ for all $n\ge2$ and choosing $c=2$.

- **Base case** ($n=2$): $T(2)=2T(1)+2=4$, and $2\cdot2\cdot\log_2 2=4$. So the bound holds.
- **Inductive step** ($n\ge4$): assume the bound holds for $n/2$. We check the base case $n=2$ separately because $cn\log n=0$ at $n=1$.

$$T(n) = 2T(n/2) + n \le 2 \cdot c\,\frac{n}{2}\log_2\frac{n}{2} + n = cn\log_2 n - cn + n$$

Since $c\ge1$, $-cn+n\le0$. Therefore $T(n)\le c n\log_2 n$, which proves $T(n)=O(n\log n)$.

**Method 2: Recursion tree**

| Level | Number of nodes | Size of each node | Work per level |
|-------|-----------------|-------------------|----------------|
| 0 | 1 | $n$ | $n$ |
| 1 | 2 | $n/2$ | $2 \cdot n/2 = n$ |
| 2 | 4 | $n/4$ | $4 \cdot n/4 = n$ |
| ... | ... | ... | $n$ |
| $\log_2 n$ | $n$ | 1 | $n$ |

![Recursion tree for T(n) = 2T(n/2) + n](diagrams/b1-theory-02-recursion-tree.svg)

There are $\log_2 n+1$ levels, and each level does $n$ work. The total is $n(\log_2 n+1)=\Theta(n\log n)$.

**Method 3: Master Theorem**

Here $a=2$, $b=2$, and $f(n)=n$. Thus $n^{\log_b a}=n^{\log_2 2}=n$. Since $f(n)$ has the same growth, this is **Case 2** of the Master Theorem, so $T(n)=\Theta(n\log n)$.

**Final answer:** $T(n)=\Theta(n\log n)$. For powers of 2, the exact solution is $T(n)=n\log_2 n+n$. Check: $T(4)=12$ and $T(8)=32$.

---

### Q3. Divide and Conquer, Merge Sort, Quick Sort, Heap Sort

#### Q3(a)

**Question (transcribed):** Explain the main steps of the Divide-and-Conquer algorithmic paradigm.

**Answer.**

1. **Divide**: split the problem into smaller parts.
2. **Conquer**: solve each part. Solve a small enough part directly; this is the **base case**.
3. **Combine**: join the smaller answers to get the final answer.

**Illustrative example: merge sort on $[5, 2, 4, 7]$**

![Divide, conquer, and combine in merge sort](diagrams/b1-theory-13-merge-sort.svg)

```text
[5, 2, 4, 7]          divide
[5, 2]   [4, 7]       divide
[2, 5]   [4, 7]       conquer (sort each half)
[2, 4, 5, 7]          combine (merge)
```

#### Q3(b)

**Question (transcribed):** Analyze the recurrence relation for Merge Sort: T(n) = 2T(n/2) + O(n). What is its time complexity?

**Answer.**

**Idea:** split the array into two halves, sort each half, then merge the sorted halves.

**Recurrence:**

$$T(n) = 2T(n/2) + \Theta(n), \qquad T(1) = \Theta(1)$$

For powers of two, the two halves have equal size. For other $n$, split into sizes $\lfloor n/2\rfloor$ and $\lceil n/2\rceil$; the time bound stays the same.

![Balanced merge-sort recursion and level costs](diagrams/b1-theory-02-recursion-tree.svg)

- **Divide:** find the middle, which takes $\Theta(1)$ time.
- **Conquer:** sort two halves recursively.
- **Combine:** merge the halves by scanning their $n$ items, which takes $\Theta(n)$ time.

**Recursion tree:** each level does $\Theta(n)$ work. There are $\log_2 n+1$ levels, so the total time is $T(n)=\Theta(n\log n)$.

**Master Theorem:** $a=2$, $b=2$, and $f(n)=n=\Theta(n^{\log_2 2})$. This is **Case 2**, so $T(n)=\Theta(n\log n)$.

**Space:** array merge sort uses a $\Theta(n)$ temporary buffer, so it is **not in-place**.

#### Q3(c)

**Question (transcribed):** What is in-place sorting? Is Quicksort an in-place sorting algorithm? Justify.

**Answer.**

An **in-place sort** rearranges the input using little extra memory. Under the strict definition, it uses $O(1)$ extra memory in total. Some textbooks do not count the recursion stack.

Quicksort's **partition** step rearranges items around a pivot using swaps and uses $O(1)$ extra memory. Its recursive calls use $O(\log n)$ stack space on average with random pivots, but can use $O(n)$ in the worst case. So quicksort is usually called in-place when the stack is not counted. Recursing on the smaller part and looping over the larger part limits stack space to $O(\log n)$; worst-case time can still be $\Theta(n^2)$.

![Quicksort partition workspace versus recursion stack](diagrams/b1-theory-14-quicksort-space.svg)

> [!NOTE]
> Quick sort is **not stable**: equal elements may change their relative order.

#### Q3(d)

**Question (transcribed):** Trace Heap Sort on the array A = [7, 2, 5, 3, 4, 6, 1]. Show the heap construction and sorting phases step by step.

**Answer.**

**Given input:** $A=[7,2,5,3,4,6,1]$. Indices start at 0. At index $i$, the children are at $2i+1$ and $2i+2$ if they are inside the heap. First build a **max-heap**, where each parent is at least as large as its children. Then move the largest item to the end on each round.

**Step 1: Build the max-heap** (restore heap order, or heapify, from index 2 down to 0)

- $i=2$ (value 5): the children are 6 and 1. Swap 5 with the larger child, 6. Array: $[7, 2, 6, 3, 4, 5, 1]$
- $i=1$ (value 2): the children are 3 and 4. Swap 2 with the larger child, 4. Array: $[7, 4, 6, 3, 2, 5, 1]$
- $i=0$ (value 7): it is already larger than both children, 4 and 6, so no swap is needed.

Heap as a tree:

![Max-heap after the build step](diagrams/b1-theory-03-heap-build-tree.svg)

**Step 2: Sort (repeat until size is 1)**

Each round, swap the root (the largest item) with the last item in the heap. Shorten the heap by one, then restore the heap property from the root.

| Round | Swap root with | Array after the round |
|-------|----------------|-----------------------|
| 1 | last element | $[6, 4, 5, 3, 2, 1, 7]$ |
| 2 | last heap element | $[5, 4, 1, 3, 2, 6, 7]$ |
| 3 | last heap element | $[4, 3, 1, 2, 5, 6, 7]$ |
| 4 | last heap element | $[3, 2, 1, 4, 5, 6, 7]$ |
| 5 | last heap element | $[2, 1, 3, 4, 5, 6, 7]$ |
| 6 | last heap element | $[1, 2, 3, 4, 5, 6, 7]$ |

**Final sorted array:** $[1, 2, 3, 4, 5, 6, 7]$

**Complexity:** building the heap takes $\Theta(n)$. The next $n-1$ rounds take at most $O(\log n)$ each, so heapsort's worst-case time is $\Theta(n\log n)$. Iterative sift-down uses $O(1)$ extra memory, so heapsort is in-place. It is **not stable**: equal items may change order.

---

### Q4. Greedy Algorithms, Memoization vs Tabulation, and MST

#### Q4(a)

**Question (transcribed):** At each step, Greedy Algorithm chooses local optimal solution. With suitable example show that, choosing local optimal solution at each step may not lead to the global optimal solution.

**Answer.**

A **greedy algorithm** builds a solution one step at a time. It picks the best-looking choice at each step and does not change earlier choices.

**Illustrative counterexample: coin change.** Use unlimited coins with denominations $\{1,3,4\}$. Make exactly $6$ using as few coins as possible.

![Greedy versus optimal coin change](diagrams/b1-theory-15-coin-change.svg)

- Greedy picks the largest coin first: $4+1+1$, for **3 coins**.
- The best answer is $3+3$, for **2 coins**.

So a greedy choice does not always give the best full answer. Greedy works when each local choice is safe, meaning it can still be part of a best answer, as in Kruskal's and Prim's MST algorithms.

#### Q4(b)

**Question (transcribed):** Differentiate between memoization and tabulation.

**Answer.**

Both are **dynamic programming** methods. They save answers to smaller problems so they do not need to solve the same problem again.

- **Memoization (top-down)**: use recursion and save each answer in a cache (a store for saved answers) the first time it is found.
- **Tabulation (bottom-up)**: use a loop to fill a table, starting with the smallest problems and building up to the answer.

**Illustrative example: Fibonacci:** $F_0=0$, $F_1=1$, and $F_n=F_{n-1}+F_{n-2}$ for integers $n\ge2$. Both functions accept nonnegative integers.

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
| Direction | Top-down: start with the big problem | Bottom-up: start with small problems |
| Method | Recursion and a cache | A loop and a table |
| Recursion | Uses the call stack | Does not use recursion |
| States computed | Only the states the recursion needs | Every state in the chosen table order |

Both Fibonacci versions use $O(n)$ arithmetic operations. Memoization stores $O(n)$ values and uses $O(n)$ stack space. Tabulation stores $O(n)$ values in this code, but can keep only the two previous values and use $O(1)$ memory.

#### Q4(c)

**Question (transcribed):** Consider the following graph with weighted edges: Vertices: A, B, C, D, E; Edges: A-B (2), A-C (3), B-C (1), B-D (4), C-D (5), C-E (6), D-E (7). (i) Find the Minimum Spanning Tree using Prim's Algorithm. (ii) Find the Minimum Spanning Tree using Kruskal's Algorithm.

**Answer.**

A **minimum spanning tree (MST)** connects every vertex, has no cycles, and has the smallest possible total edge weight. It has $|V|-1$ edges.

**Given graph:** a connected, simple, undirected graph with $V=\{A,B,C,D,E\}$ and the weighted edges from the question, listed below.

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

1. Start with $\{A\}$. The choices are A-B (2) and A-C (3). Pick **A-B (2)**.
2. The tree is $\{A,B\}$. The choices are A-C (3), B-C (1), and B-D (4). Pick **B-C (1)**.
3. The tree is $\{A,B,C\}$. The choices are B-D (4), C-D (5), and C-E (6). Pick **B-D (4)**.
4. The tree is $\{A,B,C,D\}$. The choices are C-E (6) and D-E (7). Pick **C-E (6)**.

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

**Total MST weight:** $1+2+4+6=13$

Both algorithms give this MST. Since all edge weights are different, it is the only MST. Prim adds the lightest edge from its tree to an outside vertex. Kruskal adds the lightest edge that does not make a cycle.

---

## Section B

### Q5. Backtracking

#### Q5(a)

**Question (transcribed):** Explain the concept of Backtracking.

**Answer.**

**Backtracking** builds a solution one choice at a time. It checks each partial solution against the rules. If a choice leads to a **dead end**, it undoes that choice and tries another.

Backtracking explores a **state-space tree** in **depth-first search (DFS)** order: it follows one branch as far as possible, then returns to try another. It uses **pruning** to stop exploring a branch that cannot lead to a valid answer. The number of branches can still grow exponentially.

![Choose, reject, undo, and find a four-queen solution](diagrams/b1-theory-18-queens-backtracking.svg)

#### Q5(b)

**Question (transcribed):** Describe how a backtracking algorithm would typically solve the N-Queen problem. How would it determine where to place the k-th queen, and what are the conditions that would lead to backtracking?

**Answer.**

Place $N$ queens on an $N\times N$ board so that no two queens share a row, column, or diagonal.

**Illustrative instance:** Place 4 queens on a $4\times4$ board. Rows and columns start at 0.

![Four-queen search branches and the first solution board](diagrams/b1-theory-18-queens-backtracking.svg)

**Idea:** put one queen in each row. To place the $k$-th queen in row $k$:

1. Try columns $0,1,\dots,N-1$ in order.
2. A column is safe if no earlier queen is in the same column or diagonal.
3. Put the queen in a safe column and continue to row $k+1$.
4. If no column is safe, **backtrack**: return to row $k-1$ and try its next column.

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

**When to backtrack**

- A queen is already in the same column.
- A queen is already on the same diagonal.
- No column is safe in row $k$, so return to row $k-1$.

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

Call `SOLVE(0)` with a length-$N$ array `board`; each entry stores a queen's column. The search checks only earlier rows, so old values in later rows do not matter after backtracking. For $N=4$, there are exactly two solutions: $[1,3,0,2]$ and $[2,0,3,1]$. The first is shown above.

#### Q5(c)

**Question (transcribed):** Find a subset of the given set A = {3, 5, 6, 7} whose sum is d = 15. Show a partial trace of the backtracking algorithm and highlight when it explores a path and when it backtracks.

**Answer.**

**Given input:** $A=\{3,5,6,7\}$ contains four different positive numbers, each used at most once. Find subsets that sum to $d=15$. Check the numbers in order, trying **take** before **skip**. The trace and diagram show the search only through its first solution.

- If the sum is greater than $d$, **prune** the branch. This is safe because all remaining numbers are positive.
- If the sum equals $d$, we have a solution.
- If no numbers remain and the sum is not $d$, we have reached a **dead end**.

**Trace**

1. Take 3: sum = 3.
2. Take 5: sum = 8.
3. Take 6: sum = 14.
4. Take 7: sum = 21. This is more than 15, so **prune**.
5. Skip 7: sum = 14. No items left, so **dead end**. Backtrack.
6. Skip 6: sum = 8.
7. Take 7: sum = 15. **Solution found.**

![Backtracking trace for subset sum with d = 15](diagrams/b1-theory-04-subset-sum-tree.svg)

**Answer: $\{3,5,7\}$**, because $3+5+7=15$. This is the only solution: sums of zero or one number are below 15, every two-number sum is at most 13, the other three-number sums are 14, 16, and 18, and all four numbers sum to 21. Since all numbers are positive, once the sum reaches 15, adding another number cannot give another solution.

```text
SUBSETS(i, total, chosen):
    if total == d: output chosen; return
    if total > d or i == length(A): return
    SUBSETS(i + 1, total + A[i], chosen followed by A[i])
    SUBSETS(i + 1, total, chosen)
```

Call `SUBSETS(0, 0, [])`. At each number, the algorithm tries **take** and **skip**. It stops a branch when it finds the target, goes over it, or runs out of numbers.

#### Q5(d)

**Question (transcribed):** Trace the initial steps of the backtracking algorithm, starting from vertex a, to find a Hamiltonian Circuit. Show at least two different paths explored (one that might lead to a solution, and one that leads to backtracking).

**Answer.**

A **Hamiltonian circuit** visits every vertex once, then returns to its starting vertex.

**Graph transcribed from the paper's figure:** an undirected graph on $V=\{a,b,c,d,e,f\}$. The adjacency list below gives every edge in the figure.

| Vertex | Neighbours |
|--------|------------|
| a | b, c, d |
| b | a, c, f |
| c | a, b, d, e, f |
| d | a, c, e |
| e | c, d, f |
| f | b, c, e |

**Idea:** start at $a$ and try unvisited neighbours in alphabetical order. If the path gets stuck, backtrack and try another neighbour.

**Trace**

1. Try $a \to b \to c \to d \to e \to f$. All 6 vertices are visited, but $f$ is not joined to $a$. **Dead end.**
2. Return to $c$ and try $e$: $a \to b \to c \to e \to d$. The only unvisited vertex is $f$, but there is no edge from $d$ to $f$. **Dead end.**
3. Backtrack from $d$ to $e$, then try $f$: $a \to b \to c \to e \to f$. The only unvisited vertex is $d$, but there is no edge from $f$ to $d$. **Dead end.**
4. Return to $c$ and try $f$: $a \to b \to c \to f \to e \to d$. All 6 vertices are visited, and $d$ is joined to $a$. **Circuit found.**

![Backtracking search tree using the graph shown in the paper](diagrams/b1-theory-05-hamiltonian-tree.svg)

**Answer:** $a-b-c-f-e-d-a$. Another valid circuit is $a-b-f-e-d-c-a$. Every pair of neighbours in each circuit, including the last vertex and $a$, appears in the adjacency list.

```text
EXTEND(path, used):
    if length(path) == |V|:
        if edge(last(path), a): output path followed by a
        return
    for v in neighbours(last(path)) in alphabetical order:
        if v not in used:
            EXTEND(path followed by v, used union {v})
```

Call `EXTEND([a], {a})`. Stop at the first circuit for this trace, or continue to find more. Add only unused vertices, and check that the final vertex connects back to $a$.

---

### Q6. Dynamic Programming

#### Q6(a)

**Question (transcribed):** What are the two key properties that a problem must possess for Dynamic Programming to be applicable?

**Answer.**

1. **Optimal substructure**: the best answer to a problem can be built from the best answers to smaller problems.
2. **Overlapping subproblems**: the same smaller problems appear more than once. DP saves each answer and reuses it.

![Overlapping knapsack states and optimal substructure](diagrams/b1-theory-19-dp-properties.svg)

#### Q6(b)

**Question (transcribed):** Define the DP[i][w] state for the 0/1 Knapsack problem. Write down the dynamic programming recurrence relation for the knapsack problem.

**Answer.**

**Problem:** There are $n\ge1$ items. Item $i$ has a positive integer weight $w_i$ and a nonnegative profit $p_i$. The capacity $W$ is a nonnegative integer. Take each item whole, at most once, and keep the total weight at most $W$. Taking no items is allowed. Maximize total profit.

![Knapsack skip/take dependencies and worked DP table](diagrams/b1-theory-20-knapsack.svg)

**State:** $DP[i][w]$ is the greatest profit using the first $i$ items with capacity $w$.

**Recurrence:**

$$DP[i][w] = \begin{cases} DP[i-1][w] & \text{if } w_i > w \\ \max\big(DP[i-1][w],\; p_i + DP[i-1][w - w_i]\big) & \text{if } w_i \le w \end{cases}$$

If item $i$ does not fit, skip it. Otherwise compare skipping it with taking it and adding the best profit for the remaining capacity.

**Base cases:** $DP[0][w]=0$ for $0\le w\le W$, and $DP[i][0]=0$. Fill the table by rows, using the row above for each calculation.

**Answer:** $DP[n][W]$. For $W\ge1$, the time and full-table space are $O(nW)$. A one-row table uses $O(W)$ space if capacities are updated from high to low. If $W=0$, the answer is 0. To find the chosen items, trace backward through the full table. Q7(c) shows an example.

#### Q6(c)

**Question (transcribed):** Given the following 4 x 3 grid with coins (1) or no coins (0) at each cell, construct the DP table and trace the path that yields the maximum number of coins collected from (0,0) to (3,2). What is the maximum number of coins?

**Answer.**

**Grid from the paper:** the question does not say which moves are allowed, so assume we can move only **right or down** from $(0,0)$ to $(3,2)$. No cells are blocked. Collect the 0 or 1 coin in each visited cell, including the start and end cells.

![Grid values, DP values, and an optimal path](diagrams/b1-theory-21-grid.svg)

| | col 0 | col 1 | col 2 |
|---|---|---|---|
| row 0 | 1 | 0 | 1 |
| row 1 | 0 | 1 | 0 |
| row 2 | 1 | 1 | 1 |
| row 3 | 0 | 0 | 1 |

Set $dp[0][0]=\text{grid}[0][0]$. Each $dp[r][c]$ stores the most coins that can be collected on a path to cell $(r,c)$. Fill the table from top to bottom and left to right using $dp[r][c]=\text{grid}[r][c]+\max(dp[r-1][c],dp[r][c-1])$, using only cells above or to the left that exist. The last move must come from one of those two cells. For an $R\times C$ grid, the time and full-table space are $O(RC)$; storing only values can use $O(C)$ space.

| | col 0 | col 1 | col 2 |
|---|---|---|---|
| row 0 | 1 | 1 | 2 |
| row 1 | 1 | 2 | 2 |
| row 2 | 2 | 3 | 4 |
| row 3 | 2 | 3 | **5** |

**Answer: 5 coins.** One best path is $(0,0)\to(0,1)\to(1,1)\to(2,1)\to(2,2)\to(3,2)$. It collects $1+0+1+1+1+1=5$ coins. The path $(0,0)\to(1,0)\to(2,0)\to(2,1)\to(2,2)\to(3,2)$ also collects 5 coins.

#### Q6(d)

**Question (transcribed):** Solve the change-making problem by DP for the amount n = 6 and the denominations 1, 3, and 4.

**Answer.**

**Given instance:** use any number of coins with denominations $D=\{1,3,4\}$ to make exactly 6.

**Recurrence:** $C[x]=1+\min_{c\in D,\ c\le x}C[x-c]$, with $C[0]=0$. If no coin can make an amount, its value is $\infty$ (unreachable). Fill the table from smaller amounts to larger ones. Each choice adds one coin to the best answer for the amount left over.

![Minimum-coin DP table and greedy counterexample](diagrams/b1-theory-15-coin-change.svg)

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $C[x]$ | 0 | 1 | 2 | 1 | 1 | 2 | 2 |

**Answer: 2 coins**, using $3+3$. Traceback goes $6\to3\to0$, subtracting 3 each time. Greedy gives $4+1+1$, or 3 coins, as in Q4(a). For amount $M$, this DP takes $O(|D|M)$ time and $O(M)$ space. These bounds depend on the number $M$, not on the number of bits used to write it; this is called pseudo-polynomial time.

---

### Q7. Shortest Paths, Optimality, and Knapsack

#### Q7(a)

**Question (transcribed):** Explain why Dijkstra's algorithm fails to find correct shortest paths in graphs with negative-weight edges, whereas Bellman-Ford succeeds.

**Answer.**

Dijkstra repeatedly **settles** (finalizes) the unsettled vertex with the smallest current distance, then does not change it again. This is correct when all edge weights are nonnegative. A negative edge can make a settled distance too large.

**Illustrative directed counterexample:** $V=\{A,B,C\}$ with exactly these edges: $A\to B=1$, $A\to C=4$, and $C\to B=-5$. The source is $A$.

![Negative-edge failure of label-setting Dijkstra](diagrams/b1-theory-22-negative-edge.svg)

- Dijkstra settles $B$ first, at distance 1.
- Then $C$, at distance 4, gives a shorter route to $B$: $4+(-5)=-1$. Dijkstra has already settled $B$, so Dijkstra keeps $B = 1$. The true answer is $-1$.

**Bellman-Ford** starts with distance 0 at the source and $\infty$ at every other vertex. It relaxes every edge up to $|V|-1$ times. To **relax** an edge $(u,v)$, check that $dist[u]\ne\infty$ and see whether $dist[u]+w(u,v)<dist[v]$; if so, lower $dist[v]$.

If no negative cycle can be reached from the source, a shortest path has no repeated vertices and uses at most $|V|-1$ edges. So $|V|-1$ passes are enough. Stop early if a full pass makes no change. The time is $O(VE)$ and the distance and predecessor arrays use $O(V)$ space.

**Negative-cycle check:** after the passes, if an edge from a reachable vertex can still be relaxed, a negative cycle is reachable from the source. Vertices reachable from that cycle have no finite shortest distance. A negative cycle that cannot be reached from the source does not affect this search.

#### Q7(b)

**Question (transcribed):** Consider the directed graph with vertices A, B, C, D, E and the edges A-B (6), A-C (7), B-D (5), B-E (-4), C-B (-3), C-D (8), D-E (-2), and E-A (2). Using Bellman-Ford, find the shortest paths from source vertex A to all other vertices.

**Answer.**

**Given graph:** a directed graph with $V=\{A,B,C,D,E\}$ and source A. The edges, in the question's order, are A to B = 6, A to C = 7, B to D = 5, B to E = -4, C to B = -3, C to D = 8, D to E = -2, and E to A = 2.

Use **in-place relaxation**: an updated distance can be used by later edges in the same pass. For example, in pass 1, A to B sets B to 6; then C to B gives $7+(-3)=4$, so B becomes 4.

| Pass | A | B | C | D | E |
|------|---|---|---|---|---|
| Start | 0 | $\infty$ | $\infty$ | $\infty$ | $\infty$ |
| 1 | 0 | 4 | 7 | 11 | 2 |
| 2 | 0 | 4 | 7 | 9 | 0 |
| 3 | 0 | 4 | 7 | 9 | 0 |

Pass 3 makes no changes, so we stop.

**Final distances from A:** A = 0; B = 4 (A to C to B); C = 7 (A to C); D = 9 (A to C to B to D); E = 0 (A to C to B to E).

**Negative cycle:** there is none. Every cycle returns to A. The smallest cycle total is 2, for A to C to B to E to A: $7-3-4+2=2$.

![Bellman-Ford directed graph with shortest distances from A](diagrams/b1-theory-06-bellman-ford-graph.svg)

#### Q7(c)

**Question (transcribed):** What is algorithm optimality? Find an optimal solution for the 0/1 knapsack problem using dynamic programming. Maximum weight = 8; item weights = [3, 4, 5, 6]; item profits = [2, 3, 1, 4].

**Answer.**

**Optimality has two meanings:** a solution is optimal if it is the best valid answer. An algorithm is optimal in resource use if it matches a proven lower bound on time or memory. Finding the best solution does not by itself prove that the algorithm uses the least possible resources.

**The 0/1 knapsack DP finds an optimal solution.** For each item, either skip it or take it if it fits. In the take case, use the best answer for the earlier items and the remaining capacity. These are all possible choices, so the recurrence gives the best profit. Its time is $O(nW)$; this does not show that the algorithm is best possible in time or memory.

![Knapsack recurrence, full table, and optimal item choice](diagrams/b1-theory-20-knapsack.svg)

**Given instance:** 0/1 knapsack with capacity $W=8$. The total weight may be at most 8, and taking no items is allowed. The four items are listed below.

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

**Answer: profit 5**, using items 1 and 2 (weight $3+4=7\le8$, profit $2+3=5$).

**Traceback:** $DP[4][8]=DP[3][8]=5$, so skip item 4. The value also stays 5 in row 3, so skip item 3. Since $DP[2][8]=5$ but $DP[1][8]=2$, take item 2 and reduce the capacity to $8-4=4$. Since $DP[1][4]=2$ but $DP[0][4]=0$, take item 1.

---

### Q8. P, NP, Decision vs Optimization, and Dijkstra

#### Q8(a)

**Question (transcribed):** Define the classes P, NP, NP-hard, and NP-complete. Explain the relationships between these classes.

**Answer.**

These classes describe **decision problems**, whose answers are yes or no. Running time is measured against the input's bit length (the number of bits needed to write the input). **Polynomial time** means the time is bounded by $n^k$ for some fixed constant $k$, where $n$ is the input length.

- **P**: decision problems that can be solved in polynomial time. Example: “Is there a path from $s$ to $t$ with cost at most $K$?” in a graph with nonnegative integer edge weights.
- **NP**: decision problems where every yes-instance has a **polynomial-length certificate** (a proof or witness) that can be checked in polynomial time. A no-instance has no certificate that passes. For example, a Hamiltonian cycle is a certificate for the Hamiltonian-cycle problem. NP does not mean “not polynomial.”
- **NP-hard**: every problem in NP can be reduced to this problem in polynomial time. For a decision problem, the reduction preserves yes-or-no answers. An NP-hard problem does not have to be in NP; it may even be an optimization problem.
- **NP-complete**: a decision problem that is both in NP and NP-hard. Examples are SAT and the Hamiltonian-cycle decision problem.

**Known relations:** $P\subseteq NP$, and NP-complete problems are exactly the problems in $NP\cap NP\text{-hard}$. Whether $P=NP$ is **open**. If any NP-complete problem can be solved in polynomial time, then $P=NP$. We do not know that $P$ is strictly smaller than $NP$.

![How P, NP, NP-hard, and NP-complete relate](diagrams/b1-theory-07-classes-venn.svg)

#### Q8(b)

**Question (transcribed):** Differentiate between decision problems and optimization problems in the context of NP-completeness.

**Answer.**

For the **traveling salesperson problem (TSP)**, a tour visits every vertex once and returns to its start. The tour's cost is the sum of its edge weights.

- A **decision problem** asks a yes-or-no question: “Is there a tour with cost at most $k$?”
- An **optimization problem** asks for the best answer: “Find the cheapest tour.”

NP-completeness is for decision problems. TSP's decision problem is NP-complete; finding the cheapest tour is an NP-hard optimization problem. If costs are integers in a known range whose endpoints are short to write, and each threshold question can be answered in polynomial time, binary search can find the cheapest value. Finding the value does not always give the actual tour.

![Threshold decision, value search, and conditional witness recovery](diagrams/b1-theory-23-decision-optimization.svg)

#### Q8(c)

**Question (transcribed):** For the following graph, find the shortest path along with cost from Node A to all other nodes using Dijkstra's Algorithm. Mention the formula for relaxation.

**Answer.**

**Graph transcribed from the paper's figure:** an undirected graph with nonnegative edge weights, vertices $A,B,C,D,E,F$, and source $A$. Its full edge list is: A-B (2), A-D (8), B-D (5), B-E (6), D-E (3), D-F (2), E-F (1), E-C (9), and F-C (3).

Set $dist[A]=0$ and all other distances to $\infty$. Repeatedly choose the not-yet-finalized vertex with the smallest distance and finalize it. For each neighbour $v$ not yet finalized, use the relaxation formula $dist[v]\leftarrow\min(dist[v],dist[u]+w(u,v))$. If the distance gets smaller, set `pred[v] = u`; this records the previous vertex on the path. Keep the first predecessor when distances tie. Stop when no reachable vertex remains.

| Step | Visit | Distances updated |
|------|-------|-------------------|
| 1 | A (0) | B = 2, D = 8 |
| 2 | B (2) | E = 8, D = 7 |
| 3 | D (7) | F = 9 |
| 4 | E (8) | C = 17. (F: 8 + 1 = 9, no change) |
| 5 | F (9) | C = 12 |
| 6 | C (12) | none |

**Final distances:** A = 0, B = 2, D = 7, E = 8, F = 9, C = 12.

**Shortest paths and costs:**

- B: A to B, cost $2$.
- D: A to B to D, cost $2+5=7$.
- E: A to B to E, cost $2+6=8$.
- F: A to B to D to F, cost $2+5+2=9$.
- C: A to B to D to F to C, cost $2+5+2+3=12$.

**Shortest path to C:** A to B to D to F to C, with cost $2+5+2+3=12$.

There is a tie for F: A to B to D to F and A to B to E to F both cost 9 ($2+5+2=2+6+1$). So C also has two shortest paths, through D-F or E-F, each with cost 12. The displayed tree uses B←A, D←B, E←B, F←D, and C←F. With a binary heap, Dijkstra takes $O((V+E)\log V)$ time and $O(V+E)$ graph space. A simple array version takes $O(V^2+E)$ time.

![Dijkstra shortest path tree from A](diagrams/b1-theory-08-dijkstra-graph.svg)

---

## Verification

Run `python tools/verify_b1_theory.py` from the repository root to check the numerical tables, graph/search results, local links, all 27 question diagrams, and all 23 SVG/Excalidraw pairs. These read-only checks supplement the review; they do not prove every prose statement.

## Quick Revision

| Topic | Easy memory line |
|-------|-----------------|
| Design and analysis | Design = choose the method; analysis = study time and memory use |
| Recurrences | Solve by substitution, a recursion tree, or the Master Theorem |
| Merge sort | Split, sort, and merge; time $\Theta(n\log n)$; needs $\Theta(n)$ extra memory |
| Quicksort | Partition in place; usually fast, but worst-case time is $\Theta(n^2)$; not stable |
| Heapsort | Build a max-heap in $\Theta(n)$; worst-case sorting time is $\Theta(n\log n)$; in-place, not stable |
| Greedy | Pick the best-looking next choice; it does not always give the best full answer |
| Memoization and tabulation | Memoization = recursion plus saved answers; tabulation = fill a table from small cases up |
| MST | Prim grows one tree; Kruskal adds the lightest edge that does not make a cycle |
| Backtracking | Choose, check, and undo a choice if it leads to a dead end |
| Subset sum | Try take or skip; if all numbers are positive, prune when the sum exceeds $d$ |
| Hamiltonian circuit | Visit every vertex once and return to the start |
| Dynamic programming | Store repeated subproblem answers; optimization DP needs optimal substructure |
| 0/1 knapsack | Compare skipping an item with taking it if it fits; time $O(n(W+1))$ |
| Grid coins | Best total = coins in this cell + the larger of the best totals above or left |
| Coin change DP | $C[x]=1+\min C[x-c]$; greedy can fail |
| Bellman-Ford | Relax every edge up to $V-1$ times; check for a reachable negative cycle |
| Dijkstra and Bellman-Ford | Dijkstra needs nonnegative edges; Bellman-Ford can handle negative edges |
| Optimality | Best answer and best possible resource use are different ideas |
| P, NP, NP-hard, NP-complete | $P\subseteq NP$; NP-complete = NP and NP-hard; whether $P=NP$ is open |
| Decision and optimization | Decision = yes/no; optimization = find the best answer |
| Dijkstra | Finalize the nearest not-yet-finalized vertex, then relax its edges |

---

[Previous: Chapter 0 - Previous Year Questions](../../README.md) | [Home](../../../README.md) | [Next: 2nd Batch Theory](../../2nd%20Batch/Theory/README.md)
