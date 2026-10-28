"""Hand-positioned visuals owned by 1st Batch/Theory only.

Run from any directory: python tools/b1_theory_diagrams.py
Uses the shared engine without modifying it. Existing manual scenes not listed in
SPECS are deliberately preserved. After manual edits, export the matching SVG;
rerunning this script replaces only its explicitly listed generated scenes.
"""
from __future__ import annotations

import json
from pathlib import Path

from excalidraw_gen import D, E, N, _anchor_points, _base, render_excalidraw, render_svg
from state_space_tree import S, state_space_tree

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Chapter 0 - Previous Year Questions/1st Batch/Theory/diagrams"
SPECS: list[D] = []


def box(i, text, x, y, w=260, h=80, color="blue", size=16):
    return N(i, text, x, y, w, h, color, size=size)


def add(key, title, size, nodes, edges=()):
    d = D("b1-theory-" + key, title, size, nodes, list(edges))
    SPECS.append(d)
    return d


def sequence(key, title, labels):
    nodes = [box(str(i), text, 80, 80 + i * 130, 640, 90, color)
             for i, (text, color) in enumerate(labels)]
    return add(key, title, (800, 100 + 130 * len(labels)), nodes,
               [E(str(i), str(i + 1)) for i in range(len(labels) - 1)])


sequence("01-question-escalator", "1st Batch Theory: full-paper roadmap", [
    ("Q1: Design, correctness, cases, growth\nQ2: Loops and recurrences", "blue"),
    ("Q3: Sorting and divide-and-conquer\nQ4: Greedy, caching, minimum spanning trees", "teal"),
    ("Q5: Backtracking\nQ6: Dynamic programming", "violet"),
    ("Q7: Shortest paths, optimality, knapsack\nQ8: Complexity classes, decisions, Dijkstra", "green"),
])

nodes, edges = [], []
for level in range(4):
    count = 2 ** level
    for j in range(count):
        nid = f"l{level}-{j}"
        nodes.append(box(nid, str(8 // count), 30 + (j + .5) * 800 / count - 35,
                         85 + 105 * level, 70, 50, "green" if level == 3 else "blue"))
        if level:
            edges.append(E(f"l{level-1}-{j//2}", nid, directed=False, route="straight"))
    nodes.append(box(f"cost{level}", f"{count} x {8//count} = 8", 850,
                     85 + 105 * level, 180, 50, "yellow"))
nodes += [box("sum", "Illustrative n = 8: 3 internal levels + leaves = 32\nFor n = 2^k: T(n) = n log2(n) + n; T(1) = 1", 100, 505, 850, 80, "teal")]
add("02-recursion-tree", "Q2(a,c), Q3(b): balanced recurrence", (1080, 630), nodes, edges)

# Slide-style yes/no state-space tree (yes = take, no = skip); dashed = never reached.
add_scene = SPECS.append
add_scene(state_space_tree(
    "b1-theory-04-subset-sum-tree",
    "Q5(c): Subset-Sum State-Space Tree (search prefix)",
    "A = {3, 5, 6, 7},   target d = 15;   yes = take, no = skip",
    S("0",
      yes=S("3",
            yes=S("8",
                  yes=S("14",
                        yes=S("21", color="red", note="21 > 15\nprune"),
                        no=S("14", color="red", note="14 ≠ 15\ndead end")),
                  no=S("8",
                       yes=S("15", color="green", note="15 = d\nsolution ✓"),
                       no=S("…", color="light", stub=True))),
            no=S("…", color="light", stub=True)),
      no=S("…", color="light", stub=True)),
    ["i₁: 3", "i₂: 5", "i₃: 6", "i₄: 7"],
    "The sum of the taken numbers is stored at the node.\nDashed nodes are not explored: the trace stops at the first solution.",
))

# Full reconstructed graph above the actual alphabetical DFS prefix.
positions = {"a": (95, 100), "b": (445, 100), "c": (270, 200),
             "d": (95, 300), "e": (445, 300), "f": (620, 200)}
nodes = [N(v, v, x, y, 52, 52, "teal", "ellipse", 18) for v, (x, y) in positions.items()]
# Nine edges, as drawn in the paper (there is no c-f edge); the layout is planar.
graph_edges = ["ab", "ac", "ad", "bc", "bf", "cd", "ce", "de", "ef"]
edges = [E(s, t, directed=False, route="straight") for s, t in graph_edges]
nodes += [box("given", "Undirected graph transcribed from the paper; no unlisted edges\nBelow: DFS prefix only, until first circuit", 50, 425, 900, 70, "gray")]
for nid, label, x, y, w, color in [
    ("ab", "a-b", 390, 530, 220, "blue"),
    ("abc", "a-b-c", 150, 640, 220, "blue"),
    ("abf", "a-b-f", 640, 640, 220, "green"),
    ("abcd", "a-b-c-d", 20, 750, 220, "blue"),
    ("abce", "a-b-c-e", 280, 750, 220, "blue"),
    ("abfe", "a-b-f-e", 640, 750, 220, "green"),
    ("abcdef", "a-b-c-d-e-f\nNo f-a: dead end", 10, 860, 200, "red"),
    ("abced", "a-b-c-e-d\nNo d-f: dead end", 225, 860, 200, "red"),
    ("abcef", "a-b-c-e-f\nNo f-d: dead end", 440, 860, 200, "red"),
    ("abfecd", "a-b-f-e-c-d-a\nCircuit closes", 655, 860, 200, "green"),
]:
    nodes.append(box(nid, label, x, y, w, 80, color))
edges += [E(a, b, route="straight") for a, b in [
    ("ab", "abc"), ("ab", "abf"), ("abc", "abcd"), ("abc", "abce"),
    ("abf", "abfe"), ("abcd", "abcdef"), ("abce", "abced"),
    ("abce", "abcef"), ("abfe", "abfecd")]]
add("05-hamiltonian-tree", "Q5(d): paper graph and backtracking", (1000, 1010), nodes, edges)

add("07-classes-venn", "Q8(a): known class relations (not a strict Venn)", (850, 670), [
    box("p", "P\nPolynomial-time decision", 40, 100, 300, 80, "blue"),
    box("np", "NP\nPolynomial certificate verifier", 440, 100, 370, 80, "teal"),
    box("npc", "NP-complete\nExactly NP intersect NP-hard", 240, 310, 380, 80, "violet"),
    box("hard", "NP-hard\nEvery L in NP reduces to H", 440, 500, 370, 80, "orange"),
    box("open", "P = NP? OPEN\nNo strict separation asserted", 30, 500, 370, 80, "yellow"),
], [E("p", "np", "subset", route="straight"),
    E("npc", "np", "subset", route="straight"), E("npc", "hard", "subset", route="straight")])

sequence("09-design-analysis", "Q1(a): design and analysis", [
    ("Specify valid inputs and required outputs\nInclude boundary cases and constraints", "blue"),
    ("Design precise, effective steps\nChoose representations and a strategy", "teal"),
    ("Prove correctness and termination\nAll valid inputs must meet the specification", "green"),
    ("Analyze time and auxiliary space\nState size, model, cases, and tradeoffs", "violet"),
])

add("10-case-analysis", "Q1(b): illustrative linear search, n = 5", (800, 650), [
    box("array", "Array: [9, 2, 7, 4, 1]\nScan left to right, stop on the first match", 60, 80, 680, 80),
    box("best", "Best: target 9\n1 comparison = Theta(1)", 60, 220, 310, 90, "green"),
    box("worst", "Worst: target 1 or absent\n5 comparisons = Theta(n)", 430, 220, 310, 90, "red"),
    box("average", "Average: target occurs once; uniform position\n(1 + 2 + 3 + 4 + 5) / 5 = 3\nIn general (n + 1) / 2 = Theta(n)", 60, 390, 680, 120, "yellow"),
    box("distribution", "Different probabilities can change the average; state them.", 60, 550, 680, 55, "gray", 15),
])

nodes = [box("limit", "(n log2(n)) / n^2 = log2(n) / n tends to 0\nFixed constants affect crossover, not the eventual growth order", 60, 475, 680, 85, "yellow", 15)]
for r, values in enumerate([
    ["n", "n^2", "n log2(n)"],
    ["10", "100", "33.22"],
    ["1,000", "1,000,000", "9,965.78"],
    ["1,000,000", "10^12", "19,931,568.57"],
]):
    for c, value in enumerate(values):
        nodes.append(box(f"growth{r}-{c}", value, 35 + 245*c, 80 + 95*r, 235, 65,
                         ["gray", "blue", "teal", "green"][r]))
add("11-growth", "Q1(c): unit-coefficient growth comparison", (800, 610), nodes)

add("12-loop-counts", "Q2(b): illustrative n = 8 loop counts", (800, 600), [
    box("outer", "Both outer loops use i = 1, 2, 4, 8\nK = floor(log2(n)) = 3", 70, 80, 660, 80),
    box("one", "(i) Inner limit n\n8 + 8 + 8 + 8 = 32\nn (floor(log2(n)) + 1)", 35, 240, 350, 130, "blue"),
    box("two", "(ii) Inner limit i\n1 + 2 + 4 + 8 = 15\n2^(K+1) - 1", 415, 240, 350, 130, "green"),
    box("bounds", "(i) Theta(n log n)     (ii) Theta(n)\nPositive integer n, constant-time body, no overflow", 70, 455, 660, 85, "yellow"),
], [E("outer", "one", route="straight"), E("outer", "two", route="straight")])

add("13-merge-sort", "Q3(a): illustrative divide, conquer, combine", (800, 650), [
    box("root", "[5, 2, 4, 7]", 250, 85, 300, 60),
    box("l", "[5, 2]", 60, 215, 280, 60), box("r", "[4, 7]", 460, 215, 280, 60),
    box("ls", "[5] + [2] => [2, 5]", 40, 345, 320, 70, "teal"),
    box("rs", "[4] + [7] => [4, 7]", 440, 345, 320, 70, "teal"),
    box("out", "Merge => [2, 4, 5, 7]", 200, 505, 400, 70, "green"),
], [E("root", "l", "divide", route="straight"), E("root", "r", "divide", route="straight"),
    E("l", "ls", "conquer"), E("r", "rs", "conquer"),
    E("ls", "out", "combine", route="straight"), E("rs", "out", "combine", route="straight")])

sequence("14-quicksort-space", "Q3(c): quicksort space conventions", [
    ("Array partition uses swaps\nO(1) auxiliary partition workspace", "blue"),
    ("Ordinary two-call recursion stack\nExpected O(log n) with random pivots; worst O(n)", "orange"),
    ("Recurse on smaller side; iterate on larger\nWorst-case stack O(log n); time can remain Theta(n^2)", "teal"),
    ("Strict in-place means O(1) TOTAL auxiliary space\nCalling quicksort in-place usually excludes its stack", "yellow"),
])

add("15-coin-change", "Q4(a), Q6(d): unlimited coins {1, 3, 4}, amount 6", (850, 700), [
    box("greedy", "Largest-first greedy\n4 + 1 + 1 = 6\n3 coins", 35, 90, 360, 120, "red"),
    box("opt", "Optimal\n3 + 3 = 6\n2 coins", 455, 90, 360, 120, "green"),
    box("state", "C[0] = 0\nC[x] = 1 + min C[x-c], c in {1,3,4}, c <= x\nUnreachable / empty minimum = infinity", 45, 280, 760, 110, "blue"),
    box("table", "Amount x:   0   1   2   3   4   5   6\nMin coins:   0   1   2   1   1   2   2", 45, 445, 760, 85, "teal"),
    box("trace", "Traceback: 6 -> 3 -> 0 (subtract coin 3 twice)\nNo single available coin has value 6, so two is optimal", 45, 575, 760, 80, "green", 15),
])

add("16-memo-tab", "Q4(b): Fibonacci F0 = 0, F1 = 1", (850, 750), [
    box("memo", "Memoization: request F5", 40, 90, 360, 70),
    box("m4", "Compute F4, then F3\nCache each non-base result", 40, 235, 360, 90, "teal"),
    box("m3", "Repeated F3 uses cached result\nF5 = 3 + 2 = 5", 40, 405, 360, 90, "green"),
    box("tab", "Tabulation: start at F0, F1", 450, 90, 360, 70),
    box("t2", "Fill F2, F3, F4, F5\n0, 1, 1, 2, 3, 5", 450, 235, 360, 90, "teal"),
    box("t3", "Read table[5] = 5\nNo recursion stack", 450, 405, 360, 90, "green"),
    box("model", "Both visit all needed Fibonacci states: O(n) arithmetic operations\nO(n) stored values here; tabulation can keep two previous values\nUnit-cost arithmetic model; large integers require more bit work", 40, 570, 770, 115, "yellow", 15),
], [E("memo", "m4"), E("m4", "m3"), E("tab", "t2"), E("t2", "t3")])

nodes = [N(v, v, x, y, 60, 60, "blue", "ellipse", 18) for v, x, y in [
    ("A", 75, 120), ("B", 325, 120), ("C", 75, 370), ("D", 575, 120), ("E", 575, 370)]]
edges = [E(s, t, str(w), color="#2f9e44" if take else "#868e96", directed=False, route="straight")
         for s, t, w, take in [("A", "B", 2, 1), ("A", "C", 3, 0), ("B", "C", 1, 1),
                              ("B", "D", 4, 1), ("C", "D", 5, 0), ("C", "E", 6, 1), ("D", "E", 7, 0)]]
nodes += [box("prim", "Prim from A: AB(2), BC(1), BD(4), CE(6)", 40, 505, 720, 60, "teal"),
          box("kruskal", "Kruskal: BC(1), AB(2), skip AC(3), BD(4),\nskip CD(5), CE(6); stop after 4 accepted edges", 40, 605, 720, 80, "blue"),
          box("result", "Reconstructed undirected graph; green = unique MST\nTotal weight = 1 + 2 + 4 + 6 = 13", 40, 725, 720, 80, "green")]
add("17-mst", "Q4(c): Prim and Kruskal on the stated graph", (800, 850), nodes, edges)

# Q5(b): 4-Queens search as a state-space tree. A node stores the columns chosen so far
# (one digit per row); each edge is the column tried in the next row. Search prefix only.
add_scene(state_space_tree(
    "b1-theory-18-queens-backtracking",
    "Q5(b): 4-Queens State-Space Tree (search prefix)",
    "Rows and columns start at 0; row k tries columns 0, 1, 2, 3",
    S("start",
      yes=S("0", edge="col 0",
            yes=S("02", edge="col 2", color="red", note="row 2:\nno safe col"),
            no=S("03", edge="col 3",
                 yes=S("031", edge="col 1", color="red", note="row 3:\nno safe col"))),
      no=S("1", edge="col 1",
           yes=S("13", edge="col 3",
                 yes=S("130", edge="col 0",
                       yes=S("1302", edge="col 2", color="green", note="solution\n[1,3,0,2]"))))),
    ["row 0", "row 1", "row 2", "row 3"],
    "A node stores the columns chosen so far, one digit per row.\n"
    "Red = dead end: backtrack.  Green = all 4 queens placed.\n"
    "Columns that clash (same column or diagonal) are not drawn.",
    level_gap=100, min_width=860,
))

# Q5(a): the backtracking idea on a tiny abstract tree. Node numbers = depth-first visit order.
add_scene(state_space_tree(
    "b1-theory-24-backtracking-concept",
    "Q5(a): Backtracking on a State-Space Tree",
    "Numbers = depth-first visit order; 1st / 2nd = order tried",
    S("start",
      yes=S("1", edge="1st", color="red", note="fails check:\nprune"),
      no=S("2", edge="2nd",
           yes=S("3", edge="1st", color="red", note="dead end:\nundo"),
           no=S("4", edge="2nd", color="green", note="solution"))),
    ["step 1", "step 2"],
    "Each level adds one more choice. Try a choice and check it; go deeper if promising.\n"
    "If it fails or is a dead end, undo it and try the next choice.",
    level_gap=100, min_width=900,
))

add("19-dp-properties", "Q6(a): valid recurrence and reusable subproblems", (850, 720), [
    box("root", "Illustrative K(3,3): weights [1,1,1], profits [1,1,1]\nK(i,w) = best profit from first i items at capacity w", 55, 80, 740, 80),
    box("skip", "Skip item 3: K(2,3)", 35, 270, 360, 75, "blue"),
    box("take", "Take item 3: 1 + K(2,2)", 455, 270, 360, 75, "teal"),
    box("repeat", "Shared non-base subproblem K(1,2) = 1\nReached by take from K(2,3), or skip from K(2,2)\nOther branches omitted: cache each identical state once", 45, 440, 760, 110, "yellow", 15),
    box("concept", "Optimal substructure: best of exhaustive skip/take cases\nOverlap: identical (i,w) states can recur\nFibonacci evaluation has no optimization objective", 45, 590, 760, 90, "green", 15),
], [E("root", "skip", "skip", route="straight"), E("root", "take", "take", route="straight"),
    E("skip", "repeat", "take", route="straight"), E("take", "repeat", "skip", route="straight")])

weights, profits = [3, 4, 5, 6], [2, 3, 1, 4]
table = [[0] * 9]
for weight, profit in zip(weights, profits):
    prev = table[-1]
    table.append([max(prev[w], profit + prev[w-weight]) if w >= weight else prev[w] for w in range(9)])
nodes = [box("rec", "K(i,w) = max(K(i-1,w), p_i + K(i-1,w-w_i))\nTake term only when w_i <= w; bases K(0,w)=K(i,0)=0", 30, 80, 790, 90, "blue", 15),
         box("input", "Illustrative W=8; weights [3,4,5,6], profits [2,3,1,4]\nEach item once, total weight <= W, empty selection allowed", 30, 210, 790, 85, "yellow", 15)]
# Separate editable cells keep both the SVG and scene table legible.
for r, values in enumerate([["i / w"] + list(range(9))] + [[i] + row for i, row in enumerate(table)]):
    for c, val in enumerate(values):
        nodes.append(box(f"cell{r}-{c}", str(val), 45 + 76*c, 345 + 58*r, 68, 48,
                         "gray" if r == 0 or c == 0 else "green" if r == 5 and c == 9 else "teal", 15))
nodes += [box("trace", "Traceback: skip 4, skip 3, take 2, take 1\nItems {1,2}: weight 7 <= 8, profit 5 (optimal)\nO(nW) time is pseudo-polynomial in binary-encoded W", 30, 740, 790, 110, "green", 15)]
add("20-knapsack", "Q6(b), Q7(c): 0/1 knapsack recurrence and table", (850, 900), nodes)

grid = [[1, 0, 1], [0, 1, 0], [1, 1, 1], [0, 0, 1]]
dp = [[1, 1, 2], [1, 2, 2], [2, 3, 4], [2, 3, 5]]
path = {(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2)}
nodes = [box("gtitle", "Input coins", 45, 85, 330, 50, "gray"),
         box("dtitle", "DP: best coin total", 475, 85, 330, 50, "gray")]
for side, values, x in [("g", grid, 50), ("d", dp, 480)]:
    for r in range(4):
        for c in range(3):
            nodes.append(box(f"{side}{r}{c}", f"({r},{c})\n{values[r][c]}", x+110*c, 180+95*r,
                             95, 75, "green" if (r,c) in path else "blue", 15))

edges = [E(f"g{r}{c}", f"g{s}{t}", color="#2f9e44", route="straight")
         for (r,c), (s,t) in zip([(0,0),(0,1),(1,1),(2,1),(2,2)], [(0,1),(1,1),(2,1),(2,2),(3,2)])]
nodes += [box("gridrule", "Illustrative 4 x 3 grid: right/down only; collect both endpoints\nGreen cells/arrows: one optimal route, total 1+0+1+1+1+1 = 5\nBase dp(0,0)=1; each next cell adds max(existing up, left)", 35, 610, 780, 110, "yellow", 15)]
add("21-grid", "Q6(c): coin grid and maximum-collection DP", (850, 770), nodes, edges)

add("22-negative-edge", "Q7(a): negative edge defeats label-setting Dijkstra", (800, 710), [
    N("A", "A", 75, 100, 65, 65, "blue", "ellipse", 20),
    N("B", "B", 615, 100, 65, 65, "red", "ellipse", 20),
    N("C", "C", 345, 300, 65, 65, "teal", "ellipse", 20),
    box("failure", "Source A: B settles at 1 before C at 4\nLater C -> B gives 4 - 5 = -1; settled B is not revised\nTrue distances: A=0, C=4, B=-1; no cycle exists", 40, 435, 720, 105, "red", 15),
    box("bf", "Bellman-Ford permits repeated improvements\nRelax all edges for at most V-1 passes\nThen check for source-reachable negative cycles", 40, 585, 720, 80, "green", 15),
], [E("A", "B", "1", route="straight"), E("A", "C", "4", route="straight"), E("C", "B", "-5", route="straight")])

sequence("23-decision-optimization", "Q8(b): threshold decision versus optimization", [
    ("Decision: is some feasible tour cost <= k?\nOptimization: find a minimum-cost feasible tour", "blue"),
    ("An exact optimizer answers the threshold question\nCompare its optimum with k; handle infeasibility", "teal"),
    ("Conversely: integer objective in known [L,U]\nBinary search threshold oracle: O(log(U-L+1)) calls\nRequires polynomial bit length and work per call", "yellow"),
    ("This gives an optimal VALUE, not automatically a tour\nTSP can recover a tour via additional self-reduction queries\nDo not claim this for arbitrary optimization problems", "violet"),
])


def emit(d: D):
    """Keep engine SVG labels/captions present and correctly sized in the scene."""
    scene = render_excalidraw(d)
    for el in scene["elements"]:
        if el["type"] == "text" and el.get("containerId"):
            lines = el["text"].splitlines()
            h = max(1, len(lines)) * el["fontSize"] * 1.25
            el["y"] += (el["height"] - h) / 2
            el["height"] = h
    index = {n.id: n for n in d.nodes}
    for i, e in enumerate(d.edges):
        if not e.label:
            continue
        pts = _anchor_points(index[e.src], index[e.dst], d.flow, e.route, e.bend, e.pts)
        j = len(pts) // 2
        x = (pts[j-1][0] + pts[j][0]) / 2
        y = (pts[j-1][1] + pts[j][1]) / 2
        width = len(e.label) * 8 + 14
        background = _base(f"{d.key}-edge-label-bg-{i}", "rectangle",
                           x-width/2, y-12, width, 24, "#ffffff", "#ffffff", 6000+i)
        background["roughness"] = 0
        scene["elements"].append(background)
        scene["elements"].append({
            **_base(f"{d.key}-edge-label-{i}", "text", x-width/2, y-9, width, 18,
                    "#495057", "#ffffff", 5000+i),
            "text": e.label, "originalText": e.label, "fontSize": 13,
            "fontFamily": 1, "textAlign": "center", "verticalAlign": "top",
            "containerId": None, "lineHeight": 1.25,
        })
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{d.key}.svg").write_text(render_svg(d), encoding="utf-8")
    (OUT / f"{d.key}.excalidraw").write_text(json.dumps(scene, indent=2), encoding="utf-8")


COVERAGE = {
    "01-question-escalator": "Overview: Q1–Q8",
    "02-recursion-tree": "Q2(a), Q2(c), Q3(b)",
    "03-heap-build-tree": "Q3(d)",
    "04-subset-sum-tree": "Q5(c)",
    "05-hamiltonian-tree": "Q5(d)",
    "06-bellman-ford-graph": "Q7(b)",
    "07-classes-venn": "Q8(a)",
    "08-dijkstra-graph": "Q8(c)",
    "09-design-analysis": "Q1(a)",
    "10-case-analysis": "Q1(b)",
    "11-growth": "Q1(c)",
    "12-loop-counts": "Q2(b)",
    "13-merge-sort": "Q3(a)",
    "14-quicksort-space": "Q3(c)",
    "15-coin-change": "Q4(a), Q6(d)",
    "16-memo-tab": "Q4(b)",
    "17-mst": "Q4(c)",
    "18-queens-backtracking": "Q5(b)",
    "24-backtracking-concept": "Q5(a)",
    "19-dp-properties": "Q6(a)",
    "20-knapsack": "Q6(b), Q7(c)",
    "21-grid": "Q6(c)",
    "22-negative-edge": "Q7(a)",
    "23-decision-optimization": "Q8(b)",
}


def write_index():
    lines = ["# 1st Batch Theory — Diagram Index", "",
             "All **27/27 subquestions** have suitable linked visuals: **24 SVG/source pairs**",
             "(23 topic visuals plus one full-paper roadmap). Shared visuals are listed against",
             "every part they genuinely explain. Printed inputs and the two source-paper graphs were",
             "checked against the supplied 2023 scan; extra teaching examples are labeled illustrative.", "",
             "The `.excalidraw` scene is editable in [Excalidraw](https://excalidraw.com).",
             "After a manual scene edit, re-export its SVG so the Markdown preview stays synchronized.",
             "The scoped generator `tools/b1_theory_diagrams.py` uses the shared engine without",
             "changing shared tools. Running it replaces its 21 listed scenes (including five",
             "corrected old visuals) and this index; it preserves manual scenes 03, 06, 08.",
             "Do not regenerate over later manual edits without reconciling them first.", "",
             "| Parts | Diagram | Preview | Editable source |", "|---|---|---|---|"]
    for suffix, parts in COVERAGE.items():
        key = "b1-theory-" + suffix
        scene = json.loads((OUT / f"{key}.excalidraw").read_text(encoding="utf-8"))
        title = next(e["text"] for e in scene["elements"] if e["type"] == "text")
        lines.append(f"| {parts} | {title} | [SVG]({key}.svg) | [Excalidraw]({key}.excalidraw) |")
    lines += ["", "## Interpretation notes", "",
              "- Recurrence tree uses a complete n=8 example, not disconnected symbolic leaves.",
              "- Subset-sum and queen trees show only the search prefix; they do not claim full enumeration.",
              "- Hamiltonian visual uses the graph transcribed from the paper and shows the search prefix through the first circuit.",
              "- NP visual states known inclusions only; it assumes neither P=NP nor P≠NP.",
              "- Green graph edges mark the reported MST/shortest-path tree, not extra graph edges.",
              "- Dijkstra keeps the first predecessor on equal distances; F and C each have tied shortest routes.",
              "", "[Back to answers](../README.md)", ""]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    for spec in SPECS:
        emit(spec)
    write_index()
    print(f"Wrote {len(SPECS)} diagram pairs and index; preserved 3 manual pairs.")
