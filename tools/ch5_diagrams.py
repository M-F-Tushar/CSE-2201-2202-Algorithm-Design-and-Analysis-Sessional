"""Chapter 5 (Sorting Algorithms) diagram specs.

Comprehensive, step-by-step explanatory diagrams visualizing each sorting algorithm
from initial unsorted state through every intermediate comparison, swap, shift,
and pass to the final sorted array.
"""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 5 - Sorting Algorithms/diagrams"


# -----------------------------------------------------------------------------
# 1 — Practical decision guide (Escalator Diagram)
# -----------------------------------------------------------------------------
choose_sort = D(
    key="ch5-01-sorting-reach-escalator",
    title="Choose a Sort by What the Situation Needs",
    size=(1270, 560),
    nodes=[
        N("esc-h", "Sorting Decision Escalator: Which Algorithm Fits Your Constraints?", 30, 16, 960, 36, "blue", size=13, bold=True),
        N("s1", "STEP 1: Small / Pre-sorted?\nInsertion Sort\n- Input: n <= 30 or near-sorted\n- Best: O(n) | Space: O(1)\n- Stable | Near-zero overhead", 30, 310, 226, 140, "yellow", size=11, bold=True),
        N("s2", "STEP 2: Small Integer Keys?\nCounting Sort\n- Input: Integer range [0..k]\n- Time: O(n + k) linear!\n- Stable | Non-comparison", 276, 250, 226, 140, "green", size=11, bold=True),
        N("s3", "STEP 3: Guaranteed & Stable?\nMerge Sort\n- Input: Arbitrary data, stable\n- Time: Theta(n log n) always\n- Stable | Uses O(n) RAM", 522, 190, 226, 140, "teal", size=11, bold=True),
        N("s4", "STEP 4: Max Speed In-Place?\nQuick Sort\n- Input: Large data, in-place\n- Time: O(n log n) average\n- Non-stable | Pivot matters", 768, 130, 226, 140, "blue", size=11, bold=True),
        N("s5", "STEP 5: Worst-Case Shield?\nHeap Sort\n- Input: Memory-critical tasks\n- Time: Theta(n log n) always\n- Strictly O(1) RAM | Non-stable", 1014, 70, 226, 140, "violet", size=11, bold=True),
        N("esc-sum", "Escalator Rule: Scale up from Step 1. Match your input size, memory limit, and stability requirement to the right step.", 30, 480, 1210, 46, "light", size=11, bold=True),
    ],
    edges=[
        E("s1", "s2"),
        E("s2", "s3"),
        E("s3", "s4"),
        E("s4", "s5"),
    ],
    flow="H",
    caption="Escalate from simplest requirements at Step 1 up to guaranteed worst-case bounds at Step 5.",
)

# -----------------------------------------------------------------------------
# 2 — Sorts grouped by how they decide order
# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
# 3A — Bubble Sort: Pass 1 Microscopic Step-by-Step Trace
# -----------------------------------------------------------------------------
def build_bubble_pass1():
    nodes = [
        N("bp1-h", "Bubble Sort: Pass 1 Adjacent Comparisons and Swaps", 28, 60, 944, 34, "blue", size=13, bold=True),
    ]

    p1_steps = [
        ("bp1-0", "Start: initial unsorted array", [5, 2, 4, 6, 1, 3], ["white"] * 6, "Begin scan at index j = 0"),
        ("bp1-1", "Compare A[0], A[1] (5 > 2) -> SWAP", [2, 5, 4, 6, 1, 3], ["teal", "teal", "white", "white", "white", "white"], "5 > 2: swap values at 0 and 1"),
        ("bp1-2", "Compare A[1], A[2] (5 > 4) -> SWAP", [2, 4, 5, 6, 1, 3], ["white", "teal", "teal", "white", "white", "white"], "5 > 4: swap values at 1 and 2"),
        ("bp1-3", "Compare A[2], A[3] (5 <= 6) -> KEEP", [2, 4, 5, 6, 1, 3], ["white", "white", "yellow", "yellow", "white", "white"], "5 <= 6: in order; no swap needed"),
        ("bp1-4", "Compare A[3], A[4] (6 > 1) -> SWAP", [2, 4, 5, 1, 6, 3], ["white", "white", "white", "teal", "teal", "white"], "6 > 1: swap values at 3 and 4"),
        ("bp1-5", "Compare A[4], A[5] (6 > 3) -> SWAP", [2, 4, 5, 1, 3, 6], ["white", "white", "white", "white", "teal", "green"], "6 > 3: swap; 6 settles at end!"),
    ]

    for idx, (sid, lbl, vals, cols, note) in enumerate(p1_steps):
        y = 104 + idx * 46
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 290, 36, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 332 + cidx * 48, y, 42, 36, col, size=15, bold=(col in ("teal", "green"))))
        nodes.append(N(f"{sid}-note", note, 636, y, 336, 36, "light" if "settles" not in note else "green", size=10, bold=("settles" in note)))

    nodes.append(N(
        "bp1-fin",
        "Pass 1 Outcome: Maximum element 6 bubbles all the way to index 5.\nTeal = swapped pair; Yellow = compared pair in order; Green = settled.",
        28, 390, 944, 44, "light", size=11,
    ))

    return D(
        key="ch5-03b-bubble-sort-pass1",
        title="Bubble Sort: Pass 1 Adjacent Comparisons & Swaps",
        size=(1000, 470),
        nodes=nodes,
        caption="Every adjacent pair is compared from left to right; larger values bubble to the right.",
    )


# -----------------------------------------------------------------------------
# 3B — Bubble Sort: All Passes Progression to Completion
# -----------------------------------------------------------------------------
def build_bubble_flow():
    nodes = [
        N("bf-h", "Bubble Sort: Progression Across All Passes to Completion", 28, 60, 944, 34, "blue", size=13, bold=True),
    ]

    passes = [
        ("bf-0", "Start: unsorted array", [5, 2, 4, 6, 1, 3], ["white"] * 6, "All 6 items unsorted"),
        ("bf-1", "Pass 1: bubble 6 to index 5", [2, 4, 5, 1, 3, 6], ["white", "white", "white", "white", "white", "green"], "6 is settled at index 5"),
        ("bf-2", "Pass 2: bubble 5 to index 4", [2, 4, 1, 3, 5, 6], ["white", "white", "white", "white", "green", "green"], "5 is settled at index 4"),
        ("bf-3", "Pass 3: bubble 4 to index 3", [2, 1, 3, 4, 5, 6], ["white", "white", "white", "green", "green", "green"], "4 is settled at index 3"),
        ("bf-4", "Pass 4: bubble 3 to index 2", [1, 2, 3, 4, 5, 6], ["white", "white", "green", "green", "green", "green"], "3 is settled; 1 & 2 are in place"),
        ("bf-5", "Pass 5: check (1, 2) -> 0 swaps", [1, 2, 3, 4, 5, 6], ["yellow", "yellow", "green", "green", "green", "green"], "0 swaps detected -> Early Exit!"),
        ("bf-fin", "Sorted Output Array", [1, 2, 3, 4, 5, 6], ["green"] * 6, "List is fully sorted in ascending order!"),
    ]

    for idx, (sid, lbl, vals, cols, note) in enumerate(passes):
        y = 104 + idx * 44
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 290, 34, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 332 + cidx * 48, y, 42, 34, col, size=15, bold=(col == "green")))
        nodes.append(N(f"{sid}-note", note, 636, y, 336, 34, "green" if "sorted" in note.lower() else "light", size=10, bold=("sorted" in note.lower())))

    nodes.append(N(
        "bf-sum",
        "Sorted suffix (green) grows leftward each pass. Early exit stops when a pass makes 0 swaps.\nTime: O(n) best case, O(n^2) worst case. Auxiliary space: O(1) in-place. Stable sort.",
        28, 420, 944, 44, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-03-bubble-sort-flow",
        title="Bubble Sort: Progression Across All Passes to Completion",
        size=(1000, 500),
        nodes=nodes,
        caption="Each pass settles one more large value at the right end. Zero swaps triggers early termination.",
    )


# -----------------------------------------------------------------------------
# 4A — Selection Sort: Round 1 Minimum Search Scan Trace
# -----------------------------------------------------------------------------
def build_selection_scan():
    nodes = [
        N("ss-h", "Selection Sort: Round 1 Scan for Minimum in Unsorted Suffix", 28, 60, 944, 34, "blue", size=13, bold=True),
    ]

    r1_steps = [
        ("ss-0", "Target slot i=0 (val 5)", [5, 2, 4, 6, 1, 3], ["yellow", "white", "white", "white", "white", "white"], "Assume minVal = 5 at minIdx = 0"),
        ("ss-1", "Scan j=1: A[1]=2 < 5 -> minVal=2", [5, 2, 4, 6, 1, 3], ["yellow", "teal", "white", "white", "white", "white"], "2 < 5: update minIdx to 1"),
        ("ss-2", "Scan j=2,3: 4, 6 >= 2 (not smaller)", [5, 2, 4, 6, 1, 3], ["yellow", "teal", "white", "white", "white", "white"], "4, 6 >= 2: minIdx remains 1"),
        ("ss-3", "Scan j=4: A[4]=1 < 2 -> minVal=1", [5, 2, 4, 6, 1, 3], ["yellow", "white", "white", "white", "teal", "white"], "1 < 2: update minIdx to 4"),
        ("ss-4", "Scan j=5: A[5]=3 >= 1 (not smaller)", [5, 2, 4, 6, 1, 3], ["yellow", "white", "white", "white", "teal", "white"], "Scan complete: global min is 1 at idx 4"),
        ("ss-5", "SWAP target A[0] (5) & min A[4] (1)", [1, 2, 4, 6, 5, 3], ["green", "white", "white", "white", "teal", "white"], "1 settles at index 0; 5 moves to idx 4"),
    ]

    for idx, (sid, lbl, vals, cols, note) in enumerate(r1_steps):
        y = 104 + idx * 46
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 290, 36, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 332 + cidx * 48, y, 42, 36, col, size=15, bold=(col in ("teal", "green", "yellow"))))
        nodes.append(N(f"{sid}-note", note, 636, y, 336, 36, "green" if "settles" in note else "light", size=10, bold=("settles" in note)))

    nodes.append(N(
        "ss-fin",
        "Round 1 Outcome: Global minimum (1) placed into target slot index 0.\nYellow = target slot; Teal = current minimum; Green = settled element.",
        28, 390, 944, 44, "light", size=11,
    ))

    return D(
        key="ch5-04b-selection-sort-scan",
        title="Selection Sort: Round 1 Minimum Scan Trace",
        size=(1000, 470),
        nodes=nodes,
        caption="Selection sort scans the entire unsorted suffix to find the minimum value before swapping.",
    )


# -----------------------------------------------------------------------------
# 4B — Selection Sort: All Rounds Progression to Completion
# -----------------------------------------------------------------------------
def build_selection_flow():
    nodes = [
        N("sf-h", "Selection Sort: Growing the Sorted Prefix Round-by-Round", 28, 60, 944, 34, "blue", size=13, bold=True),
    ]

    rounds = [
        ("sf-0", "Start: unsorted array", [5, 2, 4, 6, 1, 3], ["white"] * 6, "Initial array; sorted prefix empty"),
        ("sf-1", "Round 1: place min 1 at idx 0", [1, 2, 4, 6, 5, 3], ["green"] + ["white"] * 5, "Scan finds min 1; swap A[0] & A[4]"),
        ("sf-2", "Round 2: min 2 already at idx 1", [1, 2, 4, 6, 5, 3], ["green", "green"] + ["white"] * 4, "Min 2 is already at target; 0 swaps"),
        ("sf-3", "Round 3: place min 3 at idx 2", [1, 2, 3, 6, 5, 4], ["green"] * 3 + ["white"] * 3, "Scan finds min 3; swap A[2] & A[5]"),
        ("sf-4", "Round 4: place min 4 at idx 3", [1, 2, 3, 4, 5, 6], ["green"] * 4 + ["white"] * 2, "Scan finds min 4; swap A[3] & A[5]"),
        ("sf-5", "Round 5: 5 settles; 6 auto-settles", [1, 2, 3, 4, 5, 6], ["green"] * 6, "5 <= 6; last item 6 also in place"),
        ("sf-fin", "Sorted Output Array", [1, 2, 3, 4, 5, 6], ["green"] * 6, "List is fully sorted in ascending order!"),
    ]

    for idx, (sid, lbl, vals, cols, note) in enumerate(rounds):
        y = 104 + idx * 44
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 290, 34, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 332 + cidx * 48, y, 42, 34, col, size=15, bold=(col == "green")))
        nodes.append(N(f"{sid}-note", note, 636, y, 336, 34, "green" if "sorted" in note.lower() else "light", size=10, bold=("sorted" in note.lower())))

    nodes.append(N(
        "sf-sum",
        "The sorted prefix (green) grows rightward one item per round.\nAlways Theta(n^2) comparisons, but at most n - 1 swaps total. Not stable.",
        28, 420, 944, 44, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-04-selection-sort-flow",
        title="Selection Sort: Growing the Sorted Prefix Round-by-Round",
        size=(1000, 500),
        nodes=nodes,
        caption="Selection sort grows the sorted part from left to right, placing one minimum value each round.",
    )


# -----------------------------------------------------------------------------
# 5A — Insertion Sort: Iteration 4 Cascading Shift Trace
# -----------------------------------------------------------------------------
def build_insertion_shift():
    nodes = [
        N("is-h", "Insertion Sort: Iteration 4 Key Extraction and Element Shifting", 28, 60, 944, 34, "blue", size=13, bold=True),
    ]

    i4_steps = [
        ("is-0", "Prefix [2,4,5,6] sorted; key = 1", ["2", "4", "5", "6", "1", "3"], ["green", "green", "green", "green", "yellow", "white"], "Extract key = 1 at index 4"),
        ("is-1", "Pull key 1 (open gap at idx 4)", ["2", "4", "5", "6", "·", "3"], ["green", "green", "green", "green", "yellow", "white"], "Gap opens at position 4; hold key 1 aside"),
        ("is-2", "6 > 1 -> shift 6 right to idx 4", ["2", "4", "5", "·", "6", "3"], ["green", "green", "green", "yellow", "teal", "white"], "6 moves right into gap; gap shifts to idx 3"),
        ("is-3", "5 > 1 -> shift 5 right to idx 3", ["2", "4", "·", "5", "6", "3"], ["green", "green", "yellow", "teal", "teal", "white"], "5 moves right into gap; gap shifts to idx 2"),
        ("is-4", "4, 2 > 1 -> shift 4, 2 right", ["·", "2", "4", "5", "6", "3"], ["yellow", "teal", "teal", "teal", "teal", "white"], "4 and 2 move right; gap reaches index 0"),
        ("is-5", "Drop key 1 into gap at index 0", ["1", "2", "4", "5", "6", "3"], ["green", "green", "green", "green", "green", "white"], "Key 1 placed! Sorted prefix is now size 5"),
    ]

    for idx, (sid, lbl, vals, cols, note) in enumerate(i4_steps):
        y = 104 + idx * 46
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 290, 36, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", val, 332 + cidx * 48, y, 42, 36, col, size=15, bold=(col in ("teal", "green", "yellow"))))
        nodes.append(N(f"{sid}-note", note, 636, y, 336, 36, "green" if "placed" in note else "light", size=10, bold=("placed" in note)))

    nodes.append(N(
        "is-fin",
        "Key 1 is smaller than all sorted items, causing a 4-position cascading shift.\nYellow = open gap; Teal = shifting elements; Green = sorted prefix.",
        28, 390, 944, 44, "light", size=11,
    ))

    return D(
        key="ch5-05b-insertion-sort-shift",
        title="Insertion Sort: Iteration 4 Key Extraction & Element Shifting",
        size=(1000, 470),
        nodes=nodes,
        caption="Larger sorted items slide right one position to open a gap for the new key.",
    )


# -----------------------------------------------------------------------------
# 5B — Insertion Sort: All Iterations Progression to Completion
# -----------------------------------------------------------------------------
def build_insertion_flow():
    nodes = [
        N("if-h", "Insertion Sort: Growing Sorted Prefix Iteration-by-Iteration", 28, 60, 944, 34, "blue", size=13, bold=True),
    ]

    runs = [
        ("if-0", "Start: [5] is 1-item sorted prefix", ["5", "2", "4", "6", "1", "3"], ["green"] + ["white"] * 5, "Single element prefix is already sorted"),
        ("if-1", "Insert 2: 5 shifts right", ["2", "5", "4", "6", "1", "3"], ["green", "green"] + ["white"] * 4, "5 > 2 shifts right; insert 2 at idx 0"),
        ("if-2", "Insert 4: 5 shifts right", ["2", "4", "5", "6", "1", "3"], ["green"] * 3 + ["white"] * 3, "5 > 4 shifts right; 2 <= 4 stops shift"),
        ("if-3", "Insert 6: 5 <= 6 (0 shifts)", ["2", "4", "5", "6", "1", "3"], ["green"] * 4 + ["white"] * 2, "6 >= 5; already in order, no shifts needed"),
        ("if-4", "Insert 1: 6, 5, 4, 2 shift right", ["1", "2", "4", "5", "6", "3"], ["green"] * 5 + ["white"], "All 4 items shift right; insert 1 at idx 0"),
        ("if-5", "Insert 3: 6, 5, 4 shift right", ["1", "2", "3", "4", "5", "6"], ["green"] * 6, "6, 5, 4 shift; 2 <= 3 stops; insert 3 at idx 2"),
        ("if-fin", "Sorted Output Array", ["1", "2", "3", "4", "5", "6"], ["green"] * 6, "List is fully sorted in ascending order!"),
    ]

    for idx, (sid, lbl, vals, cols, note) in enumerate(runs):
        y = 104 + idx * 44
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 290, 34, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", val, 332 + cidx * 48, y, 42, 34, col, size=15, bold=(col == "green")))
        nodes.append(N(f"{sid}-note", note, 636, y, 336, 34, "green" if "sorted" in note.lower() else "light", size=10, bold=("sorted" in note.lower())))

    nodes.append(N(
        "if-sum",
        "Insertion sort takes each item and inserts it into its place in the sorted prefix.\nTime: O(n) best for nearly sorted, O(n^2) worst case. Stable and in-place.",
        28, 420, 944, 44, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-05-insertion-sort-flow",
        title="Insertion Sort: Growing Sorted Prefix Iteration-by-Iteration",
        size=(1000, 500),
        nodes=nodes,
        caption="Each new item is inserted into the sorted part; larger items slide right to make a gap.",
    )


# -----------------------------------------------------------------------------
# 6A — Counting Sort: Value Frequencies and Running Totals
# -----------------------------------------------------------------------------
def build_counting_totals():
    nodes = [
        N("ct-h", "Counting Sort: Input Frequencies and Running Totals (Prefix Sums)", 28, 60, 944, 34, "blue", size=13, bold=True),
        N("ct-in-lbl", "1. Input Array A (n=6, k=4)", 28, 108, 260, 44, "gray", size=11),
    ]
    in_vals = ["4", "1", "3", "4", "2", "1"]
    for i, v in enumerate(in_vals):
        nodes.append(N(f"ct-in-{i}", v, 320 + i * 52, 108, 44, 44, "white", size=15))
    nodes.append(N("ct-in-note", "Unsorted list; integer keys in range 0..4", 650, 108, 322, 44, "light", size=11))

    nodes.append(N("ct-cnt-lbl", "2. Frequency Counts\ncount[v]", 28, 168, 260, 44, "gray", size=11))
    cnt_vals = ["0:0", "1:2", "2:1", "3:1", "4:2"]
    for i, v in enumerate(cnt_vals):
        nodes.append(N(f"ct-cnt-{i}", v, 320 + i * 62, 168, 54, 44, "yellow", size=12))
    nodes.append(N("ct-cnt-note", "How often each value appears in input", 650, 168, 322, 44, "light", size=11))

    nodes.append(N("ct-tot-lbl", "3. Running Totals\ncount[v] += count[v-1]", 28, 228, 260, 44, "gray", size=11))
    tot_vals = ["0:0", "1:2", "2:3", "3:4", "4:6"]
    for i, v in enumerate(tot_vals):
        nodes.append(N(f"ct-tot-{i}", v, 320 + i * 62, 228, 54, 44, "teal", size=12, bold=True))
    nodes.append(N("ct-tot-note", "Running total = number of items <= value", 650, 228, 322, 44, "light", size=11))

    nodes.append(N(
        "ct-rule",
        "Key Positioning Rule: The running total count[v] gives the 1-based end position.\nIn a 0-based array, value v is placed at index count[v] - 1, then count[v] is decremented.",
        28, 296, 944, 48, "light", size=11,
    ))

    nodes.append(N(
        "ct-sum",
        "Counting sort avoids pairwise comparisons by indexing counts directly into memory.\nWorks best when the key range k is small: Theta(n + k) time and Theta(n + k) space.",
        28, 360, 944, 48, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-06-sorting-counts-flow",
        title="Counting Sort: Value Frequencies and Running Totals",
        size=(1000, 450),
        nodes=nodes,
        caption="The running total tells where each value belongs in the output list.",
    )


# -----------------------------------------------------------------------------
# 6B — Counting Sort: Step-by-Step Stable Backward Placement
# -----------------------------------------------------------------------------
def build_counting_placement():
    nodes = [
        N("cp-h", "Counting Sort: Right-to-Left Stable Placement into Output Array", 28, 60, 944, 34, "blue", size=13, bold=True),
    ]

    p_steps = [
        ("cp-1", "i=5: A[5]=1 -> count[1]=2 -> slot 1", "count[1] decrements to 1", ["·", "1", "·", "·", "·", "·"], ["gray", "green", "gray", "gray", "gray", "gray"]),
        ("cp-2", "i=4: A[4]=2 -> count[2]=3 -> slot 2", "count[2] decrements to 2", ["·", "1", "2", "·", "·", "·"], ["gray", "green", "green", "gray", "gray", "gray"]),
        ("cp-3", "i=3: A[3]=4 -> count[4]=6 -> slot 5", "count[4] decrements to 5", ["·", "1", "2", "·", "·", "4"], ["gray", "green", "green", "gray", "gray", "green"]),
        ("cp-4", "i=2: A[2]=3 -> count[3]=4 -> slot 3", "count[3] decrements to 3", ["·", "1", "2", "3", "·", "4"], ["gray", "green", "green", "green", "gray", "green"]),
        ("cp-5", "i=1: A[1]=1 -> count[1]=1 -> slot 0", "count[1] decrements to 0", ["1", "1", "2", "3", "·", "4"], ["green", "green", "green", "green", "gray", "green"]),
        ("cp-6", "i=0: A[0]=4 -> count[4]=5 -> slot 4", "count[4] decrements to 4", ["1", "1", "2", "3", "4", "4"], ["green"] * 6),
    ]

    slots = ["Slot 1", "Slot 2", "Slot 5", "Slot 3", "Slot 0", "Slot 4"]
    for idx, (sid, desc, note, out_vals, cols) in enumerate(p_steps):
        y = 104 + idx * 46
        nodes.append(N(f"{sid}-lbl", desc, 28, y, 320, 36, "gray", size=10))
        nodes.append(N(f"{sid}-note", note, 360, y, 220, 36, "yellow", size=10))
        for cidx, (val, col) in enumerate(zip(out_vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", val, 592 + cidx * 48, y, 42, 36, col, size=15, bold=(col == "green")))
        nodes.append(N(f"{sid}-badge", slots[idx], 892, y, 80, 36, "light", size=10))

    nodes.append(N(
        "cp-sum",
        "Reading the input from right to left places duplicate keys in their original relative order.\nThis backward pass guarantees that Counting Sort is STABLE.",
        28, 396, 944, 46, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-06b-counting-sort-placement",
        title="Counting Sort: Right-to-Left Stable Placement into Output Array",
        size=(1000, 480),
        nodes=nodes,
        caption="Scanning input from right to left preserves the original relative order of equal items (stability).",
    )


# -----------------------------------------------------------------------------
# 7A — Merge Sort: Divide and Conquer Recursion Tree
# -----------------------------------------------------------------------------
def build_merge_tree():
    nodes = [
        N("mt-h", "Merge Sort: Divide and Conquer Recursion Tree", 28, 60, 944, 34, "blue", size=13, bold=True),
        N("mt-r", "[5, 2, 4, 6, 1, 3]", 380, 104, 220, 34, "yellow", size=13, bold=True),
        N("mt-l1-l", "[5, 2, 4]", 200, 156, 140, 32, "teal", size=12),
        N("mt-l1-r", "[6, 1, 3]", 640, 156, 140, 32, "teal", size=12),
        N("mt-l2-1", "[5, 2]", 130, 206, 95, 28, "teal", size=11),
        N("mt-l2-2", "[4]", 255, 206, 75, 28, "teal", size=11),
        N("mt-l2-3", "[6, 1]", 570, 206, 95, 28, "teal", size=11),
        N("mt-l2-4", "[3]", 695, 206, 75, 28, "teal", size=11),
        N("mt-b1", "[5]", 110, 252, 50, 26, "light", size=11),
        N("mt-b2", "[2]", 170, 252, 50, 26, "light", size=11),
        N("mt-b3", "[4]", 255, 252, 75, 26, "light", size=11),
        N("mt-b4", "[6]", 550, 252, 50, 26, "light", size=11),
        N("mt-b5", "[1]", 610, 252, 50, 26, "light", size=11),
        N("mt-b6", "[3]", 695, 252, 75, 26, "light", size=11),
        N("mt-m2-1", "[2, 5]", 130, 296, 95, 28, "yellow", size=11),
        N("mt-m2-2", "[4]", 255, 296, 75, 28, "yellow", size=11),
        N("mt-m2-3", "[1, 6]", 570, 296, 95, 28, "yellow", size=11),
        N("mt-m2-4", "[3]", 695, 296, 75, 28, "yellow", size=11),
        N("mt-m1-l", "[2, 4, 5]", 200, 342, 140, 32, "yellow", size=12),
        N("mt-m1-r", "[1, 3, 6]", 640, 342, 140, 32, "yellow", size=12),
        N("mt-m0", "[1, 2, 3, 4, 5, 6]", 380, 392, 220, 34, "green", size=13, bold=True),
        N(
            "mt-sum",
            "Divide splits lists recursively until single-item base cases. Conquer merges sorted pieces back upward.\nGuaranteed Theta(n log n) time in all cases; requires Theta(n) temporary memory.",
            28, 442, 944, 44, "green", size=11, bold=True,
        ),
    ]

    edges = [
        E("mt-r", "mt-l1-l", route="straight"),
        E("mt-r", "mt-l1-r", route="straight"),
        E("mt-l1-l", "mt-l2-1", route="straight"),
        E("mt-l1-l", "mt-l2-2", route="straight"),
        E("mt-l1-r", "mt-l2-3", route="straight"),
        E("mt-l1-r", "mt-l2-4", route="straight"),
        E("mt-l2-1", "mt-b1", route="straight"),
        E("mt-l2-1", "mt-b2", route="straight"),
        E("mt-l2-3", "mt-b4", route="straight"),
        E("mt-l2-3", "mt-b5", route="straight"),
        E("mt-b1", "mt-m2-1", dashed=True, route="straight"),
        E("mt-b2", "mt-m2-1", dashed=True, route="straight"),
        E("mt-b4", "mt-m2-3", dashed=True, route="straight"),
        E("mt-b5", "mt-m2-3", dashed=True, route="straight"),
        E("mt-m2-1", "mt-m1-l", dashed=True, route="straight"),
        E("mt-m2-2", "mt-m1-l", dashed=True, route="straight"),
        E("mt-m2-3", "mt-m1-r", dashed=True, route="straight"),
        E("mt-m2-4", "mt-m1-r", dashed=True, route="straight"),
        E("mt-m1-l", "mt-m0", dashed=True, route="straight"),
        E("mt-m1-r", "mt-m0", dashed=True, route="straight"),
    ]

    return D(
        key="ch5-07-merge-sort-divide-conquer",
        title="Merge Sort: Divide and Conquer Recursion Tree",
        size=(1000, 520),
        nodes=nodes,
        edges=edges,
        caption="Solid lines show recursive splitting; dashed lines show upward merging of sorted sublists.",
    )


# -----------------------------------------------------------------------------
# 7B — Merge Sort: Two-Pointer Merge Step-by-Step Walkthrough
# -----------------------------------------------------------------------------
def build_merge_step():
    nodes = [
        N("ms-h", "Merge Sort: Two-Pointer Merge Walkthrough: MERGE(L, R)", 28, 60, 944, 34, "blue", size=13, bold=True),
        N("ms-inputs", "Left L = [2, 4, 5] (pointer i)   |   Right R = [1, 3, 6] (pointer j)", 28, 104, 944, 32, "gray", size=12),
    ]

    m_steps = [
        ("ms-1", "Compare L[0]=2 vs R[0]=1: 1 < 2", "Take 1 from Right; advance j to 1", "[1]"),
        ("ms-2", "Compare L[0]=2 vs R[1]=3: 2 < 3", "Take 2 from Left; advance i to 1", "[1, 2]"),
        ("ms-3", "Compare L[1]=4 vs R[1]=3: 3 < 4", "Take 3 from Right; advance j to 2", "[1, 2, 3]"),
        ("ms-4", "Compare L[1]=4 vs R[2]=6: 4 < 6", "Take 4 from Left; advance i to 2", "[1, 2, 3, 4]"),
        ("ms-5", "Compare L[2]=5 vs R[2]=6: 5 < 6", "Take 5 from Left; Left is exhausted!", "[1, 2, 3, 4, 5]"),
        ("ms-6", "Left empty -> copy remaining from R", "Append 6 to output -> MERGE COMPLETE", "[1, 2, 3, 4, 5, 6]"),
    ]

    for idx, (sid, cmp_txt, act_txt, acc) in enumerate(m_steps):
        y = 146 + idx * 44
        nodes.append(N(f"{sid}-cmp", cmp_txt, 28, y, 320, 36, "gray", size=10))
        nodes.append(N(f"{sid}-act", act_txt, 360, y, 320, 36, "yellow" if idx < 5 else "green", size=10, bold=(idx == 5)))
        nodes.append(N(f"{sid}-acc", acc, 692, y, 280, 36, "green" if idx == 5 else "teal", size=13, bold=True))

    nodes.append(N(
        "ms-sum",
        "Two-pointer merge runs in linear Theta(n) time. By taking equal elements from Left first, Merge Sort is STABLE.\nOverall sorting time: Theta(n log n). Auxiliary space: Theta(n).",
        28, 420, 944, 44, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-07b-merge-sort-merge-step",
        title="Merge Sort: Two-Pointer Merge Walkthrough",
        size=(1000, 500),
        nodes=nodes,
        caption="Two-pointer merge compares heads of both sorted pieces and appends the smaller value in linear time.",
    )


# -----------------------------------------------------------------------------
# 8A — Quick Sort: 3-Step Strategy Escalator (Michael Sambol Method)
# -----------------------------------------------------------------------------
def build_quick_strategy():
    nodes = [
        N("qs-h", "Quick Sort Strategy Escalator: The 3 Core Steps (Michael Sambol Method)", 28, 20, 1024, 38, "blue", size=13, bold=True),
        N("step1", "Step 1: Pick a Pivot\nSelect a benchmark item.\nUsually last item A[high].\nEverything compares to it!", 28, 80, 310, 110, "yellow", size=12, bold=True),
        N("step2", "Step 2: Partition Array\nTwo markers (i bound, j scan).\nSwap items <= pivot to left!\nFinally, swap pivot into i.\nPivot locks in final spot!", 384, 80, 310, 110, "teal", size=12, bold=True),
        N("step3", "Step 3: Recursively Repeat\nDivide and conquer!\nSort left subarray (<= pivot)\nand right subarray (> pivot).\nStop when subarray size <= 1.", 742, 80, 310, 110, "blue", size=12, bold=True),
        N("qs-base", "Base Case: Any subarray with 0 or 1 item is already sorted -> Return immediately!", 28, 218, 1024, 40, "green", size=11, bold=True),
        N("qs-takeaway", "Key Insight: No extra merging array needed. The pivot locks permanently into place in-place.", 28, 276, 1024, 40, "light", size=11),
    ]
    edges = [
        E("step1", "step2"),
        E("step2", "step3"),
    ]
    return D(
        key="ch5-08a-quick-sort-strategy",
        title="Quick Sort: 3-Step Strategy Escalator",
        size=(1080, 340),
        nodes=nodes,
        edges=edges,
        flow="H",
        caption="Quick Sort divide-and-conquer strategy: Pick Pivot, Partition array in-place, and Recurse on both sides.",
    )


# -----------------------------------------------------------------------------
# 8B — Quick Sort: Lomuto Partitioning Step-by-Step Trace
# -----------------------------------------------------------------------------
def build_quick_partition():
    nodes = [
        N("qp-h", "Quick Sort: Step-by-Step Lomuto Partitioning Trace (Pivot = 3 at A[5])", 28, 20, 1044, 34, "blue", size=13, bold=True),
    ]

    p_steps = [
        ("qp-0", "State 0: Start: pivot=3 at A[5], i=0, j=0", ["5", "2", "4", "6", "1", "3"], ["white", "white", "white", "white", "white", "yellow"], "i marks boundary where items <= 3 go; j begins scan"),
        ("qp-1", "State 1 (j=0): A[0]=5 > 3 -> No swap", ["5", "2", "4", "6", "1", "3"], ["orange", "white", "white", "white", "white", "yellow"], "5 > 3: too big! Boundary i remains at 0; advance j"),
        ("qp-2", "State 2 (j=1): A[1]=2 <= 3 -> SWAP A[0], A[1]", ["2", "5", "4", "6", "1", "3"], ["teal", "orange", "white", "white", "white", "yellow"], "2 <= 3: swap A[i=0] & A[j=1]; boundary i advances to 1"),
        ("qp-3", "State 3 (j=2): A[2]=4 > 3 -> No swap", ["2", "5", "4", "6", "1", "3"], ["teal", "orange", "orange", "white", "white", "yellow"], "4 > 3: too big! Boundary i remains at 1; advance j"),
        ("qp-4", "State 4 (j=3): A[3]=6 > 3 -> No swap", ["2", "5", "4", "6", "1", "3"], ["teal", "orange", "orange", "orange", "white", "yellow"], "6 > 3: too big! Boundary i remains at 1; advance j"),
        ("qp-5", "State 5 (j=4): A[4]=1 <= 3 -> SWAP A[1], A[4]", ["2", "1", "4", "6", "5", "3"], ["teal", "teal", "orange", "orange", "orange", "yellow"], "1 <= 3: swap A[i=1] & A[j=4]; boundary i advances to 2"),
        ("qp-6", "State 6: Scan finished! Swap A[i=2] & Pivot A[5]", ["2", "1", "3", "6", "5", "4"], ["teal", "teal", "green", "orange", "orange", "orange"], "Swap boundary A[2] (value 4) with pivot A[5] (value 3)"),
        ("qp-7", "State 7: Partition complete! Pivot locked", ["2", "1", "3", "6", "5", "4"], ["teal", "teal", "green", "white", "white", "white"], "Pivot 3 locked at idx 2! Left [2, 1] <= 3, Right [6, 5, 4] > 3"),
    ]

    for idx, (sid, lbl, vals, cols, note) in enumerate(p_steps):
        y = 66 + idx * 46
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 320, 36, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 360 + cidx * 48, y, 42, 36, col, size=14, bold=(col in ("teal", "green", "yellow"))))
        nodes.append(N(f"{sid}-note", note, 660, y, 412, 36, "green" if "locked" in note else "light", size=10, bold=("locked" in note)))

    nodes.append(N(
        "qp-sum",
        "Lomuto partition takes linear Theta(n) time and 0 extra memory. Pivot 3 is now permanently sorted at index 2.\nNext: recursively partition the left sub-array [2, 1] and the right sub-array [6, 5, 4].",
        28, 442, 1044, 44, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-08-quick-sort-partition",
        title="Quick Sort: Step-by-Step Lomuto Partitioning",
        size=(1100, 510),
        nodes=nodes,
        caption="Lomuto partitioning scans array, gathers items <= pivot to the left, and locks the pivot in place.",
    )


# -----------------------------------------------------------------------------
# 8C — Quick Sort: Visual State Machine Across Every Swap
# -----------------------------------------------------------------------------
def build_quick_states():
    nodes = [
        N("qss-h", "Quick Sort Partitioning: Visual State Machine Across Every Swap", 28, 20, 1064, 34, "blue", size=13, bold=True),
    ]

    states = [
        ("st0", "State 0: Start\ni=0, j=0, Pivot=3 at A[5]", ["5", "2", "4", "6", "1", "3"], ["white", "white", "white", "white", "white", "yellow"], "Pointers: i points to A[0]; j points to A[0]. No items categorized yet."),
        ("st1", "State 1: Swap 1 (j=1)\n2 <= 3 -> Swap A[0] (5) & A[1] (2)", ["2", "5", "4", "6", "1", "3"], ["teal", "orange", "white", "white", "white", "yellow"], "2 moves into left partition! i increments from 0 to 1; j increments to 2."),
        ("st2", "State 2: Scan (j=2, 3)\n4 > 3 and 6 > 3 (no swaps)", ["2", "5", "4", "6", "1", "3"], ["teal", "orange", "orange", "orange", "white", "yellow"], "Both 4 and 6 stay in right section. Boundary i remains unchanged at 1."),
        ("st3", "State 3: Swap 2 (j=4)\n1 <= 3 -> Swap A[1] (5) & A[4] (1)", ["2", "1", "4", "6", "5", "3"], ["teal", "teal", "orange", "orange", "orange", "yellow"], "1 moves into left partition! i increments from 1 to 2; scan finishes."),
        ("st4", "State 4: Final Pivot Swap\nSwap A[i=2] (4) & Pivot A[5] (3)", ["2", "1", "3", "6", "5", "4"], ["teal", "teal", "green", "orange", "orange", "orange"], "Pivot 3 swaps into index 2. All <= 3 on left; all > 3 on right!"),
        ("st5", "State 5: Subproblems Emerge\nLeft Part | Pivot | Right Part", ["2", "1", "3", "6", "5", "4"], ["teal", "teal", "green", "violet", "violet", "violet"], "Pivot 3 is LOCKED in final spot.\nRecurse on [2, 1] and [6, 5, 4] independently!"),
    ]

    for idx, (sid, lbl, vals, cols, note) in enumerate(states):
        y = 66 + idx * 56
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 290, 48, "gray", size=10, bold=True))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 330 + cidx * 50, y + 4, 44, 40, col, size=15, bold=True))
        nodes.append(N(f"{sid}-note", note, 646, y, 446, 48, "green" if idx >= 4 else "light", size=10, bold=(idx >= 4)))

    nodes.append(N(
        "qss-sum",
        "Summary: The boundary pointer i acts as a wall. Every item <= pivot is swapped behind the wall (left side).\nAt the end, swapping the pivot with the wall places the pivot exactly where it belongs for eternity.",
        28, 412, 1064, 44, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-08c-quick-sort-states",
        title="Quick Sort: Visual State Machine",
        size=(1120, 480),
        nodes=nodes,
        caption="Visual state snapshots during partitioning showing pointer updates, cell relocations, and pivot locking.",
    )


# -----------------------------------------------------------------------------
# 8D — Quick Sort: Recursive Subproblem Flow to Full Sorted Array
# -----------------------------------------------------------------------------
def build_quick_recursion():
    nodes = [
        N("qr-h", "Quick Sort: Subproblem Recursion Flow to Full Sorted Array", 28, 20, 1044, 34, "blue", size=13, bold=True),
    ]

    sub_steps = [
        ("qr-0", "Start: unsorted array [5, 2, 4, 6, 1, 3]", ["5", "2", "4", "6", "1", "3"], ["white"] * 6, "Initial array; pivot chosen at A[5] = 3"),
        ("qr-1", "Partition 1: pivot 3 locks at idx 2", ["2", "1", "3", "6", "5", "4"], ["white", "white", "green", "white", "white", "white"], "Subproblems formed: [2, 1] on left and [6, 5, 4] on right"),
        ("qr-2", "Left subproblem [2, 1]: pivot 1 locks", ["1", "2", "3", "6", "5", "4"], ["green", "green", "green", "white", "white", "white"], "1 locks at idx 0; 2 auto-settles at idx 1 (base case)"),
        ("qr-3", "Right subproblem [6, 5, 4]: pivot 4 locks", ["1", "2", "3", "4", "6", "5"], ["green", "green", "green", "green", "white", "white"], "4 locks at idx 3; leaves subproblem [6, 5] on indices 4..5"),
        ("qr-4", "Subproblem [6, 5]: pivot 5 locks", ["1", "2", "3", "4", "5", "6"], ["green"] * 6, "5 locks at idx 4; 6 auto-settles at idx 5 (base case)"),
        ("qr-fin", "Fully Sorted Array: [1, 2, 3, 4, 5, 6]", ["1", "2", "3", "4", "5", "6"], ["green"] * 6, "All pivots locked in final positions; entire array is sorted!"),
    ]

    for idx, (sid, lbl, vals, cols, note) in enumerate(sub_steps):
        y = 66 + idx * 46
        nodes.append(N(f"{sid}-lbl", lbl, 28, y, 320, 36, "gray", size=10))
        for cidx, (val, col) in enumerate(zip(vals, cols)):
            nodes.append(N(f"{sid}-c{cidx}", str(val), 360 + cidx * 48, y, 42, 36, col, size=14, bold=(col == "green")))
        nodes.append(N(f"{sid}-note", note, 660, y, 412, 36, "green" if "sorted" in note.lower() else "light", size=10, bold=("sorted" in note.lower())))

    nodes.append(N(
        "qr-sum",
        "Quick sort recurses on the subproblems to the left and right of each locked pivot.\nTheta(n log n) average time; Theta(n^2) worst case if pivot is unbalanced. In-place, non-stable.",
        28, 350, 1044, 44, "green", size=11, bold=True,
    ))

    return D(
        key="ch5-08b-quick-sort-recursion",
        title="Quick Sort: Subproblem Recursion Flow",
        size=(1100, 420),
        nodes=nodes,
        caption="Recursion divides subproblems around each locked pivot until all elements are in place.",
    )


# -----------------------------------------------------------------------------
# 9 — Heap Sort Phase 1: Complete Binary Tree and Bottom-Up Heapify
# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
# 10 — Heap Sort Phase 2: Root Extraction, Swap, and Sift-Down Walkthrough
# -----------------------------------------------------------------------------
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
    build_bubble_pass1(),
    build_bubble_flow(),
    build_selection_scan(),
    build_selection_flow(),
    build_insertion_shift(),
    build_insertion_flow(),
    build_counting_totals(),
    build_counting_placement(),
    build_merge_tree(),
    build_merge_step(),
    build_quick_strategy(),
    build_quick_partition(),
    build_quick_states(),
    build_quick_recursion(),
    build_heap_build(),
    build_heap_sort(),
]
