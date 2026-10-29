"""Chapter 5 (Sorting Algorithms) diagram specs.

Comprehensive, step-by-step explanatory diagrams visualizing each sorting algorithm
from initial unsorted state through every intermediate comparison, swap, shift,
and pass to the final sorted array.
"""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 5 - Sorting Algorithms/diagrams"


# 1 — Practical decision guide
choose_sort = D(
    key="ch5-01-sorting-reach-escalator",
    title="Choose a Sort by What the Situation Needs",
    size=(1020, 470),
    nodes=[
        N("small", "Insertion sort\nSmall or nearly sorted lists", 35, 100, 290, 100, "yellow", size=14, bold=True),
        N("stable", "Merge sort\nStable results\nExtra memory is okay", 365, 100, 290, 100, "teal", size=14, bold=True),
        N("general", "Quick sort\nOften fast; pivot choice matters", 695, 100, 290, 100, "blue", size=14, bold=True),
        N("memory", "Heap sort\nReliable time; little extra memory", 200, 255, 290, 100, "violet", size=13, bold=True),
        N("range", "Counting sort\nSmall, known integer range", 530, 255, 290, 100, "green", size=14, bold=True),
    ],
    caption="Choose for the input and the trade-off you care about; no single method fits every case.",
)

# 2 — Sorts grouped by how they decide order
taxonomy = D(
    key="ch5-02-sorting-taxonomy",
    title="Two Ways to Decide Which Item Comes First",
    size=(1080, 440),
    flow="V",
    nodes=[
        N("root", "Sorting methods", 405, 54, 270, 58, "blue", bold=True),
        N("compare", "Comparison sorts\nCompare items to decide their order", 90, 150, 430, 68, "yellow", size=14),
        N("count", "Counting sort\nCount known integer values", 610, 150, 380, 68, "green", size=14),
        N("simple", "Simple sorts\nBubble, selection,\ninsertion", 20, 295, 190, 76, "red", size=13),
        N("merge", "Split and join\nMerge sort", 220, 295, 190, 76, "teal", size=13),
        N("quick", "Pivot and divide\nQuick sort", 420, 295, 190, 76, "blue", size=13),
        N("heap", "Heap structure\nHeap sort", 620, 295, 190, 76, "violet", size=13),
    ],
    edges=[
        E("root", "compare"),
        E("root", "count"),
        E("compare", "simple"),
        E("compare", "merge"),
        E("compare", "quick"),
        E("compare", "heap"),
    ],
    caption="Counting sort avoids item-to-item comparisons when the possible values are few and known.",
)


# 3 — Bubble Sort: Pass 1 micro-steps + subsequent macro passes
def build_bubble_sort():
    nodes = [
        N("h-p1", "Pass 1 Detailed Trace: Each Comparison & Swap", 28, 64, 530, 36, "blue", size=13, bold=True),
        N("h-pass", "Subsequent Passes: Settle Suffix & Early Exit", 590, 64, 540, 36, "blue", size=13, bold=True),
    ]

    p1_steps = [
        ("p1-0", "Start: unsorted array", [5, 2, 4, 6, 1, 3], ["white"] * 6),
        ("p1-1", "Compare (5, 2): 5 > 2 -> SWAP", [2, 5, 4, 6, 1, 3], ["teal", "teal", "white", "white", "white", "white"]),
        ("p1-2", "Compare (5, 4): 5 > 4 -> SWAP", [2, 4, 5, 6, 1, 3], ["white", "teal", "teal", "white", "white", "white"]),
        ("p1-3", "Compare (5, 6): 5 <= 6 -> KEEP", [2, 4, 5, 6, 1, 3], ["white", "white", "yellow", "yellow", "white", "white"]),
        ("p1-4", "Compare (6, 1): 6 > 1 -> SWAP", [2, 4, 5, 1, 6, 3], ["white", "white", "white", "teal", "teal", "white"]),
        ("p1-5", "Compare (6, 3): 6 > 3 -> SWAP", [2, 4, 5, 1, 3, 6], ["white", "white", "white", "white", "teal", "green"]),
    ]

    for idx, (sid, lbl, vals, cols) in enumerate(p1_steps):
        y = 112 + idx * 46
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 220, 36, "gray", size=11))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 256 + cidx * 48, y, 42, 36, col, size=15, bold=(col in ("teal", "green"))))

    nodes.append(N(
        "p1-note",
        "Result of Pass 1: Maximum element (6) bubbled to index 5.\nTeal = swapped pair; Yellow = in order (no swap); Green = settled.",
        28, 396, 530, 48, "light", size=11,
    ))

    sub_passes = [
        ("p2", "Pass 2: bubble 5 to index 4", [2, 4, 1, 3, 5, 6], ["white", "white", "white", "white", "green", "green"]),
        ("p3", "Pass 3: bubble 4 to index 3", [2, 1, 3, 4, 5, 6], ["white", "white", "white", "green", "green", "green"]),
        ("p4", "Pass 4: bubble 3 to index 2", [1, 2, 3, 4, 5, 6], ["white", "white", "green", "green", "green", "green"]),
        ("p5", "Pass 5: check (1, 2) -> 0 swaps", [1, 2, 3, 4, 5, 6], ["yellow", "yellow", "green", "green", "green", "green"]),
        ("fin", "Sorted: all elements locked!", [1, 2, 3, 4, 5, 6], ["green"] * 6),
    ]

    for idx, (sid, lbl, vals, cols) in enumerate(sub_passes):
        y = 112 + idx * 56
        nodes.append(N(f"{sid}-lbl", lbl, 590, y, 230, 40, "gray", size=11))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 830 + cidx * 48, y, 42, 40, col, size=15, bold=(col == "green")))

    nodes.append(N(
        "sub-note",
        "Pass 5 checks (1, 2) in order; 0 swaps made -> Early Exit!\nSorted suffix grows leftward each pass: O(n) best, O(n^2) worst.",
        590, 396, 540, 48, "light", size=11,
    ))

    return D(
        key="ch5-03-bubble-sort-flow",
        title="Bubble Sort: Step-by-Step Comparisons, Swaps, and Passes",
        size=(1160, 500),
        nodes=nodes,
        caption="Left: microscopic adjacent comparisons in Pass 1. Right: macroscopic passes to sorted completion.",
    )


# 4 — Selection Sort: Round 1 search trace + all subsequent rounds
def build_selection_sort():
    nodes = [
        N("sel-h-scan", "Round 1 Anatomy: Scanning Unsorted Suffix for Min", 28, 64, 530, 36, "blue", size=13, bold=True),
        N("sel-h-rounds", "All Rounds: Growing the Sorted Prefix to Completion", 590, 64, 540, 36, "blue", size=13, bold=True),
    ]

    r1_steps = [
        ("r1-0", "Target slot i=0 (val 5)", [5, 2, 4, 6, 1, 3], ["yellow", "white", "white", "white", "white", "white"]),
        ("r1-1", "A[1]=2 < 5 -> minVal=2 (idx 1)", [5, 2, 4, 6, 1, 3], ["yellow", "teal", "white", "white", "white", "white"]),
        ("r1-2", "A[2]=4, A[3]=6 (not smaller)", [5, 2, 4, 6, 1, 3], ["yellow", "teal", "white", "white", "white", "white"]),
        ("r1-3", "A[4]=1 < 2 -> minVal=1 (idx 4)", [5, 2, 4, 6, 1, 3], ["yellow", "white", "white", "white", "teal", "white"]),
        ("r1-4", "A[5]=3 (not smaller); scan done", [5, 2, 4, 6, 1, 3], ["yellow", "white", "white", "white", "teal", "white"]),
        ("r1-5", "Swap target A[0] (5) & min A[4] (1)", [1, 2, 4, 6, 5, 3], ["green", "white", "white", "white", "teal", "white"]),
    ]

    for idx, (sid, lbl, vals, cols) in enumerate(r1_steps):
        y = 112 + idx * 46
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 220, 36, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 256 + cidx * 48, y, 42, 36, col, size=15, bold=(col in ("teal", "green", "yellow"))))

    nodes.append(N(
        "sel-r1-note",
        "Round 1 complete: global minimum (1) placed at index 0.\nYellow = target slot; Teal = current min; Green = settled.",
        28, 396, 530, 48, "light", size=11,
    ))

    sub_rounds = [
        ("sr-start", "Start: unsorted array", [5, 2, 4, 6, 1, 3], ["white"] * 6),
        ("sr-1", "Round 1: place min 1 at idx 0", [1, 2, 4, 6, 5, 3], ["green"] + ["white"] * 5),
        ("sr-2", "Round 2: min 2 already at idx 1", [1, 2, 4, 6, 5, 3], ["green", "green"] + ["white"] * 4),
        ("sr-3", "Round 3: swap 4 & min 3 at idx 5", [1, 2, 3, 6, 5, 4], ["green"] * 3 + ["white"] * 3),
        ("sr-4", "Round 4: swap 6 & min 4 at idx 5", [1, 2, 3, 4, 5, 6], ["green"] * 4 + ["white"] * 2),
        ("sr-5", "Round 5: 5 settles; 6 auto-settles", [1, 2, 3, 4, 5, 6], ["green"] * 6),
    ]

    for idx, (sid, lbl, vals, cols) in enumerate(sub_rounds):
        y = 112 + idx * 46
        nodes.append(N(f"{sid}-lbl", lbl, 590, y, 230, 36, "gray", size=11))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 830 + cidx * 48, y, 42, 36, col, size=15, bold=(col == "green")))

    nodes.append(N(
        "sel-sub-note",
        "Sorted prefix grows rightward: always O(n^2) comparisons,\nbut at most n-1 swaps total. Not stable.",
        590, 396, 540, 48, "light", size=11,
    ))

    return D(
        key="ch5-04-selection-sort-flow",
        title="Selection Sort: Scan for Minimum, Swap, and Settle",
        size=(1160, 500),
        nodes=nodes,
        caption="Left: scanning unsorted suffix to locate min. Right: rounds placing each min into position.",
    )


# 5 — Insertion Sort: Iteration 4 cascading shift trace + all iterations
def build_insertion_sort():
    nodes = [
        N("ins-h-shift", "Iteration 4 Anatomy: Cascading Shift for Key = 1", 28, 64, 530, 36, "blue", size=13, bold=True),
        N("ins-h-runs", "All Iterations: Growing Sorted Prefix to Completion", 590, 64, 540, 36, "blue", size=13, bold=True),
    ]

    i4_steps = [
        ("i4-0", "Sorted prefix [2,4,5,6], key = 1", ["2", "4", "5", "6", "1", "3"], ["green", "green", "green", "green", "yellow", "white"]),
        ("i4-1", "Pull key 1 (open gap at idx 4)", ["2", "4", "5", "6", "·", "3"], ["green", "green", "green", "green", "yellow", "white"]),
        ("i4-2", "6 > 1 -> shift 6 right to idx 4", ["2", "4", "5", "·", "6", "3"], ["green", "green", "green", "yellow", "teal", "white"]),
        ("i4-3", "5 > 1 -> shift 5 right to idx 3", ["2", "4", "·", "5", "6", "3"], ["green", "green", "yellow", "teal", "teal", "white"]),
        ("i4-4", "4, 2 > 1 -> shift 4, 2 right", ["·", "2", "4", "5", "6", "3"], ["yellow", "teal", "teal", "teal", "teal", "white"]),
        ("i4-5", "Insert key 1 into gap at index 0", ["1", "2", "4", "5", "6", "3"], ["green", "green", "green", "green", "green", "white"]),
    ]

    for idx, (sid, lbl, vals, cols) in enumerate(i4_steps):
        y = 112 + idx * 46
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 220, 36, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 256 + cidx * 48, y, 42, 36, col, size=15, bold=(col in ("teal", "green", "yellow"))))

    nodes.append(N(
        "ins-i4-note",
        "Key 1 is smaller than all sorted items, so 6, 5, 4, 2 all shift right.\nYellow = open gap; Teal = shifting items; Green = sorted prefix.",
        28, 396, 530, 48, "light", size=11,
    ))

    sub_runs = [
        ("ir-0", "Start: [5] is 1-item sorted prefix", ["5", "2", "4", "6", "1", "3"], ["green"] + ["white"] * 5),
        ("ir-1", "Insert 2: 5 shifts right", ["2", "5", "4", "6", "1", "3"], ["green", "green"] + ["white"] * 4),
        ("ir-2", "Insert 4: 5 shifts right", ["2", "4", "5", "6", "1", "3"], ["green"] * 3 + ["white"] * 3),
        ("ir-3", "Insert 6: 5 <= 6 (0 shifts)", ["2", "4", "5", "6", "1", "3"], ["green"] * 4 + ["white"] * 2),
        ("ir-4", "Insert 1: 6, 5, 4, 2 shift right", ["1", "2", "4", "5", "6", "3"], ["green"] * 5 + ["white"]),
        ("ir-5", "Insert 3: 6, 5, 4 shift -> DONE", ["1", "2", "3", "4", "5", "6"], ["green"] * 6),
    ]

    for idx, (sid, lbl, vals, cols) in enumerate(sub_runs):
        y = 112 + idx * 46
        nodes.append(N(f"{sid}-lbl", lbl, 590, y, 230, 36, "gray", size=11))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 830 + cidx * 48, y, 42, 36, col, size=15, bold=(col == "green")))

    nodes.append(N(
        "ins-sub-note",
        "Items shift right one position to make room for each new key.\nO(n) best for nearly sorted data; O(n^2) worst; STABLE sort.",
        590, 396, 540, 48, "light", size=11,
    ))

    return D(
        key="ch5-05-insertion-sort-flow",
        title="Insertion Sort: Pull Key, Shift Larger Elements, and Insert",
        size=(1160, 500),
        nodes=nodes,
        caption="Left: shift cascade creating gap for key. Right: iterations growing the sorted prefix.",
    )


# 6 — Counting Sort: Frequencies, Prefix Sums, and Right-to-Left Placement
def build_counting_sort():
    nodes = [
        N("cs-h-in", "1. Input Array A (n=6, k=4)", 28, 64, 340, 32, "blue", size=12, bold=True),
        N("cs-in-lbl", "Values in 0..4", 28, 102, 110, 36, "gray", size=11),
    ]
    in_vals = ["4", "1", "3", "4", "2", "1"]
    for i, v in enumerate(in_vals):
        nodes.append(N(f"cs-in-{i}", v, 146 + i * 36, 102, 32, 36, "white", size=14))

    nodes.append(N("cs-h-cnt", "2. Frequency Counts", 390, 64, 340, 32, "blue", size=12, bold=True))
    nodes.append(N("cs-cnt-lbl", "Count each val", 390, 102, 110, 36, "gray", size=11))
    cnt_vals = ["0:0", "1:2", "2:1", "3:1", "4:2"]
    for i, v in enumerate(cnt_vals):
        nodes.append(N(f"cs-cnt-{i}", v, 508 + i * 44, 102, 40, 36, "yellow", size=12))

    nodes.append(N("cs-h-tot", "3. Running Totals (Prefix Sums)", 750, 64, 380, 32, "blue", size=12, bold=True))
    nodes.append(N("cs-tot-lbl", "count[v] += prev", 750, 102, 140, 36, "gray", size=11))
    tot_vals = ["0:0", "1:2", "2:3", "3:4", "4:6"]
    for i, v in enumerate(tot_vals):
        nodes.append(N(f"cs-tot-{i}", v, 898 + i * 44, 102, 40, 36, "teal", size=12, bold=True))

    nodes.append(N(
        "cs-tot-note",
        "Each running total gives the 1-based end position. Target 0-based index in output is count[v] - 1.",
        28, 146, 1102, 30, "light", size=11,
    ))

    nodes.append(N(
        "cs-h-place",
        "4. Step-by-Step Stable Placement into Output Array (Scanning Input Right-to-Left)",
        28, 184, 1102, 32, "blue", size=12, bold=True,
    ))

    steps = [
        ("cs-p1", "i=5: A[5]=1 -> slot count[1]-1 = 1; count[1] becomes 1", ["·", "1", "·", "·", "·", "·"], ["gray", "green", "gray", "gray", "gray", "gray"], "count[1]=2 -> slot 1"),
        ("cs-p2", "i=4: A[4]=2 -> slot count[2]-1 = 2; count[2] becomes 2", ["·", "1", "2", "·", "·", "·"], ["gray", "green", "green", "gray", "gray", "gray"], "count[2]=3 -> slot 2"),
        ("cs-p3", "i=3: A[3]=4 -> slot count[4]-1 = 5; count[4] becomes 5", ["·", "1", "2", "·", "·", "4"], ["gray", "green", "green", "gray", "gray", "green"], "count[4]=6 -> slot 5"),
        ("cs-p4", "i=2: A[2]=3 -> slot count[3]-1 = 3; count[3] becomes 3", ["·", "1", "2", "3", "·", "4"], ["gray", "green", "green", "green", "gray", "green"], "count[3]=4 -> slot 3"),
        ("cs-p5", "i=1: A[1]=1 -> slot count[1]-1 = 0; count[1] becomes 0", ["1", "1", "2", "3", "·", "4"], ["green", "green", "green", "green", "gray", "green"], "count[1]=1 -> slot 0"),
        ("cs-p6", "i=0: A[0]=4 -> slot count[4]-1 = 4; count[4] becomes 4", ["1", "1", "2", "3", "4", "4"], ["green"] * 6, "count[4]=5 -> slot 4"),
    ]

    for idx, (sid, lbl, out_vals, cols, badge) in enumerate(steps):
        y = 224 + idx * 44
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 470, 36, "gray", size=10))
        nodes.append(N(f"{sid}-badge", badge, 508, y, 200, 36, "yellow", size=11))
        for cidx, (val, col) in enumerate(zip(out_vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", val, 720 + cidx * 46, y, 40, 36, col, size=15, bold=(col == "green")))

    nodes.append(N(
        "cs-fin-note",
        "Scanning right-to-left preserves the relative order of duplicate items (stable!). Time: O(n + k), Space: O(n + k).",
        28, 496, 1102, 34, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-06-sorting-counts-flow",
        title="Counting Sort: Count, Cumulative Totals, and Right-to-Left Placement",
        size=(1160, 580),
        nodes=nodes,
        caption="Top: count frequencies and prefix sums. Bottom: backward input scan placing items stably into output.",
    )


# 7 — Merge Sort: Divide & Conquer Tree + Two-Pointer Merge Walkthrough
def build_merge_sort():
    nodes = [
        # Left side: Divide & Conquer Tree
        N("ms-h-tree", "Divide & Conquer Recursion Tree", 28, 64, 520, 34, "blue", size=13, bold=True),
        N("ms-r", "[5, 2, 4, 6, 1, 3]", 185, 106, 206, 32, "yellow", size=12, bold=True),
        N("ms-l1-l", "[5, 2, 4]", 85, 154, 130, 30, "teal", size=12),
        N("ms-l1-r", "[6, 1, 3]", 360, 154, 130, 30, "teal", size=12),
        N("ms-l2-1", "[5, 2]", 45, 200, 85, 28, "teal", size=11),
        N("ms-l2-2", "[4]", 145, 200, 65, 28, "teal", size=11),
        N("ms-l2-3", "[6, 1]", 320, 200, 85, 28, "teal", size=11),
        N("ms-l2-4", "[3]", 420, 200, 65, 28, "teal", size=11),
        N("ms-b1", "[5]", 35, 244, 45, 26, "light", size=11),
        N("ms-b2", "[2]", 88, 244, 45, 26, "light", size=11),
        N("ms-b3", "[4]", 145, 244, 65, 26, "light", size=11),
        N("ms-b4", "[6]", 310, 244, 45, 26, "light", size=11),
        N("ms-b5", "[1]", 363, 244, 45, 26, "light", size=11),
        N("ms-b6", "[3]", 420, 244, 65, 26, "light", size=11),
        N("ms-m2-1", "[2, 5]", 45, 286, 85, 28, "yellow", size=11),
        N("ms-m2-2", "[4]", 145, 286, 65, 28, "yellow", size=11),
        N("ms-m2-3", "[1, 6]", 320, 286, 85, 28, "yellow", size=11),
        N("ms-m2-4", "[3]", 420, 286, 65, 28, "yellow", size=11),
        N("ms-m1-l", "[2, 4, 5]", 85, 330, 130, 30, "yellow", size=12),
        N("ms-m1-r", "[1, 3, 6]", 360, 330, 130, 30, "yellow", size=12),
        N("ms-m0", "[1, 2, 3, 4, 5, 6]", 185, 376, 206, 32, "green", size=12, bold=True),
        N(
            "ms-tree-note",
            "Divide: split lists to single items (base cases).\nConquer: merge pairs of sorted sublists upward.",
            28, 424, 520, 44, "light", size=11,
        ),
        # Right side: Two-Pointer Merge Walkthrough
        N("ms-h-merge", "Two-Pointer Merge Walkthrough: MERGE(L, R)", 570, 64, 560, 34, "blue", size=13, bold=True),
        N("ms-m-sub", "Left L = [2, 4, 5] (idx i)   |   Right R = [1, 3, 6] (idx j)", 570, 106, 560, 32, "gray", size=12),
    ]

    edges = [
        E("ms-r", "ms-l1-l", route="straight"),
        E("ms-r", "ms-l1-r", route="straight"),
        E("ms-l1-l", "ms-l2-1", route="straight"),
        E("ms-l1-l", "ms-l2-2", route="straight"),
        E("ms-l1-r", "ms-l2-3", route="straight"),
        E("ms-l1-r", "ms-l2-4", route="straight"),
        E("ms-l2-1", "ms-b1", route="straight"),
        E("ms-l2-1", "ms-b2", route="straight"),
        E("ms-l2-3", "ms-b4", route="straight"),
        E("ms-l2-3", "ms-b5", route="straight"),
        E("ms-b1", "ms-m2-1", dashed=True, route="straight"),
        E("ms-b2", "ms-m2-1", dashed=True, route="straight"),
        E("ms-b4", "ms-m2-3", dashed=True, route="straight"),
        E("ms-b5", "ms-m2-3", dashed=True, route="straight"),
        E("ms-m2-1", "ms-m1-l", dashed=True, route="straight"),
        E("ms-m2-2", "ms-m1-l", dashed=True, route="straight"),
        E("ms-m2-3", "ms-m1-r", dashed=True, route="straight"),
        E("ms-m2-4", "ms-m1-r", dashed=True, route="straight"),
        E("ms-m1-l", "ms-m0", dashed=True, route="straight"),
        E("ms-m1-r", "ms-m0", dashed=True, route="straight"),
    ]

    m_steps = [
        ("m1", "Compare L[0]=2 vs R[0]=1: 1 < 2 -> take R[0]", "[1]"),
        ("m2", "Compare L[0]=2 vs R[1]=3: 2 < 3 -> take L[0]", "[1, 2]"),
        ("m3", "Compare L[1]=4 vs R[1]=3: 3 < 4 -> take R[1]", "[1, 2, 3]"),
        ("m4", "Compare L[1]=4 vs R[2]=6: 4 < 6 -> take L[1]", "[1, 2, 3, 4]"),
        ("m5", "Compare L[2]=5 vs R[2]=6: 5 < 6 -> take L[2]", "[1, 2, 3, 4, 5]"),
        ("m6", "L empty; copy remaining from R -> append 6", "[1, 2, 3, 4, 5, 6]"),
    ]

    for idx, (sid, desc, acc) in enumerate(m_steps):
        y = 146 + idx * 38
        nodes.append(N(f"{sid}-lbl", desc, 570, y, 360, 32, "gray", size=10))
        nodes.append(N(f"{sid}-acc", acc, 940, y, 190, 32, "yellow" if idx < 5 else "green", size=12, bold=(idx == 5)))

    nodes.append(N(
        "ms-m-note",
        "Two-pointer merge runs in linear O(n) time and is stable.\nOverall Merge Sort time: O(n log n) guaranteed; Space: O(n).",
        570, 384, 560, 44, "light", size=11,
    ))

    nodes.append(N(
        "ms-fin-bar",
        "Merge Sort complete: stable O(n log n) divide-and-conquer sorting achieved!",
        28, 480, 1102, 34, "green", size=12, bold=True,
    ))

    return D(
        key="ch5-07-merge-sort-divide-conquer",
        title="Merge Sort: Divide Tree, Recursive Split, and Two-Pointer Merge",
        size=(1160, 560),
        nodes=nodes,
        edges=edges,
        caption="Left: recursive divide and upward conquer tree. Right: step-by-step two-pointer merge.",
    )


# 8 — Quick Sort: Lomuto partition trace + recursive flow
def build_quick_sort():
    nodes = [
        N("qs-h-part", "Lomuto Partition Trace on Array (Pivot = 3)", 28, 64, 530, 36, "blue", size=13, bold=True),
        N("qs-h-sub", "Subproblem Recursion to Full Sorted Completion", 590, 64, 540, 36, "blue", size=13, bold=True),
    ]

    p_steps = [
        ("qs-p0", "Start: pivot 3 at A[5], bnd=0", ["5", "2", "4", "6", "1", "3"], ["white", "white", "white", "white", "white", "yellow"]),
        ("qs-p1", "j=0: A[0]=5 > 3 -> no swap", ["5", "2", "4", "6", "1", "3"], ["white", "white", "white", "white", "white", "yellow"]),
        ("qs-p2", "j=1: A[1]<=3 -> swap A[0],A[1]", ["2", "5", "4", "6", "1", "3"], ["teal", "teal", "white", "white", "white", "yellow"]),
        ("qs-p3", "j=2,3: 4,6 > 3 -> no swap", ["2", "5", "4", "6", "1", "3"], ["teal", "white", "white", "white", "white", "yellow"]),
        ("qs-p4", "j=4: A[4]<=3 -> swap A[1],A[4]", ["2", "1", "4", "6", "5", "3"], ["teal", "teal", "white", "white", "white", "yellow"]),
        ("qs-p5", "Scan done: swap A[2] & pivot 3", ["2", "1", "3", "6", "5", "4"], ["teal", "teal", "green", "white", "white", "white"]),
    ]

    for idx, (sid, lbl, vals, cols) in enumerate(p_steps):
        y = 112 + idx * 46
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 220, 36, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 256 + cidx * 48, y, 42, 36, col, size=15, bold=(col in ("teal", "green", "yellow"))))

    nodes.append(N(
        "qs-p-note",
        "Pivot 3 is locked at index 2! Left [2, 1] <= 3, Right [6, 5, 4] > 3.\nYellow = pivot; Teal = <= pivot region; Green = settled pivot.",
        28, 396, 530, 48, "light", size=11,
    ))

    sub_steps = [
        ("qs-s1", "Part 1: pivot 3 locks at idx 2", ["2", "1", "3", "6", "5", "4"], ["white", "white", "green", "white", "white", "white"]),
        ("qs-s2", "Left [2, 1]: pivot 1 locks", ["1", "2", "3", "6", "5", "4"], ["green", "green", "green", "white", "white", "white"]),
        ("qs-s3", "Right [6, 5, 4]: pivot 4 locks", ["1", "2", "3", "4", "5", "6"], ["green", "green", "green", "green", "white", "white"]),
        ("qs-s4", "Subproblem [5, 6]: in order", ["1", "2", "3", "4", "5", "6"], ["green"] * 6),
        ("qs-fin", "Sorted: all pivots locked!", ["1", "2", "3", "4", "5", "6"], ["green"] * 6),
    ]

    for idx, (sid, lbl, vals, cols) in enumerate(sub_steps):
        y = 112 + idx * 56
        nodes.append(N(f"{sid}-lbl", lbl, 590, y, 230, 40, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 830 + cidx * 48, y, 42, 40, col, size=15, bold=(col == "green")))

    nodes.append(N(
        "qs-sub-note",
        "Each partition places its pivot in its permanent sorted index.\nO(n log n) average time; O(n^2) worst case if pivot is unbalanced.",
        590, 396, 540, 48, "light", size=11,
    ))

    return D(
        key="ch5-08-quick-sort-partition",
        title="Quick Sort: Step-by-Step Lomuto Partition and Subproblem Flow",
        size=(1160, 500),
        nodes=nodes,
        caption="Left: Lomuto partitioning placing pivot 3. Right: recursive partition calls completing the sort.",
    )


# 9 — Heap Sort Phase 1: Complete Binary Tree and Bottom-Up Heapify
def build_heap_build():
    nodes = [
        N("rule-box", "Complete Binary Tree Rules:\n• Left child = 2i + 1, Right = 2i + 2\n• Leaves: floor(n/2)..n-1 (already valid heaps)\n• Heapify internal nodes: floor(n/2) - 1 down to 0", 28, 64, 400, 96, "light", size=11),
        N("raw-arr-label", "Initial unsorted array A (n = 6):", 28, 172, 400, 26, "gray", size=11),
    ]
    raw_vals = [("5", "yellow"), ("2", "yellow"), ("4", "yellow"), ("6", "light"), ("1", "light"), ("3", "light")]
    for i, (v, c) in enumerate(raw_vals):
        nodes.append(N(f"raw-{i}", f"{v}\n[i={i}]", 28 + i * 66, 204, 58, 44, c, size=11))

    nodes.extend([
        N("tn-0", "5 (i=0)", 200, 268, 64, 40, "yellow", size=11, bold=True),
        N("tn-1", "2 (i=1)", 110, 332, 64, 40, "yellow", size=11, bold=True),
        N("tn-2", "4 (i=2)", 290, 332, 64, 40, "yellow", size=11, bold=True),
        N("tn-3", "6 (i=3)", 60, 396, 64, 40, "light", size=11),
        N("tn-4", "1 (i=4)", 160, 396, 64, 40, "light", size=11),
        N("tn-5", "3 (i=5)", 250, 396, 64, 40, "light", size=11),
        N("tree-note", "Leaves (gray) are valid heaps.\nHeapify internal nodes (yellow): i = 2, 1, 0.", 28, 450, 400, 40, "gray", size=11),
    ])

    edges = [
        E("tn-0", "tn-1", route="straight"),
        E("tn-0", "tn-2", route="straight"),
        E("tn-1", "tn-3", route="straight"),
        E("tn-1", "tn-4", route="straight"),
        E("tn-2", "tn-5", route="straight"),
    ]

    nodes.append(N("hb-h-steps", "Bottom-Up Heapify Execution (Linear O(n) Build)", 450, 64, 680, 36, "blue", size=13, bold=True))

    steps = [
        ("hb-s1", "1. Heapify i=2 (val 4):\nchild 3 <= 4 -> no swap needed", ["5", "2", "4", "6", "1", "3"], ["white", "white", "yellow", "white", "white", "yellow"], "Subtree at i=2\nsatisfies max-heap"),
        ("hb-s2", "2. Heapify i=1 (val 2):\nchild 6 > 2 -> SWAP A[1] & A[3]", ["5", "6", "4", "2", "1", "3"], ["white", "teal", "white", "teal", "white", "white"], "Subtree at i=1 valid\n(6 > 2, 6 > 1)"),
        ("hb-s3", "3. Heapify i=0 (val 5):\nchild 6 > 5 -> SWAP A[0] & A[1]", ["6", "5", "4", "2", "1", "3"], ["green", "teal", "white", "white", "white", "white"], "5 sifts to i=1; settles\n(5 > 2, 5 > 1)"),
        ("hb-s4", "Final: Valid Max-Heap ready!\nGlobal max (6) is at root A[0]", ["6", "5", "4", "2", "1", "3"], ["green", "yellow", "yellow", "white", "white", "white"], "Max-Heap ready:\nparent >= children"),
    ]

    for idx, (sid, lbl, vals, cols, note) in enumerate(steps):
        y = 112 + idx * 58
        nodes.append(N(f"{sid}-lbl", lbl, 450, y, 220, 48, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", val, 680 + cidx * 40, y, 36, 48, col, size=14, bold=(col in ("teal", "green", "yellow"))))
        nodes.append(N(f"{sid}-note", note, 930, y, 200, 48, "light", size=10))

    nodes.append(N(
        "hb-sum",
        "Why Bottom-Up is O(n): Most nodes reside near bottom leaves (heights 0 and 1).\nFewer comparisons are needed near leaves; total sum converges to O(n), not O(n log n).",
        450, 362, 680, 52, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-09-heap-build-flow",
        title="Heap Sort Phase 1: Complete Binary Tree and Heapify",
        size=(1160, 550),
        nodes=nodes,
        edges=edges,
        caption="Bottom-up heapify builds a valid max-heap in linear O(n) time before sorting begins.",
    )


# 10 — Heap Sort Phase 2: Root Extraction, Swap, and Sift-Down Walkthrough
def build_heap_sort():
    nodes = [
        N("hs-h", "Phase 2: Repeated Root Extraction and Heap Restoration", 28, 60, 1102, 34, "blue", size=13, bold=True),
    ]

    phase2_rows = [
        ("hs-r0", "Initial Max-Heap (size 6)", ["6", "5", "4", "2", "1", "3"], ["green", "yellow", "yellow", "white", "white", "white"], "Global maximum 6 is at root A[0]. Ready for extraction."),
        ("hs-r1a", "Extract 6: swap A[0], A[5]", ["3", "5", "4", "2", "1", "6"], ["yellow", "white", "white", "white", "white", "green"], "Root 6 locks in sorted tail. 3 moves to root (violates max-heap)."),
        ("hs-r1b", "Heapify root: sift down 3", ["5", "3", "4", "2", "1", "6"], ["yellow", "teal", "white", "white", "white", "green"], "3 swaps with max child 5. Active heap size 5 restored!"),
        ("hs-r2a", "Extract 5: swap A[0], A[4]", ["1", "3", "4", "2", "5", "6"], ["yellow", "white", "white", "white", "green", "green"], "Root 5 locks in sorted tail. 1 moves to root (violates max-heap)."),
        ("hs-r2b", "Heapify root: sift down 1", ["4", "3", "1", "2", "5", "6"], ["yellow", "white", "teal", "white", "green", "green"], "1 swaps with max child 4. Active heap size 4 restored!"),
        ("hs-r3a", "Extract 4: swap A[0], A[3]", ["2", "3", "1", "4", "5", "6"], ["yellow", "white", "white", "green", "green", "green"], "Root 4 locks in sorted tail. 2 moves to root (violates max-heap)."),
        ("hs-r3b", "Heapify root: sift down 2", ["3", "2", "1", "4", "5", "6"], ["yellow", "teal", "white", "green", "green", "green"], "2 swaps with child 3. Active heap size 3 restored!"),
        ("hs-r4a", "Extract 3: swap A[0], A[2]", ["1", "2", "3", "4", "5", "6"], ["yellow", "white", "green", "green", "green", "green"], "Root 3 locks in sorted tail. 1 moves to root."),
        ("hs-r4b", "Heapify root: sift down 1", ["2", "1", "3", "4", "5", "6"], ["yellow", "teal", "green", "green", "green", "green"], "1 swaps with child 2. Active heap size 2 restored!"),
        ("hs-r5", "Extract 2: swap A[0], A[1]", ["1", "2", "3", "4", "5", "6"], ["green"] * 6, "2 locks in tail; 1 remains at A[0]. Array is FULLY SORTED!"),
    ]

    for idx, (sid, lbl, vals, cols, note) in enumerate(phase2_rows):
        y = 104 + idx * 42
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 220, 36, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", val, 256 + cidx * 46, y, 40, 36, col, size=15, bold=(col == "green")))
        nodes.append(N(f"{sid}-note", note, 540, y, 590, 36, "light" if "SORTED" not in note else "green", size=10, bold=("SORTED" in note)))

    nodes.append(N(
        "hs-fin-note",
        "Each extraction locks the maximum of the active heap at the end, then restores the heap in O(log n) time.\nTotal sorting phase time: (n - 1) * O(log n) = O(n log n). In-place and non-stable.",
        28, 532, 1102, 40, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-10-heap-sort-flow",
        title="Heap Sort Phase 2: Root Extraction, Swap, and Sift-Down Walkthrough",
        size=(1160, 620),
        nodes=nodes,
        caption="Each extraction swaps the root maximum to the end and sifts down the new root in O(log n) time.",
    )


# All diagrams for Chapter 5
DIAGRAMS = [
    choose_sort,
    taxonomy,
    build_bubble_sort(),
    build_selection_sort(),
    build_insertion_sort(),
    build_counting_sort(),
    build_merge_sort(),
    build_quick_sort(),
    build_heap_build(),
    build_heap_sort(),
]
