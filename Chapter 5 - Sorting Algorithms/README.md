# Chapter 5 - Sorting Algorithms

[Previous: Chapter 4 - Searching and Basic Traversal](../Chapter%204%20-%20Searching%20and%20Basic%20Traversal/README.md) | [Home](../README.md) | [Next: Chapter 6 - Divide and Conquer](../Chapter%206%20-%20Divide%20and%20Conquer/README.md)

Sorting means putting items into an order, such as smallest to largest. It makes many other tasks easier: for example, finding an item, spotting duplicates, or arranging appointments.

This chapter introduces several ways to sort. The examples use small lists so you can follow each move by hand.

1. What sorting means and how sorts differ
2. Choosing a sorting method
3. Bubble sort
4. Selection sort
5. Insertion sort
6. Merge sort
7. Quick sort
8. Heap sort
9. Counting sort
10. Comparing the methods

---

## Start Here: The Idea in Plain Words

**The goal:** rearrange a list so the values go from smallest to largest. For example, `[5, 2, 4]` becomes `[2, 4, 5]`. The list keeps the same items; only their positions change.

**Tiny example.** Look at the neighboring values in `[5, 2, 4]`. Since 5 is bigger than 2, switch them: `[2, 5, 4]`. Then switch 5 and 4: `[2, 4, 5]`. That is the basic idea behind bubble sort. Other methods choose a smallest item, insert an item into its place, split the list into smaller lists, or count how often each value appears.

**Words used in this chapter, in simple terms**

| Word | Simple meaning |
| :--- | :--- |
| Compare | Check which of two values comes first. |
| Key | The value used to decide an item's order. |
| Stable | Equal-key items stay in the same relative order they had before sorting. |
| In place | Sorts inside the original list, using little extra memory. |
| Pivot | A chosen value used to divide a list in quick sort. |
| Max-heap | A tree-shaped arrangement where each parent is at least as large as its children. |
| Key range | The set of values counting sort must keep track of. |

**How to read the pseudocode:** these examples use common code symbols, but remain pseudocode rather than one specific programming language.

| Notation | Meaning |
| :--- | :--- |
| `A[i]` | The item at index `i` in array `A`. Indexes start at 0, so the last item is `A[n - 1]` when `n = length(A)`. |
| `A[left..right]` | The part of the array from `left` through `right`, including both ends. |
| `i: integer`, `swapped: boolean`, `key: item` | Examples of types: a whole number, a true/false value, or one item being sorted. |
| `=` and `==` | `=` stores a value; `==` checks whether two values are equal. |
| `<`, `<=`, `>`, `>=` | Compare which value is smaller or larger. |
| `&&` | “And.” The second test is checked only if the first one is true, which helps avoid looking outside the array. |
| `+= 1`, `-= 1` | Add one to or subtract one from a value. |
| `for i = 0 to n - 1`, `downto` | The loop includes its final value; `downto` counts backward. |
| `length(A)`, `floor(x)` | Count the items in `A`; round `x` down to a whole number. |
| `swap(x, y)`, `append(list, x)`, `break`, `return` | Exchange two values, add to a list, leave a loop, or finish and give back a result. |
| `-> array`, `-> integer`, `-> void` | The result type: return an array, return an integer, or change the array without returning a value. |

**Before you start:** it helps to know how to read [Big-O notation](../Chapter%202%20-%20Complexity%20Analysis%20and%20Asymptotic%20Notation/README.md). **Reading tip:** first understand the everyday idea and follow the example list; then use the pseudocode to check the steps.

---

## 1. What Sorting Means and How Sorts Differ

A sorting method takes a list and rearranges it into the chosen order. In this chapter, the chosen order is smallest to largest.

### Visual Map: Two Ways to Sort

![Sorting methods grouped by how they decide the order](diagrams/ch5-02-sorting-taxonomy.svg)

Most methods here are **comparison sorts**: they decide which item comes first by comparing items. Counting sort is different: it counts how often each allowed number appears, so it does not compare items with each other.

A **stable** sort keeps equal-key items in their original relative order. For example, if two students have the same score and the first student was listed first, a stable sort keeps that order. Stability matters when items have other information attached to their keys.

An **in-place** sort works in the original list and needs little extra memory. Merge sort and counting sort need extra storage for their work. Quick sort rearranges the original list, but its recursive calls still use some extra memory.

There is an important limit: any comparison sort needs at least about `n log n` comparisons in the worst case, where `n` is the number of items. Counting sort can be faster when the values come from a small, known range because it uses counts instead of comparisons.

---

## 2. Choosing a Sorting Method

No method is best for every situation. The useful question is what matters most: a simple approach, stable ordering, a reliable time guarantee, or a small range of integer values.

### Visual Map: Choose by What You Need

![A quick guide to choosing a sorting method](diagrams/ch5-01-sorting-reach-escalator.svg)

- For a tiny list or one that is nearly sorted, insertion sort is often a good fit.
- For a guaranteed `O(n log n)` time and stable results, choose merge sort if extra memory is available.
- For `O(n log n)` time with little extra memory, heap sort is an option when stability is not needed.
- Quick sort is often fast in practice, but a poor pivot can make it much slower.
- Counting sort is useful when the list contains small, nonnegative integers.

---

## 3. Bubble Sort

**Core idea:** look at neighboring items and switch them when they are in the wrong order. A large value moves toward the end with each pass.

Imagine walking along the list from left to right. At each pair, put the larger value on the right. When you reach the end, the largest value you had not placed yet is in its final position. Repeat on the part that remains.

### Visual Walkthrough: One Pass at a Time

![Bubble sort moves large values to the end with each pass](diagrams/ch5-03-bubble-sort-flow.svg)

Start with `[5, 2, 4, 6, 1, 3]`:

| Step | List after the pass | What is now settled? |
| :--- | :--- | :--- |
| Start | `[5, 2, 4, 6, 1, 3]` | Nothing yet |
| Pass 1 | `[2, 4, 5, 1, 3, 6]` | 6 is at the end |
| Pass 2 | `[2, 4, 1, 3, 5, 6]` | 5 and 6 are at the end |
| Pass 3 | `[2, 1, 3, 4, 5, 6]` | 4, 5, and 6 are at the end |
| Pass 4 | `[1, 2, 3, 4, 5, 6]` | The list is sorted |
| Pass 5 | `[1, 2, 3, 4, 5, 6]` | No switch is needed, so stop |

### Instructions

1. Count the items and begin at the first pair, at positions 0 and 1.
2. Compare each pair of neighbors from left to right. If the left value is larger, switch the two values; if they are equal or already in order, leave them alone.
3. Continue to the end of the part that is not settled yet. The largest value in that part will have moved to its final position at the right.
4. Start another pass, stopping one position earlier because the rightmost value is already settled.
5. If a pass makes no switches, stop: the list is already in order. Otherwise, keep passing through the remaining part until it is sorted.

### Pseudocode

```text
BUBBLE-SORT(A: array of comparable items) -> array of comparable items
n: integer = length(A)
if n < 2:
    return A

for pass: integer = 0 to n - 2:
    swapped: boolean = false
    for j: integer = 0 to n - 2 - pass:
        if A[j] > A[j + 1]:
            swap(A[j], A[j + 1])
            swapped = true
    if swapped == false:
        break
return A
```

### How much work does it do?

- Best case: `Θ(n)` when the list is already sorted and the method stops after one pass.
- Average and worst case: `Θ(n²)` comparisons.
- Extra memory: `Θ(1)`.
- Stable: yes. Equal items are not switched with each other.

---

## 4. Selection Sort

**Core idea:** find the smallest item that has not been placed yet, then put it in the next open position.

At first, the whole list is waiting to be sorted. Find its smallest value and move that value to the first position. Then look only at the remaining part, find its smallest value, and place it second. The sorted part grows one position at a time.

### Visual Walkthrough: Pick the Next Smallest Item

![Selection sort grows a sorted part from left to right](diagrams/ch5-04-selection-sort-flow.svg)

Start with `[5, 2, 4, 6, 1, 3]`:

| Round | List after the round | Smallest value placed |
| :--- | :--- | :---: |
| Start | `[5, 2, 4, 6, 1, 3]` | — |
| 1 | `[1, 2, 4, 6, 5, 3]` | 1 |
| 2 | `[1, 2, 4, 6, 5, 3]` | 2 (already there) |
| 3 | `[1, 2, 3, 6, 5, 4]` | 3 |
| 4 | `[1, 2, 3, 4, 5, 6]` | 4 |
| 5 | `[1, 2, 3, 4, 5, 6]` | 5 (already there) |

### Instructions

1. Treat the left side as the settled part; at the beginning it is empty. Let `i` be the first position that is not settled.
2. Assume `A[i]` is the smallest value in the remaining part and remember its position as `minIndex`.
3. Check every value to the right, from `i + 1` through the last position. If `A[j]` is smaller than `A[minIndex]`, update `minIndex` to `j`.
4. When the scan reaches the end, switch `A[i]` with `A[minIndex]`. If the smallest value was already at `i`, this switch changes nothing.
5. Move `i` one position right and repeat. Once only one value remains, it must be in the correct place.

### Pseudocode

```text
SELECTION-SORT(A: array of comparable items) -> array of comparable items
n: integer = length(A)
for i: integer = 0 to n - 2:
    minIndex: integer = i
    for j: integer = i + 1 to n - 1:
        if A[j] < A[minIndex]:
            minIndex = j
    swap(A[i], A[minIndex])
return A
```

### How much work does it do?

- Best, average, and worst case: `Θ(n²)` comparisons. It scans the remaining items even if the list is already sorted.
- It makes at most `n - 1` swaps.
- Extra memory: `Θ(1)`.
- Stable: usually no. A long-distance switch can move an item past an equal item.

---

## 5. Insertion Sort

**Core idea:** keep the left side sorted, then take each new item and insert it into the right place in that sorted part.

Think of sorting playing cards in your hand. Hold the next card, move any larger cards one place to the right, and put the held card into the gap. The sorted part grows by one item each time.

### Visual Walkthrough: Insert One Item at a Time

![Insertion sort puts each new item into the sorted part](diagrams/ch5-05-insertion-sort-flow.svg)

Start with `[5, 2, 4, 6, 1, 3]`:

| Item being added | List after insertion | Sorted part |
| :---: | :--- | :--- |
| — | `[5, 2, 4, 6, 1, 3]` | `[5]` |
| 2 | `[2, 5, 4, 6, 1, 3]` | `[2, 5]` |
| 4 | `[2, 4, 5, 6, 1, 3]` | `[2, 4, 5]` |
| 6 | `[2, 4, 5, 6, 1, 3]` | `[2, 4, 5, 6]` |
| 1 | `[1, 2, 4, 5, 6, 3]` | `[1, 2, 4, 5, 6]` |
| 3 | `[1, 2, 3, 4, 5, 6]` | The whole list |

For example, when adding 1, the values 6, 5, 4, and 2 each move one place right. That creates a gap at the beginning for 1.

### Instructions

1. If the list has fewer than two items, it is already sorted. Otherwise, treat `A[0]` as the first sorted part.
2. Take the next item, `A[i]`, and hold its value aside as `key`. The open position it leaves is the gap.
3. Look left through the sorted part. While the item before the gap is larger than `key`, copy it one position to the right and move the gap one position left.
4. Stop when the gap reaches the beginning or the item before it is no larger than `key`.
5. Put `key` into the gap. The sorted part is now one item longer; repeat with the next item.

### Pseudocode

```text
INSERTION-SORT(A: array of comparable items) -> array of comparable items
n: integer = length(A)
for i: integer = 1 to n - 1:
    key: item = A[i]
    j: integer = i - 1
    while j >= 0 && A[j] > key:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = key
return A
```

### How much work does it do?

- Best case: `Θ(n)` when the list is already sorted; each item needs only a quick check.
- Average and worst case: `Θ(n²)`.
- Extra memory: `Θ(1)`.
- Stable: yes. An item moves only past items that are strictly larger.
- Often useful for tiny or nearly sorted lists.

---

## 6. Merge Sort

**Core idea:** split the list until each piece has one item, then repeatedly join two sorted pieces in the right order.

A one-item list is already sorted. To join two sorted pieces, compare the first item in each piece and move the smaller one to the result. Keep doing that until one piece is empty, then add the remaining items.

### Visual Walkthrough: Split, Then Join in Order

![Merge sort splits the list and joins sorted pieces](diagrams/ch5-07-merge-sort-divide-conquer.svg)

For `[5, 2, 4, 6, 1, 3]`, the pieces change like this:

1. Split into `[5, 2, 4]` and `[6, 1, 3]`.
2. Split those pieces again: `[5, 2]`, `[4]`, `[6, 1]`, and `[3]`.
3. Continue until every piece holds one item.
4. Join neighboring pieces in order: `[2, 5]`, `[4]`, `[1, 6]`, and `[3]`.
5. Join again: `[2, 4, 5]` and `[1, 3, 6]`.
6. Join the last two pieces to get `[1, 2, 3, 4, 5, 6]`.

For the final join, compare the front items of `[2, 4, 5]` and `[1, 3, 6]`. Take 1, then 2, then 3, then 4, then 5. The left piece is empty, so add the remaining 6.

### Instructions

1. Work on a section of the array from `left` through `right`. If `left >= right`, that section has at most one item, so it is already sorted.
2. Find the middle position and split the section into `left..mid` and `mid + 1..right`.
3. Use merge sort on each half. Keep splitting until each small section has one item.
4. To join two sorted halves, compare the first unused item in each half. Copy the smaller one into a temporary array, then advance the position in the half it came from. If the values are equal, take the left value first.
5. When one half is empty, copy all remaining items from the other half. Copy the temporary result back into the same section of the original array.

### Pseudocode

```text
MERGE-SORT(A: array of comparable items) -> array of comparable items
MERGE-RANGE(A, 0, length(A) - 1)
return A

MERGE-RANGE(A: array of items, left: integer, right: integer) -> void
if left >= right:
    return
mid: integer = floor((left + right) / 2)
MERGE-RANGE(A, left, mid)
MERGE-RANGE(A, mid + 1, right)
MERGE(A, left, mid, right)

MERGE(A: array of items, left: integer, mid: integer, right: integer) -> void
temp: array of items = []
i: integer = left
j: integer = mid + 1
while i <= mid && j <= right:
    if A[i] <= A[j]:
        append(temp, A[i])
        i += 1
    else:
        append(temp, A[j])
        j += 1
while i <= mid:
    append(temp, A[i])
    i += 1
while j <= right:
    append(temp, A[j])
    j += 1
for k: integer = 0 to length(temp) - 1:
    A[left + k] = temp[k]
```

### How much work does it do?

- Best, average, and worst case: `Θ(n log n)`.
- Extra memory: `Θ(n)` for the temporary lists used while joining.
- Stable: yes, if equal items are taken from the left piece first.
- A good choice when predictable speed and stable results matter, and extra memory is available.

---

## 7. Quick Sort

**Core idea:** choose one item as a pivot, move smaller items to one side and larger items to the other, then sort the two sides.

After a partition, the pivot is in its final position: everything to its left belongs before it, and everything to its right belongs after it. The same process is then used on each side. In this chapter's example, the last item in each part is the pivot.

### Visual Walkthrough: Place Pivots, Then Sort the Sides

![Quick sort puts each pivot in its final position](diagrams/ch5-08-quick-sort-partition.svg)

Start with `[5, 2, 4, 6, 1, 3]`:

| Step | Pivot or part being sorted | List after the step |
| :--- | :--- | :--- |
| Start | — | `[5, 2, 4, 6, 1, 3]` |
| 1 | Pivot 3 | `[2, 1, 3, 6, 5, 4]` |
| 2 | Sort `[2, 1]`, using 1 as pivot | `[1, 2, 3, 6, 5, 4]` |
| 3 | Sort `[6, 5, 4]`, using 4 as pivot | `[1, 2, 3, 4, 5, 6]` |
| 4 | The last pair `[5, 6]` is already in order | `[1, 2, 3, 4, 5, 6]` |

### Instructions

1. Work on the section from `low` through `high`. If `low >= high`, it has at most one item and needs no more work.
2. Use the last item, `A[high]`, as the pivot. Set `boundary = low`; this marks where the next value no larger than the pivot belongs.
3. Scan positions `low` through `high - 1`. Whenever `A[j] <= pivot`, switch it with `A[boundary]` and move `boundary` one position right. Larger values stay to the right for now.
4. After the scan, switch the pivot with `A[boundary]`. The pivot is now in its final position: values no larger than it are to the left, and larger values are to the right.
5. Repeat the same steps on the sections before and after the pivot. Stop a section when it has at most one item.

### Pseudocode

```text
Call QUICK-SORT(A, 0, length(A) - 1) to sort the whole array.

QUICK-SORT(A: array of comparable items, low: integer, high: integer) -> void
if low >= high:
    return
p: integer = PARTITION(A, low, high)
QUICK-SORT(A, low, p - 1)
QUICK-SORT(A, p + 1, high)

PARTITION(A: array of comparable items, low: integer, high: integer) -> integer
pivot: item = A[high]
boundary: integer = low
for j: integer = low to high - 1:
    if A[j] <= pivot:
        swap(A[boundary], A[j])
        boundary += 1
swap(A[boundary], A[high])
return boundary
```

### Choosing a pivot

This example uses the last item because it makes the steps easy to follow. A real implementation can choose a first item, a random item, or a middle-of-three choice. A better choice makes it more likely that the pivot divides the list into two similar-sized parts.

### How much work does it do?

- Best and average case: `Θ(n log n)` when the divisions are reasonably balanced.
- Worst case: `Θ(n²)` when the divisions are very uneven, such as repeatedly leaving one large part and one tiny part.
- Extra memory: the in-place partition needs little extra space; recursive calls use `Θ(log n)` space on average and can use `Θ(n)` in the worst case.
- Stable: no. Items can cross each other during partitioning.

---

## 8. Heap Sort

**Core idea:** arrange the values so the largest is easy to reach, move it to the end, and repeat with the values that remain.

Heap sort first builds a **max-heap**. Picture a tree where each parent is at least as large as its children. The largest item is at the top. The same tree can be stored in the list: for each parent, its children are the next positions assigned to it.

After building the heap, switch the top value with the last value not yet sorted. That puts the largest remaining value at the end. Shrink the heap, then move the new top down until the parent-is-larger rule is restored.

### Visual Walkthrough: Build a Heap, Then Shrink It

![Heap sort moves the largest heap value to the sorted end](diagrams/ch5-09-heap-sort-flow.svg)

For `[5, 2, 4, 6, 1, 3]`, building the max-heap gives `[6, 5, 4, 2, 1, 3]`. The largest value, 6, is now at the top of the heap.

| Step | List after moving the largest remaining value | Sorted end |
| :--- | :--- | :--- |
| Move 6 | `[5, 3, 4, 2, 1, 6]` | `[6]` |
| Move 5 | `[4, 3, 1, 2, 5, 6]` | `[5, 6]` |
| Move 4 | `[3, 2, 1, 4, 5, 6]` | `[4, 5, 6]` |
| Move 3 | `[2, 1, 3, 4, 5, 6]` | `[3, 4, 5, 6]` |
| Move 2 | `[1, 2, 3, 4, 5, 6]` | `[2, 3, 4, 5, 6]` |

The remaining 1 is already in the right place.

### Instructions

1. Store the list as a tree in array order. The root is at index 0; for a parent at index `i`, its left child is at `2 * i + 1` and its right child is at `2 * i + 2`.
2. Build a max-heap from the bottom upward. Starting at the last parent and moving back to index 0, move each parent down until it is at least as large as its children. The largest item is then at the root, `A[0]`.
3. Switch `A[0]` with the last item still in the heap. That last item is now in its final sorted position.
4. Shrink the heap so it excludes that sorted item. Move the new root down: compare it with its existing children and switch it with the larger child until the parent is at least as large as either child, or it has no children.
5. Repeat the root switch and repair until only one item remains in the heap. The sorted part grows from the right-hand end of the array.

The pseudocode uses `heapSize` as the first index outside the heap. Items from `A[heapSize]` to the end are already in the sorted part.

### Pseudocode

```text
HEAP-SORT(A: array of comparable items) -> array of comparable items
n: integer = length(A)
for i: integer = floor(n / 2) - 1 downto 0:
    SIFT-DOWN(A, i, n)
for end: integer = n - 1 downto 1:
    swap(A[0], A[end])
    SIFT-DOWN(A, 0, end)
return A

SIFT-DOWN(A: array of comparable items, root: integer, heapSize: integer) -> void
while 2 * root + 1 < heapSize:
    left: integer = 2 * root + 1
    right: integer = 2 * root + 2
    largerChild: integer = left
    if right < heapSize && A[right] > A[left]:
        largerChild = right
    if A[root] >= A[largerChild]:
        break
    swap(A[root], A[largerChild])
    root = largerChild
```

### How much work does it do?

- Building the heap takes `Θ(n)` time.
- Moving each largest item and repairing the heap gives `Θ(n log n)` time overall, in the best, average, and worst cases.
- Extra memory: `Θ(1)`.
- Stable: no. The switches can change the order of equal items.

---

## 9. Counting Sort

**Core idea:** count how many times each allowed value appears, then use those counts to place the values in order.

Counting sort does not compare items. It is useful when the items are nonnegative integers in a small known range, such as 0 through 4. If the range is huge, keeping a count for every possible value wastes time and memory.

### Visual Walkthrough: Count, Add, and Place

![Counting sort uses counts to place values in order](diagrams/ch5-06-sorting-counts-flow.svg)

Use `[4, 1, 3, 4, 2, 1]`, where the values range from 0 through 4:

| Value | 0 | 1 | 2 | 3 | 4 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| How many times it appears | 0 | 2 | 1 | 1 | 2 |
| Total items up to this value | 0 | 2 | 3 | 4 | 6 |

The running totals tell us the last output position for each value. Read the input from right to left and place each value in its next available position. The placements, numbered from 1, are: the rightmost 1 goes in slot 2, the 2 in slot 3, the rightmost 4 in slot 6, the 3 in slot 4, the leftmost 1 in slot 1, and the leftmost 4 in slot 5. The result is `[1, 1, 2, 3, 4, 4]`.

### Instructions

1. Let `n` be the number of items and `k` the largest allowed value. Check that every item is an integer from 0 through `k`, then make a counter for each value in that range.
2. Set every counter to zero. Scan `A[0]` through `A[n - 1]` and add one to the counter for the value you see.
3. Change the counts into running totals. For each value `v` from 1 through `k`, add the total for `v - 1` to the total for `v`. Now `count[v]` tells how many input items are no larger than `v`.
4. Make an empty output array of length `n`. Read the input from right to left. For a value `v`, put it at index `count[v] - 1`, then decrease `count[v]` by one so the next `v` uses the previous slot.
5. Return the output array. Reading from right to left is what keeps equal-key items in their original order.

### Pseudocode

```text
COUNTING-SORT(A: array of integers, k: integer) -> array of integers
n: integer = length(A)
count: array[0..k] of integers
for v: integer = 0 to k:
    count[v] = 0
for i: integer = 0 to n - 1:
    count[A[i]] += 1
for v: integer = 1 to k:
    count[v] += count[v - 1]
output: array[0..n - 1] of integers
for i: integer = n - 1 downto 0:
    v: integer = A[i]
    output[count[v] - 1] = v
    count[v] -= 1
return output
```

Reading the input from right to left keeps equal-key items in their original order. That is why this version is stable.

### How much work does it do?

- Time: `Θ(n + k)`, where `n` is the number of items and `k` is the largest allowed value.
- Extra memory: `Θ(n + k)` for the counters and output list.
- Stable: yes, when items are placed from right to left as described.
- Use it when the allowed integer range is small; it is not a good fit when that range is very large.

---

## 10. Comparing the Methods

Here, `n` is the number of items. For counting sort, `k` is the largest value in the known range.

| Method | Best time | Average time | Worst time | Extra memory | Stable? | In place? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble sort | `Θ(n)` | `Θ(n²)` | `Θ(n²)` | `Θ(1)` | Yes | Yes |
| Selection sort | `Θ(n²)` | `Θ(n²)` | `Θ(n²)` | `Θ(1)` | No | Yes |
| Insertion sort | `Θ(n)` | `Θ(n²)` | `Θ(n²)` | `Θ(1)` | Yes | Yes |
| Merge sort | `Θ(n log n)` | `Θ(n log n)` | `Θ(n log n)` | `Θ(n)` | Yes | No |
| Quick sort | `Θ(n log n)` | `Θ(n log n)` | `Θ(n²)` | `Θ(log n)` average; up to `Θ(n)` | No | Yes, with a recursion stack |
| Heap sort | `Θ(n log n)` | `Θ(n log n)` | `Θ(n log n)` | `Θ(1)` | No | Yes |
| Counting sort | `Θ(n + k)` | `Θ(n + k)` | `Θ(n + k)` | `Θ(n + k)` | Yes | No |

A quick way to remember the trade-offs:

- **Bubble, selection, and insertion sort** are easy to follow, but can take much longer on large lists.
- **Insertion sort** is especially useful for small or nearly sorted lists.
- **Merge sort** is steady and stable, but needs extra memory.
- **Quick sort** is often fast, but its performance depends on how well the pivot divides the list.
- **Heap sort** guarantees `Θ(n log n)` time and uses little extra memory, but is not stable.
- **Counting sort** can be very fast for a small range of integer values, but it needs space for that range.

---

## Summary

- Sorting rearranges items into a chosen order without adding or removing items.
- Bubble sort switches neighboring items; selection sort repeatedly chooses the smallest; insertion sort places each new item in a sorted part.
- Merge sort splits and joins lists. Quick sort places pivots and sorts the two sides. Heap sort repeatedly moves the largest value to the end.
- Counting sort uses value counts instead of comparing items, so it works best for a small known range.
- Consider time, extra memory, stability, and the kind of input when choosing a method.
