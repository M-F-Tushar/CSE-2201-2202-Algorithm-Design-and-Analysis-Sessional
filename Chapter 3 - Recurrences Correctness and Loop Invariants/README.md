# Chapter 3 - Recurrences Correctness and Loop Invariants

[Previous: Chapter 2 - Complexity Analysis and Asymptotic Notation](../Chapter%202%20-%20Complexity%20Analysis%20and%20Asymptotic%20Notation/README.md) | [Home](../README.md) | [Next: Chapter 4 - Searching and Basic Traversal](../Chapter%204%20-%20Searching%20and%20Basic%20Traversal/README.md)

---

A recurrence relation expresses the running time of a recursive algorithm in terms of the running time on smaller inputs, plus a base case. This chapter shows how to build a recurrence directly from a recursive algorithm, how to solve it by manual expansion (the recursion-tree/substitution idea), and how to solve general divide-and-conquer recurrences quickly using the Master Theorem.

---

## Table of Contents

1. [What Is a Recurrence Relation?](#1-what-is-a-recurrence-relation)
2. [Case Study: Binary Search Recurrence](#2-case-study-binary-search-recurrence)
   - [Solving by Expansion (Unrolling)](#solving-by-expansion-recursion-treesubstitution)
3. [The Substitution Method (Inductive Proof)](#3-the-substitution-method-inductive-proof)
4. [General Divide-and-Conquer Recurrence](#4-general-divide-and-conquer-recurrence)
5. [Master Theorem](#5-master-theorem)
6. [Worked Examples Using the Master Theorem](#6-worked-examples-using-the-master-theorem)
   - [Example 1: T(n) = 8T(n/2) + n^2](#example-1-tn--8tn2--n2)
   - [Example 2: T(n) = T(n/2) + c](#example-2-tn--tn2--c)
7. [Analyze Time Complexity of Above Recurrences](#7-analyze-time-complexity-of-above-recurrences)
8. [Algorithm Correctness and Loop Invariants](#8-algorithm-correctness-and-loop-invariants)
   - [Loop Invariant Framework](#the-three-loop-invariant-properties)
   - [Case Study: Correctness of Insertion Sort](#case-study-correctness-of-insertion-sort)
   - [Mathematical Induction in Algorithm Proofs](#mathematical-induction-in-algorithm-proofs)

---

## 1. What Is a Recurrence Relation?

A recurrence relation defines a function's value in terms of its value on smaller inputs, together with a base case for the smallest input. For a recursive algorithm, the recurrence directly mirrors the recursive calls made by the algorithm:

$$
T(n) = \text{(cost of the recursive subproblem(s))} + \text{(cost of dividing and combining)}
$$

Solving the recurrence means reducing it to a closed-form asymptotic bound such as $O(\log n)$, $O(n)$, or $O(n \log n)$.

---

## 2. Case Study: Binary Search Recurrence

Binary search discards half of the remaining search space using only $O(1)$ extra work (one comparison) per call, so its recurrence is:

$$
T(n) = T(n/2) + c, \qquad T(1) = 1
$$

Written as a piecewise (base-case + recursive-case) definition, the same recurrence reads:

$$
T(n) = \begin{cases} T(n/2) + c & \text{if } n > 1 \\ 1 & \text{if } n = 1 \end{cases}
$$

### Solving by Expansion (Recursion-Tree/Substitution)

Expand the recurrence one level at a time:

$$
T(n) = T(n/2) + c
$$

$$
T(n/2) = T(n/4) + c \implies T(n) = T(n/4) + 2c
$$

$$
T(n/4) = T(n/8) + c \implies T(n) = T(n/8) + 3c
$$

After $k$ expansions, the pattern is:

$$
T(n) = T(n/2^k) + kc
$$

The recursion bottoms out at the base case, i.e., when:

$$
\frac{n}{2^k} = 1 \implies n = 2^k \implies k = \log_2 n
$$

Substituting back with $T(1) = 1$:

$$
T(n) = T(1) + c\log_2 n = 1 + c\log_2 n
$$

Dropping the constant factor and the lower-order additive term:

$$
T(n) = \Theta(\log n)
$$

So **binary search runs in $O(\log n)$ time**, matching the iterative analysis in [Chapter 4 - Searching and Basic Traversal](../Chapter%204%20-%20Searching%20and%20Basic%20Traversal/README.md).

> **Where the $\log n$ comes from:** substituting $n = 2^k$ into $T(n) = T(n/2^k) + kc$ gives $\log_2 n = \log_2 2^k = k \log_2 2 = k$, so $k = \log_2 n$ &mdash; this is exactly the substitution used above.

### Visual Map: Recursion Tree for T(n) = T(n/2) + c

![Recursion Tree for T(n) = T(n/2) + c](diagrams/ch3-01-recursion-tree.svg)

---

## 3. The Substitution Method (Inductive Proof)

While expansion (unrolling) is intuitive for discovering candidate bounds, the formal **Substitution Method** (as presented in CLRS Chapter 4) consists of two rigorous steps:
1. **Guess** the mathematical form of the solution (guided by recursion trees or pattern inspection).
2. **Prove by mathematical induction** that the bound holds for all $n$, finding specific constants $c > 0$ and $n_0 \ge 1$ that satisfy the base and recursive cases.

### Worked Example: Proving $T(n) = 2T(\lfloor n/2 \rfloor) + n = O(n \log n)$

Consider the divide-and-conquer recurrence:
$$
T(n) = 2T(\lfloor n/2 \rfloor) + n, \qquad T(1) = 1
$$
We guess that $T(n) \le c n \log_2 n$ for some constant $c > 0$.

1. **Inductive Hypothesis:** Assume $T(k) \le c k \log_2 k$ holds for all $k < n$, specifically for $k = \lfloor n/2 \rfloor$.
2. **Inductive Step:** Substitute the hypothesis into the recurrence:
   $$
   \begin{aligned}
   T(n) &\le 2\left(c \lfloor n/2 \rfloor \log_2 \lfloor n/2 \rfloor\right) + n \\
   &\le 2 c \left(\frac{n}{2}\right) \log_2\left(\frac{n}{2}\right) + n \\
   &= c n (\log_2 n - \log_2 2) + n \\
   &= c n \log_2 n - c n + n \\
   &= c n \log_2 n - (c - 1) n
   \end{aligned}
   $$
   To establish $T(n) \le c n \log_2 n$, we require $-(c - 1)n \le 0$, which holds whenever $c \ge 1$.
3. **Base Case:** For $n = 2$ and $n = 3$, $c \cdot 2 \log_2 2 = 2c \ge T(2)$. Choosing $c \ge \max(1, T(2)/2)$ satisfies the base conditions.

Hence, by mathematical induction, $T(n) = O(n \log n)$.

---

## 4. General Divide-and-Conquer Recurrence

Most divide-and-conquer algorithms produce a recurrence of the form:

$$
T(n) = aT(n/b) + f(n)
$$

| Symbol | Meaning |
| :---: | :--- |
| $a$ | Number of subproblems the problem is divided into ($a \ge 1$) |
| $n/b$ | Size of each subproblem ($b > 1$) |
| $f(n)$ | Cost of dividing the problem and combining the subproblem results |

---

## 5. Master Theorem

The Master Theorem gives the asymptotic solution to $T(n) = aT(n/b) + f(n)$ directly, by comparing $f(n)$ against the **watershed function** $n^{\log_b a}$.

| Case | Condition on $f(n)$ | Result |
| :---: | :--- | :--- |
| 1 | $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$ ($f(n)$ grows polynomially **slower**) | $T(n) = \Theta(n^{\log_b a})$ |
| 2 | $f(n) = \Theta(n^{\log_b a} \log^k n)$ for some $k \ge 0$ ($f(n)$ grows at the **same** rate) | $T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$ |
| 3 | $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some $\epsilon > 0$, and the regularity condition $a \cdot f(n/b) \le c \cdot f(n)$ holds for some $c < 1$ and all large $n$ ($f(n)$ grows polynomially **faster**) | $T(n) = \Theta(f(n))$ |

### Visual Map: Choosing the Right Case

![Master Theorem Decision Flow - T(n) = aT(n/b) + f(n)](diagrams/ch3-02-master-theorem-cases.svg)

---

## 6. Worked Examples Using the Master Theorem

### Example 1: T(n) = 8T(n/2) + n^2

Here $a = 8$, $b = 2$, $f(n) = n^2$.

$$
n^{\log_b a} = n^{\log_2 8} = n^3
$$

Compare $f(n) = n^2$ with $n^{\log_b a} = n^3$:

$$
n^2 = O(n^{3 - \epsilon}) \quad \text{for } \epsilon = 1
$$

This satisfies **Case 1**, so:

$$
T(n) = \Theta(n^3)
$$

### Example 2: T(n) = T(n/2) + c

Here $a = 1$, $b = 2$, $f(n) = c$ (a constant, i.e., $\Theta(1)$).

$$
n^{\log_b a} = n^{\log_2 1} = n^0 = 1
$$

Compare $f(n) = c = \Theta(n^0 \log^0 n)$ with $n^{\log_b a} = n^0$: they match with $k = 0$.

This satisfies **Case 2**, so:

$$
T(n) = \Theta(n^0 \log^{0+1} n) = \Theta(\log n)
$$

This confirms the same result found earlier by direct expansion of the binary search recurrence.

---

## 7. Analyze Time Complexity of Above Recurrences

| Recurrence | $a$ | $b$ | $f(n)$ | $n^{\log_b a}$ | Master Theorem Case | Result |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| $T(n) = T(n/2) + c$ (Binary Search) | 1 | 2 | $\Theta(1)$ | $1$ | Case 2 ($k=0$) | $\Theta(\log n)$ |
| $T(n) = 8T(n/2) + n^2$ | 8 | 2 | $n^2$ | $n^3$ | Case 1 | $\Theta(n^3)$ |

---

## 8. Algorithm Correctness and Loop Invariants

An algorithm is said to be **correct** if, for every valid input instance, it halts with the correct output. While empirical testing shows that code runs on selected test inputs, mathematical proof guarantees correctness on **all possible** inputs.

### The Three Loop Invariant Properties

A **loop invariant** is a formal assertion about program variables that is true before and after each iteration of a loop. Proving algorithm correctness using a loop invariant requires establishing three properties (directly analogous to mathematical induction):

1. **Initialization (Base Case):**
   The invariant is true prior to the first iteration of the loop.
2. **Maintenance (Inductive Step):**
   If the invariant is true before an iteration of the loop, it remains true before the next iteration.
3. **Termination:**
   When the loop terminates, the invariant provides a useful property that proves the algorithm halts with the correct output.

| Property | Induction Counterpart | Verification Step |
| :--- | :--- | :--- |
| **Initialization** | Base Case | Verify the invariant holds before loop index $j$ takes its initial value. |
| **Maintenance** | Inductive Step | Show that executing loop body preserves the invariant for index $j + 1$. |
| **Termination** | Final Conclusion | Evaluate the invariant at loop exit ($j = \text{exit bound}$) to establish postcondition correctness. |

### Case Study: Correctness of Insertion Sort

Consider the standard Insertion Sort algorithm:

```text
INSERTION-SORT(A, n)
1. for j = 2 to n:
2.     key = A[j]
3.     // Insert A[j] into the sorted subarray A[1 .. j - 1]
4.     i = j - 1
5.     while i > 0 and A[i] > key:
6.         A[i + 1] = A[i]
7.         i = i - 1
8.     A[i + 1] = key
```

#### Stated Loop Invariant
> At the start of each iteration of the outer `for` loop (lines 1–8), the subarray $A[1 \dots j-1]$ consists of the elements originally in $A[1 \dots j-1]$, but in sorted order.

#### Formal Proof
1. **Initialization:**
   Prior to the first iteration, $j = 2$. The subarray $A[1 \dots j-1]$ is simply $A[1 \dots 1]$, consisting of a single element. A single-element array is trivially sorted, so the invariant holds before the loop begins.
2. **Maintenance:**
   The inner `while` loop (lines 5–7) shifts elements $A[j-1], A[j-2], \dots$ that are greater than `key` one position to the right until the appropriate spot for `key` is found. Line 8 inserts `key` into this position. The subarray $A[1 \dots j]$ now contains the original elements of $A[1 \dots j]$ in sorted order. Incrementing $j$ for the next iteration preserves the invariant for $j + 1$.
3. **Termination:**
   The outer loop terminates when $j > n$, which means $j = n + 1$. Substituting $j = n + 1$ into the invariant: the subarray $A[1 \dots (n + 1) - 1] = A[1 \dots n]$ consists of the original elements of $A[1 \dots n]$ in sorted order. Since $A[1 \dots n]$ is the entire array, the algorithm is proven correct.

### Mathematical Induction in Algorithm Proofs

For recursive algorithms, correctness is demonstrated using **mathematical induction on input size $n$**:
- **Weak Induction:** Assume correctness for subproblems of size $n - 1$ to prove correctness for size $n$ (used in decrease-and-conquer procedures).
- **Strong Induction:** Assume correctness for all subproblem sizes $k < n$ to prove correctness for size $n$ (used in divide-and-conquer algorithms like Merge Sort and Quick Sort).

---

[Previous: Chapter 2 - Complexity Analysis and Asymptotic Notation](../Chapter%202%20-%20Complexity%20Analysis%20and%20Asymptotic%20Notation/README.md) | [Home](../README.md) | [Next: Chapter 4 - Searching and Basic Traversal](../Chapter%204%20-%20Searching%20and%20Basic%20Traversal/README.md)
