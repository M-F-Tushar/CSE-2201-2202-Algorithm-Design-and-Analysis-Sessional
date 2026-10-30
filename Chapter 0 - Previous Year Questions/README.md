# Chapter 0 - Previous Year Questions

[Previous: Root README](../README.md) | [Home](../README.md) | [Next: Chapter 1 - Introduction and Algorithm Foundations](../Chapter%201%20-%20Introduction%20and%20Algorithm%20Foundations/README.md)

---

This chapter serves as the central question bank and exam-preparation portal for CSE 2201 (Theory) and CSE 2202 (Sessional). It contains complete, diagram-backed solutions to previous-year university final examinations, lab finals, class tests, and hands-on lab practice programs in C++.

Every solved problem provides step-by-step working, algorithmic dry runs, complexity analysis, and direct cross-links to the corresponding conceptual theory chapters.

---

## Table of Contents

1. [Overview](#1-overview)
2. [1st Batch Materials](#2-1st-batch-materials)
   - [1st Batch Theory Answers](#1st-batch-theory-answers)
   - [1st Batch Lab Final](#1st-batch-lab-final)
3. [2nd Batch Materials](#3-2nd-batch-materials)
   - [2nd Batch Theory Answers](#2nd-batch-theory-answers)
   - [2nd Batch Lab Final](#2nd-batch-lab-final)
4. [3rd Batch Class Tests](#4-3rd-batch-class-tests)
5. [Lab Practice Programs (C++)](#5-lab-practice-programs-c)
6. [Exam Strategy and Cross-Reference Map](#6-exam-strategy-and-cross-reference-map)

---

## 1. Overview

The previous-year materials are organized across batches and formats:

| Batch / Category | Type | Coverage | Primary Link |
| :--- | :--- | :--- | :--- |
| **1st Batch** | Theory Final | 2023 Final Exam (8 questions, 27 parts, answer 6 of 8 = 210 marks; 280 marks total paper) | [1st Batch Theory README](1st%20Batch/Theory/README.md) |
| **1st Batch** | Lab Final | 10 classic lab final algorithmic problems with complete C++ implementations | [1st Batch Lab Final README](1st%20Batch/Lab%20Final/README.md) |
| **2nd Batch** | Theory Final | Complete final examination paper (8 questions, 24 parts) | [2nd Batch Theory README](2nd%20Batch/Theory/README.md) |
| **2nd Batch** | Lab Final | 3 core lab problems (Distinct elements, Max subarray sum, Linear search) | [2nd Batch Lab Final README](2nd%20Batch/Lab%20Final/README.md) |
| **3rd Batch** | Class Tests | 4 Class Tests (CT1–CT4, 20 marks each = 80 marks total) | [3rd Batch CT README](3rd%20Batch/CT/README.md) |
| **Lab Practice** | Source Code | 12 C++ programs for lab final practice & trial problems | [Lab Practice Directory](Lab%20Practice/) |

---

## 2. 1st Batch Materials

### 1st Batch Theory Answers

Comprehensive solutions to the 2023 CSE 2201 Final Examination:

- **Section A:**
  - **Q1:** Algorithm design foundations, time and space complexity, asymptotic bounds ($O, \Omega, \Theta$).
  - **Q2:** Recurrences by substitution and Master Theorem, loop analysis.
  - **Q3:** Divide-and-conquer recurrences, merge sort, quicksort partition, and heapsort.
  - **Q4:** Greedy strategy, memoization vs. tabulation, Kruskal's MST.
- **Section B:**
  - **Q5:** Backtracking paradigms: $N$-Queens, Subset Sum, Hamiltonian Circuit.
  - **Q6:** Dynamic programming: 0/1 Knapsack, grid path counting, Coin Change.
  - **Q7:** Shortest paths (Dijkstra negative-edge failure vs Bellman-Ford trace), Algorithm optimality, and 0/1 Knapsack by DP.
  - **Q8:** Complexity classes ($\text{P}, \text{NP}, \text{NPC}, \text{NP-Hard}$), Decision vs. Optimization, Dijkstra's algorithm.

📂 Detailed document: [1st Batch Theory Guide](1st%20Batch/Theory/README.md)

### 1st Batch Lab Final

Step-by-step problem statements, logic breakdowns, and clean C++ implementations for 10 lab final problems:

1. [Linear and Binary Search](1st%20Batch/Lab%20Final/README.md#1-linear-and-binary-search)
2. [Iterative and Recursive Merge Sort](1st%20Batch/Lab%20Final/README.md#2-iterative-and-recursive-merge-sort)
3. [Iterative and Recursive Quick Sort](1st%20Batch/Lab%20Final/README.md#3-iterative-and-recursive-quick-sort)
4. [Greedy Change-Making](1st%20Batch/Lab%20Final/README.md#4-greedy-change-making)
5. [Greedy Fractional Knapsack](1st%20Batch/Lab%20Final/README.md#5-greedy-fractional-knapsack)
6. [Fibonacci by Recursion and DP](1st%20Batch/Lab%20Final/README.md#6-fibonacci-by-recursion-and-dynamic-programming)
7. [Coin-Row Problem by DP](1st%20Batch/Lab%20Final/README.md#7-coin-row-problem-by-dynamic-programming)
8. [Change-Making by DP](1st%20Batch/Lab%20Final/README.md#8-change-making-by-dynamic-programming)
9. [Coin-Collecting Problem by DP](1st%20Batch/Lab%20Final/README.md#9-coin-collecting-problem-by-dynamic-programming)
10. [0/1 Knapsack Problem by DP](1st%20Batch/Lab%20Final/README.md#10-01-knapsack-by-dynamic-programming)

📂 Detailed document: [1st Batch Lab Final Guide](1st%20Batch/Lab%20Final/README.md)

---

## 3. 2nd Batch Materials

### 2nd Batch Theory Answers

Complete answers for the second sitting final theory examination:

- **Section A:**
  - **Q1:** Algorithm design foundations (Time vs Space complexity), Divide & Conquer vs Greedy paradigms, and asymptotic bounds for 4 recurrences.
  - **Q2:** Class $\text{P}$ vs $\text{NP}$, BFS unweighted shortest path, Activity DAG scheduling.
  - **Q3:** Searching vs traversing, Binary Search walkthrough, Strassen's matrix multiplication.
  - **Q4:** Insertion sort vs Bubble sort (nearly sorted array), Quicksort (Lomuto partitioning trace on employee IDs), and Merge sort divide-and-conquer.
- **Section B:**
  - **Q5:** Greedy choice property, Fractional Knapsack, Kruskal's MST algorithm.
  - **Q6:** Dynamic programming foundations, Floyd-Warshall all-pairs shortest paths, LCS.
  - **Q7:** Backtracking: Graph coloring (m-colorability), LC-search state tree, 4-Queens.
  - **Q8:** Decision vs Optimization, Branch and Bound (Admissible heuristic & Job sequencing with deadlines), and TSP via Held-Karp Subset DP.

📂 Detailed document: [2nd Batch Theory Guide](2nd%20Batch/Theory/README.md)

### 2nd Batch Lab Final

Structured solutions to the three core programming problems:

1. [Count Distinct Values](2nd%20Batch/Lab%20Final/README.md#1-count-distinct-values) — Sorting and frequency scanning ($O(n \log n)$).
2. [Maximum Sum Contiguous Subarray](2nd%20Batch/Lab%20Final/README.md#2-maximum-sum-of-a-contiguous-subarray) — Kadane's algorithm ($O(n)$).
3. [Search for an Element](2nd%20Batch/Lab%20Final/README.md#3-search-for-an-element) — Linear Search ($O(n)$) on an unsorted array printing "Yes" / "No".

📂 Detailed document: [2nd Batch Lab Final Guide](2nd%20Batch/Lab%20Final/README.md)

---

## 4. 3rd Batch Class Tests

Complete answers and step-by-step scoring breakdowns for Class Tests 01 through 04 (20 marks each, 80 marks total):

- **Class Test 1: Dynamic Programming**
  - Q1: Principle of Optimality definition and routing example.
  - Q2: Elements of DP (Overlapping subproblems & Optimal substructure) with Fibonacci.
  - Q3: Longest Common Subsequence (LCS) matrix computation.
  - Q4: 0/1 Knapsack bottom-up DP table construction.
- **Class Test 2: Graph Algorithms**
  - Q1: Topological Sort on Directed Acyclic Graph (DAG).
  - Q2: Bellman-Ford single-source shortest paths with edge relaxation passes.
  - Q3: Floyd-Warshall all-pairs shortest path matrix progression ($D^{(0)} \dots D^{(4)}$).
- **Class Test 3: Union-Find, Maximum Subarray, and Segment Tree**
  - Q1: Disjoint Set Union (DSU) and Union by Rank height bound.
  - Q2: Divide-and-Conquer Maximum Subarray Sum ($O(n \log n)$).
  - Q3: Segment Tree range-sum query and point update implementation.
- **Class Test 4: Backtracking and N-Queens**
  - Q1: State-Space Tree formulation and pruning condition.
  - Q2: Diagonal conflict constraints for the $N$-Queens problem ($|r_1 - r_2| = |c_1 - c_2|$).
  - Q3: Backtracking applications (Graph coloring, Hamiltonian path, Subset sum).
  - Q4: Recursive backtracking algorithm for $N$-Queens.

📂 Detailed document: [3rd Batch Class Tests Guide](3rd%20Batch/CT/README.md)

---

## 5. Lab Practice Programs (C++)

Standalone, runnable C++ source files for essential algorithms tested during sessional examinations:

| Program File | Topic | Paradigm | Complexity |
| :--- | :--- | :--- | :---: |
| [`0_1_knapsack.cpp`](Lab%20Practice/0_1_knapsack.cpp) | 0/1 Knapsack | Dynamic Programming | $O(nW)$ |
| [`Backtracking.cpp`](Lab%20Practice/Backtracking.cpp) | $N$-Queens Problem | Backtracking | Exponential |
| [`Connected Component.cpp`](Lab%20Practice/Connected%20Component.cpp) | Connected Components | BFS / DFS Traversal | $O(V + E)$ |
| [`Disjoint Kruskal.cpp`](Lab%20Practice/Disjoint%20Kruskal.cpp) | Minimum Spanning Tree | Greedy + DSU | $O(E \log E)$ |
| [`Disjoint Set Cycle.cpp`](Lab%20Practice/Disjoint%20Set%20Cycle.cpp) | Cycle Detection | Disjoint Set Union (Naive) | $O(EV)$ ($O(E\alpha(V))$ with rank & path compression) |
| [`Floyd Warshall.cpp`](Lab%20Practice/Floyd%20Warshall.cpp) | All-Pairs Shortest Path | Dynamic Programming | $O(V^3)$ |
| [`Fractional Knapsack.cpp`](Lab%20Practice/Fractional%20Knapsack.cpp) | Fractional Knapsack | Greedy Method | $O(n \log n)$ |
| [`lcs.cpp`](Lab%20Practice/lcs.cpp) | Longest Common Subsequence | Dynamic Programming | $O(nm)$ |
| [`lis.cpp`](Lab%20Practice/lis.cpp) | Longest Increasing Subsequence | Dynamic Programming | $O(n^2)$ |
| [`Maximum Sum Subarray.cpp`](Lab%20Practice/Maximum%20Sum%20Subarray.cpp) | Maximum Subarray Sum | Divide & Conquer | $O(n \log n)$ |
| [`rabin_karp.cpp`](Lab%20Practice/rabin_karp.cpp) | Rabin-Karp String Matching | Rolling Hashing | $O(n + m)$ |
| [`Segment Tree.cpp`](Lab%20Practice/Segment%20Tree.cpp) | Range Sum Query | Divide & Conquer | $O(\log n)$ query |

---

## 6. Exam Strategy and Cross-Reference Map

To maximize exam performance, cross-reference solved questions with the theory chapters:

| Topic Area | Theory Chapter | Solved Question Reference |
| :--- | :--- | :--- |
| **Foundations & Asymptotics** | [Chapter 1](../Chapter%201%20-%20Introduction%20and%20Algorithm%20Foundations/README.md), [Chapter 2](../Chapter%202%20-%20Complexity%20Analysis%20and%20Asymptotic%20Notation/README.md) | 1st Batch Q1, 2nd Batch Q1 |
| **Recurrences & Master Theorem** | [Chapter 3](../Chapter%203%20-%20Recurrences%20Correctness%20and%20Loop%20Invariants/README.md) | 1st Batch Q2, 2nd Batch Q1(c) |
| **Searching & Traversal** | [Chapter 4](../Chapter%204%20-%20Searching%20and%20Basic%20Traversal/README.md) | 2nd Batch Q2(b), Q3(a), Lab Finals |
| **Sorting Algorithms** | [Chapter 5](../Chapter%205%20-%20Sorting%20Algorithms/README.md) | 1st Batch Q3, 2nd Batch Q4 |
| **Divide and Conquer** | [Chapter 6](../Chapter%206%20-%20Divide%20and%20Conquer/README.md) | 2nd Batch Q3(c) (Strassen), CT3 Q2–Q3 |
| **Greedy Algorithms** | [Chapter 7](../Chapter%207%20-%20Greedy%20Algorithms/README.md) | 1st Batch Q4, 2nd Batch Q5 |
| **Dynamic Programming** | [Chapter 8](../Chapter%208%20-%20Dynamic%20Programming/README.md) | 1st Batch Q6, 2nd Batch Q6, 2nd Batch Q8(c), CT1 Q1–Q4 |
| **Backtracking** | [Chapter 9](../Chapter%209%20-%20Backtracking/README.md) | 1st Batch Q5, 2nd Batch Q7, CT4 Q1–Q4 |
| **Branch and Bound** | [Chapter 10](../Chapter%2010%20-%20Branch%20and%20Bound/README.md) | 2nd Batch Q7(b), Q8(b) |
| **Graph Algorithms & Shortest Paths** | [Chapter 11](../Chapter%2011%20-%20Graph%20Algorithms/README.md) | 1st Batch Q7, Q8(c), CT2 Q1–Q3 |
| **Complexity Classes & NP** | [Chapter 15](../Chapter%2015%20-%20Lower%20Bound%20Theory%20and%20NP%20Completeness/README.md) | 1st Batch Q8(a)–(b), 2nd Batch Q2(a), Q8(a) |

---

[Previous: Root README](../README.md) | [Home](../README.md) | [Next: Chapter 1 - Introduction and Algorithm Foundations](../Chapter%201%20-%20Introduction%20and%20Algorithm%20Foundations/README.md)
