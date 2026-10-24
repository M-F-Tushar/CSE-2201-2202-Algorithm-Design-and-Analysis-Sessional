"""Generate diagrams for the CSE 2201 Class Test 03 answers.

Run from any directory: python tools/ct3_diagrams.py
Every diagram is written as an SVG preview and editable Excalidraw scene.
"""
from __future__ import annotations

import json
from pathlib import Path

from excalidraw_gen import D, E, N, write
from verify_ct3 import MAX_ARRAY, SEGMENT_ARRAY, build_segment_tree, divide_conquer_max_subarray

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Chapter 0 - Previous Year Questions/3rd Batch/CT/diagrams"
GREEN, RED = "#2f9e44", "#e03131"


def box(id, text, x, y, w=130, h=58, color="blue", size=15):
    return N(id, text, x, y, w, h, color, size=size)


def emit(scene):
    write(scene, OUT)
    path = OUT / (scene.key + ".excalidraw")
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {element["id"]: element for element in data["elements"]}
    for text in data["elements"]:
        if text["type"] != "text" or not text.get("containerId"):
            continue
        shape = by_id[text["containerId"]]
        text["height"] = len(text["text"].splitlines()) * text["fontSize"] * text["lineHeight"]
        text["y"] = shape["y"] + (shape["height"] - text["height"]) / 2
        assert text["height"] <= shape["height"] - 8, (scene.key, text["text"])
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def union_by_rank():
    nodes, edges = [], []
    bad_positions = {str(i): (155, 98 + (i - 1) * 63) for i in range(1, 9)}
    for i, (x, y) in bad_positions.items():
        nodes.append(box(f"naive{i}", i, x, y, 64, 44, "red", 16))
    for i in range(1, 8):
        edges.append(E(f"naive{i}", f"naive{i+1}", color=RED, route="straight"))

    ranked_positions = {
        "1": (840, 105), "2": (650, 245), "3": (840, 245), "5": (1030, 245),
        "4": (840, 385), "6": (960, 385), "7": (1100, 385), "8": (1100, 525),
    }
    ranks = {"1": 3, "2": 0, "3": 1, "4": 0, "5": 2, "6": 0, "7": 1, "8": 0}
    for value, (x, y) in ranked_positions.items():
        nodes.append(box(f"ranked{value}", f"{value}\nr={ranks[value]}", x, y, 76, 54,
                         "green" if value == "1" else "blue", 15))
    for parent, child in [("1", "2"), ("1", "3"), ("3", "4"), ("1", "5"), ("5", "6"), ("5", "7"), ("7", "8")]:
        edges.append(E(f"ranked{parent}", f"ranked{child}", color=GREEN, route="straight"))

    nodes.extend([
        box("badTitle", "Naïve union order can make a chain", 70, 42, 450, 45, "red", 17),
        box("goodTitle", "Union by rank keeps the tree shallow", 600, 42, 590, 45, "green", 17),
        box("badHeight", "8 elements: height 7", 55, 625, 430, 48, "red", 16),
        box("goodHeight", "8 elements: height 3; root rank 3", 600, 625, 590, 48, "green", 16),
    ])
    return D("ct3-01-union-by-rank", "Q1: Union by rank limits DSU tree height", (1260, 710), nodes, edges)


def maximum_subarray():
    best, records = divide_conquer_max_subarray(MAX_ARRAY)
    nodes, edges = [], []

    def add(left, right, depth):
        ident = f"seg{left}_{right}"
        x = 60 + (left + right + 1) * 80
        y = 100 + depth * 128
        details = records[left, right]
        if left == right:
            value = details["best"][0]
            label = f"A[{left}] = {MAX_ARRAY[left]}\nbest = {value}"
            color = "gray"
        else:
            lval = details["left"][0]
            rval = details["right"][0]
            xval, _xs, _xe = details["cross"]
            value, start, end = details["best"]
            label = f"A[{left}..{right}]\nL={lval} R={rval} X={xval}\nbest={value} [{start}..{end}]"
            color = "green" if details["best"] == details["cross"] else "blue"
        nodes.append(box(ident, label, x - 70, y, 140, 82, color, 14))
        if left != right:
            mid = (left + right) // 2
            lchild, rchild = add(left, mid, depth + 1), add(mid + 1, right, depth + 1)
            edges.extend([E(ident, lchild, route="straight"), E(ident, rchild, route="straight")])
        return ident

    add(0, len(MAX_ARRAY) - 1, 0)
    nodes.append(box("explanation", "At each split: best = max(best-left, best-right, best-crossing).\n"
                                    "The root's crossing sum is suffix [3..3] = 4 plus prefix [4..6] = 2, giving 6.",
                     50, 635, 1260, 68, "yellow", 15))
    nodes.append(box("result", "Maximum sum = 6, from indices 3..6: [4, −1, 2, 1].\n"
                               "Each crossing scan costs Θ(n); T(n)=2T(n/2)+Θ(n)=Θ(n log n).",
                     200, 720, 960, 62, "green", 15))
    assert best == (6, 3, 6)
    return D("ct3-02-maximum-subarray", "Q2: Divide-and-conquer maximum-subarray recursion", (1370, 815), nodes, edges)


def segment_tree():
    tree, intervals = build_segment_tree(SEGMENT_ARRAY)
    query_left, query_right = 2, 6
    full = {(2, 3), (4, 5), (6, 6)}
    nodes, edges = [], []

    def add(node):
        left, right = intervals[node]
        ident = f"node{node}"

        center_x = 75 + (left + right) * 75
        depth = (node + 1).bit_length() - 1
        y = 90 + depth * 108
        if (left, right) in full:
            color = "green"
        elif right < query_left or query_right < left:
            color = "gray"
        elif query_left <= left and right <= query_right:
            color = "teal"
        else:
            color = "yellow"
        nodes.append(box(ident, f"node {node}: [{left},{right}]\nsum = {tree[node]}",
                         center_x - 67, y, 134, 68, color, 14))
        if left != right:
            lc, rc = 2 * node + 1, 2 * node + 2
            add(lc)
            add(rc)
            edges.extend([E(ident, f"node{lc}", route="straight"), E(ident, f"node{rc}", route="straight")])

    add(0)
    nodes.append(box("array", "Array indices:  0  1  2  3  4  5  6  7\n"
                               "Array values:   2  1  5  3  4  7  6  8",
                     75, 500, 1180, 58, "gray", 15))
    nodes.append(box("query", "Query [2,6] uses full-cover nodes [2,3]=8, [4,5]=11, [6,6]=6.\n"
                                "Answer = 8 + 11 + 6 = 25. Green = summed; teal = inside green cover; yellow = partial; gray = outside.", 
                     75, 575, 1180, 68, "yellow", 15))
    assert sum(tree[node] for node, span in intervals.items() if span in full) == 25
    return D("ct3-03-segment-tree", "Q3: Segment tree sums and range query [2,6]", (1330, 665), nodes, edges)


def main():
    scenes = [union_by_rank(), maximum_subarray(), segment_tree()]
    for scene in scenes:
        emit(scene)
    print(f"Wrote {len(scenes)} SVG/Excalidraw pairs to {OUT}")


if __name__ == "__main__":
    main()
