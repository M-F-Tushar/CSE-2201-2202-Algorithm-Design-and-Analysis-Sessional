# Chapter 4: Searching and Basic Traversal

[Previous: Chapter 3 - Recurrences Correctness and Loop Invariants](../Chapter%203%20-%20Recurrences%20Correctness%20and%20Loop%20Invariants/README.md) | [Home](../README.md) | [Next: Chapter 5 - Sorting Algorithms](../Chapter%205%20-%20Sorting%20Algorithms/README.md)

---

Searching and traversal are basic techniques for moving through data. Searching tries to find a required item or answer. Traversal visits elements in a planned order so that each reachable element is processed.

This chapter keeps only the requested Searching and Basic Traversal topics. The main focus is introductory graph traversal using Breadth-First Search (BFS) and Depth-First Search (DFS), with simple explanations, algorithms, queue and stack behavior, examples, applications, and time complexity.

---

## Table of Contents

1. [Searching and Basic Traversal](#searching-and-basic-traversal)
2. [Basic Search and Traversal Techniques](#1-basic-search-and-traversal-techniques)
3. [Searching vs Traversal](#2-searching-vs-traversal)
4. [Linear Search and Binary Search](#3-linear-search-and-binary-search)
   - [Linear Search (Sequential Search)](#linear-search-sequential-search)
   - [Binary Search (Divide-and-Conquer Search)](#binary-search-divide-and-conquer-search)
   - [Sequential Search vs Binary Search Comparison](#sequential-vs-binary-search-comparison)
5. [Introductory Graph Traversal](#4-introductory-graph-traversal)
   - [Classroom Representation Sequence](#classroom-representation-sequence)
6. [Breadth-First Search (BFS)](#5-breadth-first-search-bfs)
   - [BFS Traversal Graph](#bfs-traversal-graph)
   - [BFS Idea](#bfs-idea)
   - [BFS Instruction Algorithm](#bfs-instruction-algorithm)
   - [BFS Algorithm](#bfs-algorithm)
   - [Queue Implementation](#queue-implementation)
   - [BFS Traversal Walkthrough](#bfs-traversal-walkthrough)
   - [BFS Complexity Analysis](#bfs-complexity-analysis)
   - [Basic Applications of BFS](#basic-applications-of-bfs)
7. [Depth-First Search (DFS)](#6-depth-first-search-dfs)
   - [DFS Traversal Graph](#dfs-traversal-graph)
   - [DFS Idea](#dfs-idea)
   - [DFS Instruction Algorithm](#dfs-instruction-algorithm)
   - [Recursive Version](#recursive-version)
   - [Stack-Based Version](#stack-based-version)
   - [DFS Traversal Walkthrough](#dfs-traversal-walkthrough)
   - [DFS Complexity Analysis](#dfs-complexity-analysis)
   - [Basic Applications of DFS](#basic-applications-of-dfs)
8. [BFS vs DFS Quick Comparison](#7-bfs-vs-dfs-quick-comparison)
9. [Recommended Study Sequence](#8-recommended-study-sequence)
10. [Analyze Time Complexity of BFS and DFS](#9-analyze-time-complexity-of-bfs-and-dfs)
11. [Final Notes](#final-notes)

---

## Searching and Basic Traversal

Searching and traversal both move through data, but their goals are different.

- **Searching** asks: "Where is the required item?"
- **Traversal** asks: "How can we visit every required element?"

In graph problems, traversal is often the foundation for searching. If we know how to visit vertices correctly, we can also search for a target vertex, a path, a connected component, or another property.

The two most important basic graph traversal techniques are:

- **Breadth-First Search (BFS):** visits vertices level by level using a queue.
- **Depth-First Search (DFS):** goes as deep as possible before backtracking, using recursion or a stack.

### Visual Map: Search and Traversal Flow

![Searching vs Traversal - Decision and Process Flow](diagrams/ch4-01-search-traversal-flow.svg)

---

## 1. Basic Search and Traversal Techniques

A **search technique** checks elements until it finds the required target or proves that the target is not reachable.

A **traversal technique** visits elements in a controlled order. In a graph, this usually means starting from one vertex and visiting all vertices reachable from it.

Most basic searching and traversal methods use four common ideas:

| Idea | Meaning |
| :--- | :--- |
| Current element | The element being checked or processed now |
| Frontier | The waiting collection of elements to visit next |
| Visited set | A record of elements already discovered |
| Processing step | The work done when an element is visited |

The **frontier** controls the traversal order.

| Frontier type | Technique | Behavior |
| :--- | :--- | :--- |
| Queue | BFS | First discovered vertex is processed first |
| Stack | DFS | Most recently discovered vertex is processed first |
| Recursion call stack | DFS | Function calls naturally go deep before returning |

Generic graph traversal pattern:

```text
TRAVERSE(G, start)
1. create an empty frontier
2. mark start as visited
3. add start to the frontier
4. while the frontier is not empty:
5.     remove one vertex u from the frontier
6.     process u
7.     for each neighbor v of u:
8.         if v is not visited:
9.             mark v as visited
10.            add v to the frontier
```

If the frontier is a **queue**, this pattern becomes BFS. If the frontier is a **stack**, this pattern becomes DFS.

---

## 2. Searching vs Traversal

Searching and traversal are closely related, but they are not the same.

| Feature | Searching | Traversal |
| :--- | :--- | :--- |
| Main goal | Find a target or answer | Visit all reachable elements |
| Stopping condition | Usually stops when the target is found | Usually stops when all reachable elements are visited |
| Output | Target position, true/false, path, or value | Visiting order, component, tree, or processed data |
| Example question | "Is vertex G reachable from A?" | "Visit every vertex reachable from A." |
| Common tools | BFS, DFS, linear search, binary search | BFS, DFS, tree traversal |

Example:

- If we use BFS from vertex $A$ and stop when vertex $G$ is found, it is a **search**.
- If we use BFS from vertex $A$ and continue until no reachable vertex remains, it is a **traversal**.

### Visual Map: Same Movement, Different Purpose

![Same Graph Movement, Different Algorithmic Purpose](diagrams/ch4-02-movement-purpose.svg)

---

## 3. Linear Search and Binary Search

Before traversing structured networks and graphs, searching begins on linear sequences (arrays and lists). The two primary paradigms are sequential inspection and divide-and-conquer elimination.

### Linear Search (Sequential Search)

**Linear search** scans each array element sequentially from beginning to end until either the target element is found or the end of the array is reached.

#### Algorithm
```text
LINEAR-SEARCH(A, n, key)
1. for i = 0 to n - 1:
2.     if A[i] == key:
3.         return i        // Target found at index i
4. return -1               // Target not present
```

#### Properties
- **Data requirement:** None. Works on unsorted, sorted, and arbitrary sequences.
- **Best-case complexity:** $O(1)$ (target located at index 0).
- **Worst-case complexity:** $O(n)$ (target at the last position or absent).
- **Average-case complexity:** $O(n)$ ($n/2$ comparisons on average).
- **Space complexity:** $O(1)$ auxiliary memory.

---

### Binary Search (Divide-and-Conquer Search)

**Binary search** locates a target in a **sorted** array by repeatedly halving the search interval. It compares the target key to the middle element:
1. If the key equals the middle element, the search terminates successfully.
2. If the key is smaller than the middle element, the search continues in the left half.
3. If the key is larger, the search continues in the right half.

#### Iterative Algorithm
```text
BINARY-SEARCH(A, n, key)
1. low = 0
2. high = n - 1
3. while low <= high:
4.     mid = low + (high - low) / 2
5.     if A[mid] == key:
6.         return mid
7.     else if A[mid] < key:
8.         low = mid + 1
9.     else:
10.        high = mid - 1
11. return -1
```

#### Recurrence and Complexity
Each step discards half the remaining candidates with $O(1)$ comparison work:
$$
T(n) = T(n/2) + c, \qquad T(1) = 1
$$
By Master Theorem (Case 2, $a=1, b=2, k=0$) or expansion (as shown in [Chapter 3](../Chapter%203%20-%20Recurrences%20Correctness%20and%20Loop%20Invariants/README.md)):
$$
T(n) = \Theta(\log n)
$$

### Sequential vs Binary Search Comparison

| Dimension | Linear Search | Binary Search |
| :--- | :--- | :--- |
| **Input condition** | Unsorted or sorted arrays | **Must be sorted** |
| **Strategy** | Sequential scan ($1$ by $1$) | Divide and conquer (halves range each step) |
| **Worst-case time** | $\Theta(n)$ | $\Theta(\log n)$ |
| **Best-case time** | $\Theta(1)$ | $\Theta(1)$ |
| **Average-case time** | $\Theta(n)$ | $\Theta(\log n)$ |
| **Space complexity** | $O(1)$ | $O(1)$ iterative, $O(\log n)$ recursive |
| **Data structures** | Arrays, Linked Lists | Arrays (needs $O(1)$ random access) |

---

## 4. Introductory Graph Traversal

A **graph** is a collection of vertices and edges.

- A **vertex** is a point or node.
- An **edge** is a connection between two vertices.
- An **undirected graph** has edges that can be used in both directions.
- A **directed graph** has edges with a fixed direction.
- A **connected graph** has a path between every pair of vertices.
- A **disconnected graph** has at least one vertex that cannot be reached from another part of the graph.

Graph traversal means visiting vertices by following edges.

The most common graph representation for BFS and DFS is an **adjacency list**.

Example graph:

![Introductory Graph for Traversal Demonstrations](diagrams/ch4-03-intro-graph-traversal.svg)

Adjacency list for the graph:

| Vertex | Neighbors |
| :---: | :--- |
| A | B, C |
| B | A, D, E |
| C | A, F |
| D | B |
| E | B, G |
| F | C, G |
| G | E, F |

For a graph traversal, we normally maintain:

| Data | Purpose |
| :--- | :--- |
| `visited[v]` | Tells whether vertex `v` has already been discovered |
| `parent[v]` | Stores the vertex from which `v` was first reached |
| `distance[v]` | In BFS, stores the number of edges from the source |
| frontier | Queue for BFS or stack for DFS |

### Classroom Representation Sequence

For a graph-representation question, use the same order as the class notes:

1. Identify whether the graph is **directed or undirected** and **weighted or unweighted**.
2. List each vertex's neighbors as an adjacency list.
3. Fix one vertex order for the rows and columns.
4. Fill the adjacency matrix from that order. Use `1` for an unweighted edge and `0` when no edge exists.
5. For an undirected graph, check that the matrix is symmetric.

For the graph above, use the vertex order `A, B, C, D, E, F, G`.

```text
A: B, C
B: A, D, E
C: A, F
D: B
E: B, G
F: C, G
G: E, F
```

The adjacency matrix is then built one row at a time:

| From / To | A | B | C | D | E | F | G |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| B | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| C | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| D | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| E | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| F | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| G | 0 | 0 | 0 | 0 | 1 | 1 | 0 |

This representation is the starting point for the BFS and DFS traces below; always keep the neighbor order fixed while tracing.

### Traversing a Disconnected Graph

If a graph is disconnected, starting from one vertex may not visit every vertex. To traverse the whole graph, run BFS or DFS from every unvisited vertex.

```text
TRAVERSE-ALL(G)
1. for each vertex u in G:
2.     visited[u] = false
3. for each vertex u in G:
4.     if visited[u] == false:
5.         run BFS or DFS starting from u
```

This outer loop makes sure every connected part of the graph is covered.

---

## 5. Breadth-First Search (BFS)

**Breadth-First Search (BFS)** visits vertices level by level. It first visits the starting vertex, then all vertices at distance 1, then all vertices at distance 2, and so on.

BFS uses a **queue**, so the first discovered vertex is processed first.

### BFS Traversal Graph

Use this undirected graph for the BFS trace below. Process every adjacency list in alphabetical order.

![BFS Traversal on 7-Vertex Graph (Source A)](diagrams/ch4-04-bfs-traversal-graph.svg)

### BFS Idea

The main idea of BFS is simple:

1. Start from a source vertex.
2. Visit all immediate neighbors first.
3. Then visit neighbors of those neighbors.
4. Continue level by level until no reachable vertex remains.

Because BFS expands in layers, it finds the shortest path in an unweighted graph.

### Visual Map: BFS Level Movement

![BFS Level-by-Level Discovery and Queue Processing Order](diagrams/ch4-05-bfs-level-movement.svg)

### BFS Instruction Algorithm

1. Mark every vertex as unvisited. Mark the starting vertex as visited and put it into an empty queue.
2. Remove the vertex at the **front** of the queue and process it.
3. For every unvisited neighbor of that vertex, mark it visited and add it to the **back** of the queue.
4. Repeat steps 2 and 3 until the queue is empty. All reachable vertices have then been traversed.

### BFS Algorithm

```text
BFS(G, s)
1. for each vertex u in G:
2.     visited[u] = false
3.     parent[u] = NIL
4.     distance[u] = infinity
5. create an empty queue Q
6. visited[s] = true
7. distance[s] = 0
8. ENQUEUE(Q, s)
9. while Q is not empty:
10.    u = DEQUEUE(Q)
11.    process u
12.    for each vertex v in Adj[u]:
13.        if visited[v] == false:
14.            visited[v] = true
15.            parent[v] = u
16.            distance[v] = distance[u] + 1
17.            ENQUEUE(Q, v)
```

Important note: in BFS, a vertex is usually marked as visited when it is **enqueued**, not when it is dequeued. This prevents the same vertex from being inserted into the queue many times.

### Queue Implementation

A queue follows **FIFO** order: first in, first out.

| Queue operation | Meaning |
| :--- | :--- |
| `ENQUEUE(Q, x)` | Add `x` to the back of the queue |
| `DEQUEUE(Q)` | Remove and return the front element |
| `isEmpty(Q)` | Check whether the queue has no element |

BFS queue pattern:

```text
create empty queue Q
mark source as visited
ENQUEUE(Q, source)

while Q is not empty:
	u = DEQUEUE(Q)
	process u
	for each unvisited neighbor v of u:
		mark v as visited
		ENQUEUE(Q, v)
```

### BFS Traversal Walkthrough

Use the traversal graph above and start BFS from vertex $A$. Neighbors are considered in alphabetical order.

For an exam-friendly queue trace, write the initial queue, dequeue one vertex, enqueue only newly discovered neighbors, and record the resulting queue. Write the final traversal order separately. A vertex is marked visited as soon as it is enqueued, so it never appears in the queue twice.

Start with `Q = [A]`. The table follows the classroom format: list all discovered vertices, show the queue after the current vertex is processed (front first), and record the completed traversal.

| Vertices visited | Vertices in queue (front first) | Vertex traversal done |
| :--- | :--- | :---: |
| A, B, C | **B**, C | A |
| A, B, C, D, E | **C**, D, E | B |
| A, B, C, D, E, F | **D**, E, F | C |
| — | **E**, F | D |
| A, B, C, D, E, F, G | **F**, G | E |
| — | **G** | F |
| — | empty | G |

BFS traversal order from $A$:

```text
A, B, C, D, E, F, G
```

BFS distance values, grouped by level:

| Distance from A | Vertices |
| :---: | :--- |
| 0 | A |
| 1 | B, C |
| 2 | D, E, F |
| 3 | G |

### BFS Complexity Analysis

For an adjacency list representation:

| Part | Cost |
| :--- | :--- |
| Initialize all vertices | $O(V)$ |
| Enqueue and dequeue each vertex at most once | $O(V)$ |
| Scan all adjacency lists | $O(E)$ |
| Total time complexity | `O(V + E)` |
| Space complexity | $O(V)$ |

Here, $V$ is the number of vertices and $E$ is the number of edges.

BFS has time complexity `O(V + E)` because every vertex is processed once and every edge is checked through the adjacency lists.

### Basic Applications of BFS

| Application | How BFS helps |
| :--- | :--- |
| Reachability | Checks whether one vertex can be reached from another |
| Shortest path in an unweighted graph | Finds the minimum number of edges from the source |
| Level order traversal | Visits vertices by distance level |
| Connected components | Repeated BFS can find all connected parts of a graph |
| Minimum moves problems | Models each state as a vertex and each move as an edge |

BFS is usually preferred when the problem asks for the nearest answer, the smallest number of steps, or level-by-level exploration.

---

## 6. Depth-First Search (DFS)

**Depth-First Search (DFS)** explores one path as far as possible before returning to try another path.

DFS can be implemented in two common ways:

- **Recursive DFS:** uses the function call stack.
- **Stack-based DFS:** uses an explicit stack data structure.

### DFS Traversal Graph

Use this same undirected graph for the DFS trace below. Process every adjacency list in alphabetical order.

![DFS Traversal on 7-Vertex Graph (Source A)](diagrams/ch4-06-dfs-traversal-graph.svg)

### DFS Idea

The main idea of DFS is:

1. Start from a vertex.
2. Visit one unvisited neighbor.
3. Continue going deeper from that neighbor.
4. When there is no unvisited neighbor, backtrack.
5. Try another unvisited branch.

DFS is useful when we need to explore complete paths, detect structure, or process graph components.

### Visual Map: DFS Deep Movement and Backtracking

![DFS Deep Movement and Backtracking Trace](diagrams/ch4-07-dfs-backtracking.svg)

### DFS Instruction Algorithm

DFS can be executed using either a recursive call stack or an explicit stack data structure:

- **Recursive DFS:** Automatically processes the deepest unvisited branch first. When at vertex $u$, DFS immediately makes a recursive call to its first unvisited neighbor $v$ (setting $\text{parent}[v] = u$), only exploring alternative branches after the recursive call returns.
- **Stack-based DFS (Standard / Mark-on-Pop):** Vertices are pushed onto an explicit stack. A vertex is marked visited when **popped** from the stack, exactly matching recursive DFS traversal paths and parent relationships.
- **Stack-based DFS (Mark-on-Push Variant):** Neighbors are marked visited immediately upon being pushed to prevent duplicate entries on the stack. Note that marking on push locks in parent pointers at push time rather than exploration time.

### Recursive Version

Recursive DFS is the simplest version to understand. The recursion automatically remembers where to return after a deep path finishes.

```text
DFS-RECURSIVE(G, u)
1. visited[u] = true
2. process u
3. for each vertex v in Adj[u]:
4.     if visited[v] == false:
5.         parent[v] = u
6.         DFS-RECURSIVE(G, v)
```

To start DFS from source vertex `s`:

```text
for each vertex u in G:
	visited[u] = false
	parent[u] = NIL

DFS-RECURSIVE(G, s)
```

#### Recursive Call-Stack Trace

For the traversal graph above, start at `A` and consider neighbors in alphabetical order. The most recent recursive call is shown first.

| Visited vertices | Recursive call stack (top first) | Current vertex / Action |
| :--- | :--- | :--- |
| A | `DFS(A)` | A (explore neighbor B) |
| A, B | `DFS(B)`, `DFS(A)` | B (explore neighbor D) |
| A, B, D | `DFS(D)`, `DFS(B)`, `DFS(A)` | D (dead end, return to B) |
| A, B, D | `DFS(B)`, `DFS(A)` | return from D; resume B (explore E) |
| A, B, D, E | `DFS(E)`, `DFS(B)`, `DFS(A)` | E (explore neighbor G) |
| A, B, D, E, G | `DFS(G)`, `DFS(E)`, `DFS(B)`, `DFS(A)` | G (explore neighbor F) |
| A, B, D, E, G, F | `DFS(F)`, `DFS(G)`, `DFS(E)`, `DFS(B)`, `DFS(A)` | F (Adj[F]=[C, G]; C is unvisited, call C) |
| A, B, D, E, G, F, C | `DFS(C)`, `DFS(F)`, `DFS(G)`, `DFS(E)`, `DFS(B)`, `DFS(A)` | C (Adj[C]=[A, F]; both visited, return) |
| A, B, D, E, G, F, C | `DFS(F)`, `DFS(G)`, `DFS(E)`, `DFS(B)`, `DFS(A)` | return from C; F checks G (visited), return |
| A, B, D, E, G, F, C | `DFS(G)`, `DFS(E)`, `DFS(B)`, `DFS(A)` | return from F; G finished, return |
| A, B, D, E, G, F, C | `DFS(E)`, `DFS(B)`, `DFS(A)` | return from G; E finished, return |
| A, B, D, E, G, F, C | `DFS(B)`, `DFS(A)` | return from E; B finished, return |
| A, B, D, E, G, F, C | `DFS(A)` | return from B; A checks C (already visited!) |
| A, B, D, E, G, F, C | empty | DFS finished |

For a disconnected graph, call `DFS-RECURSIVE` for every unvisited vertex.

```text
DFS-ALL(G)
1. for each vertex u in G:
2.     visited[u] = false
3.     parent[u] = NIL
4. for each vertex u in G:
5.     if visited[u] == false:
6.         DFS-RECURSIVE(G, u)
```

### Stack-Based Version

Stack-based DFS replaces recursion with an explicit stack.

A stack follows **LIFO** order: last in, first out.

| Stack operation | Meaning |
| :--- | :--- |
| `PUSH(S, x)` | Add `x` to the top of the stack |
| `POP(S)` | Remove and return the top element |
| `isEmpty(S)` | Check whether the stack has no element |

Iterative DFS pattern:

```text
DFS-STACK(G, s)
1. for each vertex u in G:
2.     visited[u] = false
3.     parent[u] = NIL
4. create an empty stack S
5. visited[s] = true
6. PUSH(S, s)
7. while S is not empty:
8.     u = POP(S)
9.     process u
10.    for each vertex v in Adj[u] in reverse order:
11.        if visited[v] == false:
12.            visited[v] = true
13.            parent[v] = u
14.            PUSH(S, v)
```

Mark a vertex as visited when it is pushed, so it cannot be placed on the stack twice. The reverse order is used only to make the stack version produce a similar visiting order to the recursive version when neighbors are listed alphabetically. Different valid DFS orders are possible if neighbors are considered in a different order.

> [!NOTE]
> **Mark-on-Push vs. Mark-on-Pop:**
> The iterative algorithm above uses the **mark-on-push** approach, which bounds the stack size to $O(V)$ by preventing any vertex from appearing in the stack more than once. However, because $C$ is pushed and marked by $A$ at step 1, $F$ later cannot explore edge $(F, C)$, which sets $\text{parent}[C] = A$.
> In contrast, the **standard recursive DFS** (and stack-based mark-on-pop DFS) explores $(F, C)$, setting $\text{parent}[C] = F$. Both visit all reachable vertices in valid DFS depth-first sequences, but produce different tree edges when cross-edges exist.

### DFS Traversal Walkthrough

Use the traversal graph above and start DFS from vertex $A$. Neighbors are considered in alphabetical order.

Follow the classroom DFS sequence: visit the current vertex, choose the first unvisited neighbor, continue until no choice remains, then explicitly backtrack to the most recent vertex with an unvisited neighbor.

Use the stack-based DFS trace below. Vertices are marked visited when pushed; the stack is shown with its top first.

| Vertices visited | Vertices in stack (top first) | Vertex traversal done |
| :--- | :--- | :---: |
| A, B, C | **B**, C | A |
| A, B, C, D, E | **D**, E, C | B |
| — | **E**, C | D |
| A, B, C, D, E, G | **G**, C | E |
| A, B, C, D, E, F, G | **F**, C | G |
| — | **C** | F |
| — | empty | C |

DFS traversal order from $A$:

```text
A, B, D, E, G, F, C
```

The exact DFS order can change if the adjacency list order changes. The important rule is that DFS keeps going deeper whenever an unvisited neighbor exists.

### DFS Complexity Analysis

For an adjacency list representation:

| Part | Cost |
| :--- | :--- |
| Initialize all vertices | $O(V)$ |
| Visit each vertex once | $O(V)$ |
| Scan all adjacency lists | $O(E)$ |
| Total time complexity | `O(V + E)` |
| Space complexity | $O(V)$ |

DFS has time complexity `O(V + E)` because each vertex is visited once and each edge is examined through the adjacency lists.

Space complexity is $O(V)$ because of the visited array and either the recursion call stack or the explicit stack.

### Basic Applications of DFS

| Application | How DFS helps |
| :--- | :--- |
| Reachability | Checks whether one vertex can be reached from another |
| Connected components | Repeated DFS can identify separate graph parts |
| Path finding | Explores possible paths from a source vertex |
| Cycle detection | Finds whether backtracking reaches an already active vertex |
| Topological ordering | Orders tasks in a directed acyclic graph |

DFS is usually preferred when the problem needs deep exploration, backtracking, or structural information about a graph.

---

## 7. BFS vs DFS Quick Comparison

| Feature | BFS | DFS |
| :--- | :--- | :--- |
| Full form | Breadth-First Search | Depth-First Search |
| Main behavior | Visits level by level | Goes deep, then backtracks |
| Data structure | Queue | Recursion stack or explicit stack |
| First vertices visited after source | All immediate neighbors | One full branch first |
| Shortest path in unweighted graph | Yes | Not guaranteed |
| Time complexity | `O(V + E)` | `O(V + E)` |
| Space complexity | $O(V)$ | $O(V)$ |
| Best for | Nearest answer, minimum edges, level order | Deep exploration, components, backtracking |

### Visual Map: BFS Queue vs DFS Stack

![BFS Queue vs DFS Stack Comparison](diagrams/ch4-08-bfs-queue-vs-dfs-stack.svg)

---

## 8. Recommended Study Sequence

Study this chapter in the following order:

1. Understand the difference between searching and traversal.
2. Learn the basic graph terms: vertex, edge, neighbor, path, connected graph, and disconnected graph.
3. Learn why `visited` is necessary in graph traversal.
4. Study BFS and its queue-based level movement.
5. Trace BFS manually on a small graph.
6. Study DFS recursively.
7. Trace DFS manually with backtracking.
8. Convert recursive DFS into stack-based DFS.
9. Compare BFS and DFS applications.
10. Practice calculating `O(V + E)` time complexity.

---

## 9. Analyze Time Complexity of BFS and DFS

BFS and DFS have the same asymptotic time complexity when the graph is stored using an adjacency list.

Let:

- $V$ = number of vertices.
- $E$ = number of edges.

Why the time complexity is `O(V + E)`:

| Reason | Explanation |
| :--- | :--- |
| Every vertex is initialized | This costs $O(V)$ |
| Every vertex is visited at most once | This costs $O(V)$ |
| Every adjacency list is scanned | Across the whole graph, this costs $O(E)$ |
| Total | $O(V) + O(E) = O(V + E)$ |

For an undirected graph, each edge appears in two adjacency lists, but this is still $O(E)$ because constant factors are ignored in asymptotic notation.

Final complexity summary:

| Algorithm | Data structure | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| BFS | Queue | `O(V + E)` | $O(V)$ |
| DFS recursive | Recursion call stack | `O(V + E)` | $O(V)$ |
| DFS stack-based | Explicit stack | `O(V + E)` | $O(V)$ |

---

## 10. Final Notes

BFS and DFS are the foundation of many graph algorithms. For this chapter, the most important points are:

- BFS uses a queue and explores level by level.
- DFS uses recursion or a stack and explores deeply before backtracking.
- Both BFS and DFS need a `visited` record to avoid repeated visits.
- Both BFS and DFS run in `O(V + E)` time with an adjacency list.
- BFS is better for nearest or shortest unweighted paths.
- DFS is better for deep exploration and backtracking-based structure.

---

[Previous: Chapter 3 - Recurrences Correctness and Loop Invariants](../Chapter%203%20-%20Recurrences%20Correctness%20and%20Loop%20Invariants/README.md) | [Home](../README.md) | [Next: Chapter 5 - Sorting Algorithms](../Chapter%205%20-%20Sorting%20Algorithms/README.md)
