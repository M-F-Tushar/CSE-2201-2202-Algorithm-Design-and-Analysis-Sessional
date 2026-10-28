"""Independent regression checks for the cumulative CSE 2201 CT1–CT4 answers.

Run from the repository root: python tools/verify_ct3.py
Uses only the Python standard library. Recomputes CT1–CT3 examples and checks
all four tests' question and diagram inventory; verify_ct4.py checks the new
N-Queens solution and CT4 diagram content.
"""
from __future__ import annotations

import json
import math
import re
import unittest
from collections import Counter
from itertools import combinations
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CT = ROOT / "Chapter 0 - Previous Year Questions/3rd Batch/CT"
MAX_ARRAY = [-2, 1, -3, 4, -1, 2, 1, -5]
SEGMENT_ARRAY = [2, 1, 5, 3, 4, 7, 6, 8]
LCS_X, LCS_Y = "AGGTAB", "GXTXAYB"
KNAP_W, KNAP_P, KNAP_CAP = [3, 4, 5, 6], [2, 3, 1, 4], 8
TOPO_VERTICES = [1, 2, 3, 4, 5, 6]
TOPO_EDGES = [(5, 6), (4, 6), (5, 2), (4, 1), (2, 3), (3, 1)]
BF_VERTICES = ["S", "A", "B", "C", "D", "T"]
BF_EDGES = [("S", "A", 5), ("S", "C", -2), ("A", "B", 1), ("C", "A", 2), ("C", "B", 4),
            ("C", "D", 4), ("B", "D", -1), ("B", "T", 3), ("D", "T", 1)]
FW_VERTICES = [1, 2, 3, 4]
FW_EDGES = [(1, 2, 2), (2, 3, 3), (3, 4, 1), (4, 3, 12), (4, 1, 4), (1, 4, 5), (3, 1, 6), (4, 2, 7)]


def dsu_union_by_rank(n, operations):
    parent, rank = list(range(n)), [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for a, b in operations:
        ra, rb = find(a), find(b)
        if ra == rb:
            continue
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
    return parent, rank, find


def dsu_depth(parent, node):
    depth = 0
    while parent[node] != node:
        node = parent[node]
        depth += 1
    return depth


def fib_naive_call_counts(n):
    counts = Counter()

    def fib(k):
        counts[k] += 1
        return k if k < 2 else fib(k - 1) + fib(k - 2)

    fib(n)
    return counts


def fib_tabulation(n):
    values = [0, 1]
    while len(values) <= n:
        values.append(values[-1] + values[-2])
    return values[:n + 1]


def lcs_table(x, y):
    dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    for i, a in enumerate(x, 1):
        for j, b in enumerate(y, 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if a == b else max(dp[i - 1][j], dp[i][j - 1])
    return dp


def lcs_bruteforce(x, y):
    def is_subsequence(candidate, text):
        it = iter(text)
        return all(any(next_char == letter for next_char in it) for letter in candidate)

    common = {"".join(items) for size in range(len(x) + 1) for items in combinations(x, size)
              if is_subsequence(items, y)}
    best = max(map(len, common))
    return best, {candidate for candidate in common if len(candidate) == best}


def knapsack_table(weights, profits, capacity):
    dp = [[0] * (capacity + 1)]
    for weight, profit in zip(weights, profits):
        prev = dp[-1]
        dp.append([max(prev[c], prev[c - weight] + profit) if c >= weight else prev[c]
                   for c in range(capacity + 1)])
    return dp


def lcs_arrows(x, y, dp):
    arrows = [[""] * (len(y) + 1)]
    for i, a in enumerate(x, 1):
        row = [""]
        for j, b in enumerate(y, 1):
            if a == b:
                row.append("nwarrow")
            else:
                row.append("uparrow" if dp[i - 1][j] >= dp[i][j - 1] else "leftarrow")
        arrows.append(row)
    return arrows


def knapsack_arrows(weights, profits, dp):
    arrows = [[""] * len(dp[0])]
    for i, (weight, profit) in enumerate(zip(weights, profits), 1):
        row = [""]
        for c in range(1, len(dp[0])):
            take = c >= weight and dp[i - 1][c - weight] + profit > dp[i - 1][c]
            row.append("nwarrow" if take else "uparrow")
        arrows.append(row)
    return arrows


def split_arrow_grid(grid):
    """Parse cells like `2 (\\nwarrow)`; grid[0] is the header and column 0 is a label."""
    values, arrows = [], []
    for row in grid[1:]:
        parsed = [re.fullmatch(r"(-?\d+)(?: \(\\(\w+)\))?", cell) for cell in row[1:]]
        if not all(parsed):
            raise AssertionError(f"Unparseable cell in {row}")
        values.append([int(m[1]) for m in parsed])
        arrows.append([m[2] or "" for m in parsed])
    return values, arrows


def dfs_finish_stack(vertices, edges):
    adjacency = {v: sorted(b for a, b in edges if a == v) for v in vertices}
    seen, stack = set(), []

    def visit(u):
        seen.add(u)
        for w in adjacency[u]:
            if w not in seen:
                visit(w)
        stack.append(u)

    for v in vertices:
        if v not in seen:
            visit(v)
    return stack


def bellman_ford_selected_rounds(vertices, edges, source, rounds):
    """Per round, the dist array seen just before each vertex's out-edges are relaxed."""
    dist = {v: math.inf for v in vertices}
    dist[source] = 0
    parent = {v: None for v in vertices}
    all_rounds = []
    for _ in range(rounds):
        rows = []
        for u in vertices:
            rows.append([dist[v] for v in vertices])
            for a, b, weight in edges:
                if a == u and dist[a] + weight < dist[b]:
                    dist[b] = dist[a] + weight
                    parent[b] = a
        all_rounds.append(rows)
    return all_rounds, dist, parent


def kahn(vertices, edges):
    indegree = {v: 0 for v in vertices}
    for _, v in edges:
        indegree[v] += 1
    queue = [v for v in vertices if indegree[v] == 0]
    order = []
    while queue:
        u = queue.pop(0)
        order.append(u)
        for a, b in edges:
            if a == u:
                indegree[b] -= 1
                if indegree[b] == 0:
                    queue.append(b)
    return order


def bellman_ford(vertices, edges, source):
    dist = {v: math.inf for v in vertices}
    dist[source] = 0
    parent = {v: None for v in vertices}
    snapshots = [dict(dist)]
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
        snapshots.append(dict(dist))
    negative_cycle = any(dist[u] + weight < dist[v] for u, v, weight in edges)
    return snapshots, parent, negative_cycle


def floyd_warshall(vertices, edges):
    distance = {(u, v): (0 if u == v else math.inf) for u in vertices for v in vertices}
    for u, v, weight in edges:
        distance[u, v] = min(distance[u, v], weight)
    matrices = [dict(distance)]
    for k in vertices:
        distance = {(i, j): min(distance[i, j], distance[i, k] + distance[k, j])
                    for i in vertices for j in vertices}
        matrices.append(dict(distance))
    return matrices


def divide_conquer_max_subarray(values, left=0, right=None, records=None):
    if right is None:
        right = len(values) - 1
    if records is None:
        records = {}
    if left == right:
        result = (values[left], left, right)
        records[left, right] = {"left": result, "right": result, "cross": result, "best": result}
        return result, records
    mid = (left + right) // 2
    best_left, _ = divide_conquer_max_subarray(values, left, mid, records)
    best_right, _ = divide_conquer_max_subarray(values, mid + 1, right, records)
    running, suffix_sum, suffix_start = 0, -math.inf, mid
    for i in range(mid, left - 1, -1):
        running += values[i]
        if running > suffix_sum:
            suffix_sum, suffix_start = running, i
    running, prefix_sum, prefix_end = 0, -math.inf, mid + 1
    for i in range(mid + 1, right + 1):
        running += values[i]
        if running > prefix_sum:
            prefix_sum, prefix_end = running, i
    crossing = (suffix_sum + prefix_sum, suffix_start, prefix_end)
    best = max((best_left, best_right, crossing), key=lambda item: item[0])
    records[left, right] = {"left": best_left, "right": best_right, "cross": crossing, "best": best}
    return best, records


def brute_force_max_subarray(values):
    return max((sum(values[i:j]), i, j - 1)
               for i in range(len(values)) for j in range(i + 1, len(values) + 1))


def build_segment_tree(values):
    tree = [0] * (4 * len(values))
    intervals = {}

    def build(node, left, right):
        intervals[node] = (left, right)
        if left == right:
            tree[node] = values[left]
            return
        mid = left + (right - left) // 2
        build(2 * node + 1, left, mid)
        build(2 * node + 2, mid + 1, right)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

    build(0, 0, len(values) - 1)
    return tree, intervals


def query_segment_tree(tree, node, left, right, ql, qr):
    if qr < left or right < ql:
        return 0
    if ql <= left and right <= qr:
        return tree[node]
    mid = left + (right - left) // 2
    return (query_segment_tree(tree, 2 * node + 1, left, mid, ql, qr)
            + query_segment_tree(tree, 2 * node + 2, mid + 1, right, ql, qr))


def canonical_ranges(intervals, query_left, query_right):
    covered = [(left, right) for left, right in intervals.values()
               if query_left <= left and right <= query_right]
    return sorted((left, right) for left, right in covered
                  if not any((a, b) != (left, right) and a <= left and right <= b
                             for a, b in covered))


def clean(value):
    return value.replace("$", "").replace("**", "").replace("`", "").strip()


def tables(text):
    parsed = []
    for block in re.findall(r"(?m)(?:^\|[^\n]*\|[ \t]*\n?)+", text):
        rows = [[clean(cell) for cell in re.split(r"(?<!\\)\|", line.strip()[1:-1])]
                for line in block.splitlines()]
        if len(rows) >= 2 and all(re.fullmatch(r":?-+:?", cell.replace(" ", ""))
                                  for cell in rows[1]):
            width = len(rows[0])
            if any(len(row) != width for row in rows):
                raise AssertionError(f"Ragged Markdown table: {rows[0]}")
            parsed.append([rows[0]] + rows[2:])
    return parsed


def question_block(test_text, start, end=None):
    match = re.search(rf"(?m)^### {re.escape(start)}\b[^\n]*", test_text)
    if not match:
        raise AssertionError(f"Missing question heading {start}")
    later = list(re.finditer(r"(?m)^### Q\d\.", test_text[match.end():]))
    stop = match.end() + later[0].start() if later else len(test_text)
    if end:
        end_match = re.search(rf"(?m)^### {re.escape(end)}\b", test_text[match.end():])
        if end_match:
            stop = min(stop, match.end() + end_match.start())
    return test_text[match.start():stop]


class VerifyClassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (CT / "README.md").read_text(encoding="utf-8")
        cls.tests = {}
        matches = list(re.finditer(r"(?m)^## Class Test ([1234]):[^\n]*", cls.text))
        if [match[1] for match in matches] != ["1", "2", "3", "4"]:
            raise AssertionError(f"Class test sequence differs: {[m[1] for m in matches]}")
        for i, match in enumerate(matches):
            stop = matches[i + 1].start() if i + 1 < len(matches) else len(cls.text)
            cls.tests[match[1]] = cls.text[match.start():stop]
        cls.tests["3"] = re.split(r"(?m)^## Verification", cls.tests["3"], maxsplit=1)[0]

    def test_sequential_question_inventory(self):
        expected = {"1": ["Q1", "Q2", "Q3", "Q4"],
                    "2": ["Q1", "Q2", "Q3"],
                    "3": ["Q1", "Q2", "Q3"],
                    "4": ["Q1", "Q2", "Q3", "Q4"]}
        for test, labels in expected.items():
            actual = re.findall(r"(?m)^### (Q\d)\.", self.tests[test])
            self.assertEqual(actual, labels)
        self.assertIn("CSE 2201 - CT - 3.pdf", self.text)
        self.assertIn("Class Test: 01", self.tests["3"])
        self.assertIn("CSE 2201 - CT - 4.pdf", self.text)

    def test_ct1_fibonacci(self):
        counts = fib_naive_call_counts(5)
        self.assertEqual(dict(counts), {5: 1, 4: 1, 3: 2, 2: 3, 1: 5, 0: 3})
        self.assertEqual(sum(counts.values()), 15)
        self.assertEqual(fib_tabulation(5), [0, 1, 1, 2, 3, 5])
        self.assertIn("15 calls", self.tests["1"])
        section = question_block(self.tests["1"], "Q2")
        parts, _, series = tables(section)
        self.assertEqual([row[0] for row in parts[1:]],
                         ["State", "Base case", "Recurrence", "Table order", "Final answer"])
        self.assertEqual(series[0][1:], [str(n) for n in range(6)])
        self.assertEqual(series[1][1:], [str(v) for v in fib_tabulation(5)])

    def test_ct1_principle_of_optimality_table(self):
        grid, = tables(question_block(self.tests["1"], "Q1"))
        best = {row[0]: row[-1] for row in grid[1:]}
        self.assertEqual(best, {"T": "0", "B": "3", "A": "4 (via B)", "S": "6 (via A)"})
        # best(S) = min(2 + best(A), 5 + best(B)) with A->B 1, A->T 7, B->T 3
        best_b = 3
        best_a = min(1 + best_b, 7)
        self.assertEqual((best_a, min(2 + best_a, 5 + best_b)), (4, 6))

    def test_ct1_lcs_table_and_optimum(self):
        expected = lcs_table(LCS_X, LCS_Y)
        self.assertEqual(lcs_bruteforce(LCS_X, LCS_Y), (4, {"GTAB"}))
        section = question_block(self.tests["1"], "Q3")
        parts, grid = tables(section)[:2]
        self.assertEqual([row[0] for row in parts[1:]],
                         ["State", "Base case", "Recurrence", "Table order", "Final answer"])
        self.assertEqual(grid[0][2:], list(LCS_Y))
        values, arrows = split_arrow_grid(grid)
        self.assertEqual(values, expected)
        self.assertEqual(arrows, lcs_arrows(LCS_X, LCS_Y, expected))
        self.assertIn("GTAB", section)

    def test_ct1_knapsack_table(self):
        expected = knapsack_table(KNAP_W, KNAP_P, KNAP_CAP)
        section = question_block(self.tests["1"], "Q4")
        parts, grid = tables(section)[:2]
        self.assertEqual([row[0] for row in parts[1:]],
                         ["State", "Base case", "Recurrence", "Table order", "Final answer"])
        self.assertEqual(grid[0][3:], [f"W={c}" for c in range(KNAP_CAP + 1)])
        self.assertEqual([row[1:3] for row in grid[2:]],
                         [[str(w), str(p)] for w, p in zip(KNAP_W, KNAP_P)])
        values, arrows = split_arrow_grid([row[2:] for row in grid])
        self.assertEqual(values, expected)
        self.assertEqual(arrows, knapsack_arrows(KNAP_W, KNAP_P, expected))
        self.assertEqual(expected[-1][-1], 5)
        self.assertIn("items **1 and 2**", section)

    def test_ct2_topological_order(self):
        section = question_block(self.tests["2"], "Q1")
        stack = dfs_finish_stack(TOPO_VERTICES, TOPO_EDGES)
        self.assertEqual(stack, [1, 3, 2, 6, 4, 5])
        order = list(reversed(stack))
        self.assertEqual(order, [5, 4, 6, 2, 3, 1])
        positions = {vertex: i for i, vertex in enumerate(order)}
        self.assertTrue(all(positions[u] < positions[v] for u, v in TOPO_EDGES))
        adjacency, steps = tables(section)
        for row in adjacency[1:]:
            expected = sorted(b for a, b in TOPO_EDGES if a == int(row[0]))
            self.assertEqual([] if row[1] == "-" else [int(x) for x in row[1].split(",")], expected)
        finish_stacks = [[int(x) for x in row[-1].split(",")] for row in steps[1:]]
        self.assertEqual(finish_stacks, [stack[:i] for i in (1, 2, 3, 4, 5, 6)])
        self.assertIn("5,\\ 4,\\ 6,\\ 2,\\ 3,\\ 1", section.replace("$", ""))
        kahn_order = kahn(TOPO_VERTICES, TOPO_EDGES)
        self.assertEqual(kahn_order, [4, 5, 6, 2, 3, 1])
        kahn_positions = {vertex: i for i, vertex in enumerate(kahn_order)}
        self.assertTrue(all(kahn_positions[u] < kahn_positions[v] for u, v in TOPO_EDGES))
        self.assertIn("4, 5, 6, 2, 3, 1", section)

    def test_ct2_bellman_ford_passes(self):
        snapshots, parent, negative = bellman_ford(BF_VERTICES, BF_EDGES, "S")
        self.assertFalse(negative)
        section = question_block(self.tests["2"], "Q2")
        grids = tables(section)
        rounds, dist, parent = bellman_ford_selected_rounds(BF_VERTICES, BF_EDGES, "S", 3)
        self.assertEqual(rounds[2][0], rounds[2][-1])  # Round 3: nothing changes
        round_tables, final = grids[:3], grids[3]
        for grid, expected in zip(round_tables, rounds):
            self.assertEqual([row[0] for row in grid[1:]], BF_VERTICES)
            actual = [[math.inf if c == "\\infty" else int(c) for c in row[1:]] for row in grid[1:]]
            self.assertEqual(actual, expected)
        self.assertEqual(final[1][1:], [str(dist[v]) for v in BF_VERTICES])
        self.assertEqual([dist[v] for v in BF_VERTICES], [0, 0, 1, -2, 0, 1])
        for before, after in zip(snapshots, snapshots[1:]):
            self.assertTrue(all(after[v] <= before[v] for v in BF_VERTICES))
        path, node = [], "T"
        while node is not None:
            path.append(node)
            node = parent[node]
        self.assertEqual(list(reversed(path)), ["S", "C", "A", "B", "D", "T"])
        self.assertIn("S→C→A→B→D→T", section)

    def test_ct2_floyd_warshall_matrices(self):
        matrices = floyd_warshall(FW_VERTICES, FW_EDGES)
        section = question_block(self.tests["2"], "Q3")
        found = re.findall(r"D\^\{\((\d)\)\}=\s*\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}", section, re.S)
        self.assertEqual([k for k, _ in found], ["0", "1", "2", "3", "4"])
        for (_, body), matrix in zip(found, matrices):
            rows = [r.strip() for r in body.strip().split("\\\\") if r.strip()]
            actual = [[math.inf if c.strip() == "\\infty" else int(c) for c in r.split("&")]
                      for r in rows]
            self.assertEqual(actual, [[matrix[i, j] for j in FW_VERTICES] for i in FW_VERTICES])
        # Per-cell min lines: D[i,j]=min(old, D[i,k]+D[k,j])=value
        pattern = (r"D\[(\d),(\d)\]=\\min\(([^,]+),\\ D\[(\d),(\d)\]\+D\[(\d),(\d)\]\)"
                   r"=\\min\([^)]*\)=([^$\s]+)")
        lines = re.findall(pattern, section)
        self.assertEqual(len(lines), 24)
        as_value = lambda s: math.inf if s == "\\infty" else int(s)
        for i, j, old, i2, k, k2, j2, value in lines:
            i, j, k = int(i), int(j), int(k)
            self.assertEqual((int(i2), int(k2), int(j2)), (i, k, j))
            self.assertEqual(as_value(old), matrices[k - 1][i, j])
            self.assertEqual(as_value(value), matrices[k][i, j])
        # Cells that changed at each k, and the arrow-guided tables for them
        expected_changes = []
        for k_index, k in enumerate(FW_VERTICES):
            before, after = matrices[k_index], matrices[k_index + 1]
            expected_changes.append([f"D[{i},{j}]" for i in FW_VERTICES for j in FW_VERTICES
                                     if before[i, j] != after[i, j]])
        self.assertEqual(expected_changes,
                         [["D[3,2]", "D[4,2]"], ["D[1,3]", "D[4,3]"],
                          ["D[2,1]", "D[2,4]"], ["D[2,1]", "D[3,1]", "D[3,2]"]])
        arrow_tables = [g for g in tables(section) if g[0][0] == "Cell"]
        self.assertEqual([[row[0] for row in grid[1:]] for grid in arrow_tables], expected_changes)
        for k_index, grid in enumerate(arrow_tables):
            after = matrices[k_index + 1]
            for row in grid[1:]:
                i, j = map(int, re.fullmatch(r"D\[(\d),(\d)\]", row[0]).groups())
                self.assertEqual(int(row[-1]), after[i, j])

    def test_ct3_union_rank_example(self):
        operations = [(0, 1), (2, 3), (4, 5), (6, 7), (0, 2), (4, 6), (0, 4)]
        parent, rank, find = dsu_union_by_rank(8, operations)
        height = max(dsu_depth(parent, v) for v in range(8))
        root = find(0)
        self.assertEqual({find(v) for v in range(8)}, {root})
        self.assertEqual(rank[root], 3)
        self.assertEqual(height, 3)
        q1 = question_block(self.tests["3"], "Q1")
        self.assertIn("height **3**", q1)
        self.assertIn("height **7**", q1)
        self.assertIn("UNION-BY-RANK(rootX, rootY)", q1)
        trace = next(g for g in tables(q1) if g[0][0] == "Operation")
        ops = [tuple(int(x) for x in re.findall(r"\d+", row[0])) for row in trace[1:]]
        self.assertEqual([(a - 1, b - 1) for a, b in ops], operations)
        parent, rank = list(range(8)), [0] * 8
        for (a, b), row in zip(ops, trace[1:]):
            a, b = a - 1, b - 1
            self.assertEqual(rank[a], rank[b])  # every step is a tie in this example
            parent[b] = a
            rank[a] += 1
            self.assertEqual(row[3], f"{a + 1} ({rank[a]})")
            self.assertEqual(row[4], str(rank[a]))

    def test_ct3_watershed_row(self):
        q2 = question_block(self.tests["3"], "Q2")
        self.assertIn("T(n)=2T(n/2)+\\Theta(n)", q2.replace("$", ""))
        row = next(r for g in tables(q2) if g[0][0] == "a" for r in g[1:])
        self.assertEqual(row[:3], ["2", "2", "n"])
        self.assertIn("Case 2", row[4])
        self.assertIn("\\Theta(n\\log n)", row[5])

    def test_ct3_maximum_subarray(self):
        best, records = divide_conquer_max_subarray(MAX_ARRAY)
        self.assertEqual(best, (6, 3, 6))
        self.assertEqual(best, brute_force_max_subarray(MAX_ARRAY))
        self.assertEqual(records[0, 7]["left"], (4, 3, 3))
        self.assertEqual(records[0, 7]["right"], (3, 5, 6))
        self.assertEqual(records[0, 7]["cross"], (6, 3, 6))

    def test_ct3_segment_tree_and_query(self):
        tree, intervals = build_segment_tree(SEGMENT_ARRAY)
        self.assertEqual(tree[:15], [36, 11, 25, 3, 8, 11, 14, 2, 1, 5, 3, 4, 7, 6, 8])
        self.assertEqual(query_segment_tree(tree, 0, 0, 7, 2, 6), 25)
        self.assertEqual(canonical_ranges(intervals, 2, 6), [(2, 3), (4, 5), (6, 6)])
        section = question_block(self.tests["3"], "Q3")
        trace = next(g for g in tables(section) if g[0][0] == "Node" and g[0][-1] == "Returns")
        stored = next(g for g in tables(section) if g[0][-1] == "Stored sum")
        for row in stored[1:]:
            self.assertEqual(int(row[2]), tree[int(row[0])])
            self.assertEqual(row[1], "[%d,%d]" % intervals[int(row[0])])
        calls = []

        def visit(node, left, right):
            if right < 2 or 6 < left:
                value = 0
            elif 2 <= left and right <= 6:
                value = tree[node]
            else:
                mid = left + (right - left) // 2
                value = visit(2 * node + 1, left, mid) + visit(2 * node + 2, mid + 1, right)
            calls.append((node, left, right, value))
            return value

        self.assertEqual(visit(0, 0, 7), 25)
        expected = sorted(calls)
        actual = sorted((int(r[0]), *map(int, re.findall(r"\d+", r[1])), int(r[3]))
                        for r in trace[1:])
        self.assertEqual(len(trace) - 1, 9)
        self.assertEqual([int(r[3]) for r in trace[1:]], [25, 8, 0, 8, 17, 11, 6, 6, 0])
        self.assertEqual(actual, expected)
        self.assertIn("query(0, 0, n - 1, 2, 6)", section)

    def test_all_diagram_pairs_and_local_links(self):
        for target in re.findall(r"\]\(([^)]+)\)", self.text):
            if target.startswith(("http://", "https://", "#")):
                continue
            path = unquote(urlsplit(target).path)
            self.assertTrue((CT / path).resolve().exists(), target)
        embedded = sorted(set(re.findall(r"\]\((diagrams/[^)]+\.svg)\)", self.text)))
        self.assertEqual(len(embedded), 15)
        self.assertEqual([path.name for path in sorted((CT / "diagrams").glob("*.svg"))],
                         sorted(Path(item).name for item in embedded))
        index = (CT / "diagrams/README.md").read_text(encoding="utf-8")
        for svg in embedded:
            path = CT / svg
            scene_path = path.with_suffix(".excalidraw")
            self.assertTrue(scene_path.exists(), svg)
            self.assertTrue(json.loads(scene_path.read_text(encoding="utf-8"))["elements"], svg)
            self.assertIn(path.name, index)


if __name__ == "__main__":
    unittest.main(verbosity=2)
