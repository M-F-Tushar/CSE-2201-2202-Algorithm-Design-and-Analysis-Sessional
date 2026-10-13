"""Chapter 5 (Sorting Algorithms) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 5 - Sorting Algorithms/diagrams"


def stack(items, x=300, w=320, y0=30, gap=34):
    """Vertical flowchart column. Each item: (id, label, color, shape, height)."""
    nodes, y = [], y0
    for nid, label, color, shape, h in items:
        nodes.append(N(nid, label, x, y, w, h, color, shape, 15))
        y += h + gap
    return nodes


# 1 ---------------------------------------------------- reach escalator
reach_escalator = D(
    key="ch5-01-sorting-reach-escalator",
    title="Sorting Reach Escalator: From Quadratic Sorts to O(n log n)",
    size=(1200, 560),
    flow="H",
    nodes=[
        N("e1", "Bubble, Selection, Insertion\nO(n²) worst case", 40, 370, 250, 90, "red", size=14, bold=True),
        N("e2", "Merge Sort\nO(n log n) always", 330, 280, 250, 90, "yellow", size=14, bold=True),
        N("e3", "Quick Sort\nO(n log n) average, in-place", 620, 190, 250, 90, "teal", size=14, bold=True),
        N("e4", "Heap Sort\nO(n log n), in-place", 910, 100, 250, 90, "green", size=14, bold=True),
    ],
    edges=[
        E("e1", "e2", "climb", route="straight"),
        E("e2", "e3", "climb", route="straight"),
        E("e3", "e4", "climb", route="straight"),
    ],
    caption="Each step reaches a faster guarantee; counting and radix sort go further by avoiding comparisons",
)

# 2 ---------------------------------------------------- taxonomy
taxonomy = D(
    key="ch5-02-sorting-taxonomy",
    title="Classification of Sorting Algorithms in This Chapter",
    size=(1180, 420),
    flow="V",
    nodes=[
        N("root", "Sorting Algorithms", 440, 30, 220, 56, "blue", bold=True),
        N("comp", "Comparative Sorts\nDecide order by comparing two items", 20, 150, 640, 64, "yellow"),
        N("non", "Non-Comparative Sorts\nUse digit or key structure", 700, 150, 380, 64, "green"),
        N("quad", "Quadratic\nBubble, Selection, Insertion", 20, 280, 250, 64, "red", size=14),
        N("dnc", "Divide and Conquer\nMerge Sort, Quick Sort", 290, 280, 220, 64, "teal", size=14),
        N("heap", "Heap-Based\nHeap Sort", 530, 280, 220, 64, "violet", size=14),
        N("cnt", "Counting Sort\nSmall key range", 780, 280, 170, 64, "green", size=14),
        N("rad", "Radix / Bucket\nDigit-by-digit", 970, 280, 170, 64, "green", size=14),
    ],
    edges=[
        E("root", "comp"), E("root", "non"),
        E("comp", "quad"), E("comp", "dnc"), E("comp", "heap"),
        E("non", "cnt"), E("non", "rad"),
    ],
    caption="Comparative sorts are bounded below by Ω(n log n); non-comparative sorts can beat that bound under key assumptions",
)

# 3 ---------------------------------------------------- bubble sort flow
bubble_flow = D(
    key="ch5-03-bubble-sort-flow",
    title="Bubble Sort Control Flow",
    size=(780, 720),
    flow="V",
    nodes=stack([
        ("s", "Start pass with j = 0", "blue", "rect", 54),
        ("c", "Compare A[j] with A[j+1]", "yellow", "rect", 54),
        ("d", "A[j] > A[j+1]?", "yellow", "diamond", 80),
        ("sw", "Swap the pair\nset swapped = true", "green", "rect", 60),
        ("adv", "Move to next pair (j = j + 1)", "blue", "rect", 54),
        ("end", "End of unsorted part?", "yellow", "diamond", 80),
        ("fin", "No swap in a full pass?\nIf not, repeat with one fewer item", "teal", "rect", 60),
    ]),
    edges=[
        E("s", "c"), E("c", "d"),
        E("d", "sw", "Yes"),
        E("sw", "adv"),
        E("d", "adv", "No", route="loopr", bend=60),
        E("adv", "end"),
        E("end", "c", "No", route="loopr", bend=100),
        E("end", "fin", "Yes"),
    ],
    caption="The largest unsorted value bubbles to the end of each pass",
)

# 4 ---------------------------------------------------- selection sort flow
selection_flow = D(
    key="ch5-04-selection-sort-flow",
    title="Selection Sort Control Flow",
    size=(780, 620),
    flow="V",
    nodes=stack([
        ("s", "Start with i = 0\n(whole array unsorted)", "blue", "rect", 60),
        ("scan", "Scan A[i..n-1] for the minimum", "yellow", "rect", 54),
        ("swp", "Swap minimum with A[i]\n(at most n - 1 swaps)", "green", "rect", 60),
        ("grow", "Grow sorted prefix: i = i + 1", "blue", "rect", 54),
        ("chk", "Is i < n - 1?", "yellow", "diamond", 80),
        ("done", "Array fully sorted", "teal", "rect", 54),
    ]),
    edges=[
        E("s", "scan"), E("scan", "swp"), E("swp", "grow"), E("grow", "chk"),
        E("chk", "scan", "Yes", route="loopr", bend=60),
        E("chk", "done", "No"),
    ],
    caption="Selection sort always scans the unsorted part fully, even when the array is already sorted",
)

# 5 ---------------------------------------------------- insertion sort flow
insertion_flow = D(
    key="ch5-05-insertion-sort-flow",
    title="Insertion Sort Control Flow",
    size=(780, 620),
    flow="V",
    nodes=stack([
        ("s", "Treat A[0] as the sorted prefix", "blue", "rect", 54),
        ("pick", "Take key = A[i] (next item)", "yellow", "rect", 54),
        ("shift", "Shift larger items one step right", "green", "rect", 60),
        ("place", "Drop key into the gap", "green", "rect", 54),
        ("more", "More items left?", "yellow", "diamond", 80),
        ("done", "Array fully sorted", "teal", "rect", 54),
    ]),
    edges=[
        E("s", "pick"), E("pick", "shift"), E("shift", "place"), E("place", "more"),
        E("more", "pick", "Yes", route="loopr", bend=60),
        E("more", "done", "No"),
    ],
    caption="Insertion sort is fast on nearly sorted input because the shift loop does little work",
)

# 6 ---------------------------------------------------- counting sort flow
counting_flow = D(
    key="ch5-06-counting-sort-flow",
    title="Counting Sort Pipeline",
    size=(780, 620),
    flow="V",
    nodes=stack([
        ("s", "Find min and max keys\nk = max - min + 1", "blue", "rect", 60),
        ("cnt", "Count occurrences of each key", "yellow", "rect", 54),
        ("pre", "Prefix sums give final positions", "yellow", "rect", 54),
        ("build", "Place items from right to left\n(keeps equal keys stable)", "green", "rect", 60),
        ("done", "Sorted output\nO(n + k) time, O(k) space", "teal", "rect", 60),
    ]),
    edges=[E("s", "cnt"), E("cnt", "pre"), E("pre", "build"), E("build", "done")],
    caption="Counting sort never compares elements, so it works only when the key range k is small",
)

# 7 ---------------------------------------------------- merge sort flow
merge_flow = D(
    key="ch5-07-merge-sort-divide-conquer",
    title="Merge Sort: Divide and Conquer Phases",
    size=(780, 620),
    flow="V",
    nodes=stack([
        ("s", "Input array of n items", "blue", "rect", 54),
        ("div", "DIVIDE: split into two halves", "yellow", "rect", 54),
        ("base", "Recurse until one item is left", "yellow", "rect", 60),
        ("con", "CONQUER: merge two sorted halves\nusing a temporary buffer", "green", "rect", 60),
        ("done", "Sorted array\n(log n levels of merging)", "teal", "rect", 60),
    ]),
    edges=[E("s", "div"), E("div", "base"), E("base", "con"), E("con", "done")],
    caption="The divide step costs nothing; all comparisons happen while merging, so merge sort is always O(n log n)",
)

# 8 ---------------------------------------------------- quick sort flow
quick_flow = D(
    key="ch5-08-quick-sort-partition",
    title="Quick Sort Partition Flow",
    size=(780, 620),
    flow="V",
    nodes=stack([
        ("s", "Choose a pivot value\n(first, last, median, or random)", "blue", "rect", 60),
        ("part", "Partition: smaller values left,\nlarger values right", "yellow", "rect", 60),
        ("piv", "Pivot lands in its final position", "green", "rect", 54),
        ("rec", "Recurse on left and right parts", "yellow", "rect", 54),
        ("base", "Stop when 0 or 1 item is left", "teal", "rect", 54),
    ]),
    edges=[E("s", "part"), E("part", "piv"), E("piv", "rec"), E("rec", "base")],
    caption="A poor pivot produces unbalanced partitions, which raises the worst case to O(n²)",
)

# 9 ---------------------------------------------------- heap sort flow
heap_flow = D(
    key="ch5-09-heap-sort-flow",
    title="Heap Sort Control Flow",
    size=(780, 660),
    flow="V",
    nodes=stack([
        ("s", "Build max-heap from the array", "blue", "rect", 54),
        ("swp", "Swap root (largest) with last item", "green", "rect", 54),
        ("shr", "Shrink heap by one item", "yellow", "rect", 54),
        ("fix", "Sift new root down to restore heap", "yellow", "rect", 54),
        ("chk", "Heap size > 1?", "yellow", "diamond", 80),
        ("done", "Ascending array\nO(n log n) time, O(1) extra space", "teal", "rect", 60),
    ]),
    edges=[
        E("s", "swp"), E("swp", "shr"), E("shr", "fix"), E("fix", "chk"),
        E("chk", "swp", "Yes", route="loopr", bend=60),
        E("chk", "done", "No"),
    ],
    caption="The sorted tail grows at the end of the array while the heap shrinks at the front",
)

DIAGRAMS = [
    reach_escalator,
    taxonomy,
    bubble_flow,
    selection_flow,
    insertion_flow,
    counting_flow,
    merge_flow,
    quick_flow,
    heap_flow,
]
