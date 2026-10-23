# 2nd Batch Theory: Answers

[Previous: 1st Batch Theory](../../1st%20Batch/Theory/README.md) | [Chapter 0 - Previous Year Questions](../../README.md) | [Home](../../../README.md) | [Next: 2nd Batch Lab Final](../Lab%20Final/README.md)

This guide answers all 24 subquestions in the supplied CSE 2201 final-examination paper for 2024. The paper says to answer any 3 questions from each section. Question wording, year, marks, and printed data were checked against the supplied scan; line breaks are normalized.

> [!IMPORTANT]
> **Source:** the supplied scan identifies the paper as the 2024 CSE 2201 final examination. Question wording and all printed numerical data were checked against it. Q7(a), Q7(b), and Q8(b) do not give specific graph, item, or job data, so their worked examples are clearly labeled as examples chosen for the answers.

Every subquestion includes a relevant SVG preview with an editable Excalidraw source in the [diagram index](diagrams/README.md).

**Language:** Answers use short explanations and show the working. Necessary course terms are kept and explained in simple words.

| Question | Topic | (a) marks | (b) marks | (c) marks |
|----------|-------|-----------|-----------|-----------|
| Q1 | Algorithm design, time and space, asymptotic bounds | 6 | 9 | 20 |
| Q2 | NP classes, BFS shortest path, activity DAG | 7 | 10 | 18 |
| Q3 | Searching vs traversing, linear and binary search, Strassen | 5 | 20 | 10 |
| Q4 | Insertion vs bubble sort, quick sort, merge sort | 10 | 10 | 15 |
| Q5 | Greedy algorithms, fractional knapsack, MST | 8 | 12 | 15 |
| Q6 | Dynamic programming, Floyd-Warshall, LCS | 11 | 12 | 12 |
| Q7 | Backtracking: graph colouring, LC-search, N-Queens | 10 | 10 | 15 |
| Q8 | Decision vs optimization, branch and bound, TSP | 8 | 12 | 15 |

### Visual Map: Full-Paper Topic Roadmap

The roadmap groups questions by section; it is **not a prerequisite chain**. Q1's analysis techniques apply throughout. Q3 covers searching, traversal, and **Strassen's matrix multiplication**, while sorting is Q4. Greedy, dynamic programming, and backtracking are distinct strategies—not successive stages built on greedy. Specific connections include fractional knapsack's relaxation as a bound in Q7(b), dynamic programming for TSP in Q8(c), and complexity classes in Q2(a) alongside decision versus optimization in Q8(a). Q7(b) is best-first branch and bound, distinct from Q7(a)/(c)'s depth-first backtracking.

![Full-paper roadmap of all eight questions and their subtopics, grouped by section rather than prerequisites](diagrams/b2-theory-25-paper-roadmap.svg)

---

## Section A

### Q1. Algorithm Design, Complexity, and Asymptotic Bounds

#### Q1(a)

**Question (transcribed):** Define time complexity and space complexity. Provide examples demonstrating when space complexity becomes a critical factor in algorithm design.

**Answer.**

- **Time complexity** is how the number of steps grows as the input size $n$ grows. Example: a single loop over $n$ items takes $\Theta(n)$ time.
- **Space complexity** measures memory as a function of input size. **Total space** includes input storage; **auxiliary space** excludes it but includes temporary arrays and the recursion stack. Here, sorting-space comparisons mean auxiliary space: array merge sort uses $\Theta(n)$, while iterative insertion sort uses $\Theta(1)$.

Both are written with asymptotic notation (see [Chapter 2](../../../Chapter%202%20-%20Complexity%20Analysis%20and%20Asymptotic%20Notation/README.md)).

**Space becomes critical when memory is the real limit:**

1. The data is very large (for example, a billion numbers that barely fit in RAM). An algorithm that needs a second copy of the data may not fit.
2. The device is small (phones, embedded boards, sensors).
3. Many programs run at the same time and share the same memory.

Example: if $10^9$ numbers already fit in RAM but a second array does not, iterative heap sort can sort them with $\Theta(1)$ auxiliary space. If the input itself does not fit, use an external-memory method, such as external merge sort; choosing an in-place RAM algorithm alone does not solve that problem. Actual speed depends on the implementation and workload.

![Time, total space, and auxiliary space](diagrams/b2-theory-15-time-space.svg)

#### Q1(b)

**Question (transcribed):** Define algorithm design paradigm. Briefly describe divide-and-conquer and greedy paradigms with suitable examples.

**Answer.**

A **design paradigm** is a general strategy that solves many different problems. Common paradigms are divide and conquer, greedy, dynamic programming, backtracking, and branch and bound. (See [Chapter 1](../../../Chapter%201%20-%20Introduction%20and%20Algorithm%20Foundations/README.md) for the full list.)

**Divide and conquer (D&C)**

1. **Divide** the problem into smaller parts.
2. **Conquer** each part by solving it (recursively, or directly if it is small).
3. **Combine** the answers into the final answer.

Examples: merge sort and quick sort; binary search recurses into only one half (also called decrease-and-conquer) (see [Chapter 6](../../../Chapter%206%20-%20Divide%20and%20Conquer/README.md)).

**Greedy**

At every step, pick the option that looks best right now, and never go back. This works when the best local choice is always part of some best overall answer.

Example: **unweighted activity selection on one resource**. Repeatedly choose the earliest-finishing activity compatible with the last selected one, treating intervals as $[s,f)$ so that $s_{next}\ge f_{last}$ is allowed. This maximizes the number selected (see [Chapter 7](../../../Chapter%207%20-%20Greedy%20Algorithms/README.md)).

| | Divide and conquer | Greedy |
|--|--------------------|--------|
| Subproblems | Usually independent, solved recursively | One choice at a time, no recursion needed |
| Going back? | Not needed, since parts are solved fully | Never changes a choice |
| Example | Merge sort | Activity selection, Kruskal's MST |

![Divide-and-conquer and greedy design patterns](diagrams/b2-theory-16-design-paradigms.svg)

#### Q1(c)

**Question (transcribed):** Evaluate asymptotic bounds for: (i) T(n) = 2T(n/2) + n; (ii) T(n) = T(n - 1) + 1; (iii) T(n) = 4T(n/2) + n^2; (iv) T(n) = T(n/3) + log n.

**Answer.**

Assume constant positive base-case cost $T(n)=\Theta(1)$ for $n\le1$, fixed logarithm base greater than 1, and positive integer sizes. Use powers of 2 or 3 for the respective divide recurrences; standard floors/ceilings do not change the bounds.

Method used: the **Master theorem** for $T(n) = aT(n/b) + f(n)$ (see [Chapter 3](../../../Chapter%203%20-%20Recurrences%20Correctness%20and%20Loop%20Invariants/README.md)). Compare $f(n)$ with $n^{\log_b a}$:

Let $p=\log_b a$, with $a\ge1$, $b>1$ and asymptotically nonnegative $f$.

- **Case 1:** $f(n)=O(n^{p-\varepsilon})$ for some fixed $\varepsilon>0$ gives $T(n)=\Theta(n^p)$.
- **Case 2 (extended):** $f(n)=\Theta(n^p\log^k n)$, $k\ge0$, gives $T(n)=\Theta(n^p\log^{k+1}n)$.
- **Case 3:** $f(n)=\Omega(n^{p+\varepsilon})$ for some fixed $\varepsilon>0$, and $af(n/b)\le cf(n)$ for some $c<1$ and sufficiently large $n$, gives $T(n)=\Theta(f(n))$.

Merely being smaller or larger is not sufficient in Cases 1 and 3: the polynomial gap matters.

**(i) $T(n) = 2T(n/2) + n$**

- $a = 2$, $b = 2$, $n^{\log_2 2} = n$, and $f(n) = n$. They are equal, so this is **Case 2**.
- **Answer: $T(n) = \Theta(n \log n)$.**
- Check with a recursion tree: each of the $\log_2 n$ levels does $n$ work.

**(ii) $T(n) = T(n-1) + 1$**

- This is not a divide recurrence, so the Master theorem does not apply. Expand it instead:

$$T(n) = T(n-1) + 1 = T(n-2) + 2 = \dots = T(1) + (n-1)$$

- **Answer: $T(n) = \Theta(n)$.**

**(iii) $T(n) = 4T(n/2) + n^2$**

- $a = 4$, $b = 2$, $n^{\log_2 4} = n^2$, and $f(n) = n^2$. They are equal, so this is **Case 2**.
- **Answer: $T(n) = \Theta(n^2 \log n)$.**
- Check: level $i$ has $4^i$ nodes, each of size $n/2^i$, so each level does $4^i \cdot (n/2^i)^2 = n^2$ work. There are $\log_2 n$ levels.

**(iv) $T(n) = T(n/3) + \log n$**

- Here $a = 1$, $b = 3$, so $n^{\log_3 1} = 1$. The basic three-case form does not apply: $\log n$ is larger than 1 but not polynomially larger, so Case 3's polynomial-gap condition fails.
- Use the **extended** Case 2 form: if $f(n) = \Theta(\log^k n)$ with $k \ge 0$, then $T(n) = \Theta(\log^{k+1} n)$. Here $k = 1$.
- Check by expansion. Level $i$ costs $\log(n / 3^i) = \log n - i\log 3$. There are about $\log_3 n$ levels. Adding them gives about $\frac{(\log n)^2}{2\log 3}$.
- **Answer: $T(n) = \Theta(\log^2 n)$.**

| Recurrence | $a$, $b$ | Method | Result |
|------------|----------|--------|--------|
| $2T(n/2) + n$ | 2, 2 | Master, Case 2 | $\Theta(n \log n)$ |
| $T(n-1) + 1$ | - | Expansion | $\Theta(n)$ |
| $4T(n/2) + n^2$ | 4, 2 | Master, Case 2 | $\Theta(n^2 \log n)$ |
| $T(n/3) + \log n$ | 1, 3 | Extended Case 2 | $\Theta(\log^2 n)$ |

![Recursion-level costs and tight bounds](diagrams/b2-theory-17-recurrences.svg)

---

### Q2. NP Classes, BFS, and Activity Graph

#### Q2(a)

**Question (transcribed):** Define the complexity classes NP, NP-hard, and NP-complete.

**Answer.**

Use polynomial-time reductions and measure time in the **encoded input length** (for example, integer weights written in binary).

- **P**: decision problems solvable by a deterministic algorithm in polynomial time.
- **NP**: decision problems whose yes-instances have polynomial-length certificates verifiable in polynomial time. This includes **all of P**; NP does not mean “no fast solution is known.” Example: a proposed tour certifies that a TSP instance has a tour of cost at most $k$.
- **NP-hard**: every problem in NP reduces to it in polynomial time. For decision problems, use polynomial-time many-one reductions. NP-hard problems need not be in NP, or even decidable. TSP optimization is NP-hard because an optimizer would solve its NP-complete threshold decision problem.
- **NP-complete**: both in NP and NP-hard. Examples: TSP decision, SAT, Hamiltonian cycle, subset sum decision, and deciding whether a graph has a proper $k$-colouring for fixed $k\ge3$ (or when $k$ is part of the input). **2-colouring is in P**, so “graph colouring” without a specified variant is ambiguous.

Every P problem is also in NP, because a checker can simply solve the problem itself. Whether P = NP is still an open question (see [Chapter 15](../../../Chapter%2015%20-%20Lower%20Bound%20Theory%20and%20NP%20Completeness/README.md)).

![How P, NP, NP-complete, and NP-hard relate](diagrams/b2-theory-01-np-classes-venn.svg)

#### Q2(b)

**Question (transcribed):** Explain how BFS is used to find the shortest path in an unweighted graph. Demonstrate the process with a diagram and step-by-step explanation.

**Answer.**

In an **unweighted** graph every edge counts as 1 step. BFS explores the graph in levels: first all vertices 1 edge away, then 2 edges away, and so on. The first time BFS reaches a vertex, it has found the shortest path to that vertex.

**Steps**

1. Put the source $S$ in a queue. Set $d(S) = 0$ and mark it visited.
2. While the queue is not empty:
   - Remove the front vertex $u$.
   - For each neighbour $v$ of $u$ that is **not visited**: mark $v$ visited, set $d(v) = d(u) + 1$, set `parent[v] = u`, and add $v$ to the queue.
3. To print the path to a target, follow `parent` back from the target to $S$, then reverse it.

Time: $O(V+E)$ with adjacency lists; auxiliary space: $O(V)$. With an adjacency matrix, scanning neighbours takes $O(V^2)$. If a target is unreachable, its distance stays $\infty$ and no parent path exists. (BFS is covered in [Chapter 4](../../../Chapter%204%20-%20Searching%20and%20Basic%20Traversal/README.md) and [Chapter 11](../../../Chapter%2011%20-%20Graph%20Algorithms/README.md).)

**Illustrative givens.** Undirected graph $V=\{S,A,B,C,D,E\}$ with edges S-A, S-B, A-C, B-C, B-D, C-E, D-E; source $S$, target $E$. Visit each vertex's neighbours alphabetically, marking them **when enqueued**, not when dequeued.

| Step | Pop from queue | Newly discovered (distance) | Queue after step |
|------|----------------|-----------------------------|------------------|
| 0 | - | S (0) | S |
| 1 | S | A (1), B (1) | A, B |
| 2 | A | C (2) | B, C |
| 3 | B | D (2); C is already visited | C, D |
| 4 | C | E (3) | D, E |
| 5 | D | E is already visited | E |
| 6 | E | None | Empty |

Shortest path from $S$ to $E$: follow parents $E \leftarrow C \leftarrow A \leftarrow S$, so **S-A-C-E** (3 edges). S-B-D-E is also 3 edges.

![BFS shortest path from S](diagrams/b2-theory-02-bfs-graph.svg)

#### Q2(c)

**Question (transcribed):** A student performs several activities during a day. Some activities must be completed before others can begin.

**Activities:** Wake up; Brush teeth; Take breakfast; Go to class; Study in library; Do homework; Sleep.

**Dependencies:** Wake up must be completed before brushing teeth. Brushing teeth must be completed before taking breakfast. Taking breakfast must be completed before going to class. Going to class must be completed before studying in the library. Studying in the library must be completed before doing homework. Doing homework must be completed before sleeping.

Based on the above situation answer the following questions: (i) Represent the above activities and dependencies using a directed graph. (ii) Apply topological sorting to determine a valid order of activities. (iii) Is more than one valid topological order possible? Explain briefly. (iv) What will happen if sleeping is done before completing homework?

**Answer.**

**Givens from the paper.** The activities are Wake up, Brush teeth, Take breakfast, Go to class, Study in library, Do homework, and Sleep. The paper gives the six dependencies listed below. We use them to draw the graph and answer all four parts.

**(i) Directed graph.** Each activity is a vertex. Each arrow means "must finish before":

Wake up → Brush teeth → Take breakfast → Go to class → Study in library → Do homework → Sleep

This is a **DAG** (directed acyclic graph): the arrows all point forward, so there is no cycle.

**(ii) Topological order.** A topological order lists all vertices so that every arrow goes from an earlier item to a later one. Here:

1. Wake up
2. Brush teeth
3. Take breakfast
4. Go to class
5. Study in library
6. Do homework
7. Sleep

Method: Kahn's algorithm removes vertices with no incoming arrows one by one (see [Chapter 11](../../../Chapter%2011%20-%20Graph%20Algorithms/README.md)). Only "Wake up" has no incoming arrow at first, and each removal unlocks the next.

**(iii) Is more than one order possible?** For this directed **chain**, **no**: every earlier activity must precede every later one. Equivalently, Kahn's algorithm has exactly one zero-indegree choice at every step. “At most one parent per vertex” alone would not imply uniqueness (a branching tree can have many orders). If the rules were looser (for example, brushing teeth and breakfast could happen in either order), there would be more than one valid order, such as 1 Wake up, 2 Take breakfast, 3 Brush teeth, and so on.

**(iv) What if Sleep comes before Homework?** **Replace** Study in library → Do homework → Sleep with Study in library → Sleep → Do homework. The other four edges stay unchanged. The new topological order is:

1. Wake up, 2. Brush teeth, 3. Take breakfast, 4. Go to class, 5. Study in library, 6. **Sleep**, 7. **Do homework**

The replacement graph is still a DAG. In contrast, **adding** Sleep → Do homework while retaining Do homework → Sleep creates a 2-cycle, so **no** topological order exists. Merely moving Sleep earlier in a list does not change the original constraints; the new list would violate them.

![Activity DAG and the variant with Sleep before Homework](diagrams/b2-theory-03-activity-dag.svg)

---

### Q3. Searching, Traversing, and Matrix Multiplication

#### Q3(a)

**Question (transcribed):** Explain the difference between searching and traversing by highlighting their purposes, typical operations, and examples.

**Answer.**

| | Searching | Traversing |
|--|-----------|------------|
| Purpose | Find whether an item exists, and where it is | Visit every item (or vertex) once, in a systematic order |
| Main operation | Compare the target with items, stop when found | Visit each item and do some work on it |
| Stops early? | Yes, when found | Usually no, it visits all items |
| Examples | Linear search, binary search, search in a BST or hash table | BFS, DFS, in-order traversal of a tree |

A traversal can implement a search: BFS or DFS may stop when it finds a target. For disconnected graphs, a traversal from one source visits only its reachable component; restart at unvisited vertices to cover the whole graph. The distinction is the task's objective, not an absolute restriction on which algorithm can be used.

![Searching for a target versus traversing all entries](diagrams/b2-theory-18-search-traverse.svg)

Both are covered in [Chapter 4](../../../Chapter%204%20-%20Searching%20and%20Basic%20Traversal/README.md). A simple way to remember it: searching asks "Is 511 here?", traversing asks "Show me every item."

#### Q3(b)

**Question (transcribed):** A sorted list of student IDs is [102, 205, 307, 409, 511, 613, 715, 817]. Compare linear search and binary search to find ID 511 by: (i) showing all comparisons made in each method; (ii) counting the total number of comparisons for each search; (iii) analyzing the best-, average-, and worst-case time complexities; (iv) explaining which method is more efficient for this search and why.

**Answer.**

**Givens from the paper.** The sorted array is `[102, 205, 307, 409, 511, 613, 715, 817]`, and the target is $511$. Use zero-based indices and $mid=\lfloor(lo+hi)/2\rfloor$. Count one **three-way key comparison** per inspected element (less/equal/greater); do not count loop/index tests.

**Linear search** checks items from the start:

| Step | Index | Value | Equal to 511? |
|------|-------|-------|---------------|
| 1 | 0 | 102 | No |
| 2 | 1 | 205 | No |
| 3 | 2 | 307 | No |
| 4 | 3 | 409 | No |
| 5 | 4 | 511 | **Yes, found** |

Linear search needs **5 comparisons** and finds 511 at index 4.

**Binary search** checks the middle of the remaining range (the array must be sorted):

| Step | lo | hi | mid | Value at mid | Action |
|------|----|----|-----|--------------|--------|
| 1 | 0 | 7 | 3 | 409 | $409 < 511$, so $lo = 4$ |
| 2 | 4 | 7 | 5 | 613 | $613 > 511$, so $hi = 4$ |
| 3 | 4 | 4 | 4 | 511 | **Found** |

Binary search needs **3 three-way key comparisons**, inspecting 409, 613, 511. If implemented as `if a[mid] == key` followed by `elif a[mid] < key`, it uses **5 individual key predicates** (2 + 2 + 1), versus linear search's 5 equality tests. State the cost model before comparing counts.

**Best, average, and worst cases**

| Search | Best case | Average case | Worst case |
|--------|-----------|--------------|------------|
| Linear | $\Theta(1)$: target is the first item | $\Theta(n)$: $(n+1)/2$ checks for a uniformly located successful target | $\Theta(n)$: target is last or missing |
| Binary | $\Theta(1)$: target is the middle item | $\Theta(\log n)$ | $\Theta(\log n)$ |

Average-case statements assume uniformly distributed successful target positions. For this eight-item array, the exact averages are $36/8=4.5$ probes for linear search and $21/8=2.625$ for the specified binary search; binary search's worst case is **4**, not 3, probes (target 817). For 511, the counts are 5 versus 3.

**Which is better?** Binary search uses fewer probes here and requires sorted random-access data. Its worst-case successful count is $\lfloor\log_2 n\rfloor+1$ for $n\ge1$. For one query on unsorted data, linear search avoids paying for sorting; for already-sorted data, binary search can be useful even for a single query. Both iterative searches use $O(1)$ auxiliary space.

![Linear probes and binary-search intervals for 511](diagrams/b2-theory-19-search-trace.svg)

#### Q3(c)

**Question (transcribed):** Explain Strassen's matrix multiplication algorithm. Multiply the following two 2×2 matrices using Strassen's method: A = [[1, 3], [7, 5]], B = [[6, 8], [4, 2]].

**Answer.**

Strassen's idea: split each $2 \times 2$ matrix into four blocks. Normal multiplication uses 8 block products. Strassen uses **7** products and then some extra additions. This saves time for large matrices, because the recurrence becomes $T(n) = 7T(n/2) + \Theta(n^2)$, which gives $\Theta(n^{\log_2 7}) \approx \Theta(n^{2.81})$.

For the matrices stated in the question, use the following standard Strassen formulas. Here each block is a single number: $A_{11} = 1$, $A_{12} = 3$, $A_{21} = 7$, $A_{22} = 5$, and $B_{11} = 6$, $B_{12} = 8$, $B_{21} = 4$, $B_{22} = 2$.

| Product | Formula | Value |
|---------|---------|-------|
| $P_1$ | $A_{11}(B_{12} - B_{22}) = 1 \cdot (8 - 2)$ | 6 |
| $P_2$ | $(A_{11} + A_{12}) B_{22} = (1 + 3) \cdot 2$ | 8 |
| $P_3$ | $(A_{21} + A_{22}) B_{11} = (7 + 5) \cdot 6$ | 72 |
| $P_4$ | $A_{22}(B_{21} - B_{11}) = 5 \cdot (4 - 6)$ | -10 |
| $P_5$ | $(A_{11} + A_{22})(B_{11} + B_{22}) = (1 + 5)(6 + 2)$ | 48 |
| $P_6$ | $(A_{12} - A_{22})(B_{21} + B_{22}) = (3 - 5)(4 + 2)$ | -12 |
| $P_7$ | $(A_{11} - A_{21})(B_{11} + B_{12}) = (1 - 7)(6 + 8)$ | -84 |

Combine the products:

- $C_{11} = P_5 + P_4 - P_2 + P_6 = 48 - 10 - 8 - 12 = \mathbf{18}$
- $C_{12} = P_1 + P_2 = 6 + 8 = \mathbf{14}$
- $C_{21} = P_3 + P_4 = 72 - 10 = \mathbf{62}$
- $C_{22} = P_5 + P_1 - P_3 - P_7 = 48 + 6 - 72 + 84 = \mathbf{66}$

$$C = \begin{bmatrix}18 & 14 \\ 62 & 66\end{bmatrix}$$

**Check** with normal multiplication: row 1 of $A$ times column 1 of $B$ is $1 \cdot 6 + 3 \cdot 4 = 18$. The other three entries also match.

![Strassen split and results](diagrams/b2-theory-04-strassen-split.svg)

---

### Q4. Sorting: Insertion, Bubble, Quick Sort, and Merge Sort

#### Q4(a)

**Question (transcribed):** Why is insertion sort more efficient than bubble sort for nearly sorted arrays? Justify your answer with an example.

**Answer.**

Insertion sort takes each new item and slides it left into place. On a nearly sorted array, most items are already in the right place, so each one moves only a short distance. The work is close to $n$ plus the number of out-of-order pairs. (See [Chapter 5](../../../Chapter%205%20-%20Sorting%20Algorithms/README.md).)

Bubble sort swaps neighbours in repeated passes. A small item at the **end** of the array moves only **one place left per pass**, so it needs many passes even when the rest is sorted.

**Example:** $[2, 3, 4, 5, 6, 7, \mathbf{1}]$. Only the 1 is out of place.

*Insertion sort (6 shifts)*

- Items 3, 4, 5, 6, 7 each compare once with the item before them and stop. That is 5 comparisons.
- Item 1 slides left past 7, 6, 5, 4, 3, 2. That is 6 comparisons and 6 shifts.
- Total: **11 comparisons**, **6 shifts**.

*Bubble sort (with an early-exit flag)*

| Pass | Comparisons | Swap made | Array after pass |
|------|-------------|-----------|------------------|
| 1 | 6 | (7, 1) | $[2,3,4,5,6,1,7]$ |
| 2 | 5 | (6, 1) | $[2,3,4,5,1,6,7]$ |
| 3 | 4 | (5, 1) | $[2,3,4,1,5,6,7]$ |
| 4 | 3 | (4, 1) | $[2,3,1,4,5,6,7]$ |
| 5 | 2 | (3, 1) | $[2,1,3,4,5,6,7]$ |
| 6 | 1 | (2, 1) | $[1,2,3,4,5,6,7]$ |

Total: **21 comparisons**, **6 swaps**. The early-exit flag does not help here, because a swap happens in every pass.

**Conclusion:** insertion sort does about 11 comparisons and bubble sort about 21 on the same input. Insertion sort takes $\Theta(n+I)$ time for $I$ inversions, so it is linear when $I=O(n)$. This input has $I=6$. Standard **left-to-right** bubble sort, even with shrinking pass limits and early exit, can still take $\Theta(n^2)$ time on this family of inputs. This is not a claim that every nearly sorted input makes bubble sort slow; an already sorted array takes $\Theta(n)$ with early exit. Counts here include only comparisons between array keys and exclude loop tests and the final insertion write.

![Insertion shifts versus six left-to-right bubble passes](diagrams/b2-theory-20-insertion-bubble.svg)

#### Q4(b)

**Question (transcribed):** A company stores the employee IDs [1023, 1010, 1055, 1005, 1040] in an unsorted array. The HR software needs the IDs in ascending order to generate reports efficiently. (i) Explain how quick sort can be applied to sort these IDs. (ii) Show the pivot selection and partitioning steps. (iii) Give the final sorted array.

**Answer.**

We use the **last element as the pivot** (Lomuto partition, see [Chapter 5](../../../Chapter%205%20-%20Sorting%20Algorithms/README.md)). The index $i$ marks the end of the "smaller than pivot" part.

**Pass 1:** pivot = 1040, $i = -1$

| $j$ | Value | Less than 1040? | Action | Array |
|-----|-------|-----------------|--------|-------|
| 0 | 1023 | Yes | $i = 0$, swap with itself | 1023, 1010, 1055, 1005, 1040 |
| 1 | 1010 | Yes | $i = 1$, swap with itself | 1023, 1010, 1055, 1005, 1040 |
| 2 | 1055 | No | nothing | same |
| 3 | 1005 | Yes | $i = 2$, swap $a[2]$ and $a[3]$ | 1023, 1010, 1005, 1055, 1040 |

Finally, swap the pivot with $a[i+1] = a[3]$: **1023, 1010, 1005, 1040, 1055**. The pivot 1040 is now in its final place.

- Left part: $[1023, 1010, 1005]$
- Right part: $[1055]$ (one item, already sorted)

**Pass 2 (left part):** pivot = 1005. Both 1023 and 1010 are greater than 1005, so $i$ stays at $-1$. Swap the pivot with $a[0]$: **1005, 1010, 1023**. Left part is empty. Right part is $[1010, 1023]$.

**Pass 3 (right part of pass 2):** pivot = 1023. 1010 is less than 1023, so it stays. Result: **1010, 1023**. The left side is $[1010]$ and the right side is empty. There are **7 key–pivot comparisons** over the three partitions (4 + 2 + 1).

![Quick sort partition tree](diagrams/b2-theory-05-quicksort-partition.svg)

**Final sorted array: $[1005, 1010, 1023, 1040, 1055]$**

#### Q4(c)

**Question (transcribed):** Explain the divide-and-conquer technique in algorithm design. Illustrate your answer by applying it to merge sort to sort the array [38, 27, 43, 3, 9, 82, 10], showing the divide, conquer, and combine steps.

**Answer.**

**Divide** (for an odd length, put the extra element in the **left** half):

- $[38, 27, 43, 3, 9, 82, 10]$ splits into $[38, 27, 43, 3]$ and $[9, 82, 10]$.
- $[38, 27, 43, 3]$ splits into $[38, 27]$ and $[43, 3]$, then into single items.
- $[9, 82, 10]$ splits into $[9, 82]$ and $[10]$, then $[9, 82]$ into $[9]$ and $[82]$.

**Conquer and combine** (merge two sorted lists into one sorted list):

| Merge | Left | Right | Result |
|-------|------|-------|--------|
| 1 | [38] | [27] | [27, 38] |
| 2 | [43] | [3] | [3, 43] |
| 3 | [27, 38] | [3, 43] | [3, 27, 38, 43] |
| 4 | [9] | [82] | [9, 82] |
| 5 | [9, 82] | [10] | [9, 10, 82] |
| 6 | [3, 27, 38, 43] | [9, 10, 82] | **[3, 9, 10, 27, 38, 43, 82]** |

![Merge sort divide and merge tree](diagrams/b2-theory-06-mergesort-tree.svg)

Merge sort runs in $\Theta(n \log n)$ time (see Q1(c)(i)) and needs an extra $\Theta(n)$ array for merging.

---

## Section B

### Q5. Greedy Algorithms and Minimum Spanning Tree

#### Q5(a)

**Question (transcribed):** What is a greedy algorithm? State the conditions under which a greedy approach produces an optimal solution.

**Answer.**

A **greedy algorithm** builds the answer one step at a time. At each step it takes the choice that looks best **right now**, and it never undoes a choice. It is fast and simple, but it is only correct for some problems (see [Chapter 7](../../../Chapter%207%20-%20Greedy%20Algorithms/README.md)).

Greedy gives an optimal answer when two conditions hold:

1. **Greedy choice property:** a locally best choice can always be part of some optimal solution. So making it does not rule out the best answer.
2. **Optimal substructure:** after the greedy choice, the rest of the problem is the same kind of problem. An optimal answer for the rest, combined with the choice, gives an optimal answer overall.

Proofs usually use an **exchange argument**: take any optimal solution, swap in the greedy choice, and show the answer does not get worse.

**Counterexample (greedy fails):** with unlimited coins $\{1,3,4\}$, minimize the number summing to 6. Largest-coin-first takes $4+1+1$ (3 coins), but $3+3$ uses 2. Optimal substructure alone is insufficient: the **specific selection rule** must have a proved safe greedy choice on every residual instance. Runtime also depends on the algorithm; greedy does not automatically mean constant or linear time.

![Greedy exchange argument and a coin-change counterexample](diagrams/b2-theory-21-greedy-proof.svg)

#### Q5(b)

**Question (transcribed):** A thief has a knapsack with capacity 50. He can take fractions of items. The available items have the following weights and profits: Item 1 (weight 10, profit 60), Item 2 (weight 20, profit 100), Item 3 (weight 30, profit 120). Solve the fractional knapsack problem to maximize profit. Show (i) the profit-to-weight ratio for each item; (ii) the items or fractions to include in the knapsack; (iii) the maximum total profit obtained.

**Answer.**

In the **fractional** knapsack we may take part of an item. The best rule is to take items in order of **profit per unit weight** (ratio).

| Item | Weight | Profit | Ratio $p/w$ | Rank |
|------|--------|--------|-------------|------|
| 1 | 10 | 60 | 6 | 1st |
| 2 | 20 | 100 | 5 | 2nd |
| 3 | 30 | 120 | 4 | 3rd |

Selection (capacity 50):

| Step | Take | Weight used | Profit so far |
|------|------|-------------|---------------|
| 1 | All of item 1 | 10 | 60 |
| 2 | All of item 2 | 30 | 160 |
| 3 | $\frac{20}{30}$ of item 3 (only 20 weight is left) | 50 | 160 + $\frac{2}{3}$ × 120 = **240** |

**Maximum profit: 240**, with fractions $(1,1,2/3)$. Optimality: if a solution uses lower-ratio weight while higher-ratio weight remains available, exchange equal amounts of weight; profit cannot decrease. Repeating gives the stated ratio-ordered fill. Sorting costs $O(n\log n)$ and filling costs $O(n)$. (The 0/1 optimum is 220, from items 2 and 3, so splitting helps.)

![Fractional knapsack fill by decreasing profit density](diagrams/b2-theory-22-fractional-knapsack.svg)

See [Chapter 7](../../../Chapter%207%20-%20Greedy%20Algorithms/README.md) for the proof.

#### Q5(c)

**Question (transcribed):** Define minimum spanning tree (MST). Using the given graph, find the MST by using the Kruskal algorithm and show the step-by-step process by indicating the edges selected and the total minimum cost.

**Answer.**

A **minimum spanning tree** connects every vertex, has no cycle, and has the smallest possible total edge weight. For 6 vertices, a spanning tree has 5 edges.

**Graph transcribed from the paper:** this undirected graph has $V=\{1,2,3,4,5,6\}$ and exactly these edges, listed from lowest to highest weight:

$$(5,1)=1,\ (4,1)=1,\ (1,2)=2,\ (4,2)=3,\ (3,2)=3,\ (4,3)=5,\ (2,6)=7,\ (3,6)=8,\ (5,4)=9.$$

Kruskal's algorithm takes the next lightest edge if it does not make a cycle. It skips an edge if its endpoints are already connected.

| Step | Edge | Weight | Decision | Total so far |
|------|------|--------|----------|--------------|
| 1 | (5,1) | 1 | Take | 1 |
| 2 | (4,1) | 1 | Take | 2 |
| 3 | (1,2) | 2 | Take | 4 |
| 4 | (4,2) | 3 | Skip: path 4–1–2 already connects them | 4 |
| 5 | (3,2) | 3 | Take | 7 |
| 6 | (4,3) | 5 | Skip: path 4–1–2–3 already connects them | 7 |
| 7 | (2,6) | 7 | Take; we now have 5 edges, so stop | **14** |

**MST edges:** $(5,1),(4,1),(1,2),(3,2),(2,6)$.
**Minimum cost:** $1+1+2+3+7=14$.

The MST is unique: the five selected edges are the only set of five edges that connects all six vertices without a cycle at this minimum total weight. The diagram highlights these edges from the paper's graph.

![Kruskal MST on the graph shown in the paper](diagrams/b2-theory-07-kruskal-mst.svg)

#### Q6(a)

**Question (transcribed):** Define dynamic programming. Discuss overlapping subproblems using Fibonacci.

**Answer.**

**Dynamic programming (DP)** solves a problem by splitting it into smaller subproblems, solving each one **once**, storing the answer, and reusing it. DP works when:

1. **Overlapping subproblems:** the same smaller problem appears many times.
2. **Optimal substructure:** the best answer uses best answers to subproblems (see [Chapter 8](../../../Chapter%208%20-%20Dynamic%20Programming/README.md)).

**Fibonacci:** $F(0)=0$, $F(1)=1$, and $F(n)=F(n-1)+F(n-2)$ for $n\ge2$. Naive recursion stops immediately at 0 or 1. For this counting problem, DP uses a reusable recurrence; it need not be an optimization problem with a “best” answer.

The naive recursion for $F(5)$ calls:

- $F(3)$ **twice**
- $F(2)$ **three times**
- $F(1)$ five times and $F(0)$ three times
- $F(5)$ and $F(4)$ once each

In total, $F(5)$ makes **15** calls, and the number grows exponentially with $n$. Those repeated calls are the **overlapping subproblems**.

With DP, each $F(i)$ is computed once and stored:

```
if n == 0: return 0
F[0] = 0, F[1] = 1
for i = 2 to n:
    F[i] = F[i-1] + F[i-2]
return F[n]
```

The table for $F(5)$ is $[0,1,1,2,3,5]$. With unit-cost arithmetic, tabulation takes $\Theta(n)$ time and $\Theta(n)$ auxiliary words. Keeping just the previous two values reduces auxiliary storage to $\Theta(1)$ words. Exact $F(n)$ has $\Theta(n)$ bits, so arbitrary-precision arithmetic is not constant-cost: straightforward addition gives $\Theta(n^2)$ bit operations and two-value storage still uses $\Theta(n)$ bits.

![Repeated Fibonacci calls versus one stored value per state](diagrams/b2-theory-23-fibonacci-dp.svg)

#### Q6(b)

**Question (transcribed):** Explain how the Floyd-Warshall algorithm computes all-pairs shortest paths in a weighted graph. Using the adjacency matrix [[0, 5, ∞, 10], [∞, 0, 3, ∞], [∞, ∞, 0, 1], [∞, ∞, ∞, 0]], perform the algorithm step by step, updating the distance matrix for each intermediate vertex. Show all intermediate matrices in sequence and present the final shortest-path matrix with explanations.

**Answer.**

**Givens:** directed graph on vertices 1–4, with exactly the four weighted edges listed below; $\infty$ means no direct edge, and diagonal zero represents a length-zero path. Process intermediate vertices in order 1, 2, 3, 4. There are no negative cycles.

Floyd-Warshall finds the shortest distance between **every pair** of vertices. Let $D_k(i,j)$ be the shortest distance from $i$ to $j$ using only vertices $1..k$ as middle vertices. Then:

$$D_k(i,j) = \min\big(D_{k-1}(i,j),\; D_{k-1}(i,k) + D_{k-1}(k,j)\big)$$

So for each middle vertex $k$, we check whether going through $k$ is shorter (see [Chapter 11](../../../Chapter%2011%20-%20Graph%20Algorithms/README.md)). The graph has edges $1\to2$ (5), $1\to4$ (10), $2\to3$ (3), and $3\to4$ (1).

**$D_0$ (direct edges only)**

| | 1 | 2 | 3 | 4 |
|--|---|---|---|---|
| 1 | 0 | 5 | ∞ | 10 |
| 2 | ∞ | 0 | 3 | ∞ |
| 3 | ∞ | ∞ | 0 | 1 |
| 4 | ∞ | ∞ | ∞ | 0 |

**$k = 1$:** no edge comes into vertex 1, so nothing changes. $D_1 = D_0$.

**$k = 2$:** check $i \to 2 \to j$.

- $d(1,3)$: $\min(\infty, 5 + 3) = 8$. **Changed.**
- $d(4,\cdot)$ and others: no changes.

| | 1 | 2 | 3 | 4 |
|--|---|---|---|---|
| 1 | 0 | 5 | **8** | 10 |
| 2 | ∞ | 0 | 3 | ∞ |
| 3 | ∞ | ∞ | 0 | 1 |
| 4 | ∞ | ∞ | ∞ | 0 |

**$k = 3$:** check $i \to 3 \to j$.

- $d(1,4)$: $\min(10, 8 + 1) = 9$. **Changed.**
- $d(2,4)$: $\min(\infty, 3 + 1) = 4$. **Changed.**

| | 1 | 2 | 3 | 4 |
|--|---|---|---|---|
| 1 | 0 | 5 | 8 | **9** |
| 2 | ∞ | 0 | 3 | **4** |
| 3 | ∞ | ∞ | 0 | 1 |
| 4 | ∞ | ∞ | ∞ | 0 |

**$k = 4$:** no edge leaves vertex 4, so nothing changes. $D_4 = D_3$.

**Final matrix $D_4$:**

| | 1 | 2 | 3 | 4 |
|--|---|---|---|---|
| 1 | 0 | 5 | 8 | 9 |
| 2 | ∞ | 0 | 3 | 4 |
| 3 | ∞ | ∞ | 0 | 1 |
| 4 | ∞ | ∞ | ∞ | 0 |

![Floyd-Warshall graph and matrix changes](diagrams/b2-theory-08-floyd-warshall.svg)

The time is $\Theta(n^3)$ and the distance matrix takes $\Theta(n^2)$ space; in-place updates suffice. The shortest 1→4 path is **1→2→3→4**, cost 9. In general negative edges are allowed, but a negative diagonal after the algorithm signals a negative cycle, so some pairs have no finite shortest-path value.

#### Q6(c)

**Question (transcribed):** Explain how dynamic programming is used to compute the longest common subsequence (LCS) of two strings. For X = AGGTAB and Y = GXTXAYB, build the full DP table row by row. After completing the table, demonstrate how to trace back through it to find the final LCS, and clearly state both the LCS and its length.

**Answer.**

Rule (let $L[i][j]$ be the LCS length of the first $i$ letters of $X$ and the first $j$ letters of $Y$):

- Initialize $L[0][j]=L[i][0]=0$ (an empty string has LCS length zero).
- If $X_i = Y_j$: $L[i][j] = L[i-1][j-1] + 1$.
- Otherwise: $L[i][j] = \max(L[i-1][j],\ L[i][j-1])$.

**DP table** (row = letter of $X$, column = letter of $Y$):

| | | G | X | T | X | A | Y | B |
|--|---|---|---|---|---|---|---|---|
| | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | 0 | 0 | 0 | 0 | 0 | **1** | 1 | 1 |
| G | 0 | **1** | 1 | 1 | 1 | 1 | 1 | 1 |
| G | 0 | **1** | 1 | 1 | 1 | 1 | 1 | 1 |
| T | 0 | 1 | 1 | **2** | 2 | 2 | 2 | 2 |
| A | 0 | 1 | 1 | 2 | 2 | **3** | 3 | 3 |
| B | 0 | 1 | 1 | 2 | 2 | 3 | 3 | **4** |

(Bold cells are where letters match and the diagonal rule was used.)

**Traceback** (start at the bottom-right cell and move back):

1. $(6,7)$: $B = B$. Take **B**, move diagonally to $(5,6)$.
2. $(5,6)$: $A \ne Y$. Value above is 2, value to the left is 3. Move left to $(5,5)$.
3. $(5,5)$: $A = A$. Take **A**, move diagonally to $(4,4)$.
4. $(4,4)$: $T \ne X$. Move left to $(4,3)$ (value 2).
5. $(4,3)$: $T = T$. Take **T**, move diagonally to $(3,2)$.
6. $(3,2)$: $G \ne X$. Move up to $(2,2)$.
7. $(2,2)$: $G \ne X$. Move left to $(2,1)$.
8. $(2,1)$: $G = G$. Take **G**, move diagonally to $(1,0)$. Stop.

Reading the taken letters backwards gives **G, T, A, B**.

**LCS = GTAB, length = 4.** The move at $(3,2)$ is a tie; choose up to reproduce this traceback. Other valid tie choices can produce a different embedding of the same subsequence. Filling the table costs $\Theta(|X||Y|)$ time and space; traceback costs $O(|X|+|Y|)$.

![LCS table with traceback](diagrams/b2-theory-09-lcs-table.svg)

---

### Q7. Backtracking: Graph Colouring, LC-Search, and N-Queens

#### Q7(a)

**Question (transcribed):** Apply backtracking to graph colouring for a graph of 5 vertices. Show the order of colour assignment and the backtracking steps.

**Answer.**

> [!NOTE]
> **Worked example:** the paper gives no particular graph or number of colours. For a clear example, use the five-vertex graph below and three colours (Red = 1, Green = 2, Blue = 3).

**Sample graph:** edges 1-2, 1-3, 2-3, 3-4, 4-5, 3-5, 2-5.

**Method:** the sample graph is simple and undirected, with exactly the seven listed edges. Initialize all colours to `none`; colour vertices in order 1, 2, 3, 4, 5, trying Red, Green, Blue in that order. For each vertex, try each colour that differs from the colours of already-coloured neighbours. If no colour works, **backtrack** to the previous vertex and try its next colour (see [Chapter 9](../../../Chapter%209%20-%20Backtracking/README.md)).

```
colour_vertex(v):
    if v > n: return true              (all vertices coloured)
    for c in 1..3:
        if every already-coloured neighbour has a colour different from c:
            colours[v] = c
            if colour_vertex(v + 1): return true
            colours[v] = none          (undo before trying another colour)
    return false
```

**Trace**

| Step | Vertex | Colour tried | Why | Result |
|------|--------|--------------|-----|--------|
| 1 | v1 | Red | First colour | Coloured |
| 2 | v2 | Green | Red is used by neighbour v1 | Coloured |
| 3 | v3 | Blue | Red (v1) and Green (v2) are used | Coloured |
| 4 | v4 | Red | Only already-coloured neighbour is v3 (Blue) | Coloured |
| 5 | v5 | none | Neighbours v2 (Green), v3 (Blue), v4 (Red) use all 3 colours | **Dead end** |
| 6 | v4 | Green | Backtrack: next colour for v4 | Coloured |
| 7 | v5 | Red | Neighbours v2 (Green), v3 (Blue), v4 (Green) | **Solution** |

**Final colouring:** v1 Red, v2 Green, v3 Blue, v4 Green, v5 Red. Every listed edge has differently coloured endpoints. The triangle 1–2–3 requires at least three colours, and the displayed 3-colouring proves the chromatic number is **3**. The search may examine $O(m^n)$ assignments for $m$ colours ($O(nm^n)$ time if each safety check scans all vertices), with $O(n)$ search storage excluding the graph.

![Graph colouring backtracking tree](diagrams/b2-theory-10-colouring-tree.svg)

#### Q7(b)

**Question (transcribed):** Demonstrate LC-search on a 0/1 knapsack instance with at least four items. Draw the state-space tree.

**Answer.**

> [!NOTE]
> **Reconstructed example:** the original items are unavailable. The four items below specify the worked problem completely; their profits and weights are not authenticated exam givens.

**Instance:** capacity $W = 10$. Items (weight, profit): **A** (4, 40), **C** (3, 18), **B** (6, 30), **D** (5, 20). Sorted by profit per weight: A (10), C (6), B (5), D (4).

**LC-search** (least cost) uses a min-priority queue; for this maximization problem assign cost $-ub$, equivalently expand the **largest upper bound first**. This is best-first branch and bound, not ordinary depth-first backtracking. Live nodes wait in a priority queue. The node with the **best upper bound** is expanded next. Each node has a bound $ub$:

$$ub = \text{profit so far} + \text{best fractional fill of the remaining items}$$

A node is **pruned** if overweight or if $ub$ is no larger than the incumbent feasible profit. Equality pruning is sufficient to find **one** optimum, but may discard alternative optimal solutions.

**Deterministic policy:** generate include then exclude children; break equal-$ub$ queue ties by **earlier insertion** (FIFO). Initialize the incumbent to the empty selection (profit 0). Whenever a feasible partial node is generated, complete it by skipping all undecided items to update the incumbent. Thus profits 40 and 58 are incumbents before 70. A pruned node is never expanded; omitted D decisions are unnecessary once bounded.

**Expansion**

| Node | Decisions | Weight | Profit | $ub$ | Status |
|------|-----------|--------|--------|------|--------|
| Root | none | 0 | 0 | 73 | Expand first |
| A=1 | take A | 4 | 40 | 73 | Expand |
| A=0 | skip A | 0 | 0 | 52 | Pruned later (52 ≤ 70) |
| A=1, C=1 | take A, C | 7 | 58 | 73 | Expand |
| A=1, C=0 | take A, skip C | 4 | 40 | 70 | Expand before the later-inserted equal-bound node |
| A=1, C=1, B=1 | take A, C, B | 13 | 88 | — | **Infeasible** (13 > 10) |
| A=1, C=1, B=0 | take A, C | 7 | 58 | 70 | Pruned (70 ≤ 70) |
| A=1, C=0, B=1 | take A, B | 10 | 70 | 70 | **Solution: best = 70** |
| A=1, C=0, B=0 | take A | 4 | 40 | 60 | Pruned (60 ≤ 70) |

**Bound arithmetic:** root and A=1: $40+18+(3/6)30=73$; A=0: $18+30+(1/5)20=52$; A=1,C=1: $58+(3/6)30=73$; A=1,C=0: $40+30=70$; A=1,C=1,B=0: $58+(3/5)20=70$; A=1,C=0,B=0: $40+20=60$.

**Actual pop/expansion order:** root → A=1 → A=1,C=1 → A=1,C=0. At the last expansion, generating B=1 yields the complete feasible choice A+B (D=0), profit 70. The equal-bound node A=1,C=1,B=0 was enqueued **after** A=1,C=0, so FIFO ties make the stated sequence valid. Remaining live bounds are at most 70; none is expanded. The table lists generated nodes, not nine successive expansions.

**Answer:** take **A and B**. Profit = 70, weight = 10. (Checking all subsets confirms that no other set gives more profit within capacity 10.)

![LC-search state-space tree](diagrams/b2-theory-11-lc-knapsack-tree.svg)

#### Q7(c)

**Question (transcribed):** Solve the N-Queens problem for N = 5 using backtracking. Show partial board configurations and backtracking steps.

**Answer.**

Place one queen in each row. Two queens attack each other if they share a **column** or a **diagonal** ($|r_i-r_j|=|c_i-c_j|$, covering both diagonal directions). If a row has no safe column, go back to the previous row and move its queen (see [Chapter 9](../../../Chapter%209%20-%20Backtracking/README.md)).

**Trace for the first solution:** process rows 1–5 and try columns 1–5 in ascending order; reject a column if it conflicts with any earlier queen. Represent a partial board by its queen-column vector.

| Row | Columns tried | Result | Partial board (queen columns so far) |
|-----|---------------|--------|--------------------------------------|
| 1 | 1 | Safe, placed | [1] |
| 2 | 1 (same column), 2 (diagonal with (1,1)), 3 | Safe at column 3 | [1, 3] |
| 3 | 1 (column), 2 (diagonal with (2,3)), 3 (column), 4 (diagonal with (2,3)), 5 | Safe at column 5 | [1, 3, 5] |
| 4 | 1 (column), 2 | Safe at column 2 | [1, 3, 5, 2] |
| 5 | 1, 2, 3 (columns), 4 | Safe at column 4 | [1, 3, 5, 2, 4] ✓ |

**A later dead end (when enumerating all solutions).** Continue after the first two solutions under row 1 = column 1, undoing queens before each next trial. Eventually row 2 reaches column 5, giving [1, 5]:

- Row 3: only column 2 is safe, so the board is [1, 5, 2].
- Row 4: column 3 is on a diagonal with (3,2), and column 4 is on a diagonal with (1,1). **No safe column.** Row 3 has no other option, and row 2 has no columns left to try (columns 3 and 4 were already explored and gave solutions). So the search goes back to row 1 and tries column 2.

**Final board for the first solution [1, 3, 5, 2, 4]**

```
Q . . . .
. . Q . .
. . . . Q
. Q . . .
. . . Q .
```

Continuing enumeration finds **10 distinct boards** for $N=5$, counting rotations and reflections separately (**2** symmetry classes). The second ascending-column solution is [1, 4, 2, 5, 3]. A solver that stops at the first solution does not reach the later dead end or enumerate all ten. At most $O(N!)$ partial placements survive column uniqueness. Trying all $N$ columns and scanning up to $N$ earlier queens per placement gives a conservative $O(N^2 N!)$ time upper bound for a straightforward implementation, with $O(N)$ auxiliary storage.

![N-Queens backtracking tree and final board](diagrams/b2-theory-12-nqueens-tree.svg)

---

### Q8. Decision vs Optimization, Branch and Bound, and TSP

#### Q8(a)

**Question (transcribed):** Differentiate between decision problem and optimization problem in computational complexity.

**Answer.**

| | Decision problem | Optimization problem |
|--|------------------|----------------------|
| Question | Is there a solution with a property? Answer yes or no. | What is the best value (minimum or maximum)? |
| Example (0/1 knapsack) | Is there a subset with weight at most $W$ and profit at least $P$? | Among subsets of weight at most $W$, what is the maximum profit? |
| Example (TSP) | Is there a tour with cost at most $k$? | What is the cheapest tour? |
| Output | Yes or no | A value and a solution |

For problems such as TSP and knapsack, an exact optimizer answers a threshold decision query by comparing its optimum with $k$ or $P$ (handling infeasibility separately). Conversely, a threshold-decision oracle plus **known integer objective bounds** permits binary search for the optimum value in logarithmically many queries in the numeric range. For example, nonnegative integer TSP costs bounded by $M$ give a tour-cost range $[0,nM]$. This alone returns a **value**, not a tour; recovering a witness requires additional self-reduction queries. Such a reduction is not automatic for every optimization problem or arbitrary real-valued objective.

P and NP are classes of decision problems; standard TSP decision is NP-complete, while TSP optimization is NP-hard (see [Chapter 15](../../../Chapter%2015%20-%20Lower%20Bound%20Theory%20and%20NP%20Completeness/README.md)).

![Threshold decision versus finding an optimum and witness](diagrams/b2-theory-24-decision-optimization.svg)

#### Q8(b)

**Question (transcribed):** Explain admissible heuristic and bounding function in branch-and-bound. Solve a branch-and-bound job sequencing problem.

**Answer.**

**Branch and bound (B&B)** explores the state-space tree like backtracking. It also uses a **bounding function** to skip branches that cannot give a better answer than the best one found so far (see [Chapter 10](../../../Chapter%2010%20-%20Branch%20and%20Bound/README.md)).

- **Bounding function:** gives a guaranteed **upper bound** on the best feasible descendant profit for maximization, or a **lower bound** on descendant cost for minimization. It need not equal the achievable optimum; a relaxation can be deliberately optimistic.
- **Admissible heuristic:** an optimistic remaining-cost estimate. In a minimization formulation, $h(node)$ never overestimates the best remaining cost, so $g+h$ is a lower bound. In maximization, use an upper bound that never underestimates the best achievable profit. Prune when $ub\le incumbent$ (maximize), or $lb\ge incumbent$ (minimize). Equality pruning may remove tied optima, but cannot remove all optima before an equally good feasible incumbent exists.

**Job sequencing with deadlines (maximize profit).** One machine, all jobs available at time 0, positive integer deadlines, positive profits, one unit per job, no preemption. Slot $t$ runs from time $t-1$ to $t$; a job selected for profit must finish by its deadline. A selected set is feasible iff, for each integer $t\ge1$, at most $t$ selected jobs have deadline $\le t$. To test feasibility, sort the selected jobs by deadline and check the $i$th deadline is at least $i$.

> [!NOTE]
> **Worked example:** the paper asks for a job-sequencing example but gives no job list. The following four jobs are an example chosen to demonstrate the method.

**Instance:** J1 (profit 100, deadline 2), J4 (profit 27, deadline 1), J3 (profit 15, deadline 2), J2 (profit 10, deadline 1). Jobs are considered in order of profit.

**Bound:** $ub$ = selected profit + sum of profits of all undecided jobs. With these nonnegative profits it is admissible, since it relaxes all remaining deadline constraints. Use **depth-first B&B**, include child before exclude child, and start with incumbent 0. For the trace below, update the incumbent **only at complete feasible leaves**; if instead updated at every feasible partial selection, profit 127 would be known earlier and several later branches could already be pruned.

| Node | Decision | Profit | $ub$ | Status |
|------|----------|--------|------|--------|
| Root | none | 0 | 152 | Branch |
| J1 = 1 | take J1 | 100 | 152 | Branch |
| J1 = 1, J4 = 1 | take J1, J4 | 127 | 152 | Branch (feasible: J4 in slot 1, J1 in slot 2) |
| J1=1, J4=1, J3=1 | take J3 too | — | — | **Infeasible**: 3 jobs with deadline ≤ 2 |
| J1=1, J4=1, J3=0 | skip J3 | 127 | 137 | Branch |
| J1=1, J4=1, J3=0, J2=1 | take J2 too | — | — | **Infeasible**: 2 jobs with deadline ≤ 1 |
| J1=1, J4=1, J3=0, J2=0 | leaf | 127 | 127 | **Best = 127** |
| J1 = 1, J4 = 0 | skip J4 | 100 | 125 | **Pruned** (125 ≤ 127) |
| J1 = 0 | skip J1 | 0 | 52 | **Pruned** (52 ≤ 127) |

**Answer:** take **J1 and J4**. Maximum profit = **127**. Schedule: J4 in slot 1 and J1 in slot 2. The displayed bounds are $152=100+27+15+10$, $137=127+10$, $125=100+15+10$, and $52=27+15+10$. The two unvisited sibling subtrees have bounds 125 and 52, both below 127; together with the infeasible include branches, this proves optimality. This is an exponential worst-case search, not a claim that job sequencing requires B&B; this unit-time variant also admits an efficient profit-ordered greedy algorithm.

![Branch and bound tree for job sequencing](diagrams/b2-theory-13-bnb-job-tree.svg)

#### Q8(c)

**Question (transcribed):** Explain how the dynamic-programming method is used to solve the traveling salesperson problem. Using the cost matrix [[0, 20, 42, 35], [20, 0, 30, 34], [42, 30, 0, 12], [35, 34, 12, 0]] with start city 0, evaluate all relevant subsets of intermediate cities of size 1 and 2, show the partial DP table computed from these subsets, and determine the minimum tour cost based on these computed values.

**Answer.**

The travelling salesperson problem asks for the cheapest tour that visits every city once and returns to the start. Let $g(i,S)$ be the minimum cost to start at city $i$, visit every city in set $S$, then return to city 0.

$$g(i,S)=\min_{j\in S}\big(c_{ij}+g(j,S\setminus\{j\})\big),\qquad g(i,\varnothing)=c_{i0}.$$

The cost matrix in the question is for cities 0, 1, 2, and 3:

| From/to | 0 | 1 | 2 | 3 |
|---------|---|---|---|---|
| 0 | 0 | 20 | 42 | 35 |
| 1 | 20 | 0 | 30 | 34 |
| 2 | 42 | 30 | 0 | 12 |
| 3 | 35 | 34 | 12 | 0 |

The base values are:

- $g(1,\varnothing)=c_{10}=20$
- $g(2,\varnothing)=c_{20}=42$
- $g(3,\varnothing)=c_{30}=35$

**Subsets of size 1**

| State | Calculation | Value |
|-------|-------------|-------|
| $g(1,\{2\})$ | $30+42$ | 72 |
| $g(1,\{3\})$ | $34+35$ | 69 |
| $g(2,\{1\})$ | $30+20$ | 50 |
| $g(2,\{3\})$ | $12+35$ | 47 |
| $g(3,\{1\})$ | $34+20$ | 54 |
| $g(3,\{2\})$ | $12+42$ | 54 |

**Subsets of size 2**

| State | Calculation | Value |
|-------|-------------|-------|
| $g(1,\{2,3\})$ | $\min(30+47,\ 34+54)$ | **77** |
| $g(2,\{1,3\})$ | $\min(30+69,\ 12+54)$ | **66** |
| $g(3,\{1,2\})$ | $\min(34+72,\ 12+50)$ | **62** |

Now choose the first city after 0:

$$g(0,\{1,2,3\})=\min(20+77,\ 42+66,\ 35+62)=\min(97,108,97)=97.$$

**Minimum tour cost: 97.** One optimal tour is $0\to1\to2\to3\to0$; its cost is $20+30+12+35=97$. The reverse tour $0\to3\to2\to1\to0$ also costs 97. The six tours, in lexicographic order of the intermediate cities, cost **97, 108, 141, 108, 141, 97**. The subset DP takes $O(n^2 2^n)$ time and $O(n2^n)$ space.

![Held-Karp DP states for the source matrix, starting at city 0](diagrams/b2-theory-14-tsp-subsets.svg)

---

## Verification

Run `python tools/verify_b2_theory.py` from the repository root to check the numerical tables, search traces and bounds, exhaustive small-instance optima, local links, all 24 question diagrams, and all 25 SVG/Excalidraw pairs (including the roadmap). These read-only checks supplement the review; they do not prove every prose statement.

## Quick Revision

| Topic | One-line memory |
|-------|-----------------|
| Time vs space | Time counts operations; total space includes input, auxiliary space excludes input but includes the stack |
| Master theorem | Compare with $n^{\log_b a}$; Cases 1/3 need a polynomial gap, Case 3 also needs regularity |
| $T(n/3) + \log n$ | $\Theta(\log^2 n)$ (extended Case 2) |
| P, NP, NP-hard, NP-complete | P = solve fast; NP = verify fast; NP-complete = NP and NP-hard |
| BFS shortest path | Level by level with a queue; first visit = shortest distance (unweighted) |
| Topological order | Every arrow goes forward; remove vertices with no incoming arrows |
| Linear vs binary search | 5 vs 3 three-way probes for 511; binary needs sorted random access; eight-item worst case is 4 |
| Strassen | 7 block products instead of 8; $T(n) = 7T(n/2) + \Theta(n^2)$ |
| Insertion vs bubble | Insertion takes $\Theta(n+I)$ for $I$ inversions; left-to-right bubble can still be quadratic |
| Quick sort | Partition around the pivot; last-element pivot gives $[1005, 1010, 1023, 1040, 1055]$ |
| Merge sort | Split in half, merge sorted halves, $\Theta(n \log n)$, needs extra space |
| Greedy | Best local choice; needs greedy choice + optimal substructure |
| Fractional knapsack | Sort by profit/weight; take a fraction of the last item; profit 240 |
| Kruskal | Sort edges, skip cycles, stop at $V - 1$ edges; total 14 (confirm weights) |
| DP | Overlapping subproblems + optimal substructure; Fibonacci in $O(n)$ |
| Floyd-Warshall | Try each vertex as a middle vertex; $O(n^3)$; $d(1,4) = 9$ |
| LCS | Match: diagonal + 1; else max(up, left); LCS = GTAB, length 4 |
| Graph colouring | Colour in order, check neighbours, backtrack on dead end |
| LC-search | Expand the node with the best bound first; prune when $ub \le$ best |
| N-Queens | Row by row; check column and diagonals; 10 solutions for $N = 5$ |
| Decision vs optimization | Yes/no question vs find the best value |
| Branch and bound | Bounding function prunes; admissible = never too pessimistic |
| TSP DP | $g(i,S) = \min_j [c_{ij} + g(j, S \setminus j)]$; minimum tour 97 |

---

[Previous: 1st Batch Theory](../../1st%20Batch/Theory/README.md) | [Chapter 0 - Previous Year Questions](../../README.md) | [Home](../../../README.md) | [Next: 2nd Batch Lab Final](../Lab%20Final/README.md)
