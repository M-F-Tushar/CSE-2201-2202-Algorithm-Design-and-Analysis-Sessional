"""Generate diagram pairs for the CSE 2201 Class Test 04 answers.

Run from the repository root: python tools/ct4_diagrams.py
Each hand-laid-out scene is exported as an editable Excalidraw file and an SVG.
"""
from __future__ import annotations

import json
from pathlib import Path

from excalidraw_gen import D, E, N, write

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Chapter 0 - Previous Year Questions/3rd Batch/CT/diagrams"
GREEN, RED = "#2f9e44", "#e03131"


def box(id, text, x, y, w=180, h=60, color="blue", size=15, shape="rect"):
    return N(id, text, x, y, w, h, color, shape, size)


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


def state_space_tree():
    nodes = [
        box("root", "Start\nitems {2, 3}; target 3", 520, 80, 240, 66, "gray", 15),
        box("include2", "Include 2\nsum = 2", 230, 205, 220, 64, "blue", 15),
        box("exclude2", "Exclude 2\nsum = 0", 830, 205, 220, 64, "blue", 15),
        box("include2_include3", "Include 3\n{2, 3}: sum = 5\nnot target", 65, 340, 220, 76, "red", 14),
        box("include2_exclude3", "Exclude 3\n{2}: sum = 2\nnot target", 300, 340, 220, 76, "gray", 14),
        box("exclude2_include3", "Include 3\n{3}: sum = 3\ntarget ✓", 760, 340, 220, 76, "green", 14),
        box("exclude2_exclude3", "Exclude 3\n{}: sum = 0\nnot target", 995, 340, 220, 76, "gray", 14),
        box("role", "Each root-to-leaf path is one subset; all four combinations are shown.\n"
                    "Backtracking explores one path at a time. When a branch cannot lead to a solution,\n"
                    "it undoes the last choice and returns to a sibling instead of continuing down that branch.",
            60, 470, 1155, 110, "yellow", 14),
    ]
    edges = [
        E("root", "include2", route="v"), E("root", "exclude2", route="v"),
        E("include2", "include2_include3", route="v"),
        E("include2", "include2_exclude3", route="v"),
        E("exclude2", "exclude2_include3", route="v"),
        E("exclude2", "exclude2_exclude3", route="v"),
    ]
    return D(
        "ct4-01-state-space-tree",
        "CT4 Q1: Subset-sum choices form a state-space tree",
        (1280, 650), nodes, edges,
        caption="Example: subset sum for {2, 3} with target 3; each level decides whether to include the next item.",
    )


def queen_constraints():
    n, candidate_row, candidate_col = 7, 4, 3
    board_x, board_y, cell, gap = 120, 180, 42, 3
    nodes = [
        box("board_title", "Illustrative 7×7 board", 45, 75, 400, 48, "green", 15),
        box("x_axis", "x-axis: column c (0..6)", board_x, 124, 315, 26, "gray", 13),
        box("y_axis", "y-axis\nrow r\n0..6", 4, 305, 68, 90, "gray", 12),
        box("candidate_title", "Test candidate board[4][3] (zero-based)", 480, 75, 710, 48, "green", 15),
        box("column_check", "1. Same column above:\ninspect board[i][3], for i = 0..3.",
            480, 140, 710, 66, "red", 14),
        box("left_check", "2. Upper-left diagonal:\n(3,2) → (2,1) → (1,0) → stop at edge.",
            480, 218, 710, 66, "orange", 14),
        box("right_check", "3. Upper-right diagonal:\n(3,4) → (2,5) → (1,6) → stop at edge.",
            480, 296, 710, 66, "violet", 14),
        box("occupied", "If any checked cell contains 1, return false.\n"
                         "If all three scans are clear, isSafe returns true.",
            480, 374, 710, 70, "yellow", 14),
        box("row_rule", "Row uniqueness is guaranteed by solve(row):\n"
                         "place one queen, then recurse on row + 1.",
            480, 456, 710, 70, "teal", 14),
        box("legend", "Colored cells are inspected squares, not extra queens.\n"
                       "Rows below 4 are unfilled and are not scanned.",
            480, 538, 710, 70, "gray", 14),
    ]
    for col in range(n):
        nodes.append(box(f"col{col}", str(col), board_x + col * (cell + gap) + 5,
                         board_y - 30, 32, 24, "gray", 12))
    for row in range(n):
        nodes.append(box(f"row{row}", str(row), 76,
                         board_y + row * (cell + gap) + 6, 34, 30, "gray", 12))
        for col in range(n):
            if (row, col) == (candidate_row, candidate_col):
                shade, label = "green", "Q?"
            elif row < candidate_row and col == candidate_col:
                shade, label = "red", "·"
            elif row < candidate_row and col == candidate_col - (candidate_row - row):
                shade, label = "orange", "·"
            elif row < candidate_row and col == candidate_col + (candidate_row - row):
                shade, label = "violet", "·"
            elif row == candidate_row:
                shade, label = "yellow", "·"
            else:
                shade, label = ("white" if (row + col) % 2 else "light"), ""
            nodes.append(box(f"cell{row}_{col}", label,
                             board_x + col * (cell + gap), board_y + row * (cell + gap),
                             cell, cell, shade, 16))

    return D(
        "ct4-02-queen-constraints",
        "CT4 Q2: Column and two upward-diagonal checks",
        (1230, 690), nodes,
        caption="x is column and y is row; the zero-based candidate is tested only against already-filled rows above it.",
    )


def backtracking_applications():
    nodes = [
        box("graph_title", "Application 1: Graph coloring", 62, 78, 570, 54, "violet", 16),
        box("subset_title", "Application 2: Subset sum", 716, 78, 565, 54, "orange", 16),
        box("A", "A\nred", 170, 210, 100, 78, "red", 16, "ellipse"),
        box("B", "B\nblue", 420, 210, 100, 78, "blue", 16, "ellipse"),
        box("C", "C\nred", 420, 400, 100, 78, "red", 16, "ellipse"),
        box("D", "D\nblue", 170, 400, 100, 78, "blue", 16, "ellipse"),
        box("graph_note", "Assign colors one vertex at a time; reject a choice\n"
                          "when an adjacent vertex already has that color.",
            72, 540, 565, 78, "yellow", 14),
        box("sum0", "Start\nsum = 0; next item 3", 895, 165, 205, 68, "gray", 14),
        box("sum3", "Include 3\nsum = 3", 740, 290, 190, 68, "light", 14),
        box("sum0b", "Exclude 3\nsum = 0", 1065, 290, 190, 68, "blue", 14),
        box("sum7", "Include 4\nsum = 7", 740, 405, 190, 68, "light", 14),
        box("sum4", "Include 4\nsum = 4", 1065, 405, 190, 68, "blue", 14),
        box("sum12", "Include 5\nsum = 12 > 9\nprune", 740, 520, 190, 68, "red", 14),
        box("sum9", "Include 5\nsum = 9 = target ✓", 1065, 520, 190, 68, "green", 14),
        box("subset_note", "Set = {3, 4, 5, 7}, target = 9. Prune partial sums above 9.\n"
                           "Red: 3 + 4 + 5 = 12; green path: exclude 3, then 4 + 5 = 9.",
            710, 620, 600, 70, "yellow", 14),
    ]
    edges = [
        E("A", "B", route="straight", directed=False),
        E("B", "C", route="straight", directed=False),
        E("C", "D", route="straight", directed=False),
        E("D", "A", route="straight", directed=False),
        E("sum0", "sum3", route="v"), E("sum0", "sum0b", route="v"),
        E("sum3", "sum7", route="v"), E("sum7", "sum12", color=RED, route="v"),
        E("sum0b", "sum4", route="v"), E("sum4", "sum9", route="v"),
    ]
    return D(
        "ct4-03-backtracking-applications",
        "CT4 Q3: Backtracking applications beyond N-Queens",
        (1340, 730), nodes, edges,
        caption="Both problems build partial assignments and backtrack when a choice cannot complete a valid solution.",
    )


def nqueens_algorithm():
    nodes = [
        box("algorithm_title", "Backtracking algorithm — instruction-style, follows the C++ code", 45, 78, 750, 52, "blue", 16),
        box("algorithm", "1. Read n; fill board[n][n] with 0s.\n"
                        "2. In isSafe(row, col), check the same column above:\n"
                        "   inspect board[i][col] for i = 0..row−1; a 1 means false.\n"
                        "3. Scan upper-right from i = row−1, j = col+1.\n"
                        "   While i ≥ 0 and j < n, check each cell; a 1 means false.\n"
                        "   Otherwise move up-right: i ← i−1, j ← j+1.\n"
                        "4. Scan upper-left from i = row−1, j = col−1.\n"
                        "   While i ≥ 0 and j ≥ 0, check each cell; a 1 means false.\n"
                        "   Otherwise move up-left: i ← i−1, j ← j−1.\n"
                        "   If all three scans are clear, return true.\n"
                        "5. In solve(row), if row == n, return true.\n"
                        "6. Try each col = 0..n−1 in this row.\n"
                        "   If isSafe(row, col) is false, try the next column.\n"
                        "   Otherwise place queen: board[row][col] ← 1.\n"
                        "   Call solve(row + 1); if true, return true.\n"
                        "   If it fails, undo: board[row][col] ← 0; continue.\n"
                        "7. If no column works, return false.\n"
                        "8. Call solve(0); print board if true, else \"No solution\".",
            45, 145, 750, 620, "light", 16),
        box("example_title", "Illustrative first-solution run for n = 4", 835, 78, 715, 52, "green", 16),
        box("trace", "Columns 0..3: [0,2] fails; [0,3,1] fails;\n"
                     "then [1,3,0,2] is the first solution.",
            835, 145, 715, 82, "yellow", 14),
        box("vector", "q[row] = column\n\n"
                      "row 0 → 1\nrow 1 → 3\nrow 2 → 0\nrow 3 → 2\n\n"
                      "return true",
            850, 300, 220, 265, "teal", 15),
        box("result", "First solution: [1, 3, 0, 2]", 835, 590, 715, 52, "green", 16),
        box("notes", "Invariant: rows 0..row−1 already hold one mutually nonattacking queen; isSafe checks every attack direction above.\n"
                      "Worst-case time O(n·n!); board storage Θ(n²), plus Θ(n) recursion-stack space.",
            45, 800, 1505, 80, "yellow", 14),
    ]

    q = [1, 3, 0, 2]
    board_x, board_y, cell, gap = 1150, 315, 58, 2
    nodes.append(box("board_label", "Board coordinates are zero-based", board_x - 20, 250, 300, 30, "gray", 13))
    for col in range(4):
        nodes.append(box(f"bcol{col}", str(col), board_x + col * (cell + gap) + 8,
                         board_y - 30, 42, 26, "gray", 12))
    for row in range(4):
        nodes.append(box(f"brow{row}", str(row), board_x - 42,
                         board_y + row * (cell + gap) + 14, 34, 30, "gray", 12))
        for col in range(4):
            is_queen = q[row] == col
            shade = "green" if is_queen else ("white" if (row + col) % 2 else "light")
            nodes.append(box(f"board{row}_{col}", "Q" if is_queen else "·",
                             board_x + col * (cell + gap),
                             board_y + row * (cell + gap),
                             cell, cell, shade, 19 if is_queen else 16))

    return D(
        "ct4-04-nqueens-algorithm",
        "CT4 Q4: Board-based backtracking algorithm and 4-Queens solution",
        (1600, 920), nodes,
        caption="Rows are filled from 0 to n−1; scanning only upward catches every conflict with an earlier queen.",
    )


DIAGRAMS = [state_space_tree(), queen_constraints(), backtracking_applications(), nqueens_algorithm()]


def main():
    for scene in DIAGRAMS:
        emit(scene)
    print(f"Wrote {len(DIAGRAMS)} CT4 diagram pairs to {OUT}")


if __name__ == "__main__":
    main()
