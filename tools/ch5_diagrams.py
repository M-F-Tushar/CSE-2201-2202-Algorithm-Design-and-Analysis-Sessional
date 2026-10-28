"""Chapter 5 (Sorting Algorithms) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 5 - Sorting Algorithms/diagrams"


def array_walkthrough(key, title, rows, caption, size=(940, 520)):
    """Create a plain-language, row-by-row array walkthrough."""
    nodes = []
    row_y = 86
    row_height = 44
    row_gap = 12
    label_x = 30
    label_width = 220
    cell_x = 270
    cell_width = 64
    cell_gap = 8

    for row_index, step in enumerate(rows):
        y = row_y + row_index * (row_height + row_gap)
        nodes.append(
            N(
                f"step-{row_index}",
                step["label"],
                label_x,
                y,
                label_width,
                row_height,
                "gray",
                size=12,
            )
        )
        colors = step.get("colors", [])
        for item_index, value in enumerate(step["values"]):
            color = colors[item_index] if item_index < len(colors) else "white"
            nodes.append(
                N(
                    f"step-{row_index}-item-{item_index}",
                    str(value),
                    cell_x + item_index * (cell_width + cell_gap),
                    y,
                    cell_width,
                    row_height,
                    color,
                    size=16,
                    bold=color == "green",
                )
            )

    return D(
        key=key,
        title=title,
        size=size,
        nodes=nodes,
        caption=caption,
    )


def group_walkthrough(key, title, stages, caption):
    """Show merge sort's groups changing as lists split and join."""
    nodes = []
    row_y = 78
    row_height = 42
    row_gap = 8
    label_x = 24
    label_width = 226
    group_x = 275
    group_gap = 8
    group_area_width = 700

    for row_index, stage in enumerate(stages):
        y = row_y + row_index * (row_height + row_gap)
        nodes.append(
            N(
                f"stage-{row_index}",
                stage["label"],
                label_x,
                y,
                label_width,
                row_height,
                "gray",
                size=12,
            )
        )
        groups = stage["groups"]
        group_width = min(180, (group_area_width - (len(groups) - 1) * group_gap) / len(groups))
        total_width = len(groups) * group_width + (len(groups) - 1) * group_gap
        x = group_x + (group_area_width - total_width) / 2
        for group_index, group in enumerate(groups):
            nodes.append(
                N(
                    f"stage-{row_index}-group-{group_index}",
                    group,
                    x + group_index * (group_width + group_gap),
                    y,
                    group_width,
                    row_height,
                    "teal" if group_index % 2 == 0 else "yellow",
                    size=13,
                )
            )

    return D(
        key=key,
        title=title,
        size=(1000, 510),
        nodes=nodes,
        caption=caption,
    )


def counting_diagram():
    """Show counting sort's input, counts, running totals, and result."""
    nodes = []
    label_x = 30
    label_width = 220
    cell_width = 76
    cell_gap = 8
    row_height = 50
    rows = [
        ("input", "Starting list", ["4", "1", "3", "4", "2", "1"]),
        ("counts", "How often each value\nappears", ["0 : 0", "1 : 2", "2 : 1", "3 : 1", "4 : 2"]),
        ("totals", "Running totals", ["0 : 0", "1 : 2", "2 : 3", "3 : 4", "4 : 6"]),
        ("result", "Sorted list", ["1", "1", "2", "3", "4", "4"]),
    ]
    first_y = 102
    row_gap = 72

    for row_index, (row_id, label, values) in enumerate(rows):
        y = first_y + row_index * row_gap
        nodes.append(
            N(row_id, label, label_x, y, label_width, row_height, "gray", size=12)
        )
        cells_width = len(values) * cell_width + (len(values) - 1) * cell_gap
        x0 = 280 + (650 - cells_width) / 2
        for value_index, value in enumerate(values):
            color = "green" if row_id == "result" else "yellow" if row_id == "totals" else "white"
            nodes.append(
                N(
                    f"{row_id}-{value_index}",
                    value,
                    x0 + value_index * (cell_width + cell_gap),
                    y,
                    cell_width,
                    row_height,
                    color,
                    size=14,
                    bold=row_id == "result",
                )
            )

    return D(
        key="ch5-06-sorting-counts-flow",
        title="Counting Sort: Count Values, Then Place Them",
        size=(980, 500),
        nodes=nodes,
        caption="The running total tells where each value belongs in the output.",
    )


# 1 — a practical guide, not a ranking of the algorithms
choose_sort = D(
    key="ch5-01-sorting-reach-escalator",
    title="Choose a Sort by What the Situation Needs",
    size=(1020, 470),
    nodes=[
        N("small", "Insertion sort\nSmall or nearly sorted lists", 35, 100, 290, 100, "yellow", size=14, bold=True),
        N("stable", "Merge sort\nStable results\nExtra memory is okay", 365, 100, 290, 100, "teal", size=14, bold=True),
        N("general", "Quick sort\nOften fast; pivot choice matters", 695, 100, 290, 100, "blue", size=14, bold=True),
        N("memory", "Heap sort\nReliable time; little extra memory", 200, 255, 290, 100, "violet", size=14, bold=True),
        N("range", "Counting sort\nSmall, known integer range", 530, 255, 290, 100, "green", size=14, bold=True),
    ],
    caption="Choose for the input and the trade-off you care about; no single method fits every case.",
)

# 2 — sorts grouped by how they decide order
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

# 3 — bubble sort
bubble_walk = array_walkthrough(
    "ch5-03-bubble-sort-flow",
    "Bubble Sort: Large Values Move to the End",
    [
        {"label": "Starting list", "values": [5, 2, 4, 6, 1, 3]},
        {"label": "Pass 1: settle 6", "values": [2, 4, 5, 1, 3, 6], "colors": ["white", "white", "white", "white", "white", "green"]},
        {"label": "Pass 2: settle 5", "values": [2, 4, 1, 3, 5, 6], "colors": ["white", "white", "white", "white", "green", "green"]},
        {"label": "Pass 3: settle 4", "values": [2, 1, 3, 4, 5, 6], "colors": ["white", "white", "white", "green", "green", "green"]},
        {"label": "Pass 4: list is sorted", "values": [1, 2, 3, 4, 5, 6], "colors": ["green"] * 6},
        {"label": "Pass 5: no switches; stop", "values": [1, 2, 3, 4, 5, 6], "colors": ["green"] * 6},
    ],
    "Each pass settles one more large value at the right-hand end.",
)

# 4 — selection sort
selection_walk = array_walkthrough(
    "ch5-04-selection-sort-flow",
    "Selection Sort: Find the Smallest Unplaced Value",
    [
        {"label": "Starting list", "values": [5, 2, 4, 6, 1, 3]},
        {"label": "Round 1: place 1", "values": [1, 2, 4, 6, 5, 3], "colors": ["green"] + ["white"] * 5},
        {"label": "Round 2: 2 is already first", "values": [1, 2, 4, 6, 5, 3], "colors": ["green", "green"] + ["white"] * 4},
        {"label": "Round 3: place 3", "values": [1, 2, 3, 6, 5, 4], "colors": ["green"] * 3 + ["white"] * 3},
        {"label": "Round 4: place 4", "values": [1, 2, 3, 4, 5, 6], "colors": ["green"] * 4 + ["white"] * 2},
        {"label": "Round 5: no change", "values": [1, 2, 3, 4, 5, 6], "colors": ["green"] * 6},
    ],
    "The sorted part grows from the left, one position at a time.",
)

# 5 — insertion sort
insertion_walk = array_walkthrough(
    "ch5-05-insertion-sort-flow",
    "Insertion Sort: Add Each Item to the Sorted Part",
    [
        {"label": "Start with 5 sorted", "values": [5, 2, 4, 6, 1, 3], "colors": ["green"] + ["white"] * 5},
        {"label": "Insert 2", "values": [2, 5, 4, 6, 1, 3], "colors": ["green"] * 2 + ["white"] * 4},
        {"label": "Insert 4", "values": [2, 4, 5, 6, 1, 3], "colors": ["green"] * 3 + ["white"] * 3},
        {"label": "Insert 6", "values": [2, 4, 5, 6, 1, 3], "colors": ["green"] * 4 + ["white"] * 2},
        {"label": "Insert 1", "values": [1, 2, 4, 5, 6, 3], "colors": ["green"] * 5 + ["white"]},
        {"label": "Insert 3: finished", "values": [1, 2, 3, 4, 5, 6], "colors": ["green"] * 6},
    ],
    "Larger sorted items slide right to make a gap for the new item.",
)

# 6 — counting sort
counting_walk = counting_diagram()

# 7 — merge sort
merge_walk = group_walkthrough(
    "ch5-07-merge-sort-divide-conquer",
    "Merge Sort: Split the List, Then Join Sorted Pieces",
    [
        {"label": "Starting list", "groups": ["[5, 2, 4, 6, 1, 3]"]},
        {"label": "Split in two", "groups": ["[5, 2, 4]", "[6, 1, 3]"]},
        {"label": "Split again", "groups": ["[5, 2]", "[4]", "[6, 1]", "[3]"]},
        {"label": "Split to single items", "groups": ["[5]", "[2]", "[4]", "[6]", "[1]", "[3]"]},
        {"label": "Join sorted neighbors", "groups": ["[2, 5]", "[4]", "[1, 6]", "[3]"]},
        {"label": "Join larger pieces", "groups": ["[2, 4, 5]", "[1, 3, 6]"]},
        {"label": "Join to finish", "groups": ["[1, 2, 3, 4, 5, 6]"]},
    ],
    "Single-item pieces are already sorted; each join puts two sorted pieces together.",
)

# 8 — quick sort
quick_walk = array_walkthrough(
    "ch5-08-quick-sort-partition",
    "Quick Sort: Each Pivot Finds Its Final Place",
    [
        {"label": "Starting list", "values": [5, 2, 4, 6, 1, 3]},
        {"label": "Pivot 3 divides the list", "values": [2, 1, 3, 6, 5, 4], "colors": ["white", "white", "green", "white", "white", "white"]},
        {"label": "Pivot 1 settles left side", "values": [1, 2, 3, 6, 5, 4], "colors": ["green", "white", "green", "white", "white", "white"]},
        {"label": "Pivot 4 settles right side", "values": [1, 2, 3, 4, 5, 6], "colors": ["green", "white", "green", "green", "white", "white"]},
        {"label": "Last pair is already ordered", "values": [1, 2, 3, 4, 5, 6], "colors": ["green"] * 6},
    ],
    "After a pivot is placed, quick sort works on the parts to its left and right.",
)

# 9 — heap sort phase 1: CBT mapping and bottom-up heapify
build_nodes = [
    N(
        "rule-box",
        "Complete Binary Tree Rules:\n• Left child = 2i + 1, Right = 2i + 2\n• Leaves: floor(n/2)..n-1 (already heaps)\n• Start heapify at floor(n/2) - 1",
        28,
        70,
        360,
        96,
        "light",
        size=12,
    ),
    N("raw-arr-label", "Initial unsorted array A (n = 6):", 28, 180, 360, 32, "gray", size=12),
    N("raw-0", "5\n[i=0]", 28, 222, 54, 48, "yellow", size=12),
    N("raw-1", "2\n[i=1]", 88, 222, 54, 48, "yellow", size=12),
    N("raw-2", "4\n[i=2]", 148, 222, 54, 48, "yellow", size=12),
    N("raw-3", "6\n[i=3]", 208, 222, 54, 48, "light", size=12),
    N("raw-4", "1\n[i=4]", 268, 222, 54, 48, "light", size=12),
    N("raw-5", "3\n[i=5]", 328, 222, 54, 48, "light", size=12),

    N("tree-note", "Initial Tree (Leaves in gray; internal nodes in yellow)", 460, 66, 490, 32, "gray", size=12),
    N("tn-0", "5 (i=0)", 670, 108, 70, 44, "yellow", size=12, bold=True),
    N("tn-1", "2 (i=1)", 550, 180, 70, 44, "yellow", size=12, bold=True),
    N("tn-2", "4 (i=2)", 790, 180, 70, 44, "yellow", size=12, bold=True),
    N("tn-3", "6 (i=3)", 490, 252, 70, 44, "light", size=12),
    N("tn-4", "1 (i=4)", 610, 252, 70, 44, "light", size=12),
    N("tn-5", "3 (i=5)", 730, 252, 70, 44, "light", size=12),

    N("step-1-label", "1. Heapify i=2 (val 4):\nchild 3 <= 4 (no swap)", 28, 316, 340, 44, "gray", size=12),
    N("s1-0", "5", 380, 316, 44, 44, "white", size=16),
    N("s1-1", "2", 432, 316, 44, 44, "white", size=16),
    N("s1-2", "4", 484, 316, 44, 44, "yellow", size=16, bold=True),
    N("s1-3", "6", 536, 316, 44, 44, "white", size=16),
    N("s1-4", "1", 588, 316, 44, 44, "white", size=16),
    N("s1-5", "3", 640, 316, 44, 44, "yellow", size=16),
    N("s1-note", "Subtree at i=2 satisfies max-heap", 700, 316, 270, 44, "light", size=12),

    N("step-2-label", "2. Heapify i=1 (val 2):\nchild 6 > 2 -> swap A[1], A[3]", 28, 376, 340, 44, "gray", size=12),
    N("s2-0", "5", 380, 376, 44, 44, "white", size=16),
    N("s2-1", "6", 432, 376, 44, 44, "teal", size=16, bold=True),
    N("s2-2", "4", 484, 376, 44, 44, "white", size=16),
    N("s2-3", "2", 536, 376, 44, 44, "teal", size=16, bold=True),
    N("s2-4", "1", 588, 376, 44, 44, "white", size=16),
    N("s2-5", "3", 640, 376, 44, 44, "white", size=16),
    N("s2-note", "Subtree at i=1 satisfies max-heap", 700, 376, 270, 44, "light", size=12),

    N("step-3-label", "3. Heapify i=0 (val 5):\nchild 6 > 5 -> swap A[0], A[1]", 28, 436, 340, 44, "gray", size=12),
    N("s3-0", "6", 380, 436, 44, 44, "green", size=16, bold=True),
    N("s3-1", "5", 432, 436, 44, 44, "teal", size=16, bold=True),
    N("s3-2", "4", 484, 436, 44, 44, "white", size=16),
    N("s3-3", "2", 536, 436, 44, 44, "white", size=16),
    N("s3-4", "1", 588, 436, 44, 44, "white", size=16),
    N("s3-5", "3", 640, 436, 44, 44, "white", size=16),
    N("s3-note", "5 sifts to i=1; settles (5>2, 5>1)", 700, 436, 270, 44, "light", size=12),

    N("step-4-label", "Final: Valid Max-Heap ready!", 28, 496, 340, 44, "gray", size=12),
    N("s4-0", "6", 380, 496, 44, 44, "green", size=16, bold=True),
    N("s4-1", "5", 432, 496, 44, 44, "yellow", size=16),
    N("s4-2", "4", 484, 496, 44, 44, "yellow", size=16),
    N("s4-3", "2", 536, 496, 44, 44, "white", size=16),
    N("s4-4", "1", 588, 496, 44, 44, "white", size=16),
    N("s4-5", "3", 640, 496, 44, 44, "white", size=16),
    N("s4-note", "Root 6 is max; O(n) build done", 700, 496, 270, 44, "green", size=12, bold=True),
]

build_edges = [
    E("tn-0", "tn-1", route="straight"),
    E("tn-0", "tn-2", route="straight"),
    E("tn-1", "tn-3", route="straight"),
    E("tn-1", "tn-4", route="straight"),
    E("tn-2", "tn-5", route="straight"),
]

heap_build = D(
    key="ch5-09-heap-build-flow",
    title="Heap Sort Phase 1: Complete Binary Tree and Heapify",
    size=(1000, 580),
    nodes=build_nodes,
    edges=build_edges,
    caption="Bottom-up heapify builds a valid max-heap in linear O(n) time before sorting begins.",
)

# 10 — heap sort phase 2: extraction and sorting walkthrough
heap_nodes = [
    N("heap-note", "A parent is at least\nas large as its children.", 28, 128, 230, 72, "light", size=13),
    N("heap-root", "6", 470, 72, 58, 44, "green", size=18, bold=True),
    N("heap-left", "5", 360, 142, 58, 44, "yellow", size=18, bold=True),
    N("heap-right", "4", 580, 142, 58, 44, "yellow", size=18, bold=True),
    N("heap-left-left", "2", 305, 212, 58, 44, "white", size=18),
    N("heap-left-right", "1", 415, 212, 58, 44, "white", size=18),
    N("heap-right-left", "3", 525, 212, 58, 44, "white", size=18),
]

heap_rows = [
    {"label": "Move 6; repair heap", "values": [5, 3, 4, 2, 1, 6], "colors": ["yellow", "white", "white", "white", "white", "green"]},
    {"label": "Move 5; repair heap", "values": [4, 3, 1, 2, 5, 6], "colors": ["yellow", "white", "white", "white", "green", "green"]},
    {"label": "Move 4; repair heap", "values": [3, 2, 1, 4, 5, 6], "colors": ["yellow", "white", "white", "green", "green", "green"]},
    {"label": "Move 3; repair heap", "values": [2, 1, 3, 4, 5, 6], "colors": ["yellow", "white", "green", "green", "green", "green"]},
    {"label": "Move 2; list is sorted", "values": [1, 2, 3, 4, 5, 6], "colors": ["green"] * 6},
]

for row_index, step in enumerate(heap_rows):
    y = 300 + row_index * 60
    heap_nodes.append(
        N(f"heap-step-{row_index}", step["label"], 30, y, 220, 44, "gray", size=12)
    )
    colors = step["colors"]
    for item_index, value in enumerate(step["values"]):
        color = colors[item_index]
        heap_nodes.append(
            N(
                f"heap-step-{row_index}-item-{item_index}",
                str(value),
                270 + item_index * 72,
                y,
                64,
                44,
                color,
                size=16,
                bold=color == "green",
            )
        )

heap_walk = D(
    key="ch5-10-heap-sort-flow",
    title="Heap Sort Phase 2: Root Extraction and Sorting Walkthrough",
    size=(1000, 660),
    nodes=heap_nodes,
    edges=[
        E("heap-root", "heap-left", route="straight"),
        E("heap-root", "heap-right", route="straight"),
        E("heap-left", "heap-left-left", route="straight"),
        E("heap-left", "heap-left-right", route="straight"),
        E("heap-right", "heap-right-left", route="straight"),
    ],
    caption="The green tail is sorted; the remaining front part is repeatedly reduced via heapify.",
)

DIAGRAMS = [
    choose_sort,
    taxonomy,
    bubble_walk,
    selection_walk,
    insertion_walk,
    counting_walk,
    merge_walk,
    quick_walk,
    heap_build,
    heap_walk,
]
