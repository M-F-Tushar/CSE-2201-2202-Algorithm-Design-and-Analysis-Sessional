# Chapter 16 — String Matching Algorithms

[Previous: Chapter 15 - Lower Bound Theory and NP Completeness](../Chapter%2015%20-%20Lower%20Bound%20Theory%20and%20NP%20Completeness/README.md) | [Home](../README.md) | [Next: References](../References/README.md)

---

String matching means finding where a short **pattern** $P$ appears inside a longer **text** $T$. This chapter focuses on the **Rabin-Karp algorithm**, which uses polynomial hashes to check each possible window quickly.

For exam preparation, do not memorize this chapter as many long answers. Learn the seven question types below and use the same neat order every time. The most important one is the complete numerical trace: write the powers, pattern hash, prefix hash, window comparisons, and final answer.

> **Main exam focus:** Rabin-Karp dry run, polynomial-hash formulas, window-hash derivation, collisions, and complexity.

---

## Table of Contents

1. [Question Type 1: Rabin-Karp Numerical / Hand Trace](#question-type-1-rabin-karp-numerical--hand-trace)
2. [Question Type 2: Write or Explain the Rabin-Karp Algorithm](#question-type-2-write-or-explain-the-rabin-karp-algorithm)
3. [Question Type 3: Why Simple ASCII-Sum Hashing Fails](#question-type-3-why-simple-ascii-sum-hashing-fails)
4. [Question Type 4: Collision or Spurious Hit](#question-type-4-collision-or-spurious-hit)
5. [Question Type 5: Naive Search vs. Rabin-Karp](#question-type-5-naive-search-vs-rabin-karp)
6. [Question Type 6: Derive the $O(1)$ Window-Hash Formula](#question-type-6-derive-the-o1-window-hash-formula)
7. [Question Type 7: Derive Time and Space Complexity](#question-type-7-derive-time-and-space-complexity)
8. [Formulas to Memorize](#formulas-to-memorize)
9. [Most Important Exam Template](#most-important-exam-template)
10. [Short Conceptual Questions](#short-conceptual-questions)
11. [What to Prioritize for the Exam](#what-to-prioritize-for-the-exam)

---

## Question Type 1: Rabin-Karp Numerical / Hand Trace

### Possible exact question

Using the Rabin-Karp string matching algorithm, find all occurrences of pattern $P = \text{"cab"}$ in text $T = \text{"ababcabab"}$. Show the hash calculations and state the time complexity.

### Given

$$
T = \text{"ababcabab"}, \qquad P = \text{"cab"}
$$

$$
n = 9, \qquad m = 3
$$

For easy hand calculation, use:

$$
a=1,\quad b=2,\quad c=3,\quad p=10
$$

Here, $p=10$ is chosen only to make the arithmetic easy to write by hand. In a practical implementation, a larger base and a modulus are used.

### Step 1: Number of candidate windows

$$
n-m+1=9-3+1=\boxed{7}
$$

The possible starting indices are:

$$
0,1,2,3,4,5,6
$$

### Step 2: Calculate powers

Write $pw[i]=p^i$:

| $i$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $pw[i]$ | 1 | 10 | 100 | 1,000 | 10,000 | 100,000 | $10^6$ | $10^7$ | $10^8$ |

You do not need a paragraph explaining this table.

### Step 3: Calculate the pattern hash

For $P=\text{"cab"}$, the character values are $c=3$, $a=1$, and $b=2$.

$$
\begin{aligned}
patHash &= 3(10^0)+1(10^1)+2(10^2) \\
        &= 3+10+200 \\
        &= \boxed{213}
\end{aligned}
$$

Show this calculation in a numerical question.

### Step 4: Construct the prefix hash

Use:

$$
hs[i]=hs[i-1]+val(T[i])p^i
$$

For the first character, $hs[0]=val(T[0])$. No modulus is needed for this small hand calculation.

| $i$ | Character $T[i]$ | $pw[i]$ | $hs[i]$ |
| :---: | :---: | :---: | :---: |
| 0 | a | 1 | 1 |
| 1 | b | 10 | 21 |
| 2 | a | 100 | 121 |
| 3 | b | 1,000 | 2,121 |
| 4 | c | 10,000 | 32,121 |
| 5 | a | 100,000 | 132,121 |
| 6 | b | 1,000,000 | 2,132,121 |
| 7 | a | 10,000,000 | 12,132,121 |
| 8 | b | 100,000,000 | 212,132,121 |

For a handwritten exam, this table is enough; you do not need to explain every row in sentences.

### Step 5: Check each window

For a window beginning at $i$, let:

$$
l=i,\qquad r=i+m-1
$$

Its hash and the aligned pattern hash are:

$$
winHash =
\begin{cases}
hs[r], & i=0 \\
hs[r]-hs[i-1], & i>0
\end{cases}
\qquad\qquad
 target=patHash\times pw[i]
$$

Compare the two values:

| $i$ | Window | $winHash$ | $patHash\times pw[i]$ | Result |
| :---: | :---: | ---: | ---: | :---: |
| 0 | `aba` | 121 | 213 | No |
| 1 | `bab` | 2,120 | 2,130 | No |
| 2 | `abc` | 32,100 | 21,300 | No |
| 3 | `bca` | 132,000 | 213,000 | No |
| 4 | `cab` | 2,130,000 | 2,130,000 | **MATCH** |
| 5 | `aba` | 12,100,000 | 21,300,000 | No |
| 6 | `bab` | 212,000,000 | 213,000,000 | No |

![Rabin-Karp sliding-window trace for text `ababcabab` and pattern `cab`](diagrams/ch16-04-sliding-window-dry-run.svg)

Therefore:

$$
\boxed{\text{Pattern occurs at index }4}
$$

### What should appear on your exam paper?

Remember this order:

$$
\boxed{\text{Given}\rightarrow\text{Powers}\rightarrow\text{Pattern Hash}\rightarrow\text{Prefix Hash}\rightarrow\text{Window Comparison}\rightarrow\text{Answer}}
$$

---

## Question Type 2: Write or Explain the Rabin-Karp Algorithm

### Possible exact question

Describe the Rabin-Karp string matching algorithm using polynomial rolling hashing. Analyze its time and space complexity.

### Exam-ready answer

**Rabin-Karp algorithm:** Rabin-Karp searches for a pattern $P$ of length $m$ in a text $T$ of length $n$ by comparing hash values. It calculates the pattern hash once, then compares it with the hash of each text window of length $m$.

#### Step 1: Map characters to numbers

For lowercase English letters, use:

$$
val(c)=c-'a'+1
$$

Thus $a=1,b=2,\ldots,z=26$.

#### Step 2: Precompute powers

Choose a base $p$ and a modulus $M$:

$$
pw[0]=1,\qquad pw[i]=(pw[i-1]\times p)\bmod M
$$

A common practical choice is a base such as $31$ and a large modulus such as $10^9+7$. The small base $10$ above is only for easy hand calculation.

#### Step 3: Construct the text prefix hash

Set $hs[0]=val(T[0])$. For $i>0$:

$$
hs[i]=(hs[i-1]+val(T[i])\times pw[i])\bmod M
$$

#### Step 4: Calculate the pattern hash

$$
patHash=\sum_{k=0}^{m-1}val(P[k])\times pw[k]\pmod M
$$

#### Step 5: Check every text window

For a window from $l=i$ to $r=i+m-1$:

$$
winHash=
\begin{cases}
hs[r], & l=0 \\
(hs[r]-hs[l-1]+M)\bmod M, & l>0
\end{cases}
$$

Compare it with the pattern hash aligned to the same powers:

$$
\boxed{winHash=(patHash\times pw[l])\bmod M}
$$

If the hashes are equal, a possible match has been found. Because different strings can have the same hash, compare the actual characters to confirm the match when exact correctness is required.

### Complexity

With prefix hashing, power calculation, prefix-hash construction, pattern hashing, and checking all windows take $O(n+m)$ time. The power and prefix-hash arrays use $O(n)$ auxiliary space.

With character verification after hash matches, the expected time is $O(n+m)$ when collisions are rare. If many windows collide and each requires checking up to $m$ characters, the worst case is $O(nm)$.

---

## Question Type 3: Why Simple ASCII-Sum Hashing Fails

### Possible exact question

Why is simple ASCII-sum hashing unsuitable for string matching? How does polynomial hashing improve it?

### Exam-ready answer

A simple sum hash adds the character values without considering their positions:

$$
H(s)=\sum_i ASCII(s[i])
$$

For example:

$$
H(\text{"aba"})=97+98+97=292
$$

and:

$$
H(\text{"aab"})=97+97+98=292
$$

But $\text{"aba"}\ne\text{"aab"}$. The hashes are equal because addition is commutative, so this method does not preserve character order.

Polynomial hashing gives each position a different power:

$$
H(s)=\sum_{i=0}^{m-1}val(s[i])p^i\pmod M
$$

For $a=1$, $b=2$, and $p=10$:

$$
H(\text{"aba"})=1(10^0)+2(10^1)+1(10^2)=121
$$

$$
H(\text{"aab"})=1(10^0)+1(10^1)+2(10^2)=211
$$

Thus the positional powers preserve order better and avoid this particular anagram collision. Hash collisions are still possible in general, especially after taking a modulus.

![Simple ASCII-sum hashing ignores character order; polynomial hashing assigns positional weights](diagrams/ch16-02-ascii-vs-polynomial-hash.svg)

---

## Question Type 4: Collision or Spurious Hit

### Possible exact question

What is a spurious hit in Rabin-Karp? How can it be handled?

### Exam-ready answer

A **hash collision** occurs when two different strings have equal hash values:

$$
H(S_1)=H(S_2)\qquad\text{but}\qquad S_1\ne S_2
$$

A **spurious hit** occurs when the pattern hash equals a text-window hash even though the window is not the pattern.

Therefore, when:

$$
H(T[i\ldots i+m-1])=H(P)
$$

compare the characters in the window with the pattern to confirm an actual match.

$$
\boxed{\text{Hash Match}\rightarrow\text{Character Verification}\rightarrow\text{Confirmed Match}}
$$

Using a suitable base and modulus reduces collision risk; it does not make collisions impossible. With verification, the answer is always correct, though the worst-case running time can be $O(nm)$.

---

## Question Type 5: Naive Search vs. Rabin-Karp

### Possible exact question

Compare the naive string matching algorithm with Rabin-Karp.

| Feature | Naive Search | Rabin-Karp |
| :--- | :--- | :--- |
| Basic idea | Compare characters at each window | Compare a pattern hash with each window hash |
| Work per window | Up to $m$ character comparisons | $O(1)$ hash extraction and comparison |
| General time behavior | Depends on the text and pattern; worst case is $O(nm)$ | Expected $O(n+m)$ when collisions are rare |
| Worst-case time | $O(nm)$ | $O(nm)$ if many hash matches require character verification |
| Auxiliary space | $O(1)$ | $O(n)$ for the prefix-hash and power arrays in this version |
| Main issue | Repeats character comparisons | Hash collisions must be verified |

**In one sentence:** Rabin-Karp avoids repeatedly comparing every character by representing the pattern and text windows with hash values.

![Naive string matching checks characters; Rabin-Karp compares window hashes](diagrams/ch16-01-pattern-matching-naive-vs-rk.svg)

---

## Question Type 6: Derive the $O(1)$ Window-Hash Formula

### Possible exact question

Show how prefix hashing lets us obtain the hash of any text window $T[l\ldots r]$ in $O(1)$ time.

### Answer

The prefix hash through position $r$ is:

$$
hs[r]=\sum_{k=0}^{r}val(T[k])p^k
$$

The prefix hash through position $l-1$ is:

$$
hs[l-1]=\sum_{k=0}^{l-1}val(T[k])p^k
$$

Subtracting removes the terms before the window:

$$
hs[r]-hs[l-1]=\sum_{k=l}^{r}val(T[k])p^k
$$

Factor out $p^l$:

$$
\begin{aligned}
\sum_{k=l}^{r}val(T[k])p^k
&=p^l\left(val(T[l])p^0+val(T[l+1])p^1+\cdots+val(T[r])p^{r-l}\right)
\end{aligned}
$$

The extracted window hash is the normal substring hash multiplied by $p^l$. Instead of dividing the window hash, multiply the pattern hash by the same power:

$$
\boxed{winHash=(patHash\times pw[l])\bmod M}
$$

With a modulus, use safe modular subtraction:

$$
winHash=(hs[r]-hs[l-1]+M)\bmod M
$$

For $l=0$, simply use $winHash=hs[r]$. A prefix subtraction and one multiplication take constant time, so each window hash is checked in $O(1)$ time.

![Prefix hashes remove the earlier text and align the window hash with the pattern](diagrams/ch16-03-prefix-hash-window-extraction.svg)

---

## Question Type 7: Derive Time and Space Complexity

### Possible exact question

Derive the time and space complexity of Rabin-Karp using prefix polynomial hashing.

### Answer

Break the work into steps:

| Operation | Time |
| :--- | :---: |
| Build the power array | $O(n)$ |
| Build the text prefix-hash array | $O(n)$ |
| Calculate the pattern hash | $O(m)$ |
| Check $n-m+1$ windows | $O(n)$ |

Therefore, the hash calculations take:

$$
T(n,m)=O(n)+O(n)+O(m)+O(n)=\boxed{O(n+m)}
$$

The arrays $pw[0\ldots n-1]$ and $hs[0\ldots n-1]$ require:

$$
\boxed{\text{Auxiliary Space}=O(n)}
$$

If character-by-character verification is performed after hash matches, a collision-heavy worst case can take:

$$
\boxed{O(nm)}
$$

The commonly stated expected time $O(n+m)$ assumes that hash collisions are rare.

---

## Formulas to Memorize

Do not memorize every paragraph. Memorize these six formulas.

### 1. Number of windows

$$
\boxed{n-m+1}
$$

### 2. Polynomial hash

$$
\boxed{H(s)=\sum_{i=0}^{m-1}val(s[i])p^i\pmod M}
$$

### 3. Powers

$$
\boxed{pw[0]=1,\qquad pw[i]=(pw[i-1]\times p)\bmod M}
$$

### 4. Prefix hash

$$
\boxed{hs[i]=(hs[i-1]+val(T[i])\times pw[i])\bmod M}
$$

### 5. Window hash

For $l>0$:

$$
\boxed{winHash=(hs[r]-hs[l-1]+M)\bmod M}
$$

For $l=0$:

$$
\boxed{winHash=hs[r]}
$$

### 6. Comparison

$$
\boxed{winHash=(patHash\times pw[l])\bmod M}
$$

---

## Most Important Exam Template

If the question gives you a new text and pattern, follow this order.

```text
Given:
T = __________
P = __________

n = ____
m = ____
Number of windows = n - m + 1 = ____

Character mapping:
a = 1, b = 2, ..., z = 26

Base p = ____
Modulus M = ____

Step 1: Power array
pw[] = __________________________

Step 2: Pattern hash
patHash = _______________________
        = ______

Step 3: Prefix hash
Construct the hs[] table.

Step 4: Window checking

| i | Window | winHash | patHash × pw[i] | Result |
|---|--------|---------|-----------------|--------|
| 0 |        |         |                 |        |
| 1 |        |         |                 |        |
| … |        |         |                 |        |

Pattern occurs at index/indices: __________________

Expected time = O(n + m)
Auxiliary space = O(n)
```

---

## Short Conceptual Questions

These are useful as short 2- or 3-mark answers.

### Why use $a=1$, not $a=0$?

If $a=0$, strings made only from `a` (such as `a`, `aa`, and `aaa`) all have hash $0$ under this polynomial formula. Mapping $a$ to $1$ avoids making those characters disappear from the hash.

### Why use a modulus?

Powers grow quickly. Taking values modulo a large $M$ keeps the hashes bounded and prevents integer values from growing without limit. A modulus reduces the hash range, so collisions remain possible.

### Why is the base usually greater than 26?

With values $1$ through $26$, a base larger than the alphabet range helps positional weights behave like distinct digit places. Practical Rabin-Karp still uses a modulus, so choosing a good base does not guarantee that collisions cannot happen.

### What is the difference between a hash match and an actual match?

A hash match means the two hash values are equal. An actual match means every character in the text window equals the corresponding pattern character. Verify characters when exact correctness is required.

---

## What to Prioritize for the Exam

### Must know

1. Complete Rabin-Karp numerical / dry run.
2. Polynomial-hash formula.
3. Prefix-hash and window-hash formulas.
4. Collision / spurious hit and character verification.
5. Expected and worst-case complexity.

### Useful short questions

6. Why simple ASCII-sum hashing fails.
7. Why $a=1$, not $a=0$.
8. Why a modulus is used.
9. Naive search vs. Rabin-Karp.
10. Why multiply the pattern hash by $pw[l]$ instead of dividing the window hash.

### Do not spend limited revision time memorizing

- Twelve long answers word-for-word.
- Every explanatory paragraph.
- A long proof about why the sample happens to have no hash collision.

For a new dry-run question, use the same sequence every time:

$$
\boxed{\text{Given}\rightarrow\text{Powers}\rightarrow\text{Pattern Hash}\rightarrow\text{Prefix Hash}\rightarrow\text{Window Comparison}\rightarrow\text{Answer}}
$$

---

[Previous: Chapter 15 - Lower Bound Theory and NP Completeness](../Chapter%2015%20-%20Lower%20Bound%20Theory%20and%20NP%20Completeness/README.md) | [Home](../README.md) | [Next: References](../References/README.md)
