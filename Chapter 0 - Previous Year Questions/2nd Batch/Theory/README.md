# 2nd Batch Theory: Answers

[Previous: 1st Batch Theory](../../1st%20Batch/Theory/README.md) | [Chapter 0 - Previous Year Questions](../../README.md) | [Home](../../../README.md) | [Next: 2nd Batch Lab Final](../Lab%20Final/README.md)

This guide answers all 24 subquestions in the supplied CSE 2201 final-examination paper for 2024. The paper says to answer any 3 questions from each section. Question wording, year, marks, and printed data were checked against the supplied scan; line breaks are normalized.

> [!IMPORTANT]
> **Source:** the supplied scan identifies the paper as the 2024 CSE 2201 final examination. Question wording and all printed numerical data were checked against it. Q7(a), Q7(b), and Q8(b) do not give specific graph, item, or job data, so their worked examples are clearly labeled as examples chosen for the answers.

Every subquestion includes a relevant SVG preview with an editable Excalidraw source in the [diagram index](diagrams/README.md).

Recurrence, search/traversal, greedy, dynamic programming, and graph answers use the tables, notation, and step order taught in [Chapter 3](../../../Chapter%203%20-%20Recurrences%20Correctness%20and%20Loop%20Invariants/README.md), [Chapter 4](../../../Chapter%204%20-%20Searching%20and%20Basic%20Traversal/README.md), [Chapter 7](../../../Chapter%207%20-%20Greedy%20Algorithms/README.md), [Chapter 8](../../../Chapter%208%20-%20Dynamic%20Programming/README.md), and [Chapter 11](../../../Chapter%2011%20-%20Graph%20Algorithms/README.md): the watershed function $n^{\log_b a}$, the queue trace table, $c[i,j]$ with arrows for LCS, $D^{(k)}$ matrices for Floyd-Warshall, $g(i,S)$ for TSP, and `FIND`/`UNION` for Kruskal. The questions say *profit*; the chapters say *value*.

**Language:** Answers use the simplest words possible and show the working. Course terms are kept and explained in simple words. Each answer ends with a short **memory trick**. Answer length follows the marks: about 5 lines for 5 marks, half a page for 10 marks, and a full page for 15 or more marks.

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

## Table of Contents

- [Visual Map: Full-Paper Topic Roadmap](#visual-map-full-paper-topic-roadmap)
- [Section A](#section-a)
  - [Q1. Algorithm Design, Complexity, and Asymptotic Bounds](#q1-algorithm-design-complexity-and-asymptotic-bounds)
  - [Q2. NP Classes, BFS, and Activity Graph](#q2-np-classes-bfs-and-activity-graph)
  - [Q3. Searching, Traversing, and Matrix Multiplication](#q3-searching-traversing-and-matrix-multiplication)
  - [Q4. Sorting: Insertion, Bubble, Quick Sort, and Merge Sort](#q4-sorting-insertion-bubble-quick-sort-and-merge-sort)
- [Section B](#section-b)
  - [Q5. Greedy Algorithms and Minimum Spanning Tree](#q5-greedy-algorithms-and-minimum-spanning-tree)
  - [Q6. Dynamic Programming, Floyd-Warshall, and LCS](#q6-dynamic-programming-floyd-warshall-and-lcs)
  - [Q7. Backtracking: Graph Colouring, LC-Search, and N-Queens](#q7-backtracking-graph-colouring-lc-search-and-n-queens)
  - [Q8. Decision vs Optimization, Branch and Bound, and TSP](#q8-decision-vs-optimization-branch-and-bound-and-tsp)
- [Verification](#verification)
- [Quick Revision](#quick-revision)

---

## Section A

### Q1. Algorithm Design, Complexity, and Asymptotic Bounds

#### Q1(a)

**Question (transcribed):** Define time complexity and space complexity. Provide examples demonstrating when space complexity becomes a critical factor in algorithm design.

**Answer.**

- **Time complexity**: how the **number of steps** grows as the input size `n` grows. Example: one loop over `n` items is Θ(n).
- **Space complexity**: how the **memory used** grows as `n` grows. It includes the input, extra arrays, and the recursion stack. The *extra* memory only is called **auxiliary space**.

**When space becomes critical**

1. **Very big data.** There is no room for a second copy. Merge sort needs O(n) extra space, but heap sort needs only O(1). So heap sort is better when memory is tight.
2. **Small devices** such as phones, sensors, and embedded systems have very little memory.
3. **Deep recursion** can overflow the stack.
4. **Large DP tables.** The LCS table of two strings of length 10⁵ needs 10¹⁰ cells, so we keep only the last row.

> Memory trick: Time = how many steps. Space = how much memory.

![Time, total space, and auxiliary space](diagrams/b2-theory-15-time-space.svg)

#### Q1(b)

**Question (transcribed):** Define algorithm design paradigm. Briefly describe divide-and-conquer and greedy paradigms with suitable examples.

**Answer.**

An **algorithm design paradigm** is a *general strategy* (a ready-made plan) for designing algorithms. Examples: divide and conquer, greedy, dynamic programming, backtracking, branch and bound.

**Divide and conquer (D&C)**

1. **Divide** the problem into smaller parts.
2. **Conquer**: solve each part recursively. A tiny part is solved directly (**base case**).
3. **Combine** the part answers into the final answer.

Example: **merge sort**. Split the array, sort both halves, merge them. Time Θ(n log n). Quick sort is another example.

**Greedy**

A greedy algorithm builds the answer step by step. It always picks the choice that looks **best right now** and **never changes it later**.

Example: **activity selection**. Always pick the compatible activity that finishes first. Other examples: Kruskal's MST, fractional knapsack.

| | Divide and conquer | Greedy |
|--|--------------------|--------|
| Idea | Split, solve, combine | Pick the best choice now |
| Recursion | Usually yes | Usually no |
| Never changes choice? | Not applicable | Yes |
| Example | Merge sort | Activity selection |

> Memory trick: D&C = split and merge. Greedy = grab the best now.

![Divide-and-conquer and greedy design patterns](diagrams/b2-theory-16-design-paradigms.svg)

#### Q1(c)

**Question (transcribed):** Evaluate asymptotic bounds for: (i) T(n) = 2T(n/2) + n; (ii) T(n) = T(n - 1) + 1; (iii) T(n) = 4T(n/2) + n^2; (iv) T(n) = T(n/3) + log n.

**Answer.**

Assume $T(n)=\Theta(1)$ for $n\le1$.

The **Master Theorem** solves $T(n)=aT(n/b)+f(n)$, where $a\ge1$ and $b>1$ are constants. Here $a$ is the number of subproblems, $n/b$ is the size of each, and $f(n)$ is the divide-and-combine cost. It compares $f(n)$ with the **watershed function** $n^{\log_b a}$ (see [Chapter 3](../../../Chapter%203%20-%20Recurrences%20Correctness%20and%20Loop%20Invariants/README.md)):

| Case | Condition on $f(n)$ | Result |
| :---: | :--- | :--- |
| 1 | $f(n)=O(n^{\log_b a-\epsilon})$ for some $\epsilon>0$ ($f(n)$ grows polynomially **slower**) | $T(n)=\Theta(n^{\log_b a})$ |
| 2 | $f(n)=\Theta(n^{\log_b a}\log^k n)$ for some $k\ge0$ (**same** rate) | $T(n)=\Theta(n^{\log_b a}\log^{k+1}n)$ |
| 3 | $f(n)=\Omega(n^{\log_b a+\epsilon})$ for some $\epsilon>0$, and $a\,f(n/b)\le c\,f(n)$ for some $c<1$ (polynomially **faster**) | $T(n)=\Theta(f(n))$ |

**(i) $T(n) = 2T(n/2) + n$**

Here $a=2$, $b=2$, $f(n)=n$.

$$
n^{\log_b a}=n^{\log_2 2}=n
$$

$f(n)=n=\Theta(n^1\log^0 n)$ matches the watershed function with $k=0$. This is **Case 2**, so $T(n)=\Theta(n\log n)$.

Check with a recursion tree: each of the $\log_2 n$ levels does $n$ work.

**(ii) $T(n) = T(n-1) + 1$**

This does not divide the input by a constant $b>1$, so the Master Theorem does not apply. Use expansion:

$$
T(n)=T(n-1)+1=T(n-2)+2=T(n-3)+3
$$

After $k$ expansions, $T(n)=T(n-k)+k$. The recursion stops when $n-k=1$, so $k=n-1$:

$$
T(n)=T(1)+(n-1)=\Theta(n)
$$

**(iii) $T(n) = 4T(n/2) + n^2$**

Here $a=4$, $b=2$, $f(n)=n^2$.

$$
n^{\log_b a}=n^{\log_2 4}=n^2
$$

$f(n)=n^2=\Theta(n^2\log^0 n)$, so this is **Case 2** with $k=0$, and $T(n)=\Theta(n^2\log n)$.

Check: level $i$ has $4^i$ nodes, each of size $n/2^i$, so each level does $4^i\cdot(n/2^i)^2=n^2$ work. There are $\log_2 n$ levels.

**(iv) $T(n) = T(n/3) + \log n$**

Here $a=1$, $b=3$, $f(n)=\log n$.

$$
n^{\log_b a}=n^{\log_3 1}=n^0=1
$$

$f(n)=\log n=\Theta(n^0\log^1 n)$ matches the watershed function with $k=1$. This is **Case 2**, so

$$
T(n)=\Theta(n^0\log^{1+1}n)=\Theta(\log^2 n)
$$

Check by expansion: level $i$ costs $\log n-i\log 3$. There are about $\log_3 n$ levels, and their total is about $\frac{(\log n)^2}{2\log 3}$.

**Summary**

| Recurrence | $a$ | $b$ | $f(n)$ | $n^{\log_b a}$ | Case | Result |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| $T(n)=2T(n/2)+n$ | 2 | 2 | $n$ | $n$ | Case 2 ($k=0$) | $\Theta(n\log n)$ |
| $T(n)=T(n-1)+1$ | - | - | $1$ | - | Expansion | $\Theta(n)$ |
| $T(n)=4T(n/2)+n^2$ | 4 | 2 | $n^2$ | $n^2$ | Case 2 ($k=0$) | $\Theta(n^2\log n)$ |
| $T(n)=T(n/3)+\log n$ | 1 | 3 | $\log n$ | $1$ | Case 2 ($k=1$) | $\Theta(\log^2 n)$ |

> Memory trick: if $f(n)$ matches $n^{\log_b a}$, multiply by $\log n$.

![Recursion-level costs and tight bounds](diagrams/b2-theory-17-recurrences.svg)

---

### Q2. NP Classes, BFS, and Activity Graph

#### Q2(a)

**Question (transcribed):** Define the complexity classes NP, NP-hard, and NP-complete.

**Answer.**

These classes are about **decision problems** (yes or no answers).

- **P**: problems that can be **solved** in polynomial time. Example: sorting, shortest path.
- **NP**: problems where a given answer (**certificate**) can be **checked** in polynomial time. Example: for TSP, we can quickly check that a given tour costs at most k. P is inside NP.
- **NP-hard**: **at least as hard as every problem in NP**. Every NP problem can be reduced to it in polynomial time. It need not be in NP. Example: TSP optimization.
- **NP-complete**: a problem that is **in NP and also NP-hard**. Examples: SAT, Hamiltonian cycle, TSP decision, subset sum.

**P = NP?** is still an **open question**.

> Memory trick: P = solve fast. NP = check fast. NP-complete = NP + NP-hard.

![How P, NP, NP-complete, and NP-hard relate](diagrams/b2-theory-01-np-classes-venn.svg)

#### Q2(b)

**Question (transcribed):** Explain how BFS is used to find the shortest path in an unweighted graph. Demonstrate the process with a diagram and step-by-step explanation.

**Answer.**

**Breadth-First Search (BFS)** finds the shortest path in an unweighted graph by visiting vertices level by level from the source vertex.
Since every edge has equal cost, the first time BFS reaches a vertex, it has found a shortest path to that vertex. BFS uses a FIFO queue.(see [Chapter 4](../../../Chapter%204%20-%20Searching%20and%20Basic%20Traversal/README.md) and [Chapter 11](../../../Chapter%2011%20-%20Graph%20Algorithms/README.md)).

**Steps**

1. Set $dist[v]=\infty$ and $parent[v]=\text{NIL}$ for every vertex. Set $dist[S]=0$, mark $S$ visited, and enqueue $S$.
2. While the queue is not empty:
   - Dequeue the front vertex $u$.
   - For each unvisited neighbour $v$ of $u$ (in alphabetical order), mark it visited **when it is enqueued**, set $dist[v]=dist[u]+1$, set $parent[v]=u$, and enqueue it.
3. To get a path to a target, follow `parent` links back to $S$, then reverse the list.

With adjacency lists, BFS takes $\Theta(V+E)$ time and $\Theta(V)$ extra space. With an adjacency matrix, it takes $\Theta(V^2)$ time. If the target cannot be reached, its distance stays $\infty$ and it has no parent path.

**Illustrative givens.** Undirected graph $V=\{S,A,B,C,D,E\}$ with edges S-A, S-B, A-C, B-C, B-D, C-E, D-E; source $S$, target $E$.

**Adjacency list** (neighbours in alphabetical order):

| Vertex | Neighbours |
| :---: | :--- |
| S | A, B |
| A | C, S |
| B | C, D, S |
| C | A, B, E |
| D | B, E |
| E | C, D |

**Queue trace.** Start with $Q=[S]$. The table shows all discovered vertices, the queue after the current vertex is processed (front first, in bold), and the vertex whose processing is done:

| Vertices visited | Vertices in queue (front first) | Vertex traversal done |
| :--- | :--- | :---: |
| S, A, B | **A**, B | S |
| S, A, B, C | **B**, C | A |
| S, A, B, C, D | **C**, D | B |
| S, A, B, C, D, E | **D**, E | C |
| — | **E** | D |
| — | empty | E |

When B is processed, C is already visited, so it is not added again. When D is processed, E is already visited.

BFS traversal order from $S$: S, A, B, C, D, E. Distances and parents, grouped by level:

| Distance from S | Vertices | Parents |
| :---: | :--- | :--- |
| 0 | S | - |
| 1 | A, B | $parent[A]=S$, $parent[B]=S$ |
| 2 | C, D | $parent[C]=A$, $parent[D]=B$ |
| 3 | E | $parent[E]=C$ |

Shortest path from $S$ to $E$: follow parents $E \leftarrow C \leftarrow A \leftarrow S$, so **S-A-C-E** (3 edges). S-B-D-E is also 3 edges.

> Memory trick: BFS = queue + levels. The first visit gives the shortest distance.

![BFS shortest path from S](diagrams/b2-theory-02-bfs-graph.svg)

#### Q2(c)

**Question (transcribed):** A student performs several activities during a day. Some activities must be completed before others can begin.

**Activities:** Wake up; Brush teeth; Take breakfast; Go to class; Study in library; Do homework; Sleep.

**Dependencies:** Wake up must be completed before brushing teeth. Brushing teeth must be completed before taking breakfast. Taking breakfast must be completed before going to class. Going to class must be completed before studying in the library. Studying in the library must be completed before doing homework. Doing homework must be completed before sleeping.

Based on the above situation answer the following questions: (i) Represent the above activities and dependencies using a directed graph. (ii) Apply topological sorting to determine a valid order of activities. (iii) Is more than one valid topological order possible? Explain briefly. (iv) What will happen if sleeping is done before completing homework?

**Answer.**

**Givens from the paper.** The activities are Wake up, Brush teeth, Take breakfast, Go to class, Study in library, Do homework, and Sleep. The paper gives the six dependencies listed below. We use them to draw the graph and answer all four parts (see [Chapter 11](../../../Chapter%2011%20-%20Graph%20Algorithms/README.md)).

**(i) Directed graph.** Each activity is a vertex. Each arrow $u\to v$ means "$u$ must finish before $v$":

Wake up → Brush teeth → Take breakfast → Go to class → Study in library → Do homework → Sleep

This is a **DAG** (directed acyclic graph): the arrows all point forward, so there is no cycle.

| Vertex | Outgoing neighbours |
| :--- | :--- |
| Wake up | Brush teeth |
| Brush teeth | Take breakfast |
| Take breakfast | Go to class |
| Go to class | Study in library |
| Study in library | Do homework |
| Do homework | Sleep |
| Sleep | — |

![Q2(c)(i): directed graph of the activity dependencies](diagrams/b2-theory-03-activity-dag.svg)

*Editable Excalidraw source: [b2-theory-03-activity-dag.excalidraw](diagrams/b2-theory-03-activity-dag.excalidraw). The left panel is the given DAG; the right panel adds the reverse dependency discussed in part (iv), while keeping the original edges.*

**(ii) Topological order (DFS method).** Run DFS from each unvisited vertex. Push a vertex onto a stack only **after** all of its outgoing neighbours have finished. The left-to-right stack is the finish order; its rightmost item is popped first.

| Step | DFS call / return action | Why it happens | Finish stack |
| :---: | :--- | :--- | :--- |
| 1 | `DFS(Wake up) → DFS(Brush teeth) → DFS(Take breakfast) → DFS(Go to class) → DFS(Study in library) → DFS(Do homework) → DFS(Sleep)` | Each vertex has one unvisited outgoing neighbour, so follow it. | empty |
| 2 | Finish `Sleep`; push `Sleep` | Sleep has no outgoing neighbour. | Sleep |
| 3 | Return to and finish `Do homework`; push it | Its only neighbour, Sleep, is complete. | Sleep, Do homework |
| 4 | Finish `Study in library`; push it | Do homework is complete. | Sleep, Do homework, Study in library |
| 5 | Finish `Go to class`; push it | Study in library is complete. | Sleep, Do homework, Study in library, Go to class |
| 6 | Finish `Take breakfast`; push it | Go to class is complete. | Sleep, Do homework, Study in library, Go to class, Take breakfast |
| 7 | Finish `Brush teeth`; push it | Take breakfast is complete. | Sleep, Do homework, Study in library, Go to class, Take breakfast, Brush teeth |
| 8 | Finish `Wake up`; push it | Brush teeth is complete. | Sleep, Do homework, Study in library, Go to class, Take breakfast, Brush teeth, Wake up |

Now pop from the right of the stack. The valid order is:

1. Wake up
2. Brush teeth
3. Take breakfast
4. Go to class
5. Study in library
6. Do homework
7. Sleep

Every arrow points left to right in this order. DFS-based topological sort takes $\Theta(V+E)$ time. (Kahn's algorithm, which repeatedly removes a vertex with indegree 0, gives the same order here: only Wake up has indegree 0, and each removal unlocks the next activity.)

**(iii) Is more than one order possible?** No. The graph is one chain, so each activity must follow the one before it. (A topological order is not unique only when two vertices have no dependency path between them.)

**(iv) What if Sleep comes before Homework?** This breaks the given dependency Do homework → Sleep. So it is not a valid order for the given graph. If we also forced the rule "Sleep before Homework", we would get a cycle (Do homework → Sleep → Do homework), and then no topological order would exist.

> Memory trick: a DAG has a topological order. A cycle has none.

---

### Q3. Searching, Traversing, and Matrix Multiplication

#### Q3(a)

**Question (transcribed):** Explain the difference between searching and traversing by highlighting their purposes, typical operations, and examples.

**Answer.**

A **search technique** checks elements until it finds the required target or proves that it is not there. A **traversal technique** visits elements in a controlled order. In a graph, this usually means starting from one vertex and visiting every vertex reachable from it (see [Chapter 4](../../../Chapter%204%20-%20Searching%20and%20Basic%20Traversal/README.md)).

| Feature | Searching | Traversal |
| :--- | :--- | :--- |
| Main goal (purpose) | Find a target or answer | Visit all reachable elements |
| Typical operation | Compare the target with the current element | Visit the element and process it |
| Stopping condition | Usually stops when the target is found | Usually stops when all reachable elements are visited |
| Output | Target position, true/false, path, or value | Visiting order, component, tree, or processed data |
| Example question | "Is 511 in the list?" or "Is vertex G reachable from A?" | "Visit every vertex reachable from A." |
| Common tools | Linear search, binary search, BFS, DFS | BFS, DFS, tree traversal (in-order, pre-order, post-order) |

Both use the same four ideas: the **current element**, a **frontier** (the waiting collection of elements to visit next), a **visited set**, and a **processing step**. The frontier controls the order: a queue gives BFS, and a stack or the recursion call stack gives DFS.

- If we use BFS from vertex $A$ and stop when $G$ is found, it is a **search**.
- If we use BFS from vertex $A$ and continue until no reachable vertex remains, it is a **traversal**.

From one start vertex, a graph traversal visits only the vertices it can reach. To visit a disconnected graph fully, run BFS or DFS again from every unvisited vertex. The difference is the goal: find one item, or visit them all.

> Memory trick: searching asks "Is 511 here?", traversing asks "Show me every item."

![Searching for a target versus traversing all entries](diagrams/b2-theory-18-search-traverse.svg)

#### Q3(b)

**Question (transcribed):** A sorted list of student IDs is [102, 205, 307, 409, 511, 613, 715, 817]. Compare linear search and binary search to find ID 511 by: (i) showing all comparisons made in each method; (ii) counting the total number of comparisons for each search; (iii) analyzing the best-, average-, and worst-case time complexities; (iv) explaining which method is more efficient for this search and why.

**Answer.**

**Givens from the paper.** The sorted array is `[102, 205, 307, 409, 511, 613, 715, 817]`, and the target is $511$. Use zero-based indices and $mid=\lfloor(lo+hi)/2\rfloor$. Count one key comparison for each inspected value (less than, equal to, or greater than the target). Do not count loop or index checks.

**Linear search** checks each item from the start until it finds 511:

| Step | Index | Value | Equal to 511? |
|------|-------|-------|---------------|
| 1 | 0 | 102 | No |
| 2 | 1 | 205 | No |
| 3 | 2 | 307 | No |
| 4 | 3 | 409 | No |
| 5 | 4 | 511 | **Yes, found** |

Linear search needs **5 comparisons** and finds 511 at index 4.

**Binary search** checks the middle item and keeps the half that may contain 511. The array must be sorted.

| Step | lo | hi | mid | Value at mid | Action |
|------|----|----|-----|--------------|--------|
| 1 | 0 | 7 | 3 | 409 | $409 < 511$, so $lo = 4$ |
| 2 | 4 | 7 | 5 | 613 | $613 > 511$, so $hi = 4$ |
| 3 | 4 | 4 | 4 | 511 | **Found** |

Binary search needs **3 comparisons**: it checks 409, 613, and 511. (If you count the equal-to test and the less-than test separately, binary search uses **5 individual key predicates**, that is, 5 yes/no tests. So always say what you count as one comparison.)

**Best, average, and worst cases**

| Search | Best case | Average case | Worst case |
|--------|-----------|--------------|------------|
| Linear | $\Theta(1)$: target is the first item | $\Theta(n)$: $(n+1)/2$ checks for a uniformly located successful target | $\Theta(n)$: target is last or missing |
| Binary | $\Theta(1)$: target is the middle item | $\Theta(\log n)$ | $\Theta(\log n)$ |

The average assumes the target is equally likely to be in any position and is present. For these 8 items, the averages are $36/8=4.5$ checks for linear search and $21/8=2.625$ checks for binary search. Binary search worst case is **4** checks here (for target 817), not 3. For 511, the counts are 5 and 3.

**Which is better?** For 511, binary search makes 3 checks instead of 5. For a large sorted array, it is usually faster because each check cuts the remaining range in half. It needs sorted data that can be accessed by index. For one search in unsorted data, linear search avoids sorting first. Both iterative methods use $O(1)$ extra space.

![Linear probes and binary-search intervals for 511](diagrams/b2-theory-19-search-trace.svg)

#### Q3(c)

**Question (transcribed):** Explain Strassen's matrix multiplication algorithm. Multiply the following two 2×2 matrices using Strassen's method: A = [[1, 3], [7, 5]], B = [[6, 8], [4, 2]].

**Answer.**

Strassen's algorithm splits each matrix into four blocks. Ordinary multiplication uses 8 block products. Strassen uses **7** products, then combines them with additions and subtractions. For large matrices, this takes $T(n)=7T(n/2)+\Theta(n^2)$ time, or $\Theta(n^{\log_2 7})\approx\Theta(n^{2.81})$.

For the given matrices, each block is one number: $A_{11}=1$, $A_{12}=3$, $A_{21}=7$, $A_{22}=5$, and $B_{11}=6$, $B_{12}=8$, $B_{21}=4$, $B_{22}=2$. Use these Strassen formulas:

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

$$
C = \begin{bmatrix}18 & 14 \\ 62 & 66\end{bmatrix}
$$

**Check** with normal multiplication: row 1 of $A$ times column 1 of $B$ is $1 \cdot 6 + 3 \cdot 4 = 18$. The other three entries also match.

> Memory trick: Strassen uses 7 multiplications instead of 8.

![Strassen split and results](diagrams/b2-theory-04-strassen-split.svg)

---

### Q4. Sorting: Insertion, Bubble, Quick Sort, and Merge Sort

#### Q4(a)

**Question (transcribed):** Why is insertion sort more efficient than bubble sort for nearly sorted arrays? Justify your answer with an example.

**Answer.**

Insertion sort builds a sorted part from left to right. It moves each new item left only as far as needed. In a nearly sorted array, most items move very little, so insertion sort is fast (see [Chapter 5](../../../Chapter%205%20-%20Sorting%20Algorithms/README.md)).

Bubble sort compares and swaps neighbouring items in repeated passes. A small item at the **end** moves only **one place left per pass**, so it may take many passes to reach the start.

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

**Conclusion:** On this input, insertion sort makes about 11 comparisons, while bubble sort makes about 21. An **inversion** is a pair of items in the wrong order. If there are $I$ inversions, insertion sort takes $\Theta(n+I)$ time, which is almost $\Theta(n)$ when $I$ is small (here, $I=6$). Bubble sort needs many passes, because the small item moves only one place left per pass, even with early exit.

> Memory trick: insertion sort jumps the item straight home. Bubble sort walks it one step per pass.

![Insertion shifts versus six left-to-right bubble passes](diagrams/b2-theory-20-insertion-bubble.svg)

#### Q4(b)

**Question (transcribed):** A company stores the employee IDs [1023, 1010, 1055, 1005, 1040] in an unsorted array. The HR software needs the IDs in ascending order to generate reports efficiently. (i) Explain how quick sort can be applied to sort these IDs. (ii) Show the pivot selection and partitioning steps. (iii) Give the final sorted array.

**Answer.**

**(i) How quick sort is applied:** pick a pivot, **partition** the array (smaller items to the left, larger items to the right), then sort the two sides recursively.

**(ii) Pivot selection and partitioning:** use the **last element as the pivot**. During partitioning, move values smaller than the pivot to its left. Index $i$ marks the end of that smaller-values part. This is Lomuto partitioning (see [Chapter 5](../../../Chapter%205%20-%20Sorting%20Algorithms/README.md)).

**Pass 1:** pivot = 1040, $i = -1$

| $j$ | Value | Less than 1040? | Action | Array |
|-----|-------|-----------------|--------|-------|
| 0 | 1023 | Yes | $i = 0$, swap with itself | 1023, 1010, 1055, 1005, 1040 |
| 1 | 1010 | Yes | $i = 1$, swap with itself | 1023, 1010, 1055, 1005, 1040 |
| 2 | 1055 | No | nothing | same |
| 3 | 1005 | Yes | $i = 2$, swap $a[2]$ and $a[3]$ | 1023, 1010, 1005, 1055, 1040 |

Finally, swap the pivot with $a[i+1]=a[3]$: **1023, 1010, 1005, 1040, 1055**. Pivot 1040 is now in its final sorted position.

- Left part: $[1023, 1010, 1005]$
- Right part: $[1055]$ (one item, already sorted)

**Pass 2 (left part):** pivot = 1005. Both 1023 and 1010 are larger, so $i$ stays at $-1$. Swap the pivot with $a[0]$: **1005, 1010, 1023**. Left part is empty; Right part is $[1010, 1023]$.

**Pass 3 (right part of pass 2):** pivot = 1023. Since 1010 is smaller, it stays to the left. Result: **1010, 1023**. The left side is $[1010]$ and the right side is empty. The three partitions make **7 key–pivot comparisons** in total (4 + 2 + 1).

![Quick sort partition tree](diagrams/b2-theory-05-quicksort-partition.svg)

**Final sorted array: $[1005, 1010, 1023, 1040, 1055]$**

> Memory trick: choose a pivot, put it in its final place, then repeat on each side.

#### Q4(c)

**Question (transcribed):** Explain the divide-and-conquer technique in algorithm design. Illustrate your answer by applying it to merge sort to sort the array [38, 27, 43, 3, 9, 82, 10], showing the divide, conquer, and combine steps.

**Answer.**

**Divide and conquer** solves a problem in three steps: divide it into smaller parts, solve those parts, and combine their answers. For an odd-length list, put the extra item in the **left** half:

**Divide**

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

Merge sort takes $\Theta(n\log n)$ time (see Q1(c)(i)) and uses an extra $\Theta(n)$ array for merging.

> Memory trick: split down to single items, then merge back up in order.

---

## Section B

### Q5. Greedy Algorithms and Minimum Spanning Tree

#### Q5(a)

**Question (transcribed):** What is a greedy algorithm? State the conditions under which a greedy approach produces an optimal solution.

**Answer.**

A **greedy algorithm** builds the answer step by step. At each step it picks the **locally best** choice that keeps the solution valid, and it **never undoes** that choice (see [Chapter 7](../../../Chapter%207%20-%20Greedy%20Algorithms/README.md)).

**Parts of a greedy algorithm**

| Part | Meaning | Example (fractional knapsack) |
| :--- | :--- | :--- |
| Candidate set | The available items, edges, coins, or activities | The items |
| Selection function | Chooses the next most promising candidate | Highest value/weight ratio |
| Feasibility function | Checks that the choice keeps the partial solution valid | The fraction fits in the remaining capacity |
| Objective function | What we minimize or maximize | Maximize total value |
| Solution function | Checks that the solution is complete | Capacity is full or no item remains |

**Greedy gives an optimal answer when the problem has both:**

1. **Greedy-choice property**: a globally optimal solution can be reached by first making the locally optimal choice.
2. **Optimal substructure**: after the greedy choice, the remaining smaller problem is the same kind of problem and is solved optimally in the same way.

**Proof ideas**

| Proof idea | Meaning | Common use |
| :--- | :--- | :--- |
| Exchange argument | Replace part of an optimal solution with the greedy choice without making it worse | Activity selection, fractional knapsack |
| Cut property | The lightest edge crossing a cut is safe for an MST | Prim, Kruskal |
| Stays-ahead argument | The greedy solution is never behind another solution after each step | Activity selection |
| Induction | Greedy first choice plus an optimal remaining solution is optimal | Many greedy algorithms |

**Works:** activity selection, fractional knapsack, Kruskal's and Prim's MST, Huffman coding.

**Fails:** 0/1 knapsack, and coin change for some coin systems. Take denominations $4,3,1$ and amount $A=6$:

| Method | Chosen coins | Number of coins |
| :--- | :--- | :---: |
| Greedy | $4+1+1$ | 3 |
| Optimal | $3+3$ | 2 |

> Memory trick: Greedy works only when the best choice now is also safe for the future.

![Greedy exchange argument and a coin-change counterexample](diagrams/b2-theory-21-greedy-proof.svg)

#### Q5(b)

**Question (transcribed):** A thief has a knapsack with capacity 50. He can take fractions of items. The available items have the following weights and profits: Item 1 (weight 10, profit 60), Item 2 (weight 20, profit 100), Item 3 (weight 30, profit 120). Solve the fractional knapsack problem to maximize profit. Show (i) the profit-to-weight ratio for each item; (ii) the items or fractions to include in the knapsack; (iii) the maximum total profit obtained.

**Answer.**

In the **fractional knapsack**, an item may be broken into fractions. The greedy choice is to take items in decreasing order of the ratio $v_i/w_i$ (value, or profit, per unit weight). If an item gives more value per unit weight, taking it earlier cannot reduce the best total, and since fractions are allowed, the last item can fill the remaining capacity exactly (see [Chapter 7](../../../Chapter%207%20-%20Greedy%20Algorithms/README.md)).

**(i) Profit-to-weight ratio** (the chapter calls profit *value*):

| Item | Weight | Value (profit) | Ratio $v/w$ | Rank |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 10 | 60 | 6 | 1st |
| 2 | 20 | 100 | 5 | 2nd |
| 3 | 30 | 120 | 4 | 3rd |

**(ii) Items to include.** Sorted by ratio: item 1, item 2, item 3. Fill the capacity $W=50$:

| Step | Item chosen | Amount taken | Capacity used | Value gained | Remaining capacity |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | Full item | 10 | 60 | 40 |
| 2 | 2 | Full item | 20 | 100 | 20 |
| 3 | 3 | $20/30$ fraction | 20 | $120 \times 20/30 = 80$ | 0 |

**(iii)** **Maximum profit: 240**, because $60+100+80=240$. The answer is to take fractions $(1,1,2/3)$ of items 1, 2, and 3. This is the best possible because every unit of weight is filled with the highest ratio still available.

```text
FRACTIONAL-KNAPSACK(items, W)
1. compute ratio[i] = value[i] / weight[i] for each item
2. sort items by decreasing ratio
3. total_value = 0; remaining = W
4. for each item i in sorted order:
5.     if weight[i] <= remaining:
6.         take the full item; total_value += value[i]; remaining -= weight[i]
7.     else:
8.         take the fraction remaining / weight[i]
9.         total_value += value[i] * remaining / weight[i]; remaining = 0; break
10. return total_value
```

Sorting takes $\Theta(n\log n)$ time and the greedy scan takes $\Theta(n)$, so the total is $\Theta(n\log n)$. The 0/1 optimum is 220 (items 2 and 3), when items cannot be split.

> Memory trick: highest profit per unit weight first, and split the last item.

![Fractional knapsack fill by decreasing profit density](diagrams/b2-theory-22-fractional-knapsack.svg)

#### Q5(c)

**Question (transcribed):** Define minimum spanning tree (MST). Using the given graph, find the MST by using the Kruskal algorithm and show the step-by-step process by indicating the edges selected and the total minimum cost.

**Answer.**

A **minimum spanning tree (MST)** connects every vertex, has no cycle, and has the smallest possible total edge weight. A tree on 6 vertices has 5 edges (see [Chapter 11](../../../Chapter%2011%20-%20Graph%20Algorithms/README.md)).

**Graph transcribed from the paper:** the undirected graph has $V=\{1,2,3,4,5,6\}$ and these edges, from lowest to highest weight:

$$
(5,1)=1,\ (4,1)=1,\ (1,2)=2,\ (4,2)=3,\ (3,2)=3,\ (4,3)=5,\ (2,6)=7,\ (3,6)=8,\ (5,4)=9.
$$

**Adjacency list** (neighbour, weight):

```text
1: 2(2), 4(1), 5(1)
2: 1(2), 3(3), 4(3), 6(7)
3: 2(3), 4(5), 6(8)
4: 1(1), 2(3), 3(5), 5(9)
5: 1(1), 4(9)
6: 2(7), 3(8)
```

**Kruskal's algorithm** begins with a forest of six one-vertex sets. Sort the edges by weight. For each edge, test `FIND(u) != FIND(v)`. If the roots differ, take the edge and `UNION` the two sets. If they are the same, the edge would close a cycle, so skip it. Stop after $V-1=5$ accepted edges. Equal-weight edges may be taken in either order.

| Scan | Edge | Weight | Decision | Selected forest after decision |
| :---: | :---: | :---: | :--- | :--- |
| 1 | (5,1) | 1 | Take | $\{1,5\}$, $\{2\}$, $\{3\}$, $\{4\}$, $\{6\}$ |
| 2 | (4,1) | 1 | Take | $\{1,4,5\}$, $\{2\}$, $\{3\}$, $\{6\}$ |
| 3 | (1,2) | 2 | Take | $\{1,2,4,5\}$, $\{3\}$, $\{6\}$ |
| 4 | (4,2) | 3 | Skip: path 4–1–2 already connects them | unchanged |
| 5 | (3,2) | 3 | Take | $\{1,2,3,4,5\}$, $\{6\}$ |
| 6 | (4,3) | 5 | Skip: path 4–1–2–3 already connects them | unchanged |
| 7 | (2,6) | 7 | Take; we now have 5 edges, so stop | $\{1,2,3,4,5,6\}$ |

The remaining edges (3,6) with weight 8 and (5,4) with weight 9 are not needed.

**MST edges:** $(5,1),(4,1),(1,2),(3,2),(2,6)$.
**Minimum cost:** $1+1+2+3+7=14$.

These edges connect all six vertices without a cycle. The MST is unique. Sorting the edges takes $\Theta(E\log E)$ time, and the DSU tests are almost constant per edge. The diagram highlights the selected edges.

> Memory trick: sort the edges, skip any edge that closes a cycle, and stop at $V-1$ edges.

![Kruskal MST on the graph shown in the paper](diagrams/b2-theory-07-kruskal-mst.svg)

---

### Q6. Dynamic Programming, Floyd-Warshall, and LCS

#### Q6(a)

**Question (transcribed):** Define dynamic programming. Discuss overlapping subproblems using Fibonacci.

**Answer.**

**Dynamic programming (DP)** solves each distinct subproblem once, stores its answer, and reuses it whenever the same subproblem appears again. It is useful when the same subproblems repeat (**overlapping subproblems**) and the full answer can be built from optimal answers to smaller ones (**optimal substructure**) (see [Chapter 8](../../../Chapter%208%20-%20Dynamic%20Programming/README.md)).

A DP solution has five parts: **state**, **recurrence**, **base case**, **table order**, and **final answer**. For Fibonacci:

| DP part | Choice for Fibonacci |
| :--- | :--- |
| State | $F(n)$ |
| Base case | $F(0)=0$ and $F(1)=1$ |
| Recurrence | $F(n)=F(n-1)+F(n-2)$ for $n\ge2$ |
| Table order | Fill $n=2,3,\dots$ upward |
| Final answer | $F(5)=5$ |

**Overlapping subproblems.** In the simple recursive method, the calls for $F(5)$ look like this. Every repeated subtree below is solved again from scratch:

```text
F(5)
├─ F(4)
│   ├─ F(3)
│   │   ├─ F(2) -> F(1), F(0)
│   │   └─ F(1)
│   └─ F(2) -> F(1), F(0)        <- F(2) repeated
└─ F(3)                          <- F(3) repeated
    ├─ F(2) -> F(1), F(0)
    └─ F(1)
```

Counting the calls:

- $F(3)$ is called **twice**.
- $F(2)$ is called **three times**.
- $F(1)$ is called five times, and $F(0)$ three times.
- $F(5)$ and $F(4)$ are each called once.

The naive recursion for $F(5)$ makes **15** calls in total. As $n$ grows, many values are recalculated, so the number of calls grows exponentially. These repeated calculations are the **overlapping subproblems**.

> Memory trick: do not solve the same thing twice. Store the answer.

With DP, each $F(i)$ is computed once and stored. Memoization stores $F(3)=2$ the first time it is found, so the second request returns the cached value. Tabulation fills the table from the base cases upward:

```text
if n == 0: return 0
F[0] = 0, F[1] = 1
for i = 2 to n:
    F[i] = F[i-1] + F[i-2]
return F[n]
```

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $F(n)$ | 0 | 1 | 1 | 2 | 3 | **5** |

The table for $F(5)$ is $[0,1,1,2,3,5]$. Counting each addition as one step, tabulation takes $\Theta(n)$ time and $\Theta(n)$ extra space. If we keep only the previous two values, the extra space is $\Theta(1)$.

![Repeated Fibonacci calls versus one stored value per state](diagrams/b2-theory-23-fibonacci-dp.svg)

#### Q6(b)

**Question (transcribed):** Explain how the Floyd-Warshall algorithm computes all-pairs shortest paths in a weighted graph. Using the adjacency matrix [[0, 5, ∞, 10], [∞, 0, 3, ∞], [∞, ∞, 0, 1], [∞, ∞, ∞, 0]], perform the algorithm step by step, updating the distance matrix for each intermediate vertex. Show all intermediate matrices in sequence and present the final shortest-path matrix with explanations.

**Answer.**

**Givens:** a directed graph with vertices 1–4 and the four weighted edges $1\to2$ (5), $1\to4$ (10), $2\to3$ (3), and $3\to4$ (1). $\infty$ means there is no direct edge; each diagonal 0 is the distance from a vertex to itself. Assume there is no negative-weight cycle (see [Chapter 11](../../../Chapter%2011%20-%20Graph%20Algorithms/README.md)).

Floyd-Warshall finds shortest distances between **every pair** of vertices. Let $D^{(k)}[i,j]$ be the shortest distance from $i$ to $j$ using only vertices $1$ through $k$ as intermediate vertices. When vertex $k$ is allowed, either do not use it, or go through it:

$$
D^{(k)}[i,j]=\min\big(D^{(k-1)}[i,j],\ D^{(k-1)}[i,k]+D^{(k-1)}[k,j]\big)
$$

**Initial matrix $D^{(0)}$** (direct edges only):

$$
D^{(0)}=
\begin{pmatrix}
0 & 5 & \infty & 10 \\
\infty & 0 & 3 & \infty \\
\infty & \infty & 0 & 1 \\
\infty & \infty & \infty & 0
\end{pmatrix}
$$

**$D^{(1)}$: allow vertex 1 as intermediate.** Row 1 and column 1 do not change. Every other cell is checked against a detour through vertex 1:

- $D[2,3]=\min(3,\ D[2,1]+D[1,3])=\min(3,\ \infty+\infty)=3$
- $D[2,4]=\min(\infty,\ D[2,1]+D[1,4])=\min(\infty,\ \infty+10)=\infty$
- $D[3,2]=\min(\infty,\ D[3,1]+D[1,2])=\min(\infty,\ \infty+5)=\infty$
- $D[3,4]=\min(1,\ D[3,1]+D[1,4])=\min(1,\ \infty+10)=1$
- $D[4,2]=\min(\infty,\ D[4,1]+D[1,2])=\min(\infty,\ \infty+5)=\infty$
- $D[4,3]=\min(\infty,\ D[4,1]+D[1,3])=\min(\infty,\ \infty+\infty)=\infty$

No edge comes into vertex 1, so nothing improves:

$$
D^{(1)}=D^{(0)}=
\begin{pmatrix}
0 & 5 & \infty & 10 \\
\infty & 0 & 3 & \infty \\
\infty & \infty & 0 & 1 \\
\infty & \infty & \infty & 0
\end{pmatrix}
$$

**$D^{(2)}$: allow vertices 1 and 2 as intermediate.** Row 2 and column 2 stay fixed:

- $D[1,3]=\min(\infty,\ D[1,2]+D[2,3])=\min(\infty,\ 5+3)=8$
- $D[1,4]=\min(10,\ D[1,2]+D[2,4])=\min(10,\ 5+\infty)=10$
- $D[3,1]=\min(\infty,\ D[3,2]+D[2,1])=\min(\infty,\ \infty+\infty)=\infty$
- $D[3,4]=\min(1,\ D[3,2]+D[2,4])=\min(1,\ \infty+\infty)=1$
- $D[4,1]=\min(\infty,\ D[4,2]+D[2,1])=\min(\infty,\ \infty+\infty)=\infty$
- $D[4,3]=\min(\infty,\ D[4,2]+D[2,3])=\min(\infty,\ \infty+3)=\infty$

Only $D[1,3]$ improves, from $\infty$ to **8**, through $1\to2\to3$:

$$
D^{(2)}=
\begin{pmatrix}
0 & 5 & 8 & 10 \\
\infty & 0 & 3 & \infty \\
\infty & \infty & 0 & 1 \\
\infty & \infty & \infty & 0
\end{pmatrix}
$$

Arrow-guided update for intermediate vertex $k=2$ (changed cell only):

| Cell | Keep direct path | Try detour through $2$ | Chosen arrow | Stored value |
| :---: | :---: | :---: | :---: | :---: |
| $D[1,3]$ | $\infty$ | $D[1,2]+D[2,3]=5+3=8$ | $1 \rightarrow 2 \rightarrow 3$ | **8** |

**$D^{(3)}$: allow vertices 1, 2, and 3 as intermediate.** Row 3 and column 3 stay fixed:

- $D[1,2]=\min(5,\ D[1,3]+D[3,2])=\min(5,\ 8+\infty)=5$
- $D[1,4]=\min(10,\ D[1,3]+D[3,4])=\min(10,\ 8+1)=9$
- $D[2,1]=\min(\infty,\ D[2,3]+D[3,1])=\min(\infty,\ 3+\infty)=\infty$
- $D[2,4]=\min(\infty,\ D[2,3]+D[3,4])=\min(\infty,\ 3+1)=4$
- $D[4,1]=\min(\infty,\ D[4,3]+D[3,1])=\min(\infty,\ \infty+\infty)=\infty$
- $D[4,2]=\min(\infty,\ D[4,3]+D[3,2])=\min(\infty,\ \infty+\infty)=\infty$

Two cells improve: $D[1,4]$ drops from 10 to **9** through $1\to2\to3\to4$, and $D[2,4]$ drops from $\infty$ to **4** through $2\to3\to4$:

$$
D^{(3)}=
\begin{pmatrix}
0 & 5 & 8 & 9 \\
\infty & 0 & 3 & 4 \\
\infty & \infty & 0 & 1 \\
\infty & \infty & \infty & 0
\end{pmatrix}
$$

Arrow-guided update for intermediate vertex $k=3$ (changed cells):

| Cell | Keep direct path | Try detour through $3$ | Chosen arrow | Stored value |
| :---: | :---: | :---: | :---: | :---: |
| $D[1,4]$ | 10 | $D[1,3]+D[3,4]=8+1=9$ | $1 \rightarrow 3 \rightarrow 4$ | **9** |
| $D[2,4]$ | $\infty$ | $D[2,3]+D[3,4]=3+1=4$ | $2 \rightarrow 3 \rightarrow 4$ | **4** |

**$D^{(4)}$: allow all vertices as intermediate (final matrix).** Row 4 and column 4 stay fixed:

- $D[1,2]=\min(5,\ D[1,4]+D[4,2])=\min(5,\ 9+\infty)=5$
- $D[1,3]=\min(8,\ D[1,4]+D[4,3])=\min(8,\ 9+\infty)=8$
- $D[2,1]=\min(\infty,\ D[2,4]+D[4,1])=\min(\infty,\ 4+\infty)=\infty$
- $D[2,3]=\min(3,\ D[2,4]+D[4,3])=\min(3,\ 4+\infty)=3$
- $D[3,1]=\min(\infty,\ D[3,4]+D[4,1])=\min(\infty,\ 1+\infty)=\infty$
- $D[3,2]=\min(\infty,\ D[3,4]+D[4,2])=\min(\infty,\ 1+\infty)=\infty$

No edge leaves vertex 4, so nothing changes:

$$
D^{(4)}=D^{(3)}=
\begin{pmatrix}
0 & 5 & 8 & 9 \\
\infty & 0 & 3 & 4 \\
\infty & \infty & 0 & 1 \\
\infty & \infty & \infty & 0
\end{pmatrix}
$$

**Negative-cycle check:** every diagonal entry of $D^{(4)}$ is still 0, so there is no negative cycle and all distances are valid.

![Floyd-Warshall graph and matrix changes](diagrams/b2-theory-08-floyd-warshall.svg)

The final distances include $d(1,3)=8$, $d(1,4)=9$, and $d(2,4)=4$. The shortest path from 1 to 4 is **1→2→3→4**, with cost $5+3+1=9$. The algorithm takes $\Theta(n^3)$ time and $\Theta(n^2)$ space. If a graph has a negative-weight cycle, some shortest-path distances are not defined.

> Memory trick: for each $k$, ask: "Is going through $k$ shorter?"

#### Q6(c)

**Question (transcribed):** Explain how dynamic programming is used to compute the longest common subsequence (LCS) of two strings. For X = AGGTAB and Y = GXTXAYB, build the full DP table row by row. After completing the table, demonstrate how to trace back through it to find the final LCS, and clearly state both the LCS and its length.

**Answer.**

A **subsequence** keeps letters in their original order but may skip letters. Let $c[i,j]$ be the length of the longest common subsequence (**LCS**) of the first $i$ letters of $X$ and the first $j$ letters of $Y$ (see [Chapter 8](../../../Chapter%208%20-%20Dynamic%20Programming/README.md)).

$$
c[i,j]=
\begin{cases}
0, & i=0 \text{ or } j=0\\
c[i-1,j-1]+1, & x_i=y_j\\
\max\big(c[i-1,j],\ c[i,j-1]\big), & x_i\ne y_j
\end{cases}
$$

| DP part | Choice for LCS |
| :--- | :--- |
| State | $c[i,j]$: LCS length of $X[1..i]$ and $Y[1..j]$ |
| Base case | $c[0,j]=c[i,0]=0$, because an empty string has no common letters |
| Recurrence | The three cases above |
| Table order | Row by row, left to right |
| Final answer | $c[6,7]$ |

**Arrow legend:** $\nwarrow$ means the letters match, so the value is the diagonal cell plus 1. $\uparrow$ means they do not match and the upper cell is chosen. $\leftarrow$ means they do not match and the left cell is chosen. If the upper and left cells tie, $\uparrow$ is chosen (the rule $c[i-1][j]\ge c[i][j-1]$ in the chapter's algorithm).

**DP table** (row = letter of $X$, column = letter of $Y$):

| $i \backslash j$ | - | G | X | T | X | A | Y | B |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | 0 | 0 ($\uparrow$) | 0 ($\uparrow$) | 0 ($\uparrow$) | 0 ($\uparrow$) | 1 ($\nwarrow$) | 1 ($\leftarrow$) | 1 ($\leftarrow$) |
| G | 0 | 1 ($\nwarrow$) | 1 ($\leftarrow$) | 1 ($\leftarrow$) | 1 ($\leftarrow$) | 1 ($\uparrow$) | 1 ($\uparrow$) | 1 ($\uparrow$) |
| G | 0 | 1 ($\nwarrow$) | 1 ($\uparrow$) | 1 ($\uparrow$) | 1 ($\uparrow$) | 1 ($\uparrow$) | 1 ($\uparrow$) | 1 ($\uparrow$) |
| T | 0 | 1 ($\uparrow$) | 1 ($\uparrow$) | 2 ($\nwarrow$) | 2 ($\leftarrow$) | 2 ($\leftarrow$) | 2 ($\leftarrow$) | 2 ($\leftarrow$) |
| A | 0 | 1 ($\uparrow$) | 1 ($\uparrow$) | 2 ($\uparrow$) | 2 ($\uparrow$) | 3 ($\nwarrow$) | 3 ($\leftarrow$) | 3 ($\leftarrow$) |
| B | 0 | 1 ($\uparrow$) | 1 ($\uparrow$) | 2 ($\uparrow$) | 2 ($\uparrow$) | 3 ($\uparrow$) | 3 ($\uparrow$) | **4** ($\nwarrow$) |

Key calculations:

- $c[1,5]=c[0,4]+1=1$, because $A=A$.
- $c[4,3]=c[3,2]+1=2$, because $T=T$.
- $c[5,5]=c[4,4]+1=3$, because $A=A$.
- $c[6,7]=c[5,6]+1=4$, because $B=B$.

**Traceback** starts at $c[6,7]=4$ and follows the arrows:

1. $c[6,7]$: $B=B$. Take **B** and move $\nwarrow$ to $c[5,6]$.
2. $c[5,6]$: $A\ne Y$. The upper value is 2 and the left value is 3, so move $\leftarrow$ to $c[5,5]$.
3. $c[5,5]$: $A=A$. Take **A** and move $\nwarrow$ to $c[4,4]$.
4. $c[4,4]$: $T\ne X$. The left value (2) is larger, so move $\leftarrow$ to $c[4,3]$.
5. $c[4,3]$: $T=T$. Take **T** and move $\nwarrow$ to $c[3,2]$.
6. $c[3,2]$: $G\ne X$. Up and left tie at 1, so move $\uparrow$ to $c[2,2]$.
7. $c[2,2]$: $G\ne X$. The left value (1) is larger, so move $\leftarrow$ to $c[2,1]$.
8. $c[2,1]$: $G=G$. Take **G** and move $\nwarrow$ to $c[1,0]$. Stop.

Reading the taken letters backwards gives **G, T, A, B**.

**LCS = GTAB, length = 4.** At $c[3,2]$, moving up or left is tied; the up-first rule gives this traceback. Other tie choices may place the same letters in different positions. Filling the table takes $\Theta(mn)$ time and space for strings of lengths $m$ and $n$. Tracing back takes $O(m+n)$ time.

> Memory trick: a match means diagonal + 1. No match means the larger of above and left.

![LCS table with traceback](diagrams/b2-theory-09-lcs-table.svg)

---

### Q7. Backtracking: Graph Colouring, LC-Search, and N-Queens

#### Q7(a)

**Question (transcribed):** Apply backtracking to graph colouring for a graph of 5 vertices. Show the order of colour assignment and the backtracking steps.

**Answer.**

> [!NOTE]
> **Worked example:** the paper gives no particular graph or number of colours. For a clear example, use the five-vertex graph below and three colours (Red = 1, Green = 2, Blue = 3).

**Sample graph:** edges 1-2, 1-3, 2-3, 3-4, 4-5, 3-5, 2-5.

**Method:** the sample graph is undirected and has exactly the seven listed edges. Start with every vertex uncoloured. Visit vertices 1 through 5, trying Red, Green, then Blue. A colour is allowed if no already-coloured neighbour has it. If no colour works, **backtrack**: undo the previous colour and try the next one (see [Chapter 9](../../../Chapter%209%20-%20Backtracking/README.md)).

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

**Final colouring:** v1 Red, v2 Green, v3 Blue, v4 Green, v5 Red. Every edge joins vertices with different colours. The triangle 1–2–3 needs at least three colours. This valid 3-colouring proves that the chromatic number is **3** (the fewest colours needed). With $m$ colours and $n$ vertices, the search may try up to $m^n$ assignments.

> Memory trick: colour in order. If stuck, go back and change the previous colour.

![Graph colouring backtracking tree](diagrams/b2-theory-10-colouring-tree.svg)

#### Q7(b)

**Question (transcribed):** Demonstrate LC-search on a 0/1 knapsack instance with at least four items. Draw the state-space tree.

**Answer.**

> [!NOTE]
> **Reconstructed example:** the original items are unavailable. The four items below specify the worked problem completely; their profits and weights are not authenticated exam givens.

**Instance:** capacity $W = 10$. Items (weight, profit): **A** (4, 40), **C** (3, 18), **B** (6, 30), **D** (5, 20). Sorted by profit per weight: A (10), C (6), B (5), D (4).

**LC-search** means least-cost search. It uses a **priority queue** to choose the next live node (an unfinished choice that may still be explored). Here we want the largest profit, so expand the node with the **largest upper bound** first. This is best-first **branch and bound**, not depth-first backtracking.

The **upper bound** estimates the most profit a node could still reach. Find it by pretending we can take fractions of the remaining items:

$$
ub=\text{profit so far}+\text{profit from the best fractional fill of remaining items}
$$

A **fractional fill** allows part of an item. **Prune** (stop exploring) a node if it is overweight or its upper bound is no greater than the best valid profit found so far. That best profit is called the **incumbent**.

Add the take-child before the skip-child. If two nodes have the same bound, expand the one added first; this is **first-in, first-out (FIFO)**. The incumbents are 40, 58, and then 70.

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

**Expanded nodes, in order:** root → A=1 → A=1,C=1 → A=1,C=0. From the last node, taking B gives the valid choice A+B, with weight 10 and profit 70. The other node with bound 70 was added later, so FIFO puts it after this node. All remaining bounds are at most 70, so they cannot give a higher profit. The table lists nine generated nodes; only four are expanded.

**Answer:** take **A and B**. Their total weight is 10 and their profit is 70. No other choice gives a higher profit within capacity 10.

> Memory trick: always expand the most promising node, and kill nodes that cannot beat the best.

![LC-search state-space tree](diagrams/b2-theory-11-lc-knapsack-tree.svg)

#### Q7(c)

**Question (transcribed):** Solve the N-Queens problem for N = 5 using backtracking. Show partial board configurations and backtracking steps.

**Answer.**

Place one queen in each row. Queens must not share a **column** or a **diagonal**. For queens at $(r_i,c_i)$ and $(r_j,c_j)$, they share a diagonal when $|r_i-r_j|=|c_i-c_j|$. If a row has no safe column, return to the previous row and move that queen (see [Chapter 9](../../../Chapter%209%20-%20Backtracking/README.md)).

**Trace of the first solution:** process rows 1–5 and try columns 1–5 in order. Reject a column if it conflicts with an earlier queen. The list records the queen's column in each row.

| Row | Columns tried | Result | Partial board (queen columns so far) |
|-----|---------------|--------|--------------------------------------|
| 1 | 1 | Safe, placed | [1] |
| 2 | 1 (same column), 2 (diagonal with (1,1)), 3 | Safe at column 3 | [1, 3] |
| 3 | 1 (column), 2 (diagonal with (2,3)), 3 (column), 4 (diagonal with (2,3)), 5 | Safe at column 5 | [1, 3, 5] |
| 4 | 1 (column), 2 | Safe at column 2 | [1, 3, 5, 2] |
| 5 | 1, 2, 3 (columns), 4 | Safe at column 4 | [1, 3, 5, 2, 4] ✓ |

**A later dead end when finding all solutions:** Continue searching with row 1 in column 1, undoing a queen before each new try. Eventually row 2 reaches column 5, giving [1, 5]:

- In row 3, only column 2 is safe, so the board is [1, 5, 2].
- In row 4, column 3 is diagonal to (3,2), and column 4 is diagonal to (1,1). **No column is safe.** Row 3 has no other choice, and row 2 has no more columns to try: columns 3 and 4 were already explored. So the search returns to row 1 and tries column 2.

**Final board for the first solution [1, 3, 5, 2, 4]**

```
Q . . . .
. . Q . .
. . . . Q
. Q . . .
. . . Q .
```

The table gives the first solution. The later branch shows how the algorithm backtracks when a row has no safe column. The search can continue to find other solutions.

> Memory trick: one queen per row. A column or diagonal conflict means skip. No safe column means go back.

![N-Queens backtracking tree and final board](diagrams/b2-theory-12-nqueens-tree.svg)

---

### Q8. Decision vs Optimization, Branch and Bound, and TSP

#### Q8(a)

**Question (transcribed):** Differentiate between decision problem and optimization problem in computational complexity.

**Answer.**

| | Decision problem | Optimization problem |
|--|------------------|----------------------|
| Question | Is there a solution that meets a condition? Answer yes or no. | What is the best value (minimum or maximum)? |
| Example (0/1 knapsack) | Is there a subset with weight at most $W$ and profit at least $P$? | What is the greatest profit among subsets with weight at most $W$? |
| Example (TSP) | Is there a tour with cost at most $k$? | What is the cheapest tour? |
| Output | Yes or no | A best value and a solution |

P and NP are classes of **decision problems** (yes-or-no problems). TSP decision is NP-complete; finding the cheapest TSP tour is NP-hard (see [Chapter 15](../../../Chapter%2015%20-%20Lower%20Bound%20Theory%20and%20NP%20Completeness/README.md)). The optimization version is at least as hard as the decision version.

> Memory trick: decision = "Can we do it?" Optimization = "What is the best?"

![Threshold decision versus finding an optimum and witness](diagrams/b2-theory-24-decision-optimization.svg)

#### Q8(b)

**Question (transcribed):** Explain admissible heuristic and bounding function in branch-and-bound. Solve a branch-and-bound job sequencing problem.

**Answer.**

**Branch and bound (B&B)** searches a tree of choices. It uses a **bounding function** to skip a branch that cannot beat the best answer found so far (see [Chapter 10](../../../Chapter%2010%20-%20Branch%20and%20Bound/README.md)).

- **Bounding function:** gives a safe limit on how good a branch can be. For maximization it is an **upper bound** on profit. For minimization it is a **lower bound** on cost. If the bound is no better than the best answer so far, **prune** the branch ($ub\le$ best profit, or $lb\ge$ best cost).
- **Admissible heuristic:** an estimate that never lies in the wrong direction. For minimization it **never overestimates** the remaining cost. For maximization it **never underestimates** the possible profit. So pruning never throws away the best answer.

**Job sequencing with deadlines (maximize profit).** Use one machine. Every job takes one time slot and earns its profit only if it finishes by its deadline. A set of jobs is **feasible** if all of them can finish on time. To check, sort the jobs by deadline; the $i$-th job's deadline must be at least $i$.

> [!NOTE]
> **Worked example:** the paper asks for a job-sequencing example but gives no job list. The following four jobs are an example chosen to demonstrate the method.

**Instance:** J1 (profit 100, deadline 2), J4 (profit 27, deadline 1), J3 (profit 15, deadline 2), J2 (profit 10, deadline 1). Jobs are considered in order of profit.

**Bound:** $ub$ = profit already selected + profits of all undecided jobs. This is a safe upper bound because it ignores deadline limits on the undecided jobs. Use **depth-first B&B**: explore the include child first, then the exclude child. Start with best profit 0. In this trace, update the best profit only at complete feasible leaves. (If updated at every feasible partial choice, profit 127 would be found earlier.)

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

**Answer:** take **J1 and J4**. Maximum profit = **127**. Schedule J4 in slot 1 and J1 in slot 2. The bounds are $152=100+27+15+10$, $137=127+10$, $125=100+15+10$, and $52=27+15+10$. The two unvisited branches have bounds 125 and 52, both below 127. The other include branches are infeasible. So no branch can give a larger profit.

> Memory trick: the bound is an optimistic guess. If even the guess cannot win, prune.

![Branch and bound tree for job sequencing](diagrams/b2-theory-13-bnb-job-tree.svg)

#### Q8(c)

**Question (transcribed):** Explain how the dynamic-programming method is used to solve the traveling salesperson problem. Using the cost matrix [[0, 20, 42, 35], [20, 0, 30, 34], [42, 30, 0, 12], [35, 34, 12, 0]] with start city 0, evaluate all relevant subsets of intermediate cities of size 1 and 2, show the partial DP table computed from these subsets, and determine the minimum tour cost based on these computed values.

**Answer.**

The travelling salesperson problem (**TSP**) asks for the cheapest tour that visits every city once and returns to the start (see [Chapter 8](../../../Chapter%208%20-%20Dynamic%20Programming/README.md)). Let $g(i,S)$ be the length of the shortest path that starts at city $i$, visits every city in the set $S$ exactly once, and then returns to start city 0. Try each possible next city $j\in S$:

$$
g(i,\varnothing)=C_{i0},\qquad g(i,S)=\min_{j\in S}\big\{C_{ij}+g(j,S\setminus\{j\})\big\}
$$

The final answer is $g(0,\{1,2,3\})=\min_{1\le j\le3}\{C_{0j}+g(j,\{1,2,3\}\setminus\{j\})\}$. (This answer keeps the question's 0-based city numbers, so the start city is 0.)

The given cost matrix $C$ is for cities 0, 1, 2, and 3:

| From/to | 0 | 1 | 2 | 3 |
|---------|---|---|---|---|
| 0 | 0 | 20 | 42 | 35 |
| 1 | 20 | 0 | 30 | 34 |
| 2 | 42 | 30 | 0 | 12 |
| 3 | 35 | 34 | 12 | 0 |

**Subsets of size 0** (return directly to city 0):

- $g(1,\varnothing)=C_{10}=20$
- $g(2,\varnothing)=C_{20}=42$
- $g(3,\varnothing)=C_{30}=35$

**Subsets of size 1:**

- $g(1,\{2\})=C_{12}+g(2,\varnothing)=30+42=72$
- $g(1,\{3\})=C_{13}+g(3,\varnothing)=34+35=69$
- $g(2,\{1\})=C_{21}+g(1,\varnothing)=30+20=50$
- $g(2,\{3\})=C_{23}+g(3,\varnothing)=12+35=47$
- $g(3,\{1\})=C_{31}+g(1,\varnothing)=34+20=54$
- $g(3,\{2\})=C_{32}+g(2,\varnothing)=12+42=54$

**Subsets of size 2:**

$$
g(1,\{2,3\})=\min(30+47,\ 34+54)=77
$$

$$
g(2,\{1,3\})=\min(30+69,\ 12+54)=66
$$

$$
g(3,\{1,2\})=\min(34+72,\ 12+50)=62
$$

**Final calculation** (choose the first city after 0):

$$
g(0,\{1,2,3\})=\min(20+77,\ 42+66,\ 35+62)=\min(97,108,97)=97
$$

**Arrow-guided subset table:**

| State | Candidate arrows | Chosen arrow | Stored cost |
| :---: | :--- | :---: | :---: |
| $g(1,\{2,3\})$ | $1 \rightarrow 2: 30+47=77$, $1 \rightarrow 3: 34+54=88$ | $1 \rightarrow 2$ | 77 |
| $g(2,\{1,3\})$ | $2 \rightarrow 1: 30+69=99$, $2 \rightarrow 3: 12+54=66$ | $2 \rightarrow 3$ | 66 |
| $g(3,\{1,2\})$ | $3 \rightarrow 1: 34+72=106$, $3 \rightarrow 2: 12+50=62$ | $3 \rightarrow 2$ | 62 |
| Final from city 0 | $0 \rightarrow 1: 97$, $0 \rightarrow 2: 108$, $0 \rightarrow 3: 97$ | $0 \rightarrow 1$ (tie with $0 \rightarrow 3$) | **97** |

**Minimum tour cost: 97.** One optimal tour is $0\to1\to2\to3\to0$, with cost $20+30+12+35=97$. Subset DP takes $\Theta(n^2 2^n)$ time and $\Theta(n2^n)$ space.

> Memory trick: the state is (where I am, which cities are left). Try every next city.

![Held-Karp DP states for the source matrix, starting at city 0](diagrams/b2-theory-14-tsp-subsets.svg)

---

## Verification

Run `python tools/verify_b2_theory.py` from the repository root to check the numerical tables, search traces and bounds, exhaustive small-instance optima, local links, all 24 question diagrams, and all 25 SVG/Excalidraw pairs (including the roadmap). These read-only checks supplement the review; they do not prove every prose statement.

## Quick Revision

| Topic | One-line memory |
|-------|-----------------|
| Time vs space | Time = number of steps; space = memory used (auxiliary space = extra memory) |
| Master theorem | Compare $f(n)$ with the watershed function $n^{\log_b a}$; if they match, multiply by $\log n$ |
| $T(n/3) + \log n$ | $\Theta(\log^2 n)$ (Case 2 with $k=1$) |
| P, NP, NP-hard, NP-complete | P = solve fast; NP = verify fast; NP-complete = NP and NP-hard |
| BFS shortest path | Level by level with a queue; mark visited when enqueued; first visit = shortest distance (unweighted) |
| Topological order | Every arrow goes forward; DFS finish stack popped from the right, or Kahn's indegree-0 removal |
| Linear vs binary search | 5 vs 3 comparisons for 511; binary search needs a sorted array; eight-item worst case is 4 |
| Strassen | 7 block products instead of 8; $T(n) = 7T(n/2) + \Theta(n^2)$ |
| Insertion vs bubble | Insertion takes $\Theta(n+I)$ for $I$ inversions; bubble sort can still need many passes |
| Quick sort | Partition around the pivot; last-element pivot gives $[1005, 1010, 1023, 1040, 1055]$ |
| Merge sort | Split in half, merge sorted halves, $\Theta(n \log n)$, needs extra space |
| Greedy | Candidate, selection, feasibility, objective, solution; needs greedy choice + optimal substructure (coins $4,3,1$ fail) |
| Fractional knapsack | Sort by value/weight ratio; take a fraction of the last item; value 240 |
| Kruskal | Sort edges, `FIND`/`UNION` skips cycles, stop at $V - 1$ edges; total 14 (confirm weights) |
| DP | Five parts: state, recurrence, base case, table order, final answer; Fibonacci in $\Theta(n)$ |
| Floyd-Warshall | $D^{(k)}[i,j]=\min(D^{(k-1)}[i,j],\ D^{(k-1)}[i,k]+D^{(k-1)}[k,j])$; $\Theta(n^3)$; $d(1,4) = 9$ |
| LCS | $c[i,j]$: match $\nwarrow$ + 1; else larger of $\uparrow$ and $\leftarrow$ (tie: up); LCS = GTAB, length 4 |
| Graph colouring | Colour in order, check neighbours, backtrack on dead end |
| LC-search | Expand the node with the best bound first; prune when $ub \le$ best |
| N-Queens | Row by row; check column and diagonals; 10 solutions for $N = 5$ |
| Decision vs optimization | Yes/no question vs find the best value |
| Branch and bound | A bound skips branches that cannot win; an admissible estimate never throws away the best answer |
| TSP DP | $g(i,S) = \min_j [C_{ij} + g(j, S \setminus j)]$; minimum tour 97 |

---

[Previous: 1st Batch Theory](../../1st%20Batch/Theory/README.md) | [Chapter 0 - Previous Year Questions](../../README.md) | [Home](../../../README.md) | [Next: 2nd Batch Lab Final](../Lab%20Final/README.md)
