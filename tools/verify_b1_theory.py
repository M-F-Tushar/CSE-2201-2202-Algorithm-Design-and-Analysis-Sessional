"""Independent, read-only validation record for 1st Batch/Theory.

Run: python tools/verify_b1_theory.py
Optional: --theory-dir PATH (a snapshot with its diagrams and navigation targets).
Uses only the standard library; does not import the diagram generator, regenerate
assets, access the network, or authenticate the unavailable historical paper.

Numeric Markdown tables are parsed from the actual document, not copied here.
Exhaustive enumeration independently checks optimization tables; graph/search
checks derive their inputs from the published edge lists or adjacency table.
This also executes the trusted local README's Fibonacci Python example. These
regressions supplement, rather than automate, the mathematical/prose review.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
THEORY = ROOT / "Chapter 0 - Previous Year Questions/1st Batch/Theory"
PARTS = [f"Q{q}({p})" for q, count in enumerate((3, 3, 4, 3, 4, 4, 3, 3), 1)
         for p in "abcd"[:count]]
NS = "{http://www.w3.org/2000/svg}"


def clean(value):
    return value.replace("$", "").replace("**", "").replace("`", "").strip()


def tables(text):
    """Parse the simple pipe tables used here, preserving headers and row labels."""
    result = []
    for block in re.findall(r"(?m)(?:^\|[^\n]*\|[ \t]*\n?)+", text):
        rows = [[clean(c) for c in re.split(r"(?<!\\)\|", line.strip()[1:-1])]
                for line in block.splitlines()]
        if len(rows) >= 2 and all(re.fullmatch(r":?-+:?", c.replace(" ", ""))
                                  for c in rows[1]):
            width = len(rows[0])
            if any(len(row) != width for row in rows):
                raise AssertionError(f"Ragged Markdown table: {rows[0]}")
            result.append([rows[0]] + rows[2:])
    return result


def number(value):
    value = clean(value).replace(",", "")
    return math.inf if value == r"\infty" else int(value)


def lead(value):
    """Leading integer of a DP cell such as '2 (up arrow)'."""
    return int(re.match(r"-?\d+", clean(value))[0])


def table_with_header(text, first):
    """First pipe table whose first header cell equals ``first``."""
    return next(t for t in tables(text) if t[0][0] == first)


def integers(value):
    return [int(v) for v in re.findall(r"-?\d+", value)]


def expression(value, n=1):
    """Evaluate only the small arithmetic syntax in the recurrence/growth tables."""
    value = clean(value).replace(",", "")
    value = value.replace(r"\log_2 n", str(math.log2(n)))
    value = value.replace(r"\cdot", "*").replace(r"\times", "*")
    value = value.replace("^", "**").replace("{", "(").replace("}", ")")
    tree = ast.parse(value.strip(), mode="eval")

    def visit(node):
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.Name) and node.id == "n":
            return n
        if isinstance(node, ast.BinOp):
            left, right = visit(node.left), visit(node.right)
            operations = {ast.Add: lambda: left + right, ast.Sub: lambda: left - right,
                          ast.Mult: lambda: left * right, ast.Div: lambda: left / right,
                          ast.Pow: lambda: left ** right}
            if type(node.op) in operations:
                return operations[type(node.op)]()
        raise AssertionError(f"Unsupported table arithmetic: {value!r}")

    return visit(tree)


def subsets(items):
    return (s for size in range(len(items) + 1) for s in combinations(items, size))


def floyd(vertices, edges, undirected=False):
    """Independent all-pairs oracle, separate from the published single-source runs."""
    dist = {(u, v): 0 if u == v else math.inf for u in vertices for v in vertices}
    for u, v, weight in edges:
        dist[u, v] = weight
        if undirected:
            dist[v, u] = weight
    for k in vertices:
        for u in vertices:
            for v in vertices:
                dist[u, v] = min(dist[u, v], dist[u, k] + dist[k, v])
    return dist


def distance_line(text, label):
    line = next(line for line in text.splitlines() if line.startswith(label))
    return {v: int(d) for v, d in re.findall(r"\b([A-Z])\s*=\s*(-?\d+)", line)}


class VerifyTheory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (THEORY / "README.md").read_text(encoding="utf-8")
        matches = list(re.finditer(r"(?m)^#### (Q\d\([a-d]\))[^\n]*", cls.text))
        names = [m[1] for m in matches]
        if names != PARTS:
            raise AssertionError(f"Subquestion inventory differs: {names}")
        cls.sections = {}
        for i, match in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(cls.text)
            # Major headings (notably Quick Revision) are not part of an answer.
            cls.sections[match[1]] = re.split(
                r"(?m)^#{2,3} ", cls.text[match.start():end], maxsplit=1
            )[0]

    def section(self, part):
        return self.sections[part]

    def test_growth_table(self):
        table, = tables(self.section("Q1(c)"))
        self.assertEqual(len(table), 4)
        for raw_n, raw_square, raw_log in table[1:]:
            n = number(raw_n)
            with self.subTest(n=n):
                self.assertEqual(expression(raw_square), n * n)
                self.assertTrue(raw_log.startswith("about "))
                rounded = raw_log.removeprefix("about ")
                # Integers round to nearest unit; 2 x 10^7 has one significant digit.
                power = re.search(r"10\^(?:\{)?(\d+)", rounded)
                quantum = 10 ** int(power[1]) if power else 1
                self.assertLessEqual(abs(expression(rounded) - n * math.log2(n)),
                                     quantum / 2)
        ratio = int(re.search(r"about ([\d,]+) times less work", self.section("Q1(c)"))[1].replace(",", ""))
        n = number(table[-1][0])
        self.assertLess(abs(ratio / (n / math.log2(n)) - 1), .01)

    def test_recurrence_table_and_loop_examples(self):
        section = self.section("Q2(c)")
        table, = tables(section)
        for n in (8, 16, 32, 64):
            for level, count, size, work in table[1:]:
                if level == "...":
                    continue
                with self.subTest(n=n, level=level):
                    k = expression(level, n)
                    self.assertEqual(expression(count, n), 2 ** k)
                    self.assertEqual(expression(size, n), n / 2 ** k)
                    for side in work.split("="):
                        self.assertEqual(expression(side, n), n)
        runtime = {1: 1}
        for k in range(1, 15):
            n = 2 ** k
            runtime[n] = 2 * runtime[n // 2] + n
            self.assertEqual(runtime[n], n * math.log2(n) + n)
        checks = re.search(r"Check: ([^\n]+)", section)[1]
        for n, value in re.findall(r"T\((\d+)\)\s*=\s*(\d+)", checks):
            self.assertEqual(runtime[int(n)], int(value))
        loops = self.section("Q2(b)")
        self.assertIn("j <= n", loops)
        self.assertIn("j <= i", loops)
        for n in range(1, 1001):
            powers, i = [], 1
            while i <= n:
                powers.append(i)
                i *= 2
            self.assertEqual(len(powers), n.bit_length())
            self.assertEqual(sum(powers), 2 ** n.bit_length() - 1)
            self.assertTrue(n <= sum(powers) <= 2 * n - 1)
        first = re.search(r"For \$n = (\d+)\$:.*?total = (\d+)", loops)
        second = re.search(r"For \$n = (\d+)\$:.*?total = \$[^\n]*?= (\d+)\$", loops)
        self.assertEqual(int(first[2]), int(first[1]) * int(first[1]).bit_length())
        self.assertEqual(int(second[2]), 2 ** int(second[1]).bit_length() - 1)

    def test_published_fibonacci_code(self):
        code, = re.findall(r"```python\n(.*?)\n```", self.section("Q4(b)"), re.S)
        namespace = {}
        exec(compile(code, str(THEORY / "README.md") + ":Q4(b)", "exec"), namespace)
        a, b = 0, 1
        for n in range(101):
            with self.subTest(n=n):
                self.assertEqual(namespace["fib_memo"](n), a)
                self.assertEqual(namespace["fib_tab"](n), a)
            a, b = b, a + b

    def test_heap_build_and_actual_round_table(self):
        text = self.section("Q3(d)")
        initial = integers(re.search(r"A = \[([^]]+)\]", text)[1])
        array = initial.copy()

        def sift(i, end):
            while 2 * i + 1 < end:
                child = 2 * i + 1
                if child + 1 < end and array[child + 1] > array[child]:
                    child += 1
                if array[i] >= array[child]:
                    break
                array[i], array[child] = array[child], array[i]
                i = child

        builds = []
        for i in range(len(array) // 2 - 1, -1, -1):
            before = array.copy()
            sift(i, len(array))
            if array != before:
                builds.append(array.copy())
        published_builds = [integers(a) for a in re.findall(r"Array: \$\[([^]]+)\]", text)]
        self.assertEqual(published_builds, builds)
        table, = tables(text)
        self.assertEqual(len(table) - 1, len(initial) - 1)
        for step, end in enumerate(range(len(array) - 1, 0, -1), 1):
            array[0], array[end] = array[end], array[0]
            sift(0, end)
            row = table[step]
            with self.subTest(round=step):
                self.assertEqual(number(row[0]), step)
                self.assertEqual(integers(row[2]), array)
        final = re.search(r"\*\*Final sorted array:\*\* \$\[([^]]+)\]", text)[1]
        self.assertEqual(integers(final), sorted(initial))

    def test_mst_edge_and_kruskal_tables(self):
        text = self.section("Q4(c)")
        given = table_with_header(text, "Edge")
        prim = table_with_header(text, "Step")
        kruskal = table_with_header(text, "Scan")
        edges = [(edge[0], edge[2], number(w)) for edge, w in given[1:]]
        vertices = set(v for u, v, _ in edges) | set(u for u, v, _ in edges)
        self.assertEqual(len({frozenset((u, v)) for u, v, _ in edges}), len(edges))
        candidates = []
        for chosen in combinations(edges, len(vertices) - 1):
            reached = {min(vertices)}
            for _ in vertices:
                for u, v, _ in chosen:
                    if u in reached or v in reached:
                        reached.update((u, v))
            if reached == vertices:
                candidates.append((sum(w for _, _, w in chosen),
                                   {frozenset((u, v)) for u, v, _ in chosen}))
        optimum = min(cost for cost, _ in candidates)
        winners = [tree for cost, tree in candidates if cost == optimum]
        self.assertEqual(len(winners), 1, "MST is claimed unique")
        reported = re.search(r"\*\*MST edges:\*\* ([^\n]+)", text)[1]
        self.assertEqual({frozenset(pair) for pair in re.findall(r"([A-Z])-([A-Z])", reported)}, winners[0])
        total = re.search(r"\*\*Total MST weight:\*\* \$([^$]+)\$", text)[1]
        for side in total.split("="):
            self.assertEqual(expression(side), optimum)
        # The adjacency list must agree with the edge table.
        block, = [b for b in re.findall(r"```text\n(.*?)\n```", text, re.S) if re.match(r"A: ", b)]
        listed = {frozenset((u, v)): int(w) for u, rest in
                  (line.split(": ") for line in block.splitlines())
                  for v, w in re.findall(r"([A-Z])\((\d+)\)", rest)}
        self.assertEqual(listed, {frozenset((u, v)): w for u, v, w in edges})
        # Kruskal: scan table with the DSU forest after every accepted edge.
        parent = {v: v for v in vertices}

        def find(v):
            while parent[v] != v:
                v = parent[v]
            return v

        def partition():
            groups = {}
            for v in vertices:
                groups.setdefault(find(v), set()).add(v)
            return {frozenset(g) for g in groups.values()}

        accepted = 0
        self.assertEqual(len(kruskal) - 1, len(edges))
        for row, (u, v, weight) in zip(kruskal[1:], sorted(edges, key=lambda e: e[2])):
            self.assertEqual(row[1:3], [f"{u}-{v}", str(weight)])
            if accepted == len(vertices) - 1:
                self.assertEqual(row[3], "Not needed")
            elif find(u) == find(v):
                self.assertTrue(row[3].startswith("Skip"), row)
                self.assertEqual(row[4], "unchanged")
            else:
                self.assertTrue(row[3].startswith("Take"), row)
                parent[find(u)] = find(v)
                accepted += 1
                shown = {frozenset(s.split(",")) for s in re.findall(r"\\\{([A-Z,]+)\\\}", row[4])}
                self.assertEqual(shown, partition(), row)
        # Prim: the published tree, crossing edge, and running weight at every step.
        reached, running = {"A"}, 0
        self.assertEqual(len(prim) - 1, len(vertices) - 1)
        for row in prim[1:]:
            self.assertEqual(set(re.findall(r"[A-Z]", row[1])), reached)
            u, v, w = min((e for e in edges if (e[0] in reached) != (e[1] in reached)),
                          key=lambda e: e[2])
            choice = re.match(r"([A-Z])-([A-Z]) \((\d+)\)", row[2])
            self.assertEqual((frozenset(choice.group(1, 2)), int(choice[3])), (frozenset((u, v)), w))
            self.assertEqual(frozenset(row[3].split("-")), frozenset((u, v)))
            running += w
            self.assertEqual(int(row[4]), running)
            reached.update((u, v))
        self.assertEqual(reached, vertices)
        self.assertEqual(running, optimum)

    def test_queens_and_subset_search(self):
        text = self.section("Q5(b)")
        n = int(re.search(r"Place (\d+) queens", text)[1])
        solutions = [q for q in permutations(range(n))
                     if all(abs(q[i] - q[j]) != j - i for i in range(n) for j in range(i + 1, n))]
        published = [tuple(integers(v)) for v in re.findall(r"\$\[([\d, ]+)\]\$", text)]
        self.assertEqual(published, solutions)
        board, = [block for block in re.findall(r"```text\n(.*?)\n```", text, re.S)
                  if re.fullmatch(r"[.Q \n]+", block)]
        rows = [line.split() for line in board.splitlines()]
        self.assertEqual([len(row) for row in rows], [n] * n)
        self.assertTrue(all(row.count("Q") == 1 for row in rows))
        self.assertEqual(tuple(row.index("Q") for row in rows), solutions[0])
        text = self.section("Q5(c)")
        items = integers(re.search(r"A\s*=\s*\{([^}]+)\}", text)[1])
        target = int(re.search(r"d\s*=\s*(\d+)", text)[1])
        answers = [s for s in subsets(items) if sum(s) == target]
        answer = tuple(integers(re.search(r"\*\*Answer: \$\\\{([^}]+)\\\}", text)[1]))
        self.assertEqual(answers, [answer])
        visits = []

        def search(i, total):
            if total == target:
                return True
            if total > target or i == len(items):
                return False
            for next_total in (total + items[i], total):
                visits.append(next_total)
                if search(i + 1, next_total):
                    return True
            return False

        self.assertTrue(search(0, 0))
        self.assertEqual([int(v) for v in re.findall(r"sum = (\d+)", text)], visits)

    def test_hamiltonian_adjacency_table_and_search(self):
        text = self.section("Q5(d)")
        table, = tables(text)
        graph = {v: neighbours.split(", ") for v, neighbours in table[1:]}
        for u, neighbours in graph.items():
            self.assertEqual(neighbours, sorted(set(neighbours)))
            self.assertNotIn(u, neighbours)
            for v in neighbours:
                self.assertIn(u, graph[v], "Undirected adjacency must be symmetric")
        leaves = []

        def search(path):
            if len(path) == len(graph):
                closes = "a" in graph[path[-1]]
                leaves.append((path, closes))
                return closes
            choices = [v for v in graph[path[-1]] if v not in path]
            if not choices:
                leaves.append((path, False))
            return any(search(path + [v]) for v in choices)

        self.assertTrue(search(["a"]))
        trace = []
        for line in text.splitlines():
            if re.match(r"\d+\. ", line):
                path, = re.findall(r"\$(a \\to [^$]+)\$", line)
                trace.append((re.findall(r"\b[a-f]\b", path), "Circuit found" in line))
        self.assertEqual(trace, leaves)
        answer_line = re.search(r"\*\*Answer:\*\* ([^\n]+)", text)[1]
        circuits = re.findall(r"\$([a-f](?:-[a-f])+)\$", answer_line)
        self.assertEqual(circuits[0].split("-"), leaves[-1][0] + ["a"])
        self.assertEqual(len(circuits), 2)
        for circuit in circuits:
            path = circuit.split("-")
            self.assertEqual(path[0], path[-1])
            self.assertEqual(sorted(path[:-1]), sorted(graph))
            self.assertTrue(all(v in graph[u] for u, v in zip(path, path[1:])))

    def test_grid_input_dp_table_and_paths(self):
        text = self.section("Q6(c)")
        given, published = [t for t in tables(text) if t[0][1:2] == ["col 0"]]
        self.assertEqual(given[0], published[0])
        self.assertEqual([row[0] for row in given], [row[0] for row in published])
        grid = [[lead(c) for c in row[1:]] for row in given[1:]]
        documented = [[lead(c) for c in row[1:]] for row in published[1:]]

        def paths(r, c):
            if (r, c) == (0, 0):
                return [grid[0][0]]
            before = (paths(r - 1, c) if r else []) + (paths(r, c - 1) if c else [])
            return [value + grid[r][c] for value in before]

        calculated = [[max(paths(r, c)) for c in range(len(grid[0]))] for r in range(len(grid))]
        self.assertEqual(documented, calculated, "Published grid DP cells differ from enumerated paths")
        # Arrows: up when the cell above is at least as good (up-first tie rule), else left.
        for r, row in enumerate(published[1:]):
            for c, cell in enumerate(row[1:]):
                if (r, c) == (0, 0):
                    self.assertNotIn("arrow", cell)
                    continue
                up = r > 0 and (c == 0 or calculated[r - 1][c] >= calculated[r][c - 1])
                self.assertIn(r"\uparrow" if up else r"\leftarrow", cell, f"arrow at {(r, c)}")
        # The stated traceback follows the arrows from the last cell back to the start.
        steps = re.findall(r"(?m)^\d+\. \$\((\d+),(\d+)\)\$: \$\\(uparrow|leftarrow)\$ to \$\((\d+),(\d+)\)\$", text)
        current = (len(grid) - 1, len(grid[0]) - 1)
        for r, c, arrow, s, t in steps:
            self.assertEqual((int(r), int(c)), current)
            current = (current[0] - 1, current[1]) if arrow == "uparrow" else (current[0], current[1] - 1)
            self.assertEqual((int(s), int(t)), current)
        self.assertEqual(current, (0, 0))
        best = calculated[-1][-1]
        self.assertEqual(int(re.search(r"\*\*Answer: (\d+) coins", text)[1]), best)
        path_count = 0
        for math_block in re.findall(r"\$([^$]+)\$", text):
            if r"\to" not in math_block:
                continue
            path = [(int(r), int(c)) for r, c in re.findall(r"\((\d+),(\d+)\)", math_block)]
            self.assertEqual(path[0], (0, 0))
            self.assertEqual(path[-1], (len(grid) - 1, len(grid[0]) - 1))
            self.assertTrue(all((s-r, t-c) in ((1, 0), (0, 1))
                                for (r, c), (s, t) in zip(path, path[1:])))
            self.assertEqual(sum(grid[r][c] for r, c in path), best)
            path_count += 1
        self.assertEqual(path_count, 2)

    def test_coin_change_actual_table(self):
        text = self.section("Q6(d)")
        coins = integers(re.search(r"\\\{([\d, ]+)\\\}", text)[1])
        target = int(re.search(r"n\s*=\s*(\d+)", text)[1])
        table = table_with_header(text, "x")
        amounts = [number(c) for c in table[0][1:]]
        self.assertEqual(amounts, list(range(target + 1)))
        oracle = []
        for amount in amounts:
            counts = product(*(range(amount // c + 1) for c in coins))
            oracle.append(min((sum(ns) for ns in counts
                               if sum(n*c for n, c in zip(ns, coins)) == amount), default=math.inf))
        self.assertEqual([number(c) for c in table[1][1:]], oracle)
        # Last coin used: the first coin (in the listed order) that achieves dp[x].
        for x, cell in enumerate(table[2][1:]):
            if x:
                self.assertEqual(int(cell), next(c for c in coins if c <= x and oracle[x - c] + 1 == oracle[x]))
        self.assertEqual(int(re.search(r"\*\*Answer: (\d+) coins", text)[1]), oracle[-1])
        remainder, greedy = target, 0
        for coin in sorted(coins, reverse=True):
            count, remainder = divmod(remainder, coin)
            greedy += count
        self.assertEqual(remainder, 0)
        q4 = self.section("Q4(a)")
        self.assertEqual(sorted(integers(re.search(r"denominations \$\\\{([^}]+)", q4)[1])), sorted(coins))
        self.assertEqual(int(re.search(r"\*\*(\d+) coins\*\*", q4)[1]), greedy)
        self.assertGreater(greedy, oracle[-1])
        steps = table_with_header(q4, "Step")
        self.assertEqual([row[1:] for row in steps[1:]], [["6", "4", "2"], ["2", "1", "1"], ["1", "1", "0"]])

    def test_knapsack_actual_item_and_dp_tables(self):
        text = self.section("Q7(c)")
        table = table_with_header(text, "Item")
        capacity = int(re.search(r"capacity \$W\s*=\s*(\d+)", text)[1])
        self.assertEqual([int(re.search(r"W=(\d+)", c)[1]) for c in table[0][3:]],
                         list(range(capacity + 1)))
        n = len(table) - 2
        self.assertEqual([number(row[0]) for row in table[1:]], list(range(n + 1)))
        weights = [lead(row[1]) for row in table[2:]]
        profits = [lead(row[2]) for row in table[2:]]
        self.assertEqual((weights, profits), ([3, 4, 5, 6], [2, 3, 1, 4]))
        oracle = []
        for i in range(n + 1):
            row = []
            for cap in range(capacity + 1):
                row.append(max(sum(profits[j] for j in s) for s in subsets(list(range(i)))
                               if sum(weights[j] for j in s) <= cap))
            oracle.append(row)
        cells = [row[3:] for row in table[1:]]
        self.assertEqual([[lead(c) for c in row] for row in cells], oracle,
                         "Published knapsack DP cells differ from exhaustive subsets")
        # Arrows: take only when the item fits and is strictly better than skipping.
        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                takes = j >= weights[i-1] and profits[i-1] + oracle[i-1][j-weights[i-1]] > oracle[i-1][j]
                self.assertIn(r"\nwarrow" if takes else r"\uparrow", cells[i][j], f"arrow V[{i},{j}]")
        self.assertEqual(int(re.search(r"\*\*Answer: profit (\d+)", text)[1]), oracle[-1][-1])
        chosen = [int(i)-1 for i in re.search(r"using items ([\d and]+) \(", text)[1].split(" and ")]
        self.assertLessEqual(sum(weights[j] for j in chosen), capacity)
        self.assertEqual(sum(profits[j] for j in chosen), oracle[-1][-1])
        # The numbered traceback selects exactly those items.
        selected, j = [], capacity
        for i in range(n, 0, -1):
            if oracle[i][j] != oracle[i-1][j]:
                selected.append(i - 1)
                j -= weights[i-1]
        self.assertEqual(sorted(selected), sorted(chosen))

    def test_bellman_ford_actual_edge_list_and_pass_table(self):
        text = self.section("Q7(b)")
        edges = [(u, v, int(w)) for u, v, w in re.findall(r"([A-Z]) to ([A-Z]) = (-?\d+)", text)]
        rounds = [t for t in tables(text) if t[0][0] == "Selected vertex"]
        vertices = rounds[0][0][1:]
        dist = {v: 0 if v == "A" else math.inf for v in vertices}
        listing, = [b for b in re.findall(r"```text\n(.*?)\n```", text, re.S) if b.startswith("A: ")]
        self.assertEqual({(u, v, int(w)) for u, rest in (l.split(": ") for l in listing.splitlines())
                          for v, w in re.findall(r"([A-Z])\((-?\d+)\)", rest)}, set(edges))
        self.assertLessEqual(len(rounds), len(vertices) - 1)
        changed_flags = []
        for r, table in enumerate(rounds, 1):
            rows = table[1:]
            self.assertEqual(len(rows), len(vertices) + 1, "one row per vertex plus the wrap row")
            changed = False
            for row, u in zip(rows, vertices):
                self.assertEqual(row[0], u)
                self.assertEqual([number(c) for c in row[1:]], [dist[v] for v in vertices],
                                 f"Round {r}, selected {u}")
                for a, b, w in edges:
                    if a == u and dist[a] + w < dist[b]:
                        dist[b] = dist[a] + w
                        changed = True
            self.assertIn("wrap", rows[-1][0])
            self.assertEqual([number(c) for c in rows[-1][1:]], [dist[v] for v in vertices],
                             f"Round {r}, wrap row")
            changed_flags.append(changed)
        self.assertEqual(changed_flags[-1], False, "The last documented round must be unchanged")
        self.assertTrue(all(changed_flags[:-1]), "Earlier rounds must each change something")
        for a, b, w in edges:
            self.assertGreaterEqual(dist[a] + w, dist[b], "Negative-cycle check pass")
        oracle = floyd(vertices, edges)
        self.assertTrue(all(oracle[v, v] == 0 for v in vertices), "Unexpected negative cycle")
        self.assertEqual(dist, {v: oracle["A", v] for v in vertices})
        self.assertEqual(distance_line(text, "**Final distances from A:**"), dist)
        weights = {(u, v): w for u, v, w in edges}
        cycles = []
        for size in range(2, len(vertices) + 1):
            for cycle in permutations(vertices, size):
                pairs = list(zip(cycle, cycle[1:] + cycle[:1]))
                if all(pair in weights for pair in pairs):
                    cycles.append(sum(weights[pair] for pair in pairs))
        stated = int(re.search(r"smallest cycle total is (\d+)", text)[1])
        self.assertEqual(min(cycles), stated)
        parents = dict(re.findall(r"\$parent\[([A-Z])\]=([A-Z])\$", text))
        self.assertEqual(set(parents), set(vertices) - {"A"})
        for v, p in parents.items():
            self.assertEqual(dist[p] + weights[p, v], dist[v], f"parent[{v}]")

    def test_dijkstra_actual_trace_and_negative_example(self):
        text = self.section("Q8(c)")
        edges = [(u, v, int(w)) for u, v, w in re.findall(r"\b([A-Z])-([A-Z])\s*\(?([0-9]+)\)?", text)]
        graph = {}
        for u, v, w in edges:
            graph.setdefault(u, {})[v] = w
            graph.setdefault(v, {})[u] = w
        listing, = [b for b in re.findall(r"```text\n(.*?)\n```", text, re.S) if b.startswith("A: ")]
        self.assertEqual({u: {v: int(w) for v, w in re.findall(r"([A-Z])\((\d+)\)", rest)}
                          for u, rest in (l.split(": ") for l in listing.splitlines())}, graph)
        table = next(t for t in tables(text) if t[0][0].startswith("Visited"))
        vertices = table[0][1:]
        dist = {v: 0 if v == "A" else math.inf for v in graph}
        settled, order, steps = set(), [], []
        for i, row in enumerate(table[1:], 1):
            u = min((v for v in graph if v not in settled), key=lambda v: (dist[v], v))
            self.assertEqual(row[0], u)
            for v, cell in zip(vertices, row[1:]):
                if v in settled:
                    self.assertIn(cell, ("", "-"), f"closed column {v} in row {u}")
                else:
                    self.assertEqual(number(cell), dist[v], f"row {u}, column {v}")
            self.assertEqual(number(row[1:][vertices.index(u)]), dist[u])
            settled.add(u)
            order.append(u)
            updates = {}
            for v, w in graph[u].items():
                if v not in settled and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updates[v] = dist[v]
            steps.append(updates)
        self.assertEqual(settled, set(graph))
        # The "Step k" text lists each relaxation that improves a distance.
        for k, (u, updates) in enumerate(zip(order, steps), 1):
            block = re.search(rf"\*\*Step {k} - [^\n]*\n(.*?)(?=\n\*\*Step |\nDistance table)", text, re.S)[1]
            documented = {v: int(w) for v, w in re.findall(r"\\Rightarrow d\(([A-Z])\)=(\d+)", block)}
            self.assertEqual(documented, updates, f"Dijkstra Step {k}")
        self.assertEqual(distance_line(text, "**Final distances:**"), dist)
        oracle = floyd(graph, edges, undirected=True)
        self.assertEqual(dist, {v: oracle["A", v] for v in graph})
        line = re.search(r"\*\*Shortest path to C:\*\* ([^\n]+)", text)[1]
        path = re.findall(r"\b[A-Z]\b", line.split("=")[0])
        self.assertEqual(sum(graph[u][v] for u, v in zip(path, path[1:])), dist["C"])
        for target in ("F", "C"):
            routes = []
            for mid in subsets(sorted(set(graph) - {"A", target})):
                for order in permutations(mid):
                    path = ("A",) + order + (target,)
                    pairs = list(zip(path, path[1:]))
                    if all(v in graph[u] for u, v in pairs):
                        if sum(graph[u][v] for u, v in pairs) == dist[target]:
                            routes.append(path)
            self.assertEqual(len(routes), 2, f"Claimed tied shortest routes to {target}")
        negative = self.section("Q7(a)")
        examples = [(u, v, int(w)) for u, v, w in re.findall(r"([A-Z])\\to ([A-Z])=(-?\d+)", negative)]
        true_distance = int(re.search(r"true answer is \$(-?\d+)\$", negative)[1])
        self.assertEqual(floyd("ABC", examples)["A", "B"], true_distance)
        labels = {v: 0 if v == "A" else math.inf for v in "ABC"}
        fixed = set()
        while len(fixed) < len(labels):
            u = min((v for v in labels if v not in fixed), key=lambda v: labels[v])
            fixed.add(u)
            for source, v, w in examples:
                if source == u and v not in fixed:
                    labels[v] = min(labels[v], labels[u] + w)
        claimed = int(re.search(r"Dijkstra keeps \$B = (\d+)\$", negative)[1])
        self.assertEqual(labels["B"], claimed)
        self.assertNotEqual(claimed, true_distance)
        # Bellman-Ford round table for the same counterexample (vertex order A, B, C).
        table, = [t for t in tables(negative) if t[0][0] == "Selected vertex"]
        bf = {v: 0 if v == "A" else math.inf for v in "ABC"}
        for row, u in zip(table[1:], "ABC"):
            self.assertEqual([number(c) for c in row[1:]], [bf[v] for v in "ABC"])
            for source, v, w in examples:
                if source == u:
                    bf[v] = min(bf[v], bf[u] + w)
        self.assertEqual([number(c) for c in table[-1][1:]], [bf[v] for v in "ABC"])
        self.assertEqual(bf["B"], true_distance)

    def test_preserved_graph_scene_geometry(self):
        for part, filename, directed in (
            ("Q7(b)", "b1-theory-06-bellman-ford-graph.excalidraw", True),
            ("Q8(c)", "b1-theory-08-dijkstra-graph.excalidraw", False),
        ):
            text = self.section(part)
            pattern = r"([A-Z]) to ([A-Z]) = (-?\d+)" if directed else r"\b([A-Z])-([A-Z])\s*\(?([0-9]+)\)?"
            edges = [(u, v, int(w)) for u, v, w in re.findall(pattern, text)]
            vertices = {v for u, v, _ in edges} | {u for u, v, _ in edges}
            elements = json.loads((THEORY / "diagrams" / filename).read_text(encoding="utf-8"))["elements"]
            centers = {e["text"]: (e["x"] + e["width"] / 2, e["y"] + e["height"] / 2)
                       for e in elements if e["type"] == "text" and e["text"] in vertices}
            self.assertEqual(set(centers), vertices)

            def nearest(x, y):
                return min(centers, key=lambda v: (centers[v][0]-x)**2 + (centers[v][1]-y)**2)

            def key(u, v):
                return (u, v) if directed else frozenset((u, v))

            actual, green = {}, set()
            for i, element in enumerate(elements):
                if element["type"] not in ("arrow", "line"):
                    continue
                first, last = element["points"][0], element["points"][-1]
                u = nearest(element["x"] + first[0], element["y"] + first[1])
                v = nearest(element["x"] + last[0], element["y"] + last[1])
                self.assertNotIn(key(u, v), actual, "Duplicate drawn edge")
                actual[key(u, v)] = int(elements[i + 1]["text"])
                self.assertEqual(element.get("endArrowhead") == "arrow", directed)
                if element["strokeColor"] == "#2f9e44":
                    green.add(key(u, v))
            self.assertEqual(actual, {key(u, v): w for u, v, w in edges}, filename)
            if directed:
                dist = floyd(vertices, edges)
                selected = {key(u, v) for u, v, w in edges if dist["A", u] + w == dist["A", v]}
            else:
                selected = {key(parent, child) for child, parent in re.findall(r"([A-Z])←([A-Z])", text)}
            self.assertEqual(green, selected, "Drawn shortest-path tree differs from answer")

    def test_links_diagram_coverage_and_assets(self):
        diagrams = THEORY / "diagrams"
        svg_files = set(diagrams.glob("*.svg"))
        sources = set(diagrams.glob("*.excalidraw"))
        self.assertEqual(len(svg_files), 24)
        self.assertEqual({p.stem for p in svg_files}, {p.stem for p in sources})
        for part in PARTS:
            images = re.findall(r"!\[[^\]]*\]\((diagrams/[^)]+\.svg)\)", self.section(part))
            self.assertTrue(images, f"{part} has no inline SVG")
            for image in images:
                self.assertIn(THEORY / image, svg_files)
                self.assertTrue((THEORY / image).with_suffix(".excalidraw").is_file())
        for markdown in THEORY.rglob("*.md"):
            for url in re.findall(r"\]\(([^)]+)\)", markdown.read_text(encoding="utf-8")):
                parsed = urlsplit(url)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                self.assertTrue((markdown.parent / unquote(parsed.path)).exists(),
                                f"Broken local link in {markdown.name}: {url}")
        index = (diagrams / "README.md").read_text(encoding="utf-8")
        self.assertEqual(set(re.findall(r"\]\(([^)]+\.svg)\)", index)), {p.name for p in svg_files})
        self.assertEqual(set(re.findall(r"\]\(([^)]+\.excalidraw)\)", index)), {p.name for p in sources})
        covered = set()
        for row in tables(index)[0][1:]:
            for part in re.findall(r"Q\d\([a-d]\)", row[0]):
                covered.add(part)
                filename, = re.findall(r"\]\(([^)]+\.svg)\)", row[2])
                self.assertIn(f"(diagrams/{filename})", self.section(part))
        self.assertEqual(covered, set(PARTS))
        for svg in sorted(svg_files):
            with self.subTest(diagram=svg.stem):
                root = ET.parse(svg).getroot()
                self.assertEqual(root.tag, NS + "svg")
                self.assertGreater(float(root.attrib["width"]), 0)
                self.assertGreater(float(root.attrib["height"]), 0)
                scene = json.loads(svg.with_suffix(".excalidraw").read_text(encoding="utf-8"))
                self.assertEqual(scene["type"], "excalidraw")
                self.assertEqual(scene["version"], 2)
                elements = scene["elements"]
                self.assertTrue(elements)
                ids = [e["id"] for e in elements]
                self.assertEqual(len(ids), len(set(ids)))
                for element in elements:
                    for field in ("x", "y", "width", "height"):
                        self.assertTrue(math.isfinite(element[field]))
                # Preserved manual scenes use equivalent but differently grouped text.
                if not svg.stem.startswith(("b1-theory-03-", "b1-theory-06-", "b1-theory-08-")):
                    preview = Counter(t.text or "" for t in root.iter(NS + "tspan"))
                    editable = Counter(line for e in elements if e["type"] == "text"
                                       for line in e["text"].splitlines())
                    self.assertEqual(preview, editable, "SVG/source text drift")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theory-dir", type=Path, default=THEORY)
    args = parser.parse_args()
    THEORY = args.theory_dir.resolve()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(VerifyTheory)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("Verified actual Markdown numeric tables and stated graph/search results.")
        print("Coverage: 27/27 subquestions; 24 valid SVG/Excalidraw pairs; local links checked.")
        print("No historical-source authentication or automatic proof of all prose is claimed.")
    sys.exit(0 if result.wasSuccessful() else 1)
