"""Chapter 7 (Greedy Algorithms) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 7 - Greedy Algorithms/diagrams"

# 1 ---------------------------------------------------- greedy decision flow
greedy_decision = D(
    key="ch7-01-greedy-decision-flow",
    title="Greedy Algorithm Decision and Proof Framework",
    size=(1180, 560),
    flow="H",
    nodes=[
        N("prob", "Optimization\nProblem", 40, 80, 150, 64, "blue", "ellipse", bold=True),
        N("cand", "Candidate\nSet of Items", 210, 80, 160, 64, "blue"),
        N("rule", "Selection Rule\nChoose locally best option", 430, 80, 230, 64, "yellow", size=14, bold=True),
        N("feas", "Still\nFeasible?", 710, 70, 160, 84, "yellow", "diamond", 15),
        N("commit", "Commit Choice\n(irrevocable)", 920, 80, 180, 64, "green", size=14),
        N("reject", "Reject\nCandidate", 705, 200, 170, 54, "red"),
        N("update", "Update Remaining\nSubproblem", 920, 200, 180, 64, "green"),
        N("done", "Solution\nComplete?", 930, 310, 160, 84, "yellow", "diamond", 15),
        N("ans", "Optimal Greedy\nSolution", 920, 440, 180, 64, "green", bold=True),
        # Proof foundation
        N("proof", "Foundational Properties for Correctness:\n1. Greedy-Choice Property: local choice leads to global optimum\n2. Optimal Substructure: optimal solution contains optimal sub-solutions",
          80, 420, 800, 74, "teal", bold=True),
    ],
    edges=[
        E("prob", "cand"), E("cand", "rule"), E("rule", "feas"),
        E("feas", "commit", "Yes"), E("feas", "reject", "No"),
        E("reject", "rule", route="v", bend=0.5),
        E("commit", "update"), E("update", "done"),
        E("done", "cand", "No", pts=[(930, 352), (290, 352), (290, 144)]),
        E("done", "ans", "Yes"),
        E("proof", "ans", "guarantees", dashed=True, color="#2f9e44"),
    ],
    caption="A greedy algorithm makes irrevocable choices that must be justified by greedy-choice and optimal substructure properties",
)

# 2 ---------------------------------------------------- local to global
local_to_global = D(
    key="ch7-02-local-to-global",
    title="From Local Best Choice to Global Optimum",
    size=(1020, 560),
    flow="V",
    nodes=[
        N("local", "Identify Best Local Choice", 380, 60, 260, 54, "yellow"),
        N("safe", "Is Local Choice Safe?\n(Greedy Choice Property)", 370, 145, 280, 80, "yellow", "diamond", 15),
        N("fail", "Greedy Rule Fails!\nCounterexample exists", 60, 155, 250, 60, "red", bold=True),
        N("part", "Add to Partial Solution", 380, 260, 260, 54, "green"),
        N("reduc", "Reduce to Smaller Problem\n(preserves same structure)", 360, 345, 300, 56, "green", size=14),
        N("opt", "Global Optimum Achieved!", 380, 440, 260, 54, "green", bold=True),
    ],
    edges=[
        E("local", "safe"),
        E("safe", "fail", "No"),
        E("safe", "part", "Yes"),
        E("part", "reduc"),
        E("reduc", "local", "repeat", route="loopr", bend=60),
        E("reduc", "opt", "base case"),
    ],
    caption="Greedy works when each local decision guarantees no loss of global optimality",
)

# 3 ---------------------------------------------------- correctness checklist
correctness_checklist = D(
    key="ch7-03-correctness-checklist",
    title="Greedy Correctness Verification Checklist",
    size=(1180, 380),
    flow="H",
    nodes=[
        N("s1", "1. Design Greedy Rule", 40, 80, 230, 54, "blue"),
        N("s2", "2. Prove Choice is Safe", 300, 80, 240, 54, "yellow", bold=True),
        N("s3", "3. Optimal Substructure", 570, 80, 250, 54, "blue", size=14),
        N("s4", "4. Time & Space Analysis", 850, 80, 250, 54, "green", size=14),
        # Proof tools
        N("p1", "Proof Method 1: Exchange Argument\nShow any optimal solution can exchange\nits element for greedy choice", 50, 190, 340, 84, "teal", size=13),
        N("p2", "Proof Method 2: Induction\nProve base case safe, then assume\nstep k safe to prove step k+1", 420, 190, 340, 84, "teal", size=13),
        N("p3", "Proof Method 3: Cut Property (for MST)\nMinimum weight crossing edge across\nany graph cut must belong to some MST", 790, 190, 340, 84, "teal", size=13),
    ],
    edges=[
        E("s1", "s2"), E("s2", "s3"), E("s3", "s4"),
        E("s2", "p1", route="v", dashed=True),
        E("s2", "p2", route="v", dashed=True),
        E("s2", "p3", route="v", dashed=True),
    ],
    caption="Exchange arguments are the most universal proof technique for greedy optimality",
)

# 4 ---------------------------------------------------- fractional knapsack
fractional_knapsack = D(
    key="ch7-04-fractional-knapsack",
    title="Fractional Knapsack Greedy Strategy (Sort by Value/Weight Ratio)",
    size=(1180, 420),
    flow="H",
    nodes=[
        N("input", "Item Pool\n(values & weights)", 40, 150, 180, 68, "blue", size=14),
        N("sort", "Sort Descending\nby Ratio (v_i / w_i)", 250, 150, 200, 68, "yellow", bold=True),
        N("i1", "Item 1 (Ratio 6)\nTake 100% (full)", 490, 70, 210, 64, "green"),
        N("i2", "Item 2 (Ratio 5)\nTake 100% (full)", 490, 160, 210, 64, "green"),
        N("i3", "Item 3 (Ratio 4)\nTake fraction", 490, 250, 210, 64, "yellow", size=14),
        N("full", "Knapsack Capacity\nFully Exhausted", 740, 150, 200, 64, "teal"),
        N("ans", "Max Value:\nTotal = 240", 975, 150, 150, 64, "green", bold=True),
    ],
    edges=[
        E("input", "sort"),
        E("sort", "i1"), E("i1", "i2"), E("i2", "i3"),
        E("i3", "full"), E("full", "ans"),
    ],
    caption="Fractional knapsack admits greedy solution because items can be subdivided; 0/1 knapsack cannot",
)

# 5 ---------------------------------------------------- coin change loop
coin_change = D(
    key="ch7-05-coin-change-loop",
    title="Coin Change Greedy Loop (Standard vs Canonical Systems)",
    size=(1080, 620),
    flow="V",
    nodes=[
        N("target", "Target Amount Remaining", 360, 60, 280, 54, "blue"),
        N("sort", "Sort Denominations Descending\n[c1 > c2 > c3 > ...]", 350, 145, 300, 54, "yellow"),
        N("pick", "Pick Largest Coin\n<= Remaining Amount", 360, 230, 280, 54, "yellow", size=14),
        N("sub", "Subtract Coin from Amount:\nRemaining -= Coin", 360, 315, 280, 54, "green"),
        N("done", "Remaining Amount\n== 0?", 400, 400, 200, 80, "yellow", "diamond", 15),
        N("ans", "Return Coin Selection", 380, 515, 240, 50, "green", bold=True),
        N("warn", "Warning: Greedy fails\nfor non-canonical systems\nsuch as {1, 3, 4} for 6!",
          690, 215, 340, 90, "red", size=13),
    ],
    edges=[
        E("target", "sort"),
        E("sort", "pick"),
        E("pick", "sub"),
        E("sub", "done"),
        E("done", "pick", "No", route="loopl", bend=60),
        E("done", "ans", "Yes"),
        E("warn", "pick", route="h", dashed=True, color="#e03131"),
    ],
    caption="Canonical coin denominations guarantee matroid properties where greedy strategy succeeds",
)

# 6 ---------------------------------------------------- fibonacci iterative
fibonacci_iterative = D(
    key="ch7-06-fibonacci-iterative",
    title="Fibonacci Number Generation - Iterative Bottom-Up Build",
    size=(1180, 340),
    flow="H",
    nodes=[
        N("f0", "F(0) = 0", 40, 70, 120, 52, "blue"),
        N("f1", "F(1) = 1", 40, 180, 120, 52, "blue"),
        N("f2", "F(2) = 1", 200, 125, 120, 52, "green"),
        N("f3", "F(3) = 2", 360, 125, 120, 52, "green"),
        N("f4", "F(4) = 3", 520, 125, 120, 52, "green"),
        N("f5", "F(5) = 5", 680, 125, 120, 52, "green"),
        N("f6", "F(6) = 8", 840, 125, 120, 52, "green"),
        N("f7", "F(7) = 13", 1000, 125, 120, 52, "yellow", bold=True),
    ],
    edges=[
        E("f0", "f2"), E("f1", "f2"),
        E("f1", "f3", route="loopb", bend=35), E("f2", "f3"),
        E("f2", "f4", route="loopt", bend=35), E("f3", "f4"),
        E("f3", "f5", route="loopt", bend=35), E("f4", "f5"),
        E("f4", "f6", route="loopt", bend=35), E("f5", "f6"),
        E("f5", "f7", route="loopt", bend=35), E("f6", "f7"),
    ],
    caption="Iterative evaluation keeps only two prior variables, achieving O(n) time and O(1) space",
)

# 7 ---------------------------------------------------- huffman merge tree
huffman_tree = D(
    key="ch7-07-huffman-merge-tree",
    title="Huffman Coding Tree Construction (Total Weight 100)",
    size=(1140, 600),
    flow="V",
    nodes=[
        N("root", "Root: 100", 500, 60, 140, 50, "yellow", bold=True),
        # Level 1
        N("f", "f: 45\ncode: 0", 250, 160, 160, 54, "green", bold=True),
        N("n55", "Internal: 55", 690, 160, 160, 50, "blue"),
        # Level 2
        N("n25", "Internal: 25", 550, 260, 160, 50, "blue"),
        N("n30", "Internal: 30", 810, 260, 160, 50, "blue"),
        # Level 3
        N("c", "c: 12\ncode: 100", 450, 360, 150, 54, "green"),
        N("d", "d: 13\ncode: 101", 620, 360, 150, 54, "green"),
        N("n14", "Internal: 14", 780, 360, 150, 50, "blue"),
        N("e", "e: 16\ncode: 111", 950, 360, 150, 54, "green"),
        # Level 4
        N("a", "a: 5\ncode: 1100", 700, 470, 150, 54, "green"),
        N("b", "b: 9\ncode: 1101", 870, 470, 150, 54, "green"),
    ],
    edges=[
        E("root", "f", "0"), E("root", "n55", "1"),
        E("n55", "n25", "0"), E("n55", "n30", "1"),
        E("n25", "c", "0"), E("n25", "d", "1"),
        E("n30", "n14", "0"), E("n30", "e", "1"),
        E("n14", "a", "0"), E("n14", "b", "1"),
    ],
    caption="Frequent characters receive shorter prefix codes; infrequent characters sit deeper in the tree",
)

# 8 ---------------------------------------------------- classroom huffman
huffman_classroom = D(
    key="ch7-08-five-symbol-huffman",
    title="Five-Symbol Huffman Tree (Total Frequency 15)",
    size=(1040, 540),
    flow="V",
    nodes=[
        N("root", "Root: 15", 450, 60, 140, 50, "yellow", bold=True),
        N("a", "A: 9\ncode: 0", 240, 160, 150, 54, "green", bold=True),
        N("n6", "Internal: 6", 610, 160, 150, 50, "blue"),
        N("n10", "Internal: 4", 480, 260, 150, 50, "blue"),
        N("n11", "Internal: 2", 730, 260, 150, 50, "blue"),
        N("g", "G: 2\ncode: 100", 400, 360, 140, 54, "green"),
        N("b", "B: 2\ncode: 101", 560, 360, 140, 54, "green"),
        N("c", "C: 1\ncode: 110", 720, 360, 140, 54, "green"),
        N("d", "D: 1\ncode: 111", 870, 360, 140, 54, "green"),
    ],
    edges=[
        E("root", "a", "0"), E("root", "n6", "1"),
        E("n6", "n10", "0"), E("n6", "n11", "1"),
        E("n10", "g", "0"), E("n10", "b", "1"),
        E("n11", "c", "0"), E("n11", "d", "1"),
    ],
    caption="Two lowest frequency symbols are repeatedly merged using a min-priority queue",
)

# 9 ---------------------------------------------------- activity selection timeline
activity_timeline = D(
    key="ch7-09-activity-selection-timeline",
    title="Activity Selection Problem - Timeline by Earliest Finish Time",
    size=(1140, 480),
    flow="V",
    containers=[
        N("box_sel", "Selected Activities (Mutually Compatible, Max Set = 4)", 50, 70, 1040, 170, "container"),
        N("box_rej", "Rejected Examples (Overlap with earlier finished selected activity)", 50, 260, 1040, 160, "container"),
    ],
    nodes=[
        # Selected
        N("a1", "A1: [1 -> 4]", 110, 115, 180, 50, "green", bold=True),
        N("a4", "A4: [5 -> 7]", 360, 115, 180, 50, "green", bold=True),
        N("a8", "A8: [8 -> 11]", 610, 115, 180, 50, "green", bold=True),
        N("a11", "A11: [12 -> 16]", 860, 115, 180, 50, "green", bold=True),
        # Rejected
        N("a2", "A2: [3 -> 5]\nConflicts with A1", 200, 310, 200, 60, "red"),
        N("a3", "A3: [0 -> 6]\nSpans too long", 460, 310, 200, 60, "red"),
        N("a6", "A6: [5 -> 9]\nConflicts with A8", 720, 310, 200, 60, "red"),
    ],
    edges=[
        E("a1", "a4", "finish 4 <= start 5"),
        E("a4", "a8", "finish 7 <= start 8"),
        E("a8", "a11", "finish 11 <= start 12"),
    ],
    caption="Sorting by earliest finish time leaves maximal room for subsequent compatible activities",
)

DIAGRAMS = [
    greedy_decision,
    local_to_global,
    correctness_checklist,
    fractional_knapsack,
    coin_change,
    fibonacci_iterative,
    huffman_tree,
    huffman_classroom,
    activity_timeline,
]
