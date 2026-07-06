# Chapter 8: Dynamic Programming

Welcome to the sessional guide on **Dynamic Programming** for the [CSE 2201 Algorithm Design and Analysis](file:///workspaces/CSE-2201-2202-Algorithm-Design-and-Analysis-Sessional/SYLLABUS.md) sessional course. This chapter covers the core concepts, mathematical recurrences, and step-by-step table updates for the required syllabus topics.

---

## Table of Contents

1. [Introduction to Dynamic Programming](#introduction-to-dynamic-programming)
2. [Fibonacci (Recursion and DP)](#1-fibonacci-recursion-and-dp)
3. [Coin-Row Problem](#2-coin-row-problem)
4. [Change-Making Problem (DP)](#3-change-making-problem-dp)
5. [Coin-Collecting Problem](#4-coin-collecting-problem)
6. [0/1 Knapsack Problem](#5-01-knapsack-problem)
7. [Longest Common Subsequence (LCS)](#6-longest-common-subsequence-lcs)
8. [Floyd-Warshall Algorithm](#7-floyd-warshall-algorithm)
9. [Traveling Salesperson Problem (TSP) using DP](#8-traveling-salesperson-problem-tsp-using-dp)
10. [Summary and Quick Reference](#summary-and-quick-reference)

---

## Introduction to Dynamic Programming

### 💡 The Easiest Explanation
Imagine you are walking up a flight of stairs and counting the steps. If someone stops you halfway and asks, "How many steps have you taken so far?" you do not go back to the bottom and start counting from 1. You remember that you are on step 10, and if you take 1 more step, you know you are on step 11.

**Dynamic Programming (DP)** is exactly that: it is the art of **remembering answers to smaller overlapping questions** so that when you face a larger question, you can build on top of your saved answers instead of starting from scratch. In this context, "Programming" does not mean writing computer code; it refers to a **tabular method** (solving problems by filling in a table of values).

### ⚔️ Divide-and-Conquer vs. Dynamic Programming
*   **Divide-and-Conquer** partitions a problem into **disjoint** (completely separate and independent) subproblems, solves them recursively, and then combines their solutions (e.g., [Merge Sort](file:///workspaces/CSE-2201-2202-Algorithm-Design-and-Analysis-Sessional/Chapter%205%20-%20Sorting%20Algorithms/README.md)).
*   **Dynamic Programming** is used when the subproblems **overlap**—that is, when subproblems share smaller sub-subproblems. In these cases, Divide-and-Conquer does redundant work, solving the same sub-subproblem repeatedly. DP avoids this by solving each subproblem exactly once and referencing its cached result in a table.

---

## 1. Fibonacci (Recursion and DP)

### 1. The Real-Life Analogy
Imagine counting rabbit pairs. Every month, a pair of rabbits produces a new pair, which itself starts producing after two months. The population size follows the Fibonacci sequence. If you calculate the population size for month 5 by drawing out the complete ancestry tree, you end up counting the descendants of month 2 and month 3 multiple times. Instead, you can write the values month-by-month in a logbook.

### 2. Inputs and Outputs
*   **Input:** An integer $n$ (the month or term index).
*   **Output:** The $n$-th Fibonacci number $F_n$.

### 3. The Core Struggle
The naive recursive relation is $F_n = F_{n-1} + F_{n-2}$. If we compute $F_5$ recursively:
*   We need $F_4$ and $F_3$.
*   To compute $F_4$, we need $F_3$ and $F_2$. (Notice $F_3$ is already computed twice).
*   This duplicates computations, leading to an exponential running time of $O(2^n)$. For $F_{50}$, the computer would perform over $1.1$ trillion additions!

### 4. The Subproblem Decomposition
The $n$-th term is computed by summing the two immediately preceding terms:
$$F_n = F_{n-1} + F_{n-2} \quad \text{for } n \ge 2, \text{ with } F_0 = 0, F_1 = 1$$

### 5. The Memory Table
*   We use a 1D array $F[0 \dots n]$.
*   $F[i]$ stores the Fibonacci value of term $i$.
*   We fill the array from index 2 up to $n$ using basic addition.

### 6. Walkthrough with Small Numbers
Let's find the 5th Fibonacci number ($F_5$):
*   $F[0] = 0$ (Base case)
*   $F[1] = 1$ (Base case)
*   $F[2] = F[1] + F[0] = 1 + 0 = 1$
*   $F[3] = F[2] + F[1] = 1 + 1 = 2$
*   $F[4] = F[3] + F[2] = 2 + 1 = 3$
*   $F[5] = F[4] + F[3] = 3 + 2 = 5$
*   The final output is **5**.

### 7. Core Algorithm

#### 📘 Algorithm 8.1: Fibonacci DP

> **Purpose:** Calculate the $n$-th Fibonacci number in linear time by storing intermediate values in a table.

```
Algorithm 8.1: FIBONACCI-DP(n)
────────────────────────────────────────────
1. Let F[0...n] be a new array
2. Set F[0] := 0
3. Set F[1] := 1
4. Repeat Step 5 for i = 2 to n:
5.     Set F[i] := F[i-1] + F[i-2]
   [End of Step 4 loop]
6. Return F[n]
```

### 8. Visual State Transition (Mermaid)

Here are the two representations showing the redundant subproblem tree and how tabulation fills values linearly:

```mermaid
graph TD
    subgraph "Naive Overlapping Recursion Tree"
        F5["F(5)"] --> F4["F(4)"]
        F5 --> F3_A["F(3) ❌"]
        F4 --> F3_B["F(3)"]
        F4 --> F2_A["F(2) ❌"]
        F3_B --> F2_B["F(2)"]
        F3_B --> F1_A["F(1)"]
        F2_B --> F1_B["F(1)"]
        F2_B --> F0_A["F(0)"]
    end
    
    style F3_A fill:#e74c3c,color:#fff
    style F2_A fill:#e74c3c,color:#fff
```

```mermaid
graph LR
    subgraph "Tabulation Table Calculation Flow"
        direction LR
        Cell0["F[0] = 0"] -.-> Cell2
        Cell1["F[1] = 1"] --> Cell2["F[2] = 1"]
        Cell1 -.-> Cell3
        Cell2 --> Cell3["F[3] = 2"]
        Cell2 -.-> Cell4
        Cell3 --> Cell4["F[4] = 3"]
        Cell3 -.-> Cell5
        Cell4 --> Cell5["F[5] = 5"]
        
        style Cell0 fill:#f5f5f5,stroke:#ccc
        style Cell1 fill:#f5f5f5,stroke:#ccc
        style Cell5 fill:#2ecc71,stroke:#27ae60,color:#fff
    end
```

### 9. Complexity Analysis
*   **Time Complexity:** $\Theta(n)$ — Fills the table of size $n+1$ in a single pass.
*   **Space Complexity:** $\Theta(n)$ — Uses an array of size $n+1$. Can be optimized to $O(1)$ by keeping only the last two values.

---

## 2. Coin-Row Problem

### 1. The Real-Life Analogy
Imagine you have a row of coins of different values. You want to pick coins to get the maximum sum. The catch: you cannot pick any two adjacent coins. If you pick a coin, you must skip its immediate neighbors. How do you choose which coins to pick to maximize your total value?

### 2. Inputs and Outputs
*   **Input:** An array $C = \langle C_1, C_2, \dots, C_n \rangle$ containing the positive values of $n$ coins in a row.
*   **Output:** The maximum total value possible without picking adjacent coins.

### 3. The Core Struggle
For $n$ coins, each coin can either be picked or skipped. This means there are $2^n$ possible subsets. Checking all of them to make sure no two chosen coins are adjacent is too slow for large coin rows.

### 4. The Subproblem Decomposition
When considering the $i$-th coin in the row, we have two choices:
*   **Option A (Pick coin $i$):** We get the coin's value $C_i$, plus the optimal value we could get from the first $i-2$ coins (since we must skip coin $i-1$):
    $$\text{Value} = C_i + F[i-2]$$
*   **Option B (Skip coin $i$):** The maximum value we can get is simply the optimal value from the first $i-1$ coins:
    $$\text{Value} = F[i-1]$$
*   We choose the option that gives the maximum value:
    $$F[i] = \max(C_i + F[i-2], F[i-1]) \quad \text{for } i \ge 2$$
    With base cases $F[0] = 0$ and $F[1] = C_1$.

### 5. The Memory Table
*   We use a 1D array $F[0 \dots n]$.
*   $F[i]$ stores the maximum value obtainable from the first $i$ coins in the row.
*   We fill the array from index 2 to $n$.

### 6. Walkthrough with Small Numbers
Let's find the optimal sum for coins: $C = \langle 5, 1, 2, 10, 6, 2 \rangle$ (size $n=6$).
*   $F[0] = 0$ (Base case)
*   $F[1] = C_1 = 5$ (Base case)
*   **For $i = 2$:** $\max(C_2 + F[0], F[1]) = \max(1 + 0, 5) = 5$
*   **For $i = 3$:** $\max(C_3 + F[1], F[2]) = \max(2 + 5, 5) = 7$
*   **For $i = 4$:** $\max(C_4 + F[2], F[3]) = \max(10 + 5, 7) = 15$
*   **For $i = 5$:** $\max(C_5 + F[3], F[4]) = \max(6 + 7, 15) = 15$
*   **For $i = 6$:** $\max(C_6 + F[4], F[5]) = \max(2 + 15, 15) = 17$
*   The maximum value is **17**. (Cuts selected: coins 1, 4, and 6: $5 + 10 + 2 = 17$).

### 7. Core Algorithm

#### 📘 Algorithm 8.2: Coin-Row Problem

> **Purpose:** Compute the maximum value obtainable from a row of $n$ coins with no two adjacent coins picked.

```
Algorithm 8.2: COIN-ROW(C, n)
────────────────────────────────────────────
C = Array of coin values
n = Number of coins

1. Let F[0...n] be a new array
2. Set F[0] := 0
3. Set F[1] := C[1]
4. Repeat Step 5 for i = 2 to n:
5.     Set F[i] := max(C[i] + F[i-2], F[i-1])
   [End of Step 4 loop]
6. Return F[n]
```

### 8. Visual State Transition (Mermaid)

The diagram below shows the binary decision tree and lookup requirements when evaluating coin $i$:

```mermaid
graph TD
    subgraph "Decision Path for Coin i"
        CoinI{"Consider Coin i"} -->|Option A: Pick i| Pick["Gain C_i + Solve F[i-2]"]
        CoinI -->|Option B: Skip i| Skip["Gain 0 + Solve F[i-1]"]
        
        Pick --> SubPrev2["Look up: F[i-2]"]
        Skip --> SubPrev1["Look up: F[i-1]"]
        
        SubPrev2 --> Best["Select Max Value"]
        SubPrev1 --> Best
        Best --> Store["Store in F[i]"]
        
        style CoinI fill:#3498db,stroke:#2980b9,color:#fff
        style Store fill:#2ecc71,stroke:#27ae60,color:#fff
    end
```

### 9. Complexity Analysis
*   **Time Complexity:** $\Theta(n)$ — Single loop from 2 to $n$.
*   **Space Complexity:** $\Theta(n)$ — Array $F$ of size $n+1$.

---

## 3. Change-Making Problem (DP)

### 1. The Real-Life Analogy
Imagine you are a cashier. A customer buys something and you need to give them exactly \$6 in change. You have coin denominations of \$1, \$3, and \$4. How can you make this change using the absolute fewest coins? 

A greedy approach would choose the largest coin first: one \$4 coin, leaving \$2, which requires two \$1 coins. This uses 3 coins total (\$4 + \$1 + \$1). However, the optimal solution is to use two \$3 coins (\$3 + \$3), which requires only 2 coins.

### 2. Inputs and Outputs
*   **Inputs:**
    *   A target change amount $n$.
    *   An array $D = \langle d_1, d_2, \dots, d_m \rangle$ of coin denominations, where $d_1 = 1$.
*   **Output:** The minimum number of coins needed to sum to $n$.

### 3. The Core Struggle
A greedy strategy does not always yield the minimum number of coins for arbitrary denominations. To find the optimal combinations, we must evaluate different choices, which grows exponentially if done recursively without caching.

### 4. The Subproblem Decomposition
To make change for amount $j$, we try using each coin denomination $d_i$ as the last coin:
*   If we use coin $d_i$, the problem reduces to finding the minimum coins needed for the remaining amount $j - d_i$.
*   The cost is 1 (for coin $d_i$) plus $F[j - d_i]$.
*   We try all denominations $d_i \le j$ and choose the minimum:
    $$F[j] = \min_{d_i \le j} (1 + F[j - d_i]) \quad \text{for } j > 0, \text{ with } F[0] = 0$$

### 5. The Memory Table
*   We use a 1D array $F[0 \dots n]$.
*   $F[j]$ stores the minimum number of coins needed to make change for amount $j$.
*   We fill the table from index 1 to $n$.

### 6. Walkthrough with Small Numbers
Let's find the minimum coins for target $n = 6$ using denominations $D = \{1, 3, 4\}$.
*   $F[0] = 0$ (Base case)
*   **For $j = 1$:** $1 + F[1 - 1] = 1 + F[0] = 1 \implies F[1] = 1$.
*   **For $j = 2$:** $1 + F[2 - 1] = 1 + F[1] = 2 \implies F[2] = 2$.
*   **For $j = 3$:**
    *   Coin 1: $1 + F[3 - 1] = 1 + 2 = 3$.
    *   Coin 3: $1 + F[3 - 3] = 1 + 0 = 1$.
    *   $\min(3, 1) = 1 \implies F[3] = 1$.
*   **For $j = 4$:**
    *   Coin 1: $1 + F[4 - 1] = 1 + 1 = 2$.
    *   Coin 3: $1 + F[4 - 3] = 1 + 1 = 2$.
    *   Coin 4: $1 + F[4 - 4] = 1 + 0 = 1$.
    *   $\min(2, 2, 1) = 1 \implies F[4] = 1$.
*   **For $j = 5$:**
    *   Coin 1: $1 + F[5 - 1] = 1 + 1 = 2$.
    *   Coin 3: $1 + F[5 - 3] = 1 + 2 = 3$.
    *   Coin 4: $1 + F[5 - 4] = 1 + 1 = 2$.
    *   $\min(2, 3, 2) = 2 \implies F[5] = 2$.
*   **For $j = 6$:**
    *   Coin 1: $1 + F[6 - 1] = 1 + 2 = 3$.
    *   Coin 3: $1 + F[6 - 3] = 1 + 1 = 2$.
    *   Coin 4: $1 + F[6 - 4] = 1 + 2 = 3$.
    *   $\min(3, 2, 3) = 2 \implies F[6] = 2$.
*   The minimum number of coins is **2**.

### 7. Core Algorithm

#### 📘 Algorithm 8.3: Change-Making DP

> **Purpose:** Compute the minimum number of coins needed to make change for a target amount.

```
Algorithm 8.3: CHANGE-MAKING-DP(D, m, n)
────────────────────────────────────────────
D = Array of coin denominations (d_1 = 1)
m = Number of denominations
n = Target change amount

1. Let F[0...n] be a new array
2. Set F[0] := 0
3. Repeat Steps 4 through 8 for j = 1 to n:
4.     Set temp := ∞
5.     Repeat Steps 6 and 7 for i = 1 to m:
6.         If j ≥ D[i], then:
7.             Set temp := min(temp, 1 + F[j - D[i]])
           [End of If structure]
       [End of Step 5 loop]
8.     Set F[j] := temp
   [End of Step 3 loop]
9. Return F[n]
```

### 8. Visual State Transition (Mermaid)

The diagram below shows the state branching when calculating the minimum coins for amount $j$:

```mermaid
graph TD
    subgraph "Change-Making State Transitions for Amount j"
        j["Amount j"] -->|Subtract d_1| j_d1["Subproblem: j - d_1"]
        j -->|Subtract d_2| j_d2["Subproblem: j - d_2"]
        j -->|Subtract d_m| j_dm["Subproblem: j - d_m"]
        
        j_d1 --> lookup1["1 + F[j - d_1]"]
        j_d2 --> lookup2["1 + F[j - d_2]"]
        j_dm --> lookup3["1 + F[j - d_m]"]
        
        lookup1 --> minVal["Min Coins = min(...)"]
        lookup2 --> minVal
        lookup3 --> minVal
        
        minVal --> Save["Save in F[j]"]
        
        style j fill:#e74c3c,stroke:#c0392b,color:#fff
        style Save fill:#2ecc71,stroke:#27ae60,color:#fff
    end
```

### 9. Complexity Analysis
*   **Time Complexity:** $\Theta(n \cdot m)$ — Nested loops (amount $n$ and denominations $m$).
*   **Space Complexity:** $\Theta(n)$ — Array $F$ of size $n+1$.

---

## 4. Coin-Collecting Problem

### 1. The Real-Life Analogy
Imagine you are playing a grid-based board game. Some cells on the board contain coins. You start at the top-left square $(1,1)$ and want to reach the bottom-right square $(m,n)$. The rules allow you to move only **right** or **down** at each step. How do you plan your moves to collect the maximum number of coins along the path?

### 2. Inputs and Outputs
*   **Input:** A 2D array $A[1 \dots m, 1 \dots n]$ representing the grid, where $A[i, j] = 1$ if cell $(i, j)$ contains a coin, and $0$ otherwise.
*   **Output:** The maximum number of coins collected from $(1, 1)$ to $(m, n)$.

### 3. The Core Struggle
The number of possible paths from top-left to bottom-right in an $m \times n$ grid is:
$$\text{Paths} = \binom{m+n-2}{m-1}$$
For a $10 \times 10$ board, there are 48,620 paths. For larger boards, checking all paths is too slow.

### 4. The Subproblem Decomposition
To reach cell $(i, j)$, you can only arrive from the cell immediately to its left $(i, j-1)$ or the cell immediately above it $(i-1, j)$.
*   The max coins collected to $(i, j)$ is the coin at $(i, j)$ plus the maximum of the coins collected along the paths to those two neighbors:
    $$F[i, j] = \max(F[i-1, j], F[i, j-1]) + A[i, j] \quad \text{for } i > 1, j > 1$$
*   **Boundary Cases:**
    *   $F[1, 1] = A[1, 1]$
    *   $F[1, j] = F[1, j-1] + A[1, j]$ (first row can only be reached from the left)
    *   $F[i, 1] = F[i-1, 1] + A[i, 1]$ (first column can only be reached from above)

### 5. The Memory Table
*   We use a 2D table $F[1 \dots m, 1 \dots n]$ of the same dimensions as the board.
*   $F[i, j]$ stores the maximum coins collected on a path from $(1, 1)$ to $(i, j)$.
*   We fill the table row by row, from left to right.

### 6. Walkthrough with Small Numbers
Let's find the max coins for a $3 \times 3$ grid $A$, where coins (1) are at $(1, 2)$, $(2, 2)$, $(3, 1)$, and $(3, 3)$:
$$A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$$

*   **Initialize Row 1 and Col 1:**
    *   $F[1, 1] = A[1, 1] = 0$.
    *   $F[1, 2] = F[1, 1] + A[1, 2] = 0 + 1 = 1$.
    *   $F[1, 3] = F[1, 2] + A[1, 3] = 1 + 0 = 1$.
    *   $F[2, 1] = F[1, 1] + A[2, 1] = 0 + 0 = 0$.
    *   $F[3, 1] = F[2, 1] + A[3, 1] = 0 + 1 = 1$.
*   **Fill the remaining cells:**
    *   **Cell $(2, 2)$:** $\max(F[1, 2], F[2, 1]) + A[2, 2] = \max(1, 0) + 1 = 2$.
    *   **Cell $(2, 3)$:** $\max(F[1, 3], F[2, 2]) + A[2, 3] = \max(1, 2) + 0 = 2$.
    *   **Cell $(3, 2)$:** $\max(F[2, 2], F[3, 1]) + A[3, 2] = \max(2, 1) + 0 = 2$.
    *   **Cell $(3, 3)$:** $\max(F[2, 3], F[3, 2]) + A[3, 3] = \max(2, 2) + 1 = 3$.
*   The maximum coins collected is **3**.

### 7. Core Algorithm

#### 📘 Algorithm 8.4: Coin Collecting

> **Purpose:** Calculate the maximum coins collected on a path from top-left to bottom-right.

```
Algorithm 8.4: COIN-COLLECTING(A, m, n)
────────────────────────────────────────────
A = 2D binary grid (1 = coin, 0 = empty)
m, n = Dimensions of the grid

1. Let F[1...m, 1...n] be a new 2D array
2. Set F[1, 1] := A[1, 1]
3. Repeat Step 4 for j = 2 to n:
4.     Set F[1, j] := F[1, j-1] + A[1, j]
   [End of loop]
5. Repeat Steps 6 through 10 for i = 2 to m:
6.     Set F[i, 1] := F[i-1, 1] + A[i, 1]
7.     Repeat Steps 8 through 10 for j = 2 to n:
8.         Set F[i, j] := max(F[i-1, j], F[i, j-1]) + A[i, j]
       [End of Step 7 loop]
   [End of Step 5 loop]
9. Return F[m, n]
```

### 8. Visual State Transition (Mermaid)

The diagram below shows how the values from top and left neighbors feed into cell $(i, j)$:

```mermaid
graph TD
    subgraph "Grid Path Selection to Cell (i, j)"
        direction TB
        Top["Top Neighbor: F[i-1, j]"] -->|Move Down| Current["Current Cell: F[i, j]"]
        Left["Left Neighbor: F[i, j-1]"] -->|Move Right| Current
        
        Current --> Formula["F[i, j] = max( Top, Left ) + A[i, j]"]
        
        style Top fill:#f39c12,stroke:#e67e22,color:#fff
        style Left fill:#3498db,stroke:#2980b9,color:#fff
        style Current fill:#e74c3c,stroke:#c0392b,color:#fff
        style Formula fill:#2ecc71,stroke:#27ae60,color:#fff
    end
```

### 9. Complexity Analysis
*   **Time Complexity:** $\Theta(m \cdot n)$ — Traverses each cell of the grid exactly once.
*   **Space Complexity:** $\Theta(m \cdot n)$ — Uses a 2D table of size $m \times n$.

---

## 5. 0/1 Knapsack Problem

### 1. The Real-Life Analogy
Imagine a thief breaks into a warehouse with a knapsack that can hold at most 5 kg. The warehouse has items of different values and weights. The thief must decide for each item whether to take it (1) or leave it (0). They cannot take a fraction of an item. How do they fill the knapsack to get the highest total value?

### 2. Inputs and Outputs
*   **Inputs:**
    *   An integer capacity $W$ (maximum weight the knapsack can carry).
    *   An array $w = \langle w_1, \dots, w_n \rangle$ of item weights.
    *   An array $v = \langle v_1, \dots, v_n \rangle$ of item values.
    *   An integer $n$ representing the number of items.
*   **Output:** The maximum total value obtainable that fits within weight $W$.

### 3. The Core Struggle
For $n$ items, there are $2^n$ possible subsets. Checking all of them to see if their weight fits within $W$ takes exponential time and is too slow for large sets of items.

### 4. The Subproblem Decomposition
When deciding on the $i$-th item with remaining capacity $j$:
*   **Option A (Skip item $i$):** The value remains the same as using the first $i-1$ items with capacity $j$:
    $$\text{Value} = V[i-1, j]$$
*   **Option B (Take item $i$):** If the item's weight $w_i \le j$, we can take it. The value is the item's value $v_i$ plus the optimal value using the first $i-1$ items with the remaining capacity $j - w_i$:
    $$\text{Value} = v_i + V[i-1, j - w_i]$$
*   We choose the option that gives the maximum value:
    $$V[i, j] = \begin{cases} \max(V[i-1, j], v_i + V[i-1, j - w_i]) & \text{if } w_i \le j \\ V[i-1, j] & \text{if } w_i > j \end{cases}$$
    With base cases $V[0, j] = 0$ and $V[i, 0] = 0$.

### 5. The Memory Table
*   We use a 2D table $V[0 \dots n, 0 \dots W]$.
*   $V[i, j]$ stores the maximum value obtainable using a subset of the first $i$ items within a weight limit of $j$.
*   We fill the table row-by-row, from left to right.

### 6. Walkthrough with Small Numbers
Let's find the max value for capacity $W = 5$ with 4 items:
1. Item 1: $w_1 = 2, v_1 = 12$
2. Item 2: $w_2 = 1, v_2 = 10$
3. Item 3: $w_3 = 3, v_3 = 20$
4. Item 4: $w_4 = 2, v_4 = 15$

*   **Initialize Row 0 and Col 0 to 0.**
*   **Row 1 (Item 1, $w_1=2, v_1=12$):**
    *   For $j < 2$: $V[1, j] = V[0, j] = 0$.
    *   For $j \ge 2$: $\max(V[0, j], 12 + V[0, j-2]) = 12$.
    *   $V[1] = \langle 0, 0, 12, 12, 12, 12 \rangle$.
*   **Row 2 (Item 2, $w_2=1, v_2=10$):**
    *   $j=1: \max(V[1, 1], 10 + V[1, 0]) = \max(0, 10) = 10$.
    *   $j=2: \max(V[1, 2], 10 + V[1, 1]) = \max(12, 10 + 0) = 12$.
    *   $j=3: \max(V[1, 3], 10 + V[1, 2]) = \max(12, 10 + 12) = 22$.
    *   $j=4: \max(V[1, 4], 10 + V[1, 3]) = \max(12, 10 + 12) = 22$.
    *   $j=5: \max(V[1, 5], 10 + V[1, 4]) = \max(12, 10 + 12) = 22$.
    *   $V[2] = \langle 0, 10, 12, 22, 22, 22 \rangle$.
*   **Row 3 (Item 3, $w_3=3, v_3=20$):**
    *   $j < 3$: $V[3, j] = V[2, j]$.
    *   $j=3: \max(V[2, 3], 20 + V[2, 0]) = \max(22, 20 + 0) = 22$.
    *   $j=4: \max(V[2, 4], 20 + V[2, 1]) = \max(22, 20 + 10) = 30$.
    *   $j=5: \max(V[2, 5], 20 + V[2, 2]) = \max(22, 20 + 12) = 32$.
    *   $V[3] = \langle 0, 10, 12, 22, 30, 32 \rangle$.
*   **Row 4 (Item 4, $w_4=2, v_4=15$):**
    *   $j < 2$: $V[4, j] = V[3, j]$.
    *   $j=2: \max(V[3, 2], 15 + V[3, 0]) = \max(12, 15) = 15$.
    *   $j=3: \max(V[3, 3], 15 + V[3, 1]) = \max(22, 15 + 10) = 25$.
    *   $j=4: \max(V[3, 4], 15 + V[3, 2]) = \max(30, 15 + 12) = 30$.
    *   $j=5: \max(V[3, 5], 15 + V[3, 3]) = \max(32, 15 + 22) = 37$.
    *   $V[4] = \langle 0, 10, 15, 25, 30, **37** \rangle$.
*   The maximum value is **37**. (Optimal subset is Items 1, 2, and 4: $2 + 1 + 2 = 5$ kg, value $12 + 10 + 15 = 37$).

### 7. Core Algorithm

#### 📘 Algorithm 8.5: 0/1 Knapsack

> **Purpose:** Calculate the maximum value obtainable within a weight limit $W$ using a 2D table.

```
Algorithm 8.5: KNAPSACK-01(w, v, n, W)
────────────────────────────────────────────
w = Array of item weights
v = Array of item values
n = Number of items
W = Knapsack capacity

1. Let V[0...n, 0...W] be a new 2D array
2. Repeat Step 3 for i = 0 to n:
3.     Set V[i, 0] := 0
   [End of loop]
4. Repeat Step 5 for j = 0 to W:
5.     Set V[0, j] := 0
   [End of loop]
6. Repeat Steps 7 through 11 for i = 1 to n:
7.     Repeat Steps 8 through 11 for j = 1 to W:
8.         If w[i] ≤ j, then:
9.             Set V[i, j] := max(V[i-1, j], v[i] + V[i-1, j - w[i]])
10.        Else:
11.            Set V[i, j] := V[i-1, j]
           [End of If structure]
       [End of Step 7 loop]
   [End of Step 6 loop]
12. Return V[n, W]
```

### 8. Visual State Transition (Mermaid)

The diagram below shows the item selection matrix and capacity check branching:

```mermaid
graph TD
    subgraph "Knapsack Selection Matrix for Item i, Capacity j"
        State["State V[i, j]"] --> Check{"Does Item i fit?<br/>w_i ≤ j?"}
        Check -->|❌ No| SkipOnly["Only option: Skip Item i"]
        Check -->|✅ Yes| Choices["Two choices: Skip vs. Take"]
        
        SkipOnly --> Lookup1["V[i-1, j]"]
        
        Choices --> ChoiceSkip["Skip: V[i-1, j]"]
        Choices --> ChoiceTake["Take: v_i + V[i-1, j - w_i]"]
        
        Lookup1 --> Store["Store in V[i, j]"]
        ChoiceSkip --> MaxVal["max( Skip, Take )"]
        ChoiceTake --> MaxVal
        MaxVal --> Store
        
        style State fill:#3498db,stroke:#2980b9,color:#fff
        style Store fill:#2ecc71,stroke:#27ae60,color:#fff
    end
```

### 9. Complexity Analysis
*   **Time Complexity:** $\Theta(n \cdot W)$ — Fills a table of size $(n+1) \times (W+1)$.
*   **Space Complexity:** $\Theta(n \cdot W)$ — Uses a 2D array of size $(n+1) \times (W+1)$.

---

## 6. Longest Common Subsequence (LCS)

### 1. The Real-Life Analogy
Imagine comparing two strands of DNA to see if they came from the same source. DNA strands are represented as strings of bases: `A`, `C`, `G`, and `T`. Because mutations insert or delete bases, they might not match exactly. Instead, we measure similarity by finding the **longest common subsequence**—a sequence where bases appear in the same order in both strands, but not necessarily next to each other.

### 2. Inputs and Outputs
*   **Inputs:** Two sequences (strings) $X = \langle x_1, \dots, x_m \rangle$ and $Y = \langle y_1, \dots, y_n \rangle$.
*   **Outputs:** 
    *   The length of the longest subsequence common to both strings.
    *   A traceback path to print the common elements in order.

### 3. The Core Struggle
To find the longest common subsequence of two strings of length $m$ and $n$, we could check all subsequences of string $X$. Since string $X$ has $2^m$ possible subsequences, checking all of them against $Y$ takes exponential time and is too slow for long strings.

### 4. The Subproblem Decomposition
Let's look at the final characters $x_m$ and $y_n$ of both strings:
*   **If $x_m == y_n$:** The final characters match. They must be part of the LCS. We solve the smaller problem of finding the LCS of $X_{m-1}$ and $Y_{n-1}$, then append this character:
    $$c[i, j] = c[i-1, j-1] + 1$$
*   **If $x_m \neq y_n$:** The final characters do not match. The LCS could end with $x_m$ (excluding $y_n$) or end with $y_n$ (excluding $x_m$). We solve both cases and take the maximum:
    $$c[i, j] = \max(c[i-1, j], c[i, j-1])$$

### 5. The Memory Table
*   We use a 2D grid $c[0 \dots m, 0 \dots n]$ to store lengths, where $c[i, j]$ is the LCS length of prefixes $X_i$ and $Y_j$.
*   We use a 2D table $b[1 \dots m, 1 \dots n]$ to store directions ($\nwarrow$, $\uparrow$, $\leftarrow$) representing matching choices.

### 6. Walkthrough with Small Numbers
Let's find the LCS of $X = \text{"ABC"}$ and $Y = \text{"BDC"}$.
*   **Initialize:** Set Row 0 and Column 0 of table $c$ to 0.
*   **Row 1 ($i=1, x_1=\text{'A'}$):**
    *   $j=1 (y_1=\text{'B'}): \text{'A'} \neq \text{'B'} \implies c[1, 1] = \max(c[0, 1], c[1, 0]) = 0$.
    *   $j=2 (y_2=\text{'D'}): \text{'A'} \neq \text{'D'} \implies c[1, 2] = \max(c[0, 2], c[1, 1]) = 0$.
    *   $j=3 (y_3=\text{'C'}): \text{'A'} \neq \text{'C'} \implies c[1, 3] = \max(c[0, 3], c[1, 2]) = 0$.
*   **Row 2 ($i=2, x_2=\text{'B'}$):**
    *   $j=1 (y_1=\text{'B'}): \text{'B'} == \text{'B'} \implies c[2, 1] = c[1, 0] + 1 = 1$.
    *   $j=2 (y_2=\text{'D'}): \text{'B'} \neq \text{'D'} \implies c[2, 2] = \max(c[1, 2], c[2, 1]) = 1$.
    *   $j=3 (y_3=\text{'C'}): \text{'B'} \neq \text{'C'} \implies c[2, 3] = \max(c[1, 3], c[2, 2]) = 1$.
*   **Row 3 ($i=3, x_3=\text{'C'}$):**
    *   $j=1 (y_1=\text{'B'}): \text{'C'} \neq \text{'B'} \implies c[3, 1] = \max(c[2, 1], c[3, 0]) = 1$.
    *   $j=2 (y_2=\text{'D'}): \text{'C'} \neq \text{'D'} \implies c[3, 2] = \max(c[2, 2], c[3, 1]) = 1$.
    *   $j=3 (y_3=\text{'C'}): \text{'C'} == \text{'C'} \implies c[3, 3] = c[2, 2] + 1 = 2$.
*   The final cell value is **2**, representing LCS length. Traceback path matches 'C' at (3,3) and 'B' at (2,1) $\implies$ LCS is "BC".

### 7. Core Algorithms

#### 📘 Algorithm 8.6: LCS Length

> **Purpose:** Calculate the length of the LCS of two sequences and populate the traceback tables.

```
Algorithm 8.6: LCS-LENGTH(X, Y, m, n)
────────────────────────────────────────────
X, Y = Input sequences
m, n = Lengths of X and Y
c = Table for LCS lengths
b = Table for traceback directions

1. Let b[1...m, 1...n] and c[0...m, 0...n] be new tables
2. Repeat Step 3 for i = 1 to m:
3.     Set c[i, 0] := 0
   [End of loop]
4. Repeat Step 5 for j = 0 to n:
5.     Set c[0, j] := 0
   [End of loop]
6. Repeat Steps 7 through 15 for i = 1 to m:
7.     Repeat Steps 8 through 15 for j = 1 to n:
8.         If x[i] == y[j], then:
9.             Set c[i, j] := c[i - 1, j - 1] + 1
10.            Set b[i, j] := "↖"
11.        Else if c[i - 1, j] ≥ c[i, j - 1], then:
12.            Set c[i, j] := c[i - 1, j]
13.            Set b[i, j] := "↑"
14.        Else:
15.            Set c[i, j] := c[i, j - 1]
16.            Set b[i, j] := "←"
           [End of If structure]
       [End of Step 7 loop]
   [End of Step 6 loop]
17. Return c and b
```

---

#### 📘 Procedure 8.7: Print LCS

> **Purpose:** Recursively print the characters of the LCS in the correct order.

```
Procedure: PRINT-LCS(b, X, i, j)
────────────────────────────────────────────
1. If i == 0 or j == 0, then:
       Return
   [End of If structure]
2. If b[i, j] == "↖", then:
       Call PRINT-LCS(b, X, i - 1, j - 1)
       Print x[i]
   Else if b[i, j] == "↑", then:
       Call PRINT-LCS(b, X, i - 1, j)
   Else:
       Call PRINT-LCS(b, X, i, j - 1)
   [End of If structure]
```

### 8. Visual State Transition (Mermaid)

The diagram below shows character matching decisions and table cell routing:

```mermaid
graph TD
    subgraph "LCS Character Matching Decisions"
        Compare{"Compare x_i and y_j"} -->|Match: x_i = y_j| Diagonal["Extend match diagonal-wise:<br/>c[i-1, j-1] + 1"]
        Compare -->|Mismatch: x_i ≠ y_j| MaxNeighbors["Take max of neighbors:<br/>max( c[i-1, j], c[i, j-1] )"]
        
        Diagonal --> Save["Store in c[i, j]"]
        MaxNeighbors --> Save
        
        style Compare fill:#3498db,stroke:#2980b9,color:#fff
        style Save fill:#2ecc71,stroke:#27ae60,color:#fff
    end
```

### 9. Complexity Analysis
*   **Time Complexity:** $\Theta(m \cdot n)$ — Fills a table of size $m \times n$ iteratively.
*   **Space Complexity:** $O(m \cdot n)$ — Storing direction and cost tables.

---

## 7. Floyd-Warshall Algorithm

### 1. The Real-Life Analogy
Imagine you want to build a flight search engine. You want to show users the cheapest ticket between **every single pair of airports**. Instead of running a separate search for every pair of airports, the Floyd-Warshall algorithm updates the entire flight database step-by-step. It asks: "Is it cheaper to fly from Airport A to Airport B directly, or by taking a detour through Airport C?" We repeat this query for every airport, letting each one take a turn as a detour hub.

### 2. Inputs and Outputs
*   **Input:** An adjacency weight matrix $W$ of size $n \times n$, where $w_{ij}$ is the direct weight of edge $i \to j$.
*   **Output:** An $n \times n$ matrix $D$ containing the shortest path weights between all pairs of vertices.

### 3. The Core Struggle
We want to find all shortest paths in a graph. If we run Dijkstra's algorithm from every single vertex, it works but is complex to implement and fails if there are negative-weight edges. The Floyd-Warshall algorithm handles negative-weight edges efficiently using a clean matrix update.

### 4. The Subproblem Decomposition
Number the vertices of the graph from 1 to $n$. Let $d_{ij}^{(k)}$ be the weight of a shortest path from $i$ to $j$ using intermediate vertices only from the set $\{1, 2, \dots, k\}$.
When we allow vertex $k$ to be used as a detour:
*   **Case 1 (Skip $k$):** The path does not go through $k$. The shortest path remains $d_{ij}^{(k-1)}$.
*   **Case 2 (Detour through $k$):** The path goes through $k$. It splits into a path from $i \to k$ and a path from $k \to j$. The cost is $d_{ik}^{(k-1)} + d_{kj}^{(k-1)}$.
*   We choose the minimum of these two cases:
    $$d_{ij}^{(k)} = \min \left( d_{ij}^{(k-1)}, d_{ik}^{(k-1)} + d_{kj}^{(k-1)} \right)$$

### 5. The Memory Table
*   A 3D grid of size $n \times n \times (n+1)$ is used, where index $k$ represents the maximum intermediate vertex allowed.
*   **Memory Optimization:** In practice, we only need a 2D matrix of size $n \times n$ and can update it in-place since the values at step $k$ only depend on the values at step $k-1$.

### 6. Walkthrough with Small Numbers
Let's solve for a 3-vertex graph:
*   Edge $1 \to 2$ has weight 3
*   Edge $2 \to 3$ has weight 1
*   Edge $1 \to 3$ has weight 6 (direct)

Initially ($k=0$):
$$D^{(0)} = \begin{pmatrix} 0 & 3 & 6 \\ \infty & 0 & 1 \\ \infty & \infty & 0 \end{pmatrix}$$

Detour through vertex 1 ($k=1$):
*   No paths are shortened by detouring through vertex 1. $D^{(1)} = D^{(0)}$.

Detour through vertex 2 ($k=2$):
*   Check path $1 \to 3$: $\min(d_{13}^{(1)}, d_{12}^{(1)} + d_{23}^{(1)}) = \min(6, 3 + 1) = 4$.
$$D^{(2)} = \begin{pmatrix} 0 & 3 & 4 \\ \infty & 0 & 1 \\ \infty & \infty & 0 \end{pmatrix}$$

The shortest path from $1 \to 3$ is updated to **4** by detouring through vertex 2.

### 7. Core Algorithms

#### 📘 Algorithm 8.8: Floyd-Warshall

> **Purpose:** Calculate all-pairs shortest path weights in a graph with no negative-weight cycles.

```
Algorithm 8.8: FLOYD-WARSHALL(W, n)
────────────────────────────────────────────
W = Adjacency weight matrix of size n x n
D = Distance matrix of shortest path weights

1. Set D^(0) := W
2. Repeat Steps 3 through 6 for k = 1 to n:      [k is the detour vertex]
3.     Let D^(k) be a new n x n matrix
4.     Repeat Steps 5 and 6 for i = 1 to n:
5.         Repeat Step 6 for j = 1 to n:
6.             Set d^(k)[i, j] := min(d^(k-1)[i, j], d^(k-1)[i, k] + d^(k-1)[k, j])
           [End of Step 5 loop]
       [End of Step 4 loop]
   [End of Step 2 loop]
7. Return D^(n)
```

---

#### 📘 Algorithm 8.9: Transitive Closure

> **Purpose:** Find if there is a path from vertex $i$ to vertex $j$ for all pairs of vertices.

```
Algorithm 8.9: TRANSITIVE-CLOSURE(G, n)
────────────────────────────────────────────
1. Let T^(0) be a new n x n matrix
2. Repeat Steps 3 through 6 for i = 1 to n:
3.     Repeat Steps 4 through 6 for j = 1 to n:
4.         If i == j or (i, j) is an edge in G.E, then:
5.             Set t^(0)[i, j] := 1
6.         Else:
7.             Set t^(0)[i, j] := 0
           [End of If structure]
       [End of Step 3 loop]
   [End of Step 2 loop]
8. Repeat Steps 9 through 12 for k = 1 to n:
9.     Let T^(k) be a new n x n matrix
10.    Repeat Steps 11 and 12 for i = 1 to n:
11.        Repeat Step 12 for j = 1 to n:
12.            Set t^(k)[i, j] := t^(k-1)[i, j] OR (t^(k-1)[i, k] AND t^(k-1)[k, j])
           [End of Step 11 loop]
       [End of Step 10 loop]
   [End of Step 8 loop]
13. Return T^(n)
```

### 8. Visual State Transition (Mermaid)

The diagram below shows the routing detour comparison through hub $k$:

```mermaid
graph LR
    subgraph "Floyd-Warshall Detour Decision"
        direction LR
        i((i)) -->|Direct: d^(k-1)[i,j]| j((j))
        i -->|Subpath 1: d^(k-1)[i,k]| k((k))
        k -->|Subpath 2: d^(k-1)[k,j]| j
        
        style i fill:#f39c12,stroke:#e67e22,color:#fff
        style j fill:#3498db,stroke:#2980b9,color:#fff
        style k fill:#e74c3c,stroke:#c0392b,color:#fff
    end
```

### 9. Complexity Analysis
*   **Time Complexity:** $\Theta(n^3)$ — Fills distance tables over $n$ iterations with $n^2$ cells each.
*   **Space Complexity:** $\Theta(n^2)$ — Can be done in-place to use a single $n \times n$ matrix.

---

## 8. Traveling Salesperson Problem (Standard DP)

### 1. The Real-Life Analogy
Imagine you are a delivery driver who needs to start at your depot (City 1), visit a set of customers in other cities, and return back to City 1. You want to find the route that minimizes your total driving distance. Instead of randomly guessing routes, you can build paths subset-by-subset: "What is the shortest path to City 4, visiting City 2 and City 3 along the way?" Once you have these optimal sub-routes, finding the final tour is just a simple lookup.

### 2. Inputs and Outputs
*   **Input:** An adjacency distance matrix $C$ of size $n \times n$, where $C_{ij}$ is the distance from city $i$ to city $j$.
*   **Output:** The minimum total distance required to visit every city exactly once and return to City 1.

### 3. The Core Struggle
To find the optimal route for $n$ cities, we could evaluate all permutations of the cities. Since there are $(n-1)!$ possible routes, this brute-force approach is extremely slow. For 20 cities, there are $19! \approx 1.2 \times 10^{17}$ routes. Even a supercomputer would take decades to check them all!

### 4. The Subproblem Decomposition
Let $V = \{1, 2, \dots, n\}$ be the set of all cities.
*   Let $g(i, S)$ be the length of the shortest path starting at city $i$, visiting all cities in subset $S$ exactly once, and ending at City 1.
*   **Base Case (S is empty):** We must go directly from $i$ to 1:
    $$g(i, \emptyset) = C_{i1}$$
*   **Recursive Step (S is not empty):** We choose a next city $j \in S$ that minimizes the distance from $i \to j$ plus the shortest path from $j$ visiting the remaining cities in $S$:
    $$g(i, S) = \min_{j \in S} \left( C_{ij} + g(j, S - \{j\}) \right)$$
*   The final optimal tour cost starting at City 1 is:
    $$\text{Optimal Tour} = \min_{2 \le j \le n} \left( C_{1j} + g(j, V - \{1, j\}) \right)$$

### 5. The Memory Table
*   We use a table $g[i, S]$ where the row $i$ is the current city and column $S$ represents the subset of remaining cities.
*   Since there are $n$ cities and $2^{n-1}$ subsets of cities, the table size is $n \cdot 2^{n-1}$.
*   We fill the table starting with subsets of size 0, then size 1, up to size $n-2$.

### 6. Walkthrough with Small Numbers
Let's find the optimal tour for 4 cities ($V = \{1, 2, 3, 4\}$) with distance matrix:
$$C = \begin{pmatrix} 0 & 2 & 9 & 10 \\ 1 & 0 & 6 & 4 \\ 15 & 7 & 0 & 8 \\ 6 & 3 & 12 & 0 \end{pmatrix}$$

*   **Subsets of size 0 ($S = \emptyset$):**
    *   $g(2, \emptyset) = C_{21} = 1$.
    *   $g(3, \emptyset) = C_{31} = 15$.
    *   $g(4, \emptyset) = C_{41} = 6$.
*   **Subsets of size 1 ($S = \{j\}$):**
    *   $g(2, \{3\}) = C_{23} + g(3, \emptyset) = 6 + 15 = 21$.
    *   $g(2, \{4\}) = C_{24} + g(4, \emptyset) = 4 + 6 = 10$.
    *   $g(3, \{2\}) = C_{32} + g(2, \emptyset) = 7 + 1 = 8$.
    *   $g(3, \{4\}) = C_{34} + g(4, \emptyset) = 8 + 6 = 14$.
    *   $g(4, \{2\}) = C_{42} + g(2, \emptyset) = 3 + 1 = 4$.
    *   $g(4, \{3\}) = C_{43} + g(3, \emptyset) = 12 + 15 = 27$.
*   **Subsets of size 2 ($S = \{j, k\}$):**
    *   $g(2, \{3, 4\}) = \min\left( C_{23} + g(3, \{4\}), C_{24} + g(4, \{3\}) \right) = \min(6 + 14, 4 + 27) = \min(20, 31) = 20$.
    *   $g(3, \{2, 4\}) = \min\left( C_{32} + g(2, \{4\}), C_{34} + g(4, \{2\}) \right) = \min(7 + 10, 8 + 4) = \min(17, 12) = 12$.
    *   $g(4, \{2, 3\}) = \min\left( C_{42} + g(2, \{3\}), C_{43} + g(3, \{2\}) \right) = \min(3 + 21, 12 + 8) = \min(24, 20) = 20$.
*   **Final Tour Calculation:**
    $$\text{Optimal} = \min\left( C_{12} + g(2, \{3, 4\}), C_{13} + g(3, \{2, 4\}), C_{14} + g(4, \{2, 3\}) \right)$$
    $$\text{Optimal} = \min(2 + 20, 9 + 12, 10 + 20) = \min(22, 21, 30) = 21$$
*   The minimum tour cost is **21**. (Optimal path: $1 \to 3 \to 4 \to 2 \to 1$).

### 7. Core Algorithm

#### 📘 Algorithm 8.10: TSP (Held-Karp)

> **Purpose:** Calculate the optimal traveling salesperson tour using dynamic programming.

```
Algorithm 8.10: TSP-HELD-KARP(C, n)
────────────────────────────────────────────
C = Distance matrix of size n x n
n = Number of cities

1. Let g[2...n, Subsets of V-{1}] be a new table
2. Repeat Step 3 for i = 2 to n:
3.     Set g[i, ∅] := C[i, 1]
   [End of loop]
4. Repeat Steps 5 through 9 for s = 1 to n - 2:    [s is subset size]
5.     Repeat Steps 6 through 9 for each subset S of V-{1} of size s:
6.         Repeat Steps 7 through 9 for each i in V-{1} where i is not in S:
7.             Set temp := ∞
8.             Repeat Step 9 for each j in S:
9.                 Set temp := min(temp, C[i, j] + g[j, S - {j}])
               [End of Step 8 loop]
10.            Set g[i, S] := temp
   [End of Step 4 loop]
11. Set final_cost := ∞
12. Repeat Step 13 for each j = 2 to n:
13.     Set final_cost := min(final_cost, C[1, j] + g[j, V - {1, j}])
    [End of loop]
14. Return final_cost
```

### 8. Visual State Transition (Mermaid)

The diagram below shows subset transitions and recursive dependencies as the size of subset $S$ decreases:

```mermaid
graph TD
    subgraph "Held-Karp Subset Expansion from City i, Set S"
        State["State g(i, S)"] -->|Try City j_1 ∈ S| Branch1["C_i,j_1 + g(j_1, S - {j_1})"]
        State -->|Try City j_2 ∈ S| Branch2["C_i,j_2 + g(j_2, S - {j_2})"]
        State -->|Try City j_k ∈ S| Branchk["C_i,j_k + g(j_k, S - {j_k})"]
        
        Branch1 --> MinVal["Find Minimum Cost"]
        Branch2 --> MinVal
        Branchk --> MinVal
        
        MinVal --> Store["Store in g[i, S]"]
        
        style State fill:#3498db,stroke:#2980b9,color:#fff
        style Store fill:#2ecc71,stroke:#27ae60,color:#fff
    end
```

### 9. Complexity Analysis
*   **Time Complexity:** $\Theta(n^2 \cdot 2^n)$ — Iterates over $O(2^n)$ subsets, with $O(n)$ choices per subset. Much faster than $O(n!)$ brute force.
*   **Space Complexity:** $\Theta(n \cdot 2^n)$ — Storing optimal costs for $n$ cities and $2^n$ subsets.

---

## Summary and Quick Reference

### 📊 Algorithm Quick Reference

| Algorithm | Purpose | Time Complexity | Space Complexity |
|---|---|---|---|
| **8.1** | Fibonacci DP | $\Theta(n)$ | $\Theta(n)$ |
| **8.2** | Coin-Row Problem | $\Theta(n)$ | $\Theta(n)$ |
| **8.3** | Change-Making DP | $\Theta(n \cdot m)$ | $\Theta(n)$ |
| **8.4** | Coin Collecting | $\Theta(m \cdot n)$ | $\Theta(m \cdot n)$ |
| **8.5** | 0/1 Knapsack | $\Theta(n \cdot W)$ | $\Theta(n \cdot W)$ |
| **8.6** | LCS Length | $\Theta(m \cdot n)$ | $O(m \cdot n)$ |
| **8.7** | Print LCS | $O(m+n)$ | $O(m+n)$ |
| **8.8** | Floyd-Warshall | $\Theta(n^3)$ | $\Theta(n^2)$ |
| **8.9** | Transitive Closure | $\Theta(n^3)$ | $\Theta(n^2)$ |
| **8.10** | TSP (Held-Karp) | $\Theta(n^2 \cdot 2^n)$ | $\Theta(n \cdot 2^n)$ |

---

### When to Use Each Technique

```mermaid
graph TD
    Q1{"Do subproblems overlap?"} -->|No| DIV["Use Divide-and-Conquer"]
    Q1 -->|Yes| Q2{"Can we make greedy local choices?"}
    Q2 -->|Yes| GRD["Use Greedy Algorithm"]
    Q2 -->|No| Q3{"Is the problem NP-hard?"}
    Q3 -->|Yes| Q4{"Is the input size small? (n ≤ 20)"}
    Q4 -->|Yes| DP["Use Exact DP (e.g. Held-Karp TSP)"]
    Q4 -->|No| APP["Use Approximation or Heuristics"]
    Q3 -->|No| DP
```

### ⚠️ Important Takeaways

1.  **Overlapping Subproblems:** Dynamic programming only speeds up algorithms when intermediate subproblems are solved repeatedly.
2.  **Tabulation vs. Memoization:** Tabulation (bottom-up) is generally faster because it has no recursion overhead. Memoization (top-down) is preferred if you only need to solve a fraction of the subproblems.
3.  **Reconstruction Needs Choices:** To construct the optimal path or selections, you must store the local decisions (e.g., traceback pointers) during the computation phase.
4.  **NP-Hard Constraints:** For NP-hard problems (like 0/1 Knapsack and TSP), exact dynamic programming algorithms run in pseudo-polynomial or exponential time, meaning they are only practical for small inputs.

---

**End of Chapter 8**

*Continue to [Chapter 9: Backtracking](file:///workspaces/CSE-2201-2202-Algorithm-Design-and-Analysis-Sessional/Chapter%209%20-%20Backtracking/README.md)*
