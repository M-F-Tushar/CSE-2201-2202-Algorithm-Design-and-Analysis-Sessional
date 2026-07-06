# CSE 2201, 2202: Algorithm Design and Analysis, Sessional - Syllabus

## Course Information

- **Course Code:** CSE 2201, CSE 2202
- **Course Title:** Algorithm Design and Analysis / Sessional
- **Credit Hours:** 3.0 + 1.5
- **Weekly Class Hours:** 3 hours + 3 hours
- **Course Type:** Theory + Sessional
- **Primary Reference:** Introduction to Algorithms, 4th Edition by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein
- **Primary Implementation Language:** Python

---

## Official Course Description

Efficient algorithm designing techniques: Divide-and-Conquer paradigm, Greedy method, Dynamic programming, Backtracking, Branch and bound; Flow algorithms; Approximation Algorithms; Introduction to parallel and randomized algorithms.

Search and traversal: Basic search and traversal technique, Shortest path problems, Topological sorting, Connected components, Spanning trees; Graph algorithms.

Analysis of algorithms: Complexity Analysis, Solving Recurrences, Correctness and loop invariants, Algebraic simplification and transformations, Lower bound theory, NP completeness, NP-hard and NP-complete problems.

---

## Course Objectives

The objectives of this course are to help students:

1. Understand the fundamentals of algorithm design and analysis.
2. Analyze time and space complexity.
3. Solve recurrence relations.
4. Prove algorithm correctness using loop invariants and induction.
5. Apply major algorithm design paradigms.
6. Implement common algorithms using Python.
7. Solve searching, sorting, graph, and optimization problems.
8. Understand lower bound theory and computational complexity.
9. Identify NP-hard and NP-complete problems.
10. Develop structured exam-oriented problem-solving skills.

---

## Detailed Syllabus Breakdown

---

## Chapter 0 - Previous Year Questions

### Topics

- Final exam questions
- Sessional questions
- Lab questions
- Topic-wise question mapping
- Solved previous-year questions
- Exam-focused problem analysis

### Purpose

This chapter works as a question bank and topic-mapping guide. It helps identify important exam topics and connects previous questions with corresponding repository chapters.

---

## Chapter 1 - Introduction and Algorithm Foundations

### Topics

- Definition of algorithm
- Algorithm vs program
- Properties of a good algorithm
- Input and output
- Definiteness
- Finiteness
- Effectiveness
- Algorithm design
- Algorithm analysis
- Importance of algorithms
- Overview of algorithm design paradigms

### Book Reference

- CLRS Chapter 1: The Role of Algorithms in Computing
- CLRS Chapter 2: Getting Started

---

## Chapter 2 - Complexity Analysis and Asymptotic Notation

### Topics

- Time complexity
- Space complexity
- Input size
- Running time
- Best-case analysis
- Average-case analysis
- Worst-case analysis
- Growth of functions
- Big-O notation
- Big-Omega notation
- Big-Theta notation
- Algebraic simplification
- Common complexity classes

### Book Reference

- CLRS Chapter 2.2: Analyzing Algorithms
- CLRS Chapter 3: Characterizing Running Times
- CLRS Appendix A: Summations

---

## Chapter 3 - Recurrences Correctness and Loop Invariants

### Topics

- Recurrence relations
- Recurrences in recursive algorithms
- Substitution method
- Recursion-tree method
- Master theorem
- Correctness of algorithms
- Loop invariants
- Mathematical induction
- Initialization
- Maintenance
- Termination
- Correctness proof writing

### Book Reference

- CLRS Chapter 2.1: Insertion Sort and Loop Invariants
- CLRS Chapter 4: Divide-and-Conquer
- CLRS Appendix A: Summations

---

## Chapter 4 - Searching and Basic Traversal

### Topics

- Searching vs traversal
- Linear search
- Binary search
- Iterative binary search
- Recursive binary search
- Number of comparisons
- Best-case analysis
- Average-case analysis
- Worst-case analysis
- Basic traversal techniques
- Introductory graph traversal

### Book Reference

- CLRS Chapter 2: Getting Started
- CLRS Chapter 20.1: Representations of Graphs
- CLRS Chapter 20.2: Breadth-First Search
- CLRS Chapter 20.3: Depth-First Search

---

## Chapter 5 - Sorting Algorithms

### Topics

- Sorting problem
- Insertion sort
- Bubble sort
- Selection sort
- Merge sort
- Quick sort
- Heap sort
- Sorting stability
- In-place sorting
- Sorting comparison
- Lower bound of comparison sorting
- Best-case complexity
- Average-case complexity
- Worst-case complexity

### Book Reference

- CLRS Chapter 2.1: Insertion Sort
- CLRS Chapter 2.3: Merge Sort
- CLRS Chapter 6: Heapsort
- CLRS Chapter 7: Quicksort
- CLRS Chapter 8: Sorting in Linear Time

### Course Note

Bubble sort and selection sort are included as supplementary sorting algorithms because they are useful for comparison and exam-style analysis.

---

## Chapter 6 - Divide and Conquer

### Topics

- Divide-and-Conquer paradigm
- Divide step
- Conquer step
- Combine step
- Recursive problem solving
- Binary search
- Merge sort
- Quick sort
- Strassen matrix multiplication
- Divide-and-conquer recurrence analysis
- Advantages and limitations of divide-and-conquer

### Book Reference

- CLRS Chapter 2.3: Designing Algorithms
- CLRS Chapter 4: Divide-and-Conquer
- CLRS Chapter 7: Quicksort

---

## Chapter 7 - Greedy Algorithms

### Topics

- Greedy method
- Greedy-choice property
- Optimal substructure
- Local optimum vs global optimum
- When greedy works
- When greedy fails
- Activity selection
- Fractional knapsack
- Change-making problem using greedy method
- Huffman coding
- Minimum spanning tree
- Prim algorithm
- Kruskal algorithm
- Dijkstra algorithm as a greedy shortest-path algorithm

### Book Reference

- CLRS Chapter 15: Greedy Algorithms
- CLRS Chapter 21: Minimum Spanning Trees
- CLRS Chapter 22.3: Dijkstra's Algorithm

### Course Note

Fractional knapsack and greedy change-making are included because they are common university algorithm-course and exam problems.

---

## Chapter 8 - Dynamic Programming

### Topics

- Dynamic programming concept
- Overlapping subproblems
- Optimal substructure
- Memoization
- Tabulation
- Fibonacci using recursion and DP
- Coin-row problem
- Change-making problem using DP
- Coin-collecting problem
- 0/1 knapsack problem
- Longest common subsequence
- Floyd-Warshall algorithm
- Traveling salesperson problem using DP
- DP table construction
- DP trace-back method

### Book Reference

- CLRS Chapter 14: Dynamic Programming
- CLRS Chapter 23.2: Floyd-Warshall Algorithm
- CLRS Chapter 35.2: Traveling-Salesperson Problem
- CLRS Chapter 35.5: Subset-Sum Problem

### Course Note

Fibonacci, coin-row, coin-collecting, change-making, and 0/1 knapsack are included because they are common lab, sessional, and exam-oriented dynamic programming problems.

---

## Chapter 9 - Backtracking

### Topics

- Backtracking concept
- State-space tree
- Promising function
- Feasible solution
- Candidate solution
- Solution space
- N-Queens problem
- Graph coloring problem
- Subset-sum problem
- Hamiltonian circuit problem
- Backtracking trace and dry run

### Book Reference

CLRS does not contain a dedicated chapter on backtracking. Use course lectures and previous questions as the primary reference.

Supporting references:

- CLRS Chapter 34: NP-Completeness
- CLRS Chapter 35.5: Subset-Sum Problem
- CLRS Appendix B: Graphs and Trees

---

## Chapter 10 - Branch and Bound

### Topics

- Branch and bound concept
- Difference between backtracking and branch and bound
- Bounding function
- Cost function
- State-space tree
- FIFO branch and bound
- LIFO branch and bound
- LC-search
- 0/1 knapsack using LC-search
- Job sequencing using branch and bound
- Traveling salesperson problem using branch and bound

### Book Reference

CLRS does not contain a dedicated chapter on branch and bound. Use course lectures and previous questions as the primary reference.

Supporting references:

- CLRS Chapter 14: Dynamic Programming
- CLRS Chapter 34: NP-Completeness
- CLRS Chapter 35.2: Traveling-Salesperson Problem

---

## Chapter 11 - Graph Algorithms

### Topics

- Graph terminology
- Directed graph
- Undirected graph
- Weighted graph
- Unweighted graph
- Graph representation
- Adjacency matrix
- Adjacency list
- Breadth-first search
- Depth-first search
- Topological sorting
- Connected components
- Strongly connected components
- Minimum spanning tree
- Prim algorithm
- Kruskal algorithm
- Shortest path problem
- Dijkstra algorithm
- Bellman-Ford algorithm
- Floyd-Warshall algorithm

### Book Reference

- CLRS Chapter 19: Data Structures for Disjoint Sets
- CLRS Chapter 20: Elementary Graph Algorithms
- CLRS Chapter 21: Minimum Spanning Trees
- CLRS Chapter 22: Single-Source Shortest Paths
- CLRS Chapter 23: All-Pairs Shortest Paths

---

## Chapter 12 - Flow Algorithms

### Topics

- Flow network
- Source and sink
- Capacity
- Flow
- Residual graph
- Augmenting path
- Max-flow problem
- Min-cut idea
- Ford-Fulkerson method
- Edmonds-Karp algorithm
- Bipartite matching

### Book Reference

- CLRS Chapter 24: Maximum Flow
- CLRS Chapter 25: Matchings in Bipartite Graphs

---

## Chapter 13 - Approximation Algorithms

### Topics

- Exact algorithm vs approximation algorithm
- Need for approximation algorithms
- Approximation ratio
- Performance guarantee
- Vertex cover approximation
- Traveling salesperson approximation
- Set cover approximation
- Relationship with NP-hard problems

### Book Reference

- CLRS Chapter 35: Approximation Algorithms
- CLRS Chapter 34: NP-Completeness

---

## Chapter 14 - Randomized and Parallel Algorithms

### Randomized Algorithms

#### Topics

- Randomized algorithm concept
- Probabilistic analysis
- Randomized quicksort
- Randomized selection
- Expected running time

### Parallel Algorithms

#### Topics

- Parallel algorithm basics
- Parallelism
- Work and span
- Fork-join model
- Parallel merge sort
- Parallel matrix multiplication overview

### Book Reference

- CLRS Chapter 5: Probabilistic Analysis and Randomized Algorithms
- CLRS Chapter 7.3: Randomized Quicksort
- CLRS Chapter 9.2: Selection in Expected Linear Time
- CLRS Chapter 26: Parallel Algorithms

---

## Chapter 15 - Lower Bound Theory and NP Completeness

### Lower Bound Theory

#### Topics

- Lower bound concept
- Comparison sorting lower bound
- Decision tree model
- Algorithm optimality

### Complexity Classes

#### Topics

- Polynomial time
- Class P
- Class NP
- NP-hard problems
- NP-complete problems
- Decision problem
- Optimization problem
- Polynomial-time verification
- Polynomial-time reduction
- Common NP-complete problems

### Book Reference

- CLRS Chapter 8.1: Lower Bounds for Sorting
- CLRS Chapter 34: NP-Completeness
- CLRS Chapter 35: Approximation Algorithms

---

## Laboratory and Sessional Focus

The practical and sessional part of this course should focus on implementing and analyzing algorithms such as:

- Linear search
- Binary search
- Merge sort
- Quick sort
- Greedy change-making
- Greedy knapsack
- Fibonacci using recursion and DP
- Coin-row problem
- Change-making using DP
- Coin-collecting problem
- 0/1 knapsack using DP
- Graph traversal
- MST algorithms
- Shortest path algorithms
- Backtracking problems
- Branch and bound problems

Each lab solution should include:

1. Problem statement
2. Theory
3. Algorithm or recurrence relation
4. C implementation
5. Sample input
6. Sample output
7. Dry run
8. Time complexity
9. Space complexity
10. Result analysis or comparison table

---

## Expected Learning Outcomes

After completing this course, students should be able to:

- Explain fundamental algorithmic concepts.
- Analyze time and space complexity.
- Use Big-O, Big-Omega, and Big-Theta notation.
- Solve recurrence relations.
- Prove algorithm correctness using loop invariants.
- Apply divide-and-conquer, greedy, dynamic programming, backtracking, and branch-and-bound techniques.
- Implement core algorithms using C.
- Solve graph traversal, shortest path, spanning tree, and flow problems.
- Understand randomized, parallel, and approximation algorithms.
- Explain lower bound theory.
- Differentiate between P, NP, NP-hard, and NP-complete problems.
- Solve previous-year exam problems with structured explanations.

---

## Recommended Study Order

1. Algorithm foundations
2. Complexity analysis
3. Recurrences and correctness
4. Searching and sorting
5. Divide and conquer
6. Greedy algorithms
7. Dynamic programming
8. Graph algorithms
9. Backtracking
10. Branch and bound
11. Flow algorithms
12. Approximation algorithms
13. Randomized and parallel algorithms
14. Lower bound theory and NP-completeness

---

## Notes

- The chapter structure of this repository follows the CSE 2201 syllabus rather than copying the book chapter order exactly.
- Book chapters are used as references for each repository chapter.
- Some topics, such as backtracking and branch and bound, should primarily follow class lectures and previous questions because CLRS does not provide dedicated chapters for them.
- Previous-year questions should be mapped to the corresponding repository chapter for exam preparation.
