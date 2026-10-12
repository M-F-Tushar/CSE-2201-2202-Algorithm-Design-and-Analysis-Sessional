# Chapter 2 - Complexity Analysis and Asymptotic Notation

[Previous: Chapter 1 - Introduction and Algorithm Foundations](../Chapter%201%20-%20Introduction%20and%20Algorithm%20Foundations/README.md) | [Home](../README.md) | [Next: Chapter 3 - Recurrences Correctness and Loop Invariants](../Chapter%203%20-%20Recurrences%20Correctness%20and%20Loop%20Invariants/README.md)

---

Complexity analysis measures how the running time (or space) of an algorithm grows as the input size $n$ grows. Asymptotic notation gives a precise mathematical language for describing that growth while ignoring machine-dependent constants and low-order terms.

This chapter covers how to read time complexity directly from loop structure, how input size and cases (best, average, worst) affect the count, how to state growth formally using Big-O, Big-Omega, and Big-Theta notation, and the algebra and summations needed to simplify the results.

---

## Table of Contents

1. [Time Complexity of Loops](#1-time-complexity-of-loops)
   - [Linear Loops](#linear-loops)
   - [Logarithmic Loops](#logarithmic-loops)
   - [Nested Independent Loops](#nested-independent-loops)
   - [Nested Dependent Loops](#nested-dependent-loops)
   - [Visual Map: Loop Growth Rate](#visual-map-loop-growth-rate)
2. [Input Size, Running Time, and Space Complexity](#2-input-size-running-time-and-space-complexity)
3. [Best, Average, and Worst Case](#3-best-average-and-worst-case)
   - [Visual Map: Best, Average, and Worst Case](#visual-map-best-average-and-worst-case)
4. [Asymptotic Notation](#4-asymptotic-notation)
   - [Big-O Notation - Upper Bound](#big-o-notation---upper-bound)
   - [Big-Omega Notation - Lower Bound](#big-omega-notation---lower-bound)
   - [Big-Theta Notation - Tight Bound](#big-theta-notation---tight-bound)
   - [Visual Map: Upper vs Lower vs Tight Bound](#visual-map-upper-vs-lower-vs-tight-bound)
5. [Comparing the Three Notations](#5-comparing-the-three-notations)
6. [Growth of Functions and Common Complexity Classes](#6-growth-of-functions-and-common-complexity-classes)
   - [Visual Map: Common Complexity Classes](#visual-map-common-complexity-classes)
7. [Algebraic Simplification](#7-algebraic-simplification)
   - [Summations](#summations)
8. [Analyze Time Complexity of Above Loop Patterns](#8-analyze-time-complexity-of-above-loop-patterns)

---

## 1. Time Complexity of Loops

The fastest way to estimate an algorithm's running time is to count how many times its loop body executes as a function of $n$.

### Linear Loops

```c
for (i = 1; i <= n; i++) {
    // constant work
}
```

The counter $i$ increases by 1 every iteration, so the loop body runs exactly $n$ times.

$$
T(n) = n \implies T(n) = O(n)
$$

The same conclusion holds for any loop whose counter moves by a fixed step over a range of size $n$, regardless of the starting index or the comparison operator:

```c
for (j = 0; j < n; j++) {
    // constant work
}
```

This loop also runs $n$ times, so $T(n) = O(n)$.

### Logarithmic Loops

```c
for (i = 1; i <= n; i *= 2) {
    // constant work
}
```

Here $i$ does not increase by a fixed amount, it **doubles** every iteration:

$$
1, 2, 4, 8, 16, \dots, n
$$

After $k$ iterations, $i = 2^k$. The loop stops once:

$$
2^k = n \implies k = \log_2 n
$$

So the loop body runs $\log_2 n$ times:

$$
T(n) = O(\log n)
$$

The same idea applies when the counter is divided instead of multiplied each time (for example `i /= 2`): halving or doubling a value down to/up from 1, $n$ times, both take $\log_2 n$ steps.

### Nested Independent Loops

```c
for (i = 1; i <= n; i++) {
    for (j = 1; j <= n; j++) {
        // constant work
    }
}
```

The inner loop runs $n$ times for each of the $n$ outer iterations, so the body runs $n \cdot n$ times:

$$
T(n) = n \cdot n = n^2 \implies T(n) = O(n^2)
$$

### Nested Dependent Loops

```c
for (i = 1; i <= n; i++) {
    for (j = 1; j <= i; j++) {
        // constant work
    }
}
```

Now the inner loop depends on $i$: it runs $1, 2, \dots, n$ times. Adding these counts gives an arithmetic series (see [Summations](#summations)):

$$
T(n) = \sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \Theta(n^2)
$$

The exact count is about half of $n^2$, but the constant $\tfrac{1}{2}$ is dropped, so the growth is still quadratic.

### Visual Map: Loop Growth Rate

![Loop Growth Rate - Additive vs Multiplicative Steps](diagrams/ch2-01-loop-growth-rate.svg)

---

## 2. Input Size, Running Time, and Space Complexity

The **input size** $n$ is the quantity the running time is measured against. For an array or a list it is the number of elements. For a number, it is the number of digits (or bits) needed to write it, not its value. For example, the loop `for (i = 1; i <= N; i++)` runs $N$ times, but $N$ can be stored in only $\log_2 N$ bits. Measured against its input size $\log_2 N$, the loop is exponential, which is why it is called *pseudo-polynomial*. Always state what $n$ measures before writing a complexity.

**Running time** counts the basic steps an algorithm performs. **Space complexity** counts the extra memory it uses as a function of $n$, usually ignoring the input itself.

| Algorithm | Time | Extra Space | Why |
| :--- | :---: | :---: | :--- |
| Sum an array with one running total | $O(n)$ | $O(1)$ | One pass; one variable |
| Copy an array into a new array | $O(n)$ | $O(n)$ | One pass; a new array of size $n$ |
| Recursive sum `sum(A, n) = A[n-1] + sum(A, n-1)` | $O(n)$ | $O(n)$ | $n$ calls; each call waits on the stack |

```c
int sum(int A[], int n) {
    if (n == 0) return 0;
    return A[n - 1] + sum(A, n - 1);
}
```

The recursive version is slower in space, not in time: it makes $n$ calls, and up to $n$ of them are on the call stack at the same time.

---

## 3. Best, Average, and Worst Case

Some algorithms do different amounts of work on inputs of the same size. Linear search is the standard example:

```c
int linearSearch(int A[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (A[i] == key) return i;
    }
    return -1;
}
```

| Case | Input | Comparisons | Complexity |
| :---: | :--- | :---: | :---: |
| Best | `key` is at `A[0]` | $1$ | $\Theta(1)$ |
| Average | `key` is equally likely at any of the $n$ positions | $\dfrac{1 + 2 + \dots + n}{n} = \dfrac{n+1}{2}$ | $\Theta(n)$ |
| Worst | `key` is at the end, or not in the array | $n$ | $\Theta(n)$ |

- **Best case** is the smallest count over all inputs of size $n$.
- **Worst case** is the largest count over all inputs of size $n$. It is the guarantee most often used in practice.
- **Average case** is the expected count when every input is equally likely. It depends on an assumed distribution of inputs, so state that assumption.

Each case is a different input, so each has its own count. Asymptotic notation (Section 4) can be applied to each count: the best case is $\Theta(1)$, and the worst case is $O(n)$, with the exact value $n$ also giving $\Theta(n)$.

### Visual Map: Best, Average, and Worst Case

![Best, Average, and Worst Case - Linear Search](diagrams/ch2-03-best-avg-worst-case.svg)

---

## 4. Asymptotic Notation

Asymptotic notation describes how a function $f(n)$ grows for large $n$, ignoring constant factors and lower-order terms. It answers three different questions about $f(n)$: what is its **upper bound**, its **lower bound**, and its **exact bound**.

These notations describe a *function*, such as a running-time count. Whether that count is a best, average, or worst case is a separate choice about the input (Section 3).

### Big-O Notation - Upper Bound

$$
f(n) = O(g(n))
$$

if there exist positive constants $c$ and $n_0$ such that:

$$
f(n) \le c \cdot g(n), \qquad \text{for all } n \ge n_0
$$

Big-O says $f(n)$ grows **no faster than** $g(n)$: beyond $n_0$, $g(n)$ (scaled by $c$) stays above $f(n)$.

**Example:** $3n + 5 = O(n)$, because for large $n$ the term $n$ dominates the constant terms. Choosing $c = 8$ and $n_0 = 1$ satisfies $3n + 5 \le 8n$ for all $n \ge 1$.

> Some class notes label this crossing point $k$ instead of $n_0$: the graph of $f(n)$ and $c \cdot g(n)$ cross at $n = k$, and $f(n) \le c \cdot g(n)$ holds for every $n$ to the right of $k$. Both names refer to the same idea.

### Big-Omega Notation - Lower Bound

$$
f(n) = \Omega(g(n))
$$

if there exist positive constants $c$ and $n_0$ such that:

$$
f(n) \ge c \cdot g(n), \qquad \text{for all } n \ge n_0
$$

Big-Omega says $f(n)$ grows **no slower than** $g(n)$: beyond $n_0$, $f(n)$ stays above $g(n)$ (scaled by $c$). It is a lower bound on the function, not a statement about the best case of an algorithm.

Drawn on a graph, Big-O and Big-Omega look like mirror images: for Big-O, $c \cdot g(n)$ sits **above** $f(n)$ once $n \ge k$ (an upper bound); for Big-Omega, $c \cdot g(n)$ sits **below** $f(n)$ once $n \ge k$ (a lower bound).

### Big-Theta Notation - Tight Bound

$$
f(n) = \Theta(g(n))
$$

if and only if both of the following hold:

$$
f(n) = O(g(n)) \qquad \text{and} \qquad f(n) = \Omega(g(n))
$$

Equivalently, there are positive constants $c_1$, $c_2$, and $n_0$ such that $c_1 g(n) \le f(n) \le c_2 g(n)$ for all $n \ge n_0$. Big-Theta means $g(n)$ sandwiches $f(n)$ from both above and below, so it gives the **exact asymptotic growth rate**, not just a bound.

**Worked example:** $3n^2 + 5n = \Theta(n^2)$.

- Upper bound: $5n \le n^2$ when $n \ge 5$, so $3n^2 + 5n \le 4n^2$ for $n \ge 5$. Here $c_2 = 4$.
- Lower bound: $3n^2 + 5n \ge 3n^2$ for all $n \ge 1$. Here $c_1 = 3$.
- So $c_1 = 3$, $c_2 = 4$, $n_0 = 5$ works, and $3n^2 + 5n = \Theta(n^2)$.

### Visual Map: Upper vs Lower vs Tight Bound

![Asymptotic Bounds - Big-O, Big-Omega, and Big-Theta](diagrams/ch2-02-asymptotic-bounds.svg)

---

## 5. Comparing the Three Notations

| Notation | Bound Type | Condition | Reads As |
| :---: | :--- | :--- | :--- |
| $O(g(n))$ | Upper bound | $f(n) \le c \cdot g(n)$ | $f$ grows **no faster than** $g$ |
| $\Omega(g(n))$ | Lower bound | $f(n) \ge c \cdot g(n)$ | $f$ grows **no slower than** $g$ |
| $\Theta(g(n))$ | Tight bound | $O(g(n))$ and $\Omega(g(n))$ both hold | $f$ grows **exactly as fast as** $g$ |

---

## 6. Growth of Functions and Common Complexity Classes

Common running-time functions, ordered from slowest-growing to fastest-growing:

$$
O(1) \subset O(\log n) \subset O(n) \subset O(n \log n) \subset O(n^2) \subset O(n^3) \subset O(2^n) \subset O(n!)
$$

The table shows how quickly each class grows. Even at $n = 100$, the gap between polynomial and exponential is enormous:

| $f(n)$ | $n = 10$ | $n = 20$ | $n = 100$ |
| :---: | :---: | :---: | :---: |
| $\log_2 n$ | $\approx 3.3$ | $\approx 4.3$ | $\approx 6.6$ |
| $n$ | $10$ | $20$ | $100$ |
| $n \log_2 n$ | $\approx 33$ | $\approx 86$ | $\approx 664$ |
| $n^2$ | $100$ | $400$ | $10{,}000$ |
| $n^3$ | $1{,}000$ | $8{,}000$ | $1{,}000{,}000$ |
| $2^n$ | $1{,}024$ | $\approx 1.0 \times 10^6$ | $\approx 1.3 \times 10^{30}$ |
| $n!$ | $3{,}628{,}800$ | $\approx 2.4 \times 10^{18}$ | $\approx 9.3 \times 10^{157}$ |

Typical algorithms in each class:

- $O(1)$: array indexing `A[i]`
- $O(\log n)$: binary search
- $O(n)$: linear search, a single pass over an array
- $O(n \log n)$: merge sort
- $O(n^2)$: bubble sort, naive nested loops over an array
- $O(n^3)$: naive matrix multiplication
- $O(2^n)$: generating all subsets of a set
- $O(n!)$: generating all permutations of a set

### Visual Map: Common Complexity Classes

![Growth of Common Complexity Classes - Slowest to Fastest](diagrams/ch2-04-growth-classes.svg)

---

## 7. Algebraic Simplification

Use these rules to reduce an exact count to its asymptotic class:

- **Drop constant factors:** $5n^2 = O(n^2)$.
- **Drop lower-order terms:** $n^3 + 100n^2 + 7 = O(n^3)$.
- **Sum rule:** $O(f) + O(g) = O(\max(f, g))$. For example, $O(n) + O(n^2) = O(n^2)$.
- **Product rule:** $O(f) \cdot O(g) = O(f \cdot g)$. For example, a loop of $n$ iterations around a body costing $O(\log n)$ is $O(n \log n)$.
- **The base of a logarithm does not matter:** $\log_a n = \Theta(\log_b n)$ for any bases $a, b > 1$, because $\log_a n = \frac{\log_b n}{\log_b a}$ differs only by a constant factor.
- **Exponents cannot be dropped:** $4^n = 2^{2n}$ is **not** $O(2^n)$, because $\frac{4^n}{2^n} = 2^n$ grows without bound.

### Summations

Most loop counts are sums. These identities cover the common cases:

$$
\sum_{i=1}^{n} 1 = n \qquad \sum_{i=1}^{n} i = \frac{n(n+1)}{2} \qquad \sum_{i=0}^{n} 2^i = 2^{n+1} - 1
$$

The first gives a linear loop, the second gives a nested dependent loop, and the third gives a geometric sum (for example, the total work of a loop that doubles its work each level).

---

## 8. Analyze Time Complexity of Above Loop Patterns

| Loop Pattern | Counter Update | Iterations | Time Complexity |
| :--- | :--- | :---: | :---: |
| `for (i = 1; i <= n; i++)` | additive (+1) | $n$ | $O(n)$ |
| `for (j = 0; j < n; j++)` | additive (+1) | $n$ | $O(n)$ |
| `for (i = 1; i <= n; i *= 2)` | multiplicative (×2) | $\log_2 n$ | $O(\log n)$ |
| Nested: `i <= n`, `j <= n` | additive (+1) inside additive | $n \cdot n$ | $O(n^2)$ |
| Nested: `i <= n`, `j <= i` | additive (+1) inside additive | $\frac{n(n+1)}{2}$ | $\Theta(n^2)$ |

For a search algorithm, the count depends on the input case rather than the loop shape alone:

| Algorithm | Best | Average | Worst |
| :--- | :---: | :---: | :---: |
| Linear search | $\Theta(1)$ | $\Theta(n)$ | $\Theta(n)$ |

The recurrence-based way of proving the logarithmic result for divide-style recursive algorithms (rather than loops) is covered next, in [Chapter 3 - Recurrences Correctness and Loop Invariants](../Chapter%203%20-%20Recurrences%20Correctness%20and%20Loop%20Invariants/README.md).

---

[Previous: Chapter 1 - Introduction and Algorithm Foundations](../Chapter%201%20-%20Introduction%20and%20Algorithm%20Foundations/README.md) | [Home](../README.md) | [Next: Chapter 3 - Recurrences Correctness and Loop Invariants](../Chapter%203%20-%20Recurrences%20Correctness%20and%20Loop%20Invariants/README.md)
