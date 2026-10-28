"""Batch 2 Theory visuals only; shared rendering tools are deliberately unchanged.

Run from any directory: python tools/b2_theory_diagrams.py
New/replaced scenes use excalidraw_gen. Other historical manual scenes retain
all geometry, with targeted content repairs and styles synchronized to the SVG.
Manual .excalidraw files remain editable sources of truth after generation.
"""
from __future__ import annotations

import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from excalidraw_gen import D, E, N, write

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Chapter 0 - Previous Year Questions/2nd Batch/Theory/diagrams"
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


def box(id, text, x, y, w=320, h=80, color="blue", size=17):
    return N(id, text, x, y, w, h, color, size=size)


def emit(d):
    """Use the shared engine, correcting multiline text bounds locally."""
    assert all(not e.label for e in d.edges), "Put decisions in nodes in both formats"
    write(d, OUT)
    path = OUT / (d.key + ".excalidraw")
    scene = json.loads(path.read_text(encoding="utf-8"))
    by_id = {e["id"]: e for e in scene["elements"]}
    for text in scene["elements"]:
        if text["type"] != "text" or not text.get("containerId"):
            continue
        shape = by_id[text["containerId"]]
        text["height"] = len(text["text"].splitlines()) * text["fontSize"] * text["lineHeight"]
        text["y"] = shape["y"] + (shape["height"] - text["height"]) / 2
        assert text["height"] <= shape["height"] - 8, (d.key, text["text"])
    path.write_text(json.dumps(scene, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def missing_diagrams():
    yield D("b2-theory-15-time-space", "Q1(a): Time and memory measure different resources", (1040, 540), [
        box("in", "Input: n array entries\nInput storage: Θ(n)", 40, 90, 280, 100),
        box("steps", "Algorithm operations\nOne scan: Θ(n) time", 380, 90, 280, 100),
        box("out", "Result\nTime counts operations", 720, 90, 280, 100, "green"),
        box("merge", "Merge sort\nTemporary array: Θ(n)\nStack: Θ(log n)", 40, 270, 280, 120),
        box("heap", "Iterative heap sort\nAuxiliary space: Θ(1)\nInput still occupies Θ(n)", 380, 270, 280, 120, "green"),
        box("total", "Total space\n= input + auxiliary\nAuxiliary includes stack", 720, 270, 280, 120, "yellow"),
        box("limit", "Input fits, copy does not: consider in-place sorting. Input does not fit: external-memory sorting.", 40, 440, 960, 60, "gray", 16),
    ], [E("in", "steps", route="h"), E("steps", "out", route="h")])

    yield D("b2-theory-16-design-paradigms", "Q1(b): Divide and conquer versus a safe greedy choice", (1040, 660), [
        box("root", "D&C: merge sort\nSplit the array", 100, 90, 350),
        box("left", "Sort left half", 40, 250, 230), box("right", "Sort right half", 310, 250, 230),
        box("merge", "Merge sorted halves", 100, 420, 350, 80, "green"),
        box("act", "Greedy: unweighted activities\n[0,3), [1,2), [2,4)", 620, 90, 380),
        box("pick", "Choose earliest finish: [1,2)\nDiscard incompatible [0,3)", 620, 250, 380),
        box("next", "Choose compatible [2,4)\n2 activities; choices are final", 620, 420, 380, 80, "green"),
        box("why", "D&C combines solved parts. Greedy needs a proof that each irreversible choice is safe.", 40, 560, 960, 60, "yellow", 16),
    ], [E("root", "left"), E("root", "right"), E("left", "merge"), E("right", "merge"), E("act", "pick"), E("pick", "next")])

    nodes = []
    for i, (rec, levels, depth, ans) in enumerate([
        ("2T(n/2) + n", "Level i: 2^i × n/2^i = n", "Θ(log n) levels", "Θ(n log n)"),
        ("T(n−1) + 1", "Each non-base level costs 1", "n−1 non-base levels", "Θ(n)"),
        ("4T(n/2) + n²", "Level i: 4^i × (n/2^i)² = n²", "Θ(log n) levels", "Θ(n² log n)"),
        ("T(n/3) + log n", "Costs: log n, log n−log 3, …", "Θ(log n) terms; arithmetic sum", "Θ(log² n)"),
    ]):
        nodes.extend([box(f"r{i}", rec, 40 + i * 300, 100, 275, 70),
                      box(f"l{i}", levels + "\n" + depth, 40 + i * 300, 250, 275, 100, "yellow", 14),
                      box(f"a{i}", ans, 40 + i * 300, 440, 275, 70, "green")])
    yield D("b2-theory-17-recurrences", "Q1(c): Sum the work over recursion levels", (1240, 610), nodes + [
        box("base", "Constant positive base cases. Master Cases 1/3 require a polynomial gap; Case 3 also needs regularity.", 40, 540, 1175, 45, "gray", 15)
    ], [e for i in range(4) for e in (E(f"r{i}", f"l{i}"), E(f"l{i}", f"a{i}"))])

    vals = [102, 205, 307, 409, 511, 613, 715, 817]
    nodes = [box(f"a{i}", str(v), 40 + i * 115, 110, 100, 60, "green" if v == 511 else "blue") for i, v in enumerate(vals)]
    nodes += [box("find", "SEARCH: is 511 present?\nCan stop after finding index 4", 90, 260, 390, 95, "green"),
              box("visit", "TRAVERSE: process every entry\nContinue through index 7", 570, 260, 390, 95),
              box("overlap", "A traversal may implement a search. BFS/DFS from one source visits only reachable vertices.", 40, 440, 920, 65, "yellow", 16)]
    yield D("b2-theory-18-search-traverse", "Q3(a): Searching has a target; traversal covers the collection", (1000, 560), nodes,
            [E("a4", "find"), E("a7", "visit")])

    yield D("b2-theory-19-search-trace", "Q3(b): Find 511 in a sorted eight-entry array", (1060, 760), [
        box("array", "Index:    0       1       2       3       4       5       6       7\nValue: 102   205   307   409   511   613   715   817", 40, 80, 980, 90, "gray"),
        box("linear", "LINEAR: 102 → 205 → 307 → 409 → 511\n5 inspected entries; found at index 4", 40, 230, 470, 100),
        box("b1", "BINARY #1: lo=0, hi=7\nmid=3; value 409 < 511 → lo=4", 570, 230, 450, 85),
        box("b2", "BINARY #2: lo=4, hi=7\nmid=5; value 613 > 511 → hi=4", 570, 385, 450, 85),
        box("b3", "BINARY #3: lo=4, hi=4\nmid=4; value 511 → found", 570, 540, 450, 85, "green"),
        box("count", "One three-way comparison per entry\nLinear: 5; binary: 3\nSeparate == then <: binary uses 5 predicates\nWorst binary target here: 817, 4 probes", 40, 420, 470, 180, "yellow", 16),
        box("mid", "Zero-based indices; mid = floor((lo+hi)/2). Sorted random access is required for binary search.", 40, 670, 980, 50, "gray", 16),
    ], [E("b1", "b2"), E("b2", "b3")])

    bubble = ["[2,3,4,5,6,1,7]", "[2,3,4,5,1,6,7]", "[2,3,4,1,5,6,7]", "[2,3,1,4,5,6,7]", "[2,1,3,4,5,6,7]", "[1,2,3,4,5,6,7]"]
    nodes = [box("input", "Illustrative input: [2,3,4,5,6,7,1] — six inversions", 40, 75, 960, 60, "gray"),
             box("insert", "INSERTION SORT\nFirst five insertions: 5 comparisons\nInsert 1: 6 comparisons, 6 shifts\nTotal: 11 key comparisons", 40, 220, 430, 180),
             box("result", "[1,2,3,4,5,6,7]\nΘ(n + inversions) work", 40, 510, 430, 100, "green"),
             box("rule", "BUBBLE: left-to-right passes\n1 moves left only once per pass", 560, 165, 440, 75, "yellow")]
    nodes += [box(f"p{i}", f"Pass {i+1}: {bubble[i]}\n{6-i} key comparisons; 1 swap", 560, 275 + 95 * i, 440, 65, "green" if i == 5 else "blue", 16) for i in range(6)]
    nodes += [box("sum", "Bubble total: 6+5+4+3+2+1 = 21 key comparisons, 6 swaps. Early exit never triggers here.", 40, 875, 960, 60, "yellow", 16)]
    yield D("b2-theory-20-insertion-bubble", "Q4(a): A small trailing key separates insertion and bubble sort", (1040, 980), nodes,
            [E("insert", "result")] + [E(f"p{i}", f"p{i+1}") for i in range(5)])

    yield D("b2-theory-21-greedy-proof", "Q5(a): Prove the choice safe, then solve the residual problem", (1040, 640), [
        box("o", "Take an optimal solution O", 40, 110, 280, 100),
        box("swap", "Exchange in greedy choice g\nwithout worsening the objective", 370, 110, 300, 100, "yellow", 15),
        box("safe", "An optimum contains g\nGreedy-choice property", 720, 110, 280, 100, "green", 16),
        box("res", "Solve the residual instance optimally\nOptimal substructure + induction", 380, 320, 450, 100, "green"),
        box("bad", "COUNTEREXAMPLE: unlimited coins {4,3,1}, amount 6\nLargest-first: 4+1+1 (3 coins). Optimum: 3+3 (2 coins).\nOptimal substructure alone does not justify largest-first.", 40, 490, 960, 110, "red", 17),
    ], [E("o", "swap", route="h"), E("swap", "safe", route="h"), E("safe", "res")])

    yield D("b2-theory-22-fractional-knapsack", "Q5(b): Fractional fill, capacity 50", (1040, 620), [
        box("ratios", "Items (weight, value): 1=(10,60), 2=(20,100), 3=(30,120)\nRatios v/w: 6 > 5 > 4; fill in order 1, 2, 3", 40, 85, 960, 90, "gray"),
        box("i1", "Item 1: all\n10 weight\n60 value", 40, 250, 192, 120, "blue"),
        box("i2", "Item 2: all\n20 weight\n100 value", 232, 250, 384, 120, "teal"),
        box("i3", "Item 3: 2/3\n20 weight\n80 value", 616, 250, 384, 120, "green"),
        box("sum", "Weight: 10+20+20 = 50\nValue: 60+100+80 = 240 (optimal)", 250, 440, 540, 95, "green"),
        box("why", "Exchange lower-ratio weight for available higher-ratio weight: value cannot decrease.", 40, 555, 960, 40, "yellow", 16),
    ])

    fib = [0, 1, 1, 2, 3, 5]
    nodes = [box(f"f{i}", f"F({i}) = {fib[i]}", 40 + i * 160, 390, 140, 65, "green") for i in range(6)]
    nodes += [box("call", "Naive F(5): 15 calls total\nF(3) twice; F(2) three times\nF(1) five times; F(0) three times", 40, 100, 450, 140),
              box("cache", "DP: one stored answer per index\nBase cases F(0)=0, F(1)=1\nF(i)=F(i−1)+F(i−2)", 550, 100, 450, 140, "yellow"),
              box("cost", "Unit-cost arithmetic: Θ(n) time; Θ(n) table words, or Θ(1) words retaining only two values.", 40, 545, 960, 65, "gray", 16)]
    edges = [E(f"f{i-1}", f"f{i}", route="h") for i in range(2, 6)]
    edges += [E(f"f{i-2}", f"f{i}", pts=[(110+(i-2)*160,390),(110+(i-2)*160,285+20*(i-2)),(110+i*160,285+20*(i-2)),(110+i*160,390)]) for i in range(2, 6)]
    yield D("b2-theory-23-fibonacci-dp", "Q6(a): Reuse Fibonacci states instead of recomputing calls", (1040, 660), nodes, edges)

    yield D("b2-theory-24-decision-optimization", "Q8(a): TSP thresholds versus an optimal tour", (1040, 650), [
        box("inst", "Same four-city TSP instance\nFeasible tour costs are integers", 300, 80, 440, 85),
        box("dec", "DECISION\nIs there a tour costing at most k?\nk=96: NO; k=97: YES", 40, 265, 440, 130),
        box("opt", "OPTIMIZATION\nMinimum value: 97\nWitness: 0 → 1 → 2 → 3 → 0", 560, 265, 440, 130, "green"),
        box("oracle", "Integer bounds + decision queries → binary search for the optimum VALUE\nRecovering an actual tour needs additional self-reduction queries.", 40, 485, 960, 110, "yellow", 17),
    ], [E("inst", "dec"), E("inst", "opt"), E("dec", "oracle"), E("opt", "oracle")])


def roadmap_diagram():
    """Group the entire paper by section without inventing prerequisite edges."""
    nodes = [
        box("section-a", "SECTION A — Q1 to Q4", 40, 85, 520, 55, "gray", 20),
        box("section-b", "SECTION B — Q5 to Q8", 620, 85, 520, 55, "gray", 20),
    ]
    topics = [
        ("q1", "Q1 — Design and analysis\n(a) Time, total space, auxiliary space\n(b) Divide and conquer; greedy\n(c) Tight recurrence bounds", 40, 180, "blue"),
        ("q2", "Q2 — Complexity classes and graphs\n(a) NP, NP-hard, NP-complete\n(b) BFS shortest paths\n(c) Activity DAG; topological orders", 40, 380, "blue"),
        ("q3", "Q3 — Searching and matrix multiplication\n(a) Searching versus traversing\n(b) Linear and binary search\n(c) Strassen's seven-product method", 40, 580, "blue"),
        ("q4", "Q4 — Sorting\n(a) Insertion versus bubble sort\n(b) Lomuto quicksort partitions\n(c) Merge-sort splits and merges", 40, 780, "blue"),
        ("q5", "Q5 — Greedy algorithms\n(a) Safe choices; exchange proofs\n(b) Fractional knapsack\n(c) Kruskal's minimum spanning tree", 620, 180, "yellow"),
        ("q6", "Q6 — Dynamic programming\n(a) Fibonacci; overlapping subproblems\n(b) Floyd–Warshall intermediate matrices\n(c) LCS table and traceback", 620, 380, "green"),
        ("q7", "Q7 — State-space search\n(a) Graph colouring: backtracking\n(b) Knapsack: best-first branch and bound\n(c) Five queens: backtracking", 620, 580, "violet"),
        ("q8", "Q8 — Optimization and exact methods\n(a) Decision versus optimization\n(b) Job sequencing: depth-first B&B\n(c) TSP: Held–Karp subset DP", 620, 780, "orange"),
    ]
    nodes += [box(id, label, x, y, 520, 160, color, 17) for id, label, x, y, color in topics]
    nodes += [
        box("connections", "SPECIFIC CONNECTIONS, NOT A PREREQUISITE CHAIN\nQ5(b) fractional relaxation supplies Q7(b)'s upper bound.\nQ6's DP paradigm is used in Q8(c); Q2(a)'s classes connect with Q8(a).", 40, 990, 1100, 110, "teal", 17),
        box("distinct", "Q1's analysis tools apply throughout. Greedy, DP, and backtracking are distinct strategies.\nQ7(b) and Q8(b) use bounds; Q7(a)/(c) undo infeasible choices by backtracking.", 40, 1135, 1100, 80, "gray", 16),
    ]
    return D("b2-theory-25-paper-roadmap", "Full-paper topic roadmap — grouping, not prerequisites", (1180, 1260), nodes)


def kruskal_mst_diagram():
    """Draw the exact weighted graph and MST shown in the supplied paper."""
    positions = {"5": (70, 280), "4": (280, 100), "1": (280, 400),
                 "3": (590, 100), "2": (590, 400), "6": (850, 250)}
    nodes = [N(v, v, x, y, 60, 60, "blue", "ellipse", 18)
             for v, (x, y) in positions.items()]
    selected = {frozenset(edge) for edge in [(5, 1), (4, 1), (1, 2), (3, 2), (2, 6)]}
    edges_and_labels = [
        (("5", "4", 9), (165, 160)), (("5", "1", 1), (165, 360)),
        (("4", "1", 1), (300, 250)), (("4", "3", 5), (435, 75)),
        (("4", "2", 3), (445, 240)), (("1", "2", 2), (435, 420)),
        (("3", "2", 3), (610, 250)), (("3", "6", 8), (755, 155)),
        (("2", "6", 7), (755, 355)),
    ]
    edges = []
    for i, ((u, v, weight), (x, y)) in enumerate(edges_and_labels):
        color = "#2f9e44" if frozenset((int(u), int(v))) in selected else "#868e96"
        edges.append(E(u, v, directed=False, color=color, route="straight"))
        nodes.append(box(f"weight{i}", str(weight), x, y, 34, 28,
                         "green" if color == "#2f9e44" else "gray", 15))
    nodes += [
        box("sorted", "Sort by weight. Take (5,1), (4,1), (1,2); skip (4,2) (cycle).", 35, 500, 970, 55, "yellow", 16),
        box("steps", "Take (3,2); skip (4,3); take (2,6). Stop after 5 edges.", 35, 570, 970, 55, "teal", 16),
        box("result", "MST: (5,1), (4,1), (1,2), (3,2), (2,6)     Total weight = 14", 35, 640, 970, 55, "green", 16),
    ]
    return D("b2-theory-07-kruskal-mst", "Q5(c): Kruskal MST on the graph shown in the paper", (1040, 730), nodes, edges)


def repaired_diagrams():
    nodes = [N(k, f"{k}\nd={dist}", x, y, 90, 80, "green" if k in "SACE" else "blue", "ellipse", 17)
             for k, dist, x, y in [("S",0,40,235),("A",1,280,95),("B",1,280,375),("C",2,530,95),("D",2,530,375),("E",3,780,235)]]
    nodes += [box("given", "Illustrative UNDIRECTED graph; neighbours processed alphabetically", 40, 555, 880, 55, "gray", 16),
              box("path", "Green edges: S–A–C–E, distance 3. All seven edges have unit length.\nBFS tree also includes S–B and B–D; cross edges are dashed.", 40, 645, 880, 90, "yellow", 16)]
    edges = [E(a,b,route="straight",directed=False,color="#2f9e44" if (a,b) in [("S","A"),("A","C"),("C","E")] else "#343a40",dashed=(a,b) in [("B","C"),("D","E")])
             for a,b in [("S","A"),("S","B"),("A","C"),("B","C"),("B","D"),("C","E"),("D","E")]]
    yield D("b2-theory-02-bfs-graph", "Q2(b): BFS levels and a shortest path from S", (960, 780), nodes, edges)

    acts = ["Wake up", "Brush teeth", "Take breakfast", "Go to class", "Study in library", "Do homework", "Sleep"]
    nodes = [box("left", "Six dependencies from the paper", 40, 80, 400, 60, "yellow", 17),
             box("right", "REPLACE the last two edges", 540, 80, 400, 60, "yellow", 17)]
    for side, names in [("a",acts),("b",acts[:5]+["Sleep","Do homework"])]:
        nodes += [box(f"{side}{i}", name, 40 if side == "a" else 540, 180 + 95*i, 400, 55, "green" if i >= 5 else "blue") for i,name in enumerate(names)]
    nodes += [box("warning", "Each chain has one topological order. Adding Sleep → Homework without removing\nHomework → Sleep instead creates a 2-cycle: no topological order.", 40, 865, 900, 90, "red", 16)]
    yield D("b2-theory-03-activity-dag", "Q2(c): Paper dependencies and the requested variation", (980, 1000), nodes,
            [E(f"{side}{i}",f"{side}{i+1}") for side in "ab" for i in range(6)])

    nodes = [box("given", "Example instance: W=10; decision order A(4,40), C(3,18), B(6,30), D(5,20)", 30, 70, 1100, 55, "gray", 16),
             box("root", "#1 Root\nw=0, p=0, ub=73", 400, 165, 350, 85),
             box("a1", "#2 A=1\nw=4, p=40, ub=73", 230, 310, 350, 85),
             box("a0", "A=0\nub=52; pruned after best=70", 770, 310, 350, 85, "gray", 16),
             box("c1", "#3 A=1,C=1\nw=7, p=58, ub=73", 30, 465, 350, 85),
             box("c0", "#4 A=1,C=0\nw=4, p=40, ub=70", 610, 465, 350, 85),
             box("b11", "A=1,C=1,B=1\nw=13, p=88: infeasible", 30, 655, 265, 85, "red", 16),
             box("b10", "A=1,C=1,B=0\nub=70; later pruned", 315, 655, 265, 85, "gray", 16),
             box("b01", "A=1,C=0,B=1\nw=10, p=70, D=0: BEST", 610, 655, 265, 85, "green", 16),
             box("b00", "A=1,C=0,B=0\nub=60; pruned", 895, 655, 265, 85, "gray", 16),
             box("policy", "#1–#4 = actual expansions, largest ub first; equal bounds use FIFO insertion order.\nInclude child first. Feasible partial selections update the incumbent: 0 → 40 → 58 → 70.\nA=1,C=0 entered the queue before A=1,C=1,B=0; neither tied node is expanded after best=70.", 30, 820, 1130, 120, "yellow", 16)]
    yield D("b2-theory-11-lc-knapsack-tree", "Q7(b): Best-first branch and bound with reproducible ties", (1190, 990), nodes,
            [E(a,b,route="straight") for a,b in [("root","a1"),("root","a0"),("a1","c1"),("a1","c0"),("c1","b11"),("c1","b10"),("c0","b01"),("c0","b00")]])


def write_manual_scene(path, scene):
    """Keep the original manual sources' compact, one-element-per-line format."""
    lines = ["{"]
    for key, value in scene.items():
        if key == "elements":
            lines.append('  "elements": [')
            lines.extend("    " + json.dumps(e, ensure_ascii=False, separators=(",", ":")) + ("," if i < len(value)-1 else "") for i, e in enumerate(value))
            lines.append("  ],")
        else:
            suffix = "" if key == "files" else ","
            lines.append("  " + json.dumps(key) + ": " + json.dumps(value, ensure_ascii=False) + suffix)
    lines.append("}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def patch_manual(key, changes, footer_positions=None, height=None):
    """Patch paired text without regenerating manually laid-out scenes."""
    path = OUT / (key + ".excalidraw")
    scene = json.loads(path.read_text(encoding="utf-8"))
    svg_path = path.with_suffix(".svg")
    tree = ET.parse(svg_path)
    svg = tree.getroot()
    for old, new in changes:
        for e in scene["elements"]:
            if e["type"] == "text" and (old in e["text"] or new in e["text"]):
                center = e["x"] + e["width"] / 2
                e["text"] = e["text"].replace(old, new)
                e["originalText"] = e["text"]
                e["width"] = max(map(len, e["text"].splitlines())) * e["fontSize"] * 0.6
                e["x"] = center - e["width"] / 2
        for text in svg.iter(f"{{{NS}}}text"):
            if old in "".join(text.itertext()) or new in "".join(text.itertext()):
                text.text = "".join(text.itertext()).replace(old, new)
                for child in list(text):
                    text.remove(child)
    if footer_positions:
        for text, cy in footer_positions.items():
            for e in scene["elements"]:
                if e.get("text") == text:
                    e["y"] = cy - e["height"] / 2
            for e in svg.iter(f"{{{NS}}}text"):
                if "".join(e.itertext()) == text:
                    e.set("y", str(cy))
    if height:
        svg.set("height", str(height))
        vb = svg.attrib["viewBox"].split()
        vb[3] = str(height)
        svg.set("viewBox", " ".join(vb))
        for background in svg.findall(f"{{{NS}}}rect"):
            if background.get("x") is None and background.get("width") == svg.get("width"):
                background.set("height", str(height))
    write_manual_scene(path, scene)
    tree.write(svg_path, encoding="unicode")


def patch_lcs_arrows(key, x="AGGTAB", y="GXTXAYB"):
    """Add the chapter's arrow (diag/up/left, ties up) to every DP cell with i, j >= 1."""
    c = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    arrows = {}
    for i, a in enumerate(x, 1):
        for j, b in enumerate(y, 1):
            if a == b:
                c[i][j], arrows[i, j] = c[i-1][j-1] + 1, "\u2196"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j], arrows[i, j] = c[i-1][j], "\u2191"
            else:
                c[i][j], arrows[i, j] = c[i][j-1], "\u2190"
    path = OUT / (key + ".excalidraw")
    scene = json.loads(path.read_text(encoding="utf-8"))
    tree = ET.parse(path.with_suffix(".svg"))
    for e in scene["elements"]:
        if e["type"] != "text" or not e.get("containerId") or not e["text"].isdigit():
            continue
        col, row = round((e["x"] + e["width"] / 2 - 153) / 66), round((e["y"] - 130) / 40)
        if row >= 1 and col >= 1:
            assert int(e["text"]) == c[row][col], (key, row, col)
            center = e["x"] + e["width"] / 2
            e["text"] = e["originalText"] = f"{c[row][col]} {arrows[row, col]}"
            e["width"] = 34
            e["x"] = center - 17
    for text in tree.getroot().iter(f"{{{NS}}}text"):
        if not (text.text or "").isdigit() or text.get("x") is None:
            continue
        col, row = (float(text.get("x")) - 153) / 66, (float(text.get("y")) - 140) / 40
        if abs(col - round(col)) < .01 and abs(row - round(row)) < .01 and round(row) >= 1 and round(col) >= 1:
            assert int(text.text) == c[round(row)][round(col)], (key, row, col)
            text.text = f"{text.text} {arrows[round(row), round(col)]}"
    write_manual_scene(path, scene)
    tree.write(path.with_suffix(".svg"), encoding="unicode")


def synchronize_manual_styles(key):
    """Historical SVGs carried colours/dashes missing from their editable scenes."""
    path = OUT / (key + ".excalidraw")
    scene = json.loads(path.read_text(encoding="utf-8"))
    svg = ET.parse(path.with_suffix(".svg")).getroot()
    svg_lines = list(svg.iter(f"{{{NS}}}polyline"))
    scene_lines = [e for e in scene["elements"] if e["type"] in ("arrow", "line")]
    assert len(svg_lines) == len(scene_lines), key
    for e, line in zip(scene_lines, svg_lines):
        actual = [(e["x"]+q[0], e["y"]+q[1]) for q in e["points"]]
        expected = [tuple(map(float, pt.split(","))) for pt in line.attrib["points"].split()]
        assert len(actual) == len(expected) and all(abs(x-u)<0.1 and abs(y-v)<0.1 for (x,y),(u,v) in zip(actual,expected)), (key,e["id"])
        e["strokeColor"] = line.get("stroke", "#1e1e1e")
        width = float(line.get("stroke-width", "2"))
        e["strokeWidth"] = int(width) if width.is_integer() else width
        e["strokeStyle"] = "dashed" if line.get("stroke-dasharray") else "solid"
    write_manual_scene(path, scene)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--roadmap-only", action="store_true", help="Write only the full-paper roadmap pair")
    args = parser.parse_args()
    emit(roadmap_diagram())
    if args.roadmap_only:
        print("Wrote the full-paper roadmap pair; subquestion visuals were not touched.")
        return
    for d in [*missing_diagrams(), kruskal_mst_diagram(), *repaired_diagrams()]:
        emit(d)
    first = "P ⊆ NP; NP-complete = NP ∩ NP-hard."
    second = "NP-hard need not be in NP; TSP optimization is NP-hard."
    third = "Shown under P ≠ NP (unproved): P and NP-complete are then disjoint."
    patch_manual("b2-theory-01-np-classes-venn", [
        ("P is inside NP. NP-complete = NP and NP-hard together (the hardest problems in NP).", first),
        ("NP-hard problems need not be in NP (for example, optimization versions of NP-complete problems).", second),
        ("Picture assumes P is not equal to NP (not proven), so P and NP-complete do not overlap.", third),
    ], {first:460, second:490, third:520}, 550)
    patch_manual("b2-theory-05-quicksort-partition", [
        ("Pivot = 1005 → [1005, 1010, 1023]", "1005 → [1005, 1010, 1023]"),
    ])
    patch_manual("b2-theory-06-mergesort-tree", [
        ("Black arrows = divide (split in half).   Green arrows = merge (combine two sorted lists).", "Black arrows divide (extra entry left); green arrows merge sorted lists."),
    ])

    patch_manual("b2-theory-10-colouring-tree", [
        ("Step 4: v4 touches only v3, so v4 = Red is tried first.", "Step 4: only v3 is already coloured next to v4; try Red first."),
        ("Graph (5 vertices)", "Illustrative graph (5 vertices)"),
    ], height=575)
    patch_manual("b2-theory-12-nqueens-tree", [
        ("Row 4: no safe column ✗", "Row 4: none safe ✗"),
        ("The search finds all 10 solutions for N = 5. The tree shows the first two and one dead end.", "Enumeration: 10 boards (2 symmetry classes). Only two solutions and a later dead end shown."),
    ])
    patch_manual("b2-theory-14-tsp-subsets", [
        ("Q8(c): TSP by DP over Subsets (Held-Karp)", "Q8(c): Held-Karp DP, start at city 0"),
        ("g(i, S) = cheapest path that starts at i, visits every city in S once, and ends at city 1.", "g(i,S) starts at i, visits S once, then returns to city 0."),
        ("g(2, ∅) = 20", "g(1, ∅) = 20"),
        ("g(3, ∅) = 42", "g(2, ∅) = 42"),
        ("g(4, ∅) = 35", "g(3, ∅) = 35"),
        ("g(2, {3}) = 72", "g(1, {2}) = 72"),
        ("g(2, {4}) = 69", "g(1, {3}) = 69"),
        ("g(3, {2}) = 50", "g(2, {1}) = 50"),
        ("g(3, {4}) = 47", "g(2, {3}) = 47"),
        ("g(4, {2}) = 54", "g(3, {1}) = 54"),
        ("g(4, {3}) = 54", "g(3, {2}) = 54"),
        ("g(2, {3,4}) = 77", "g(1, {2,3}) = 77"),
        ("g(3, {2,4}) = 66", "g(2, {1,3}) = 66"),
        ("g(4, {2,3}) = 62", "g(3, {1,2}) = 62"),
        ("g(1, {2,3,4}) = min(20+77, 42+66, 35+62) = 97", "g(0, {1,2,3}) = min(20+77, 42+66, 35+62) = 97"),
        ("Green paths: 1→2→3→4→1 = 20 + 30 + 12 + 35 = 97,   and   1→4→3→2→1 = 35 + 12 + 30 + 20 = 97.", "Green paths: 0→1→2→3→0 = 20 + 30 + 12 + 35 = 97,   and   0→3→2→1→0 = 35 + 12 + 30 + 20 = 97."),
    ])
    patch_manual("b2-theory-08-floyd-warshall", [
        ("D0 (start)", "D(0) (start)"),
        ("D2 (after k = 2)", "D(2) (after k = 2)"),
        ("D4 = D3 (final)", "D(4) = D(3) (final)"),
    ])
    patch_manual("b2-theory-09-lcs-table", [
        ("Rule: letters match \u2192 diagonal cell + 1.   Letters differ \u2192 larger of the cell above or left.",
         "c[i,j]: match \u2192 \u2196 c[i-1,j-1] + 1; differ \u2192 larger of \u2191 above and \u2190 left (tie: \u2191)."),
        ("Traceback from (6,7): B, A, T, G.", "Traceback from c[6,7]: B, A, T, G."),
    ])
    patch_lcs_arrows("b2-theory-09-lcs-table")
    patch_manual("b2-theory-13-bnb-job-tree", [
        ("Q8(b): Branch and Bound for Job Sequencing (maximize profit)", "Q8(b): Example Job Sequencing — Depth-First B&B"),
        ("ub = profit so far + profit of every undecided job (admissible: never below the true best).", "Include first; update best only at feasible leaves. ub = profit + all undecided profits."),
    ])
    repaired = {d.key for d in repaired_diagrams()} | {kruskal_mst_diagram().key}
    for path in sorted(OUT.glob("b2-theory-*.excalidraw")):
        if int(path.stem.split("-")[2]) <= 14 and path.stem not in repaired:
            synchronize_manual_styles(path.stem)
    print("Wrote 10 new subquestion pairs and the roadmap, corrected the source-graph MST, replaced 3 other pairs, and repaired retained manual scene content/styles.")


if __name__ == "__main__":
    main()
