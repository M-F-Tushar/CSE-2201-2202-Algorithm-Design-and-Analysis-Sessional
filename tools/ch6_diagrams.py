"""Chapter 6 (Divide and Conquer) diagrams for range-query structures."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 6 - Divide and Conquer/diagrams"

# 1 ---------------------------------------------------- prefix sums
prefix_sum = D(
    key="ch6-01-prefix-sum-range-query",
    title="Prefix Sums: Fast Static Range Queries",
    size=(1500, 610),
    flow="H",
    nodes=[
        N("array-label", "Array a", 18, 160, 100, 58, "dark", size=15, bold=True),
        N("prefix-label", "Prefix P", 18, 285, 100, 58, "dark", size=15, bold=True),
        *[
            N(f"a{i}", f"i = {i}\na[i] = {value}", 130 + i * 158, 155, 144, 68, "blue", size=14)
            for i, value in enumerate([2, 1, 5, 3, 4, 7, 6, 8])
        ],
        *[
            N(
                f"p{i}",
                f"P[{i}] = {value}",
                130 + i * 158,
                280,
                144,
                68,
                "green" if i == 5 else "light",
                size=14,
                bold=i == 5,
            )
            for i, value in enumerate([2, 3, 8, 11, 15, 22, 28, 36])
        ],
        N("query-zero", "Query [0, 5]\nP[5] = 22", 160, 425, 330, 72, "green", size=16, bold=True),
        N("query-general", "Query [2, 5]\nP[5] - P[1] = 22 - 3 = 19", 585, 425, 400, 72, "teal", size=15),
        N("update-cost", "Change a[2]? Recompute P[2..7]\nPoint update costs O(n)", 1065, 425, 360, 72, "red", size=15, bold=True),
    ],
    caption="Inclusive prefix totals turn a static range sum into one subtraction, but a point change invalidates the suffix.",
)

# 2 ---------------------------------------------------- segment-tree hierarchy
_tree_values = [
    ("n0", "[0,7]\nsum = 36", 725, 90, "yellow"),
    ("n1", "[0,3]\nsum = 11", 365, 225, "blue"),
    ("n2", "[4,7]\nsum = 25", 1085, 225, "blue"),
    ("n3", "[0,1]\nsum = 3", 185, 360, "teal"),
    ("n4", "[2,3]\nsum = 8", 545, 360, "teal"),
    ("n5", "[4,5]\nsum = 11", 905, 360, "teal"),
    ("n6", "[6,7]\nsum = 14", 1265, 360, "teal"),
    ("n7", "index 0\nvalue = 2", 95, 495, "green"),
    ("n8", "index 1\nvalue = 1", 275, 495, "green"),
    ("n9", "index 2\nvalue = 5", 455, 495, "green"),
    ("n10", "index 3\nvalue = 3", 635, 495, "green"),
    ("n11", "index 4\nvalue = 4", 815, 495, "green"),
    ("n12", "index 5\nvalue = 7", 995, 495, "green"),
    ("n13", "index 6\nvalue = 6", 1175, 495, "green"),
    ("n14", "index 7\nvalue = 8", 1355, 495, "green"),
]
segment_tree = D(
    key="ch6-02-segment-tree-range-hierarchy",
    title="Segment Tree: Store Sums for Nested Ranges",
    size=(1600, 690),
    flow="V",
    nodes=[
        *[N(node_id, label, x, y, 150, 62, color, size=15, bold=y == 90) for node_id, label, x, y, color in _tree_values],
        N(
            "storage-note",
            "Leaves store a[i]    |    Parent = left sum + right sum    |    Array storage: about 4*n slots",
            260,
            610,
            1080,
            54,
            "light",
            size=15,
        ),
    ],
    edges=[
        E("n0", "n1"), E("n0", "n2"),
        E("n1", "n3"), E("n1", "n4"),
        E("n2", "n5"), E("n2", "n6"),
        E("n3", "n7"), E("n3", "n8"),
        E("n4", "n9"), E("n4", "n10"),
        E("n5", "n11"), E("n5", "n12"),
        E("n6", "n13"), E("n6", "n14"),
    ],
    caption="Each node summarizes one contiguous interval; the root covers the whole array and leaves represent individual indices.",
)

# 3 ----------------------------------------- query overlap and point update
query_update = D(
    key="ch6-03-segment-tree-query-and-update",
    title="Segment Tree: Query Overlap Cases and Update Path",
    size=(1760, 770),
    flow="V",
    nodes=[
        N("q-title", "Range query [0,5]", 75, 55, 690, 54, "yellow", size=18, bold=True),
        N("q-root", "[0,7]\npartial overlap", 305, 145, 200, 70, "yellow", size=15),
        N("q-left", "[0,3]\ncomplete: return 11", 80, 275, 230, 76, "green", size=14),
        N("q-right", "[4,7]\npartial overlap", 455, 275, 230, 76, "yellow", size=14),
        N("q-covered", "[4,5]\ncomplete: return 11", 355, 420, 240, 76, "green", size=14),
        N("q-empty", "[6,7]\nno overlap: return 0", 615, 420, 240, 76, "red", size=14),
        N("q-result", "Sum = 11 + 11 + 0 = 22", 275, 565, 390, 70, "blue", size=16, bold=True),
        N("u-title", "Point update: index 2 changes 5 -> 10", 930, 55, 760, 54, "yellow", size=18, bold=True),
        N("u-root", "[0,7]\n36 -> 41", 1220, 145, 220, 70, "orange", size=15, bold=True),
        N("u-left", "[0,3]\n11 -> 16", 1050, 275, 220, 76, "orange", size=15, bold=True),
        N("u-right", "[4,7]\n25 unchanged", 1400, 275, 220, 76, "light", size=14),
        N("u-sibling", "[0,1]\n3 unchanged", 900, 420, 210, 76, "light", size=14),
        N("u-branch", "[2,3]\n8 -> 13", 1160, 420, 220, 76, "orange", size=15, bold=True),
        N("u-leaf", "[2,2]\n5 -> 10", 1090, 555, 210, 76, "green", size=15, bold=True),
        N("u-untouched", "[3,3]\n3 unchanged", 1350, 555, 210, 76, "light", size=14),
        N("u-note", "Only the root-to-index-2 path is recomputed; untouched subtrees stay the same.", 920, 665, 700, 58, "teal", size=14),
    ],
    edges=[
        E("q-root", "q-left"), E("q-root", "q-right"),
        E("q-right", "q-covered"), E("q-right", "q-empty"),
        E("u-root", "u-left", color="#e8590c"), E("u-root", "u-right", color="#adb5bd"),
        E("u-left", "u-sibling", color="#adb5bd"), E("u-left", "u-branch", color="#e8590c"),
        E("u-branch", "u-leaf", color="#e8590c"), E("u-branch", "u-untouched", color="#adb5bd"),
    ],
    caption="A query prunes disjoint ranges and returns stored sums for fully covered ranges; an update changes one leaf and its ancestors.",
)

# 4 --------------------------------------- maximum-sum subarray
maximum_subarray = D(
    key="ch6-04-maximum-sum-subarray",
    title="Maximum Sum Subarray: Three Ways to Find the Best Contiguous Range",
    size=(1700, 890),
    flow="V",
    nodes=[
        N("array-label", "Input", 30, 102, 100, 68, "dark", size=15, bold=True),
        *[
            N(
                f"value-{i}",
                f"i = {i}\n{value}",
                145 + i * 165,
                102,
                145,
                68,
                "green" if i >= 3 else "blue",
                size=15,
                bold=i >= 3,
            )
            for i, value in enumerate([2, 3, -8, 7, 2, -1, 3])
        ],
        N("dc-title", "Divide and conquer", 65, 235, 710, 56, "yellow", size=18, bold=True),
        N("dc-root", "Solve [0,6]\nmid = 3", 300, 325, 240, 74, "yellow", size=15, bold=True),
        N("dc-left", "Left [0,3]\nbest = 7", 30, 460, 215, 76, "blue", size=14),
        N("dc-cross", "Crossing: 7 + 4\nsum = 11", 295, 460, 250, 76, "green", size=14, bold=True),
        N("dc-right", "Right [4,6]\nbest = 4", 600, 460, 215, 76, "blue", size=14),
        N("dc-result", "max(7, 4, 11) = 11\nThe crossing case wins", 175, 590, 500, 76, "green", size=16, bold=True),
        N("kadane-title", "Kadane: extend or restart at each index", 865, 235, 775, 56, "teal", size=18, bold=True),
        N("kadane-rule", "ending_here = max(a[i], ending_here + a[i])\nKeep best = max(best, ending_here)", 900, 325, 710, 74, "blue", size=15, bold=True),
        N(
            "kadane-trace",
            "i | a[i] | ending_here | best\n"
            "0 |   2  |      2      |  2\n"
            "1 |   3  |      5      |  5\n"
            "2 |  -8  |     -3      |  5\n"
            "3 |   7  |      7      |  7  restart\n"
            "4 |   2  |      9      |  9\n"
            "5 |  -1  |      8      |  9\n"
            "6 |   3  |     11      | 11",
            925,
            445,
            660,
            202,
            "light",
            size=13,
        ),
        N("kadane-result", "Best subarray: [3,6] = {7, 2, -1, 3}\nMaximum sum = 11", 920, 685, 670, 76, "green", size=15, bold=True),
        N("complexities", "Brute force O(n^2)   |   Divide and conquer O(n log n)   |   Kadane O(n)", 235, 790, 1230, 52, "dark", size=15, bold=True),
    ],
    edges=[
        E("dc-root", "dc-left"),
        E("dc-root", "dc-cross", color="#2f9e44"),
        E("dc-root", "dc-right"),
        E("dc-left", "dc-result"),
        E("dc-cross", "dc-result", color="#2f9e44"),
        E("dc-right", "dc-result"),
    ],
    caption="A non-empty maximum subarray is wholly left, wholly right, or crosses the split; Kadane keeps the best ending-at-i sum.",
)

DIAGRAMS = [prefix_sum, segment_tree, query_update, maximum_subarray]
