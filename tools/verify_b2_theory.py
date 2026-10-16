"""Read-only audit of the reconstructed 2nd Batch Theory answers and visuals.

Run: python tools/verify_b2_theory.py (standard library, Python 3.10+).
Paths are resolved relative to this script, not the current working directory.
Algorithms are implemented independently of the diagram generator. Givens are
read from Markdown; computed traces, table cells, totals, and search-node states
are compared with the actual answers. Historical exam authenticity is not tested.
No files are generated, modified, or deleted. Importing this module runs no audit.
"""

import ast
import heapq
import itertools as it
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote

BASE = Path(__file__).resolve().parents[1] / "Chapter 0 - Previous Year Questions/2nd Batch/Theory"


def expect(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}; expected {expected!r}")


def need(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def match(pattern: str, text: str, label: str, flags: int = 0) -> re.Match[str]:
    result = re.search(pattern, text, flags)
    if result is None:
        raise AssertionError(f"Missing {label}: {pattern}")
    return result


def section(text: str, q: str) -> str:
    return match(rf"(?ms)^#### Q{q[0]}\({q[1]}\).*?(?=^#{{1,4}} |\Z)", text, q).group()


def tables(text: str) -> list[list[list[str]]]:
    result: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in text.splitlines() + [""]:
        if line.startswith("|"):
            current.append([c.strip().replace("**", "") for c in line.strip("|").split("|")])
        elif current:
            need(len(current) >= 2, "Table must have a header and separator")
            result.append(current[2:])
            current = []
    return result


def integers(text: str) -> list[int]:
    return [int(x) for x in re.findall(r"-?\d+", text)]


def unstyle(text: str) -> str:
    return re.sub(r"\\(?:mathbf|mathrm|text)\{([^{}]*)\}", r"\1", text).replace("**", "")


def array(text: str) -> list[int]:
    return integers(match(r"\[\s*-?\d+(?:\s*,\s*-?\d+)*\s*\]", unstyle(text), "array").group())


def arithmetic(text: str) -> Fraction:
    """Evaluate only numeric arithmetic, never eval arbitrary Markdown/code."""
    text = unstyle(text).replace("$", "").replace("−", "-")
    text = re.sub(r"\\frac\{(-?\d+)\}\{(\d+)\}", r"(\1/\2)", text)
    text = text.replace(r"\cdot", "*").replace("×", "*")
    text = re.sub(r"(?<=[\d)])\s*(?=\()|(?<=\))\s*(?=\d)", "*", text)
    def visit(node: ast.AST) -> Fraction:
        if isinstance(node, ast.Constant):
            value = node.value
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                return Fraction(str(value))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            operand = visit(node.operand)
            return -operand if isinstance(node.op, ast.USub) else operand
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            return left / right
        raise AssertionError(f"Unsupported arithmetic: {text!r}")

    return visit(ast.parse(text.strip(), mode="eval").body)


def equation(text: str, expected: int | Fraction, label: str) -> None:
    for expression in text.split("="):
        expect(arithmetic(expression), expected, label)


def matrix(text: str) -> list[list[int]]:
    return [integers(row) for row in text.split(r"\\")]


def check_search(text: str) -> None:
    s = section(text, "3b")
    values = array(s)
    target = int(match(r"target\s*\$(\d+)\$", s, "search target").group(1))
    need(values == sorted(values), "Q3(b): binary search requires sorted input")
    linear, binary, complexity = tables(s)
    expected_linear = []
    for i, value in enumerate(values):
        expected_linear.append([str(i+1), str(i), str(value), "Yes, found" if value == target else "No"])
        if value == target:
            break
    expect(linear, expected_linear, "Q3(b) linear trace")

    def search(key: int) -> list[list[int]]:
        lo, hi, trace = 0, len(values)-1, []
        while lo <= hi:
            mid = (lo+hi)//2
            value = values[mid]
            row = [lo, hi, mid, value]
            trace.append(row)
            if value == key:
                break
            if value < key:
                lo = mid+1
            else:
                hi = mid-1
        return trace

    computed = search(target)
    expect(len(binary), len(computed), "Q3(b) binary trace row count")
    for step, (row, generated) in enumerate(zip(binary, computed), 1):
        expect([int(c) for c in row[:5]], [step]+generated, f"Q3(b) binary step {step}")
        _lo, _hi, mid, value = generated
        if value == target:
            need("Found" in row[5], f"Q3(b) step {step}: found action")
        else:
            field, new = ("lo", mid+1) if value < target else ("hi", mid-1)
            expect(int(match(rf"{field}\s*=\s*(\d+)", row[5], "binary interval update").group(1)), new, "Q3(b) next interval")
            relation = "<" if value < target else ">"
            need(f"{value} {relation} {target}" in row[5], "Q3(b) comparison direction")
    expect(int(match(r"Linear search needs \*\*(\d+) comparisons", s, "linear count").group(1)), len(linear), "Q3(b) linear count")
    expect(int(match(r"finds \d+ at index (\d+)", s, "found index").group(1)), values.index(target), "Q3(b) found index")
    expect(int(match(r"Binary search needs \*\*(\d+)", s, "binary count").group(1)), len(computed), "Q3(b) binary count")
    predicates = sum(1 if row[3] == target else 2 for row in computed)
    expect(int(match(r"uses \*\*(\d+) individual key predicates", s, "predicate count").group(1)), predicates, "Q3(b) predicate count")
    averages = re.findall(r"(\d+)/(\d+)=([\d.]+)", s)
    expect(len(averages), 2, "Q3(b) average count")
    for (numerator, denominator, decimal), total in zip(averages, [sum(range(1, len(values)+1)), sum(len(search(v)) for v in values)]):
        expect((int(numerator), int(denominator)), (total, len(values)), "Q3(b) average fraction")
        expect(Fraction(decimal), Fraction(total, len(values)), "Q3(b) average decimal")
    expect(int(match(r"worst case is \*\*(\d+)", s, "binary worst case").group(1)), max(len(search(v)) for v in values), "Q3(b) worst count")
    expect(len(complexity), 2, "Q3(b) complexity rows")


def check_strassen(text: str) -> None:
    s = section(text, "3c")
    given = {name: matrix(body) for name, body in re.findall(r"([AB])\s*=\s*\\begin\{bmatrix\}(.*?)\\end\{bmatrix\}", s)}
    a, b = given["A"], given["B"]
    (aa, ab), (ac, ad) = a
    (ba, bb), (bc, bd) = b
    products = [aa*(bb-bd), (aa+ab)*bd, (ac+ad)*ba, ad*(bc-ba), (aa+ad)*(ba+bd), (ab-ad)*(bc+bd), (aa-ac)*(ba+bb)]
    rows = tables(s)[0]
    expect(len(rows), len(products), "Q3(c) product count")
    for i, (row, value) in enumerate(zip(rows, products), 1):
        expect(integers(row[0]), [i], "Q3(c) product label")
        expect(int(row[2]), value, f"Q3(c) P{i}")
        expect(arithmetic(row[1].rsplit("=", 1)[1]), value, f"Q3(c) P{i} arithmetic")
    result = [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    combinations = re.findall(r"(?m)^- \$C_\{([12])([12])\}\s*=\s*(.*?)\$", s)
    expect(len(combinations), 4, "Q3(c) combination count")
    for i, j, rhs in combinations:
        symbolic, *numeric = rhs.split("=")
        symbolic = re.sub(r"P_(\d+)", lambda m: f"({products[int(m.group(1))-1]})", symbolic)
        value = result[int(i)-1][int(j)-1]
        expect(arithmetic(symbolic), value, "Q3(c) product-combination formula")
        for expression in numeric:
            expect(arithmetic(expression), value, "Q3(c) output arithmetic")
    expect(matrix(match(r"C = \\begin\{bmatrix\}(.*?)\\end\{bmatrix\}", s, "Strassen result").group(1)), result, "Q3(c) matrix product")


def check_insertion_bubble(text: str) -> None:
    s = section(text, "4a")
    values = array(s)
    a, comparisons, shifts, per_key = values.copy(), 0, 0, []
    for i in range(1, len(a)):
        key, j, checks, moves = a[i], i-1, 0, 0
        while j >= 0:
            checks += 1
            if a[j] <= key:
                break
            a[j+1] = a[j]
            j -= 1
            moves += 1
        a[j+1] = key
        comparisons += checks
        shifts += moves
        per_key.append((checks, moves))
    count = match(r"Total: \*\*(\d+) comparisons\*\*, \*\*(\d+) shifts", s, "insertion totals")
    expect(tuple(map(int, count.groups())), (comparisons, shifts), "Q4(a) insertion totals")
    expect(int(match(r"That is (\d+) comparisons\.", s, "initial insertions").group(1)), sum(c for c, _ in per_key[:-1]), "Q4(a) initial insertion comparisons")
    last = match(r"That is (\d+) comparisons and (\d+) shifts", s, "last insertion")
    expect(tuple(map(int, last.groups())), per_key[-1], "Q4(a) final insertion")
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i+1, len(values)))
    expect(int(match(r"I=(\d+)", s, "inversion count").group(1)), inversions, "Q4(a) inversions")
    a, passes = values.copy(), []
    for end in range(len(a)-1, 0, -1):
        swaps = []
        for j in range(end):
            if a[j] > a[j+1]:
                swaps.append((a[j], a[j+1]))
                a[j], a[j+1] = a[j+1], a[j]
        passes.append((end, swaps, a.copy()))
        if not swaps:
            break
    rows = tables(s)[0]
    expect(len(rows), len(passes), "Q4(a) bubble pass count")
    for step, (row, (count, swaps, state)) in enumerate(zip(rows, passes), 1):
        expect((int(row[0]), int(row[1])), (step, count), "Q4(a) bubble pass/comparisons")
        expect(integers(row[2]), [n for pair in swaps for n in pair], "Q4(a) bubble swaps")
        expect(array(row[3]), state, "Q4(a) bubble state")
    totals = match(r"Total: \*\*(\d+) comparisons\*\*, \*\*(\d+) swaps", s, "bubble totals")
    expect(tuple(map(int, totals.groups())), (sum(p[0] for p in passes), sum(len(p[1]) for p in passes)), "Q4(a) bubble totals")


def check_quicksort_merge(text: str) -> None:
    s = section(text, "4b")
    a = array(s)
    partitions = []

    def quick(lo, hi):
        if lo >= hi:
            return
        pivot, i, steps = a[hi], lo-1, []
        for j in range(lo, hi):
            value = a[j]
            action = None
            if value < pivot:
                i += 1
                action = (i, j)
                a[i], a[j] = a[j], a[i]
            steps.append((j, value, value < pivot, i, action, a.copy()))
        a[i+1], a[hi] = a[hi], a[i+1]
        partitions.append((pivot, steps, a.copy(), a[lo:i+1], a[i+2:hi+1], a[lo:hi+1]))
        quick(lo, i)
        quick(i+2, hi)

    quick(0, len(a)-1)
    rows = tables(s)[0]
    expect(len(rows), len(partitions[0][1]), "Q4(b) first partition row count")
    previous = array(s)
    for row, (j, value, less, i, action, state) in zip(rows, partitions[0][1]):
        expect((int(row[0]), int(row[1]), row[2]), (j, value, "Yes" if less else "No"), "Q4(b) partition comparison")
        if action is not None:
            expect(int(match(r"i\s*=\s*(\d+)", row[3], "partition i").group(1)), i, "Q4(b) partition i")
            if action[0] == action[1]:
                need("itself" in row[3], "Q4(b): self-swap action")
            else:
                expect([int(v) for v in re.findall(r"a\[(\d+)\]", row[3])], list(action), "Q4(b) swap indices")
        else:
            expect(row[3], "nothing", "Q4(b) no-swap action")
        actual = previous if row[4] == "same" else integers(row[4])
        expect(actual, state, "Q4(b) per-comparison state")
        previous = actual
    pass_blocks = re.split(r"\*\*Pass \d+", s)[1:]
    expect(len(pass_blocks), len(partitions), "Q4(b) partition count")
    for index, (block, (pivot, steps, state, left, right, local)) in enumerate(zip(pass_blocks, partitions)):
        expect(int(match(r"pivot = (\d+)", block, "pivot", re.IGNORECASE).group(1)), pivot, "Q4(b) pivot")
        if index == 0:
            after = match(r"Finally,.*?: \*\*([\d, ]+)\*\*", block, "pivot-swap state").group(1)
            expect(integers(after), state, "Q4(b) first pivot swap")
            expect(array(match(r"Left part: (.*)", block, "left partition").group(1)), left, "Q4(b) left partition")
            expect(array(match(r"Right part: (.*)", block, "right partition").group(1)), right, "Q4(b) right partition")
        elif index == 1:
            expect(integers(match(r"Swap the pivot.*?: \*\*([\d, ]+)\*\*", block, "second partition result").group(1)), local, "Q4(b) second pivot swap")
            need(not left and "Left part is empty" in block, "Q4(b) empty second left partition")
            expect(array(match(r"Right part is (.*)", block, "second right partition").group(1)), right, "Q4(b) second right partition")
        else:
            expect(integers(match(r"Result: \*\*([\d, ]+)\*\*", block, "third result").group(1)), local, "Q4(b) third partition")
            expect(array(match(r"left side is (.*)", block, "third left side").group(1)), left, "Q4(b) third left partition")
            need(not right and "right side is empty" in block, "Q4(b) empty third right partition")
    count = int(match(r"\*\*(\d+) key–pivot comparisons", s, "quicksort count").group(1))
    expect(count, sum(len(p[1]) for p in partitions), "Q4(b) total comparisons")
    expect(array(match(r"Final sorted array: (.*)", s, "quicksort output").group(1)), a, "Q4(b) sorted output")

    s = section(text, "4c")
    merges = []

    def merge_sort(values: list[int]) -> list[int]:
        if len(values) < 2:
            return values
        mid = (len(values)+1)//2
        left, right = merge_sort(values[:mid]), merge_sort(values[mid:])
        result, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        merges.append((left, right, result))
        return result

    merge_sort(array(s))
    expect([[int(row[0])]+[array(c) for c in row[1:]] for row in tables(s)[0]], [[i, *parts] for i, parts in enumerate(merges, 1)], "Q4(c) every merge input and output")


def check_fractional_mst(text: str) -> None:
    s = section(text, "5b")
    capacity = int(match(r"W\s*=\s*(\d+)", s, "fractional capacity").group(1))
    givens = s.split("\n", 1)[0]
    items = [tuple(map(int, pair)) for pair in re.findall(r"\((\d+),\s*(\d+)\)", givens)]
    rows, selections = tables(s)
    order = sorted(range(len(items)), key=lambda i: Fraction(items[i][1], items[i][0]), reverse=True)
    expect(len(rows), len(items), "Q5(b) item rows")
    for i, (row, (w, p)) in enumerate(zip(rows, items)):
        expect([int(c) for c in row[:3]], [i+1, w, p], "Q5(b) item givens")
        expect(Fraction(row[3]), Fraction(p, w), "Q5(b) density")
        expect(int(match(r"\d+", row[4], "density rank").group()), order.index(i)+1, "Q5(b) rank")
    used, profit, chosen, computed = 0, Fraction(0), [Fraction(0)]*len(items), []
    for i in order:
        w, p = items[i]
        fraction = min(Fraction(1), Fraction(capacity-used, w))
        if fraction <= 0:
            break
        chosen[i] = fraction
        used += fraction*w
        profit += fraction*p
        computed.append((i+1, fraction, used, profit))
    expect(len(selections), len(computed), "Q5(b) selection rows")
    for step, (row, (item, fraction, weight, cumulative)) in enumerate(zip(selections, computed), 1):
        expect(int(row[0]), step, "Q5(b) step")
        expect(int(match(r"item (\d+)", row[1], "selected item").group(1)), item, "Q5(b) selection order")
        if fraction == 1:
            need(row[1].startswith("All"), "Q5(b) full selection")
        else:
            expect(arithmetic(match(r"\\frac\{\d+\}\{\d+\}", row[1], "selected fraction").group()), fraction, "Q5(b) fraction")
        expect(Fraction(row[2]), weight, "Q5(b) cumulative weight")
        equation(row[3], cumulative, "Q5(b) cumulative profit")
    expect(int(match(r"Maximum profit: (\d+)", s, "fractional optimum").group(1)), profit, "Q5(b) reported optimum")
    fractions = match(r"fractions \$\((.*?)\)\$", s, "selection vector").group(1)
    expect([Fraction(c) for c in fractions.split(",")], chosen, "Q5(b) selection vector")
    vertices = []
    for fractional in range(len(items)):
        other = [i for i in range(len(items)) if i != fractional]
        for bits in it.product([0, 1], repeat=len(other)):
            weight = sum(items[i][0]*b for i, b in zip(other, bits))
            value = sum(items[i][1]*b for i, b in zip(other, bits))
            if weight <= capacity:
                fraction = min(Fraction(1), Fraction(capacity-weight, items[fractional][0]))
                vertices.append(value+fraction*items[fractional][1])
    expect(profit, max(vertices), "Q5(b) independent LP-vertex optimum")
    integer_optimum = max(sum(p*b for (_, p), b in zip(items, bits)) for bits in it.product([0, 1], repeat=len(items)) if sum(w*b for (w, _), b in zip(items, bits)) <= capacity)
    expect(int(match(r"0/1 optimum is (\d+)", s, "integer optimum").group(1)), integer_optimum, "Q5(b) exhaustive 0/1 optimum")

    s = section(text, "5c")
    edges = [tuple(map(int, triple)) for triple in re.findall(r"\((\d+),(\d+)\)=(\d+)", s)]
    vertices = set(integers(match(r"V=\\\{(.*?)\\\}", s, "MST vertices").group(1)))
    expect(edges, sorted(edges, key=lambda e: e[2]), "Q5(c) sorted edges")
    need(len({frozenset(e[:2]) for e in edges}) == len(edges), "Q5(c) unique edges")

    def reachable(start, selected):
        seen = {start}
        while True:
            new = seen | {b for a, b, _ in selected if a in seen} | {a for a, b, _ in selected if b in seen}
            if new == seen:
                return seen
            seen = new

    chosen_edges, computed, cost = [], [], 0
    for a, b, weight in edges:
        cycle = b in reachable(a, chosen_edges)
        if not cycle:
            chosen_edges.append((a, b, weight))
            cost += weight
        computed.append((a, b, weight, cycle, cost, chosen_edges.copy()))
        if len(chosen_edges) == len(vertices)-1:
            break
    rows = tables(s)[0]
    expect(len(rows), len(computed), "Q5(c) Kruskal row count")
    for i, (row, (a, b, weight, cycle, cost, selected)) in enumerate(zip(rows, computed), 1):
        expect((int(row[0]), integers(row[1]), int(row[2])), (i, [a, b], weight), "Q5(c) edge step")
        expect(row[3].startswith("Yes"), cycle, "Q5(c) cycle detection")
        expect(row[4], "Skip (cycle)" if cycle else "Take", "Q5(c) action")
        expect(int(row[5]), cost, "Q5(c) cumulative cost")
        if cycle:
            path = [int(v) for v in re.findall(r"\d+", row[3])]
            expect((path[0], path[-1]), (a, b), "Q5(c) cycle-witness endpoints")
            need(all(any({u, v} == {x, y} for x, y, _ in selected) for u, v in it.pairwise(path)), "Q5(c) cycle witness uses chosen edges")
    tree_costs = [sum(w for _, _, w in subset) for subset in it.combinations(edges, len(vertices)-1) if reachable(next(iter(vertices)), subset) == vertices]
    expect(cost, min(tree_costs), "Q5(c) exhaustive spanning-tree optimum")
    expression = match(r"Total MST cost = ([^*\n]+)", s, "MST total").group(1).rstrip(". ")
    equation(expression, cost, "Q5(c) total arithmetic")
    need(tree_costs.count(cost) > 1 and "MST is not unique" in s, "Q5(c) multiple optimum trees")
    replacement = match(r"replaces \((\d+),(\d+)\) by \((\d+),(\d+)\)", s, "alternative MST")
    a, b, c, d = map(int, replacement.groups())
    alternative = [e for e in chosen_edges if set(e[:2]) != {a, b}] + [e for e in edges if set(e[:2]) == {c, d}]
    expect((len(alternative), reachable(next(iter(vertices)), alternative), sum(e[2] for e in alternative)), (len(vertices)-1, vertices, cost), "Q5(c) alternative MST")


def check_dp(text: str) -> None:
    s = section(text, "6a")
    calls = Counter()

    def fib(n: int) -> int:
        calls[n] += 1
        return n if n < 2 else fib(n-1)+fib(n-2)

    fib(5)
    expect(int(match(r"makes \*\*(\d+)\*\* calls", s, "Fibonacci calls").group(1)), sum(calls.values()), "Q6(a) recursive calls")
    expect(calls, {5: 1, 4: 1, 3: 2, 2: 3, 1: 5, 0: 3}, "Q6(a) call multiplicities")
    expect(array(match(r"table for.*?is (.*)", s, "Fibonacci table").group(1)), [fib(i) for i in range(6)], "Q6(a) table")

    infinity = float("inf")

    def readmatrix(rows: list[list[str]]) -> list[list[int | float]]:
        return [[infinity if c == "∞" else int(c) for c in row[1:]] for row in rows]

    s = section(text, "6b")
    matrices = tables(s)
    expect(len(matrices), 4, "Q6(b) displayed matrix count")
    distance = readmatrix(matrices[0])
    stages = [distance]
    for k in range(len(distance)):
        distance = [[min(distance[i][j], distance[i][k]+distance[k][j]) for j in range(len(distance))] for i in range(len(distance))]
        stages.append(distance)
    expect(stages[1], stages[0], "Q6(b) D1=D0")
    expect(stages[4], stages[3], "Q6(b) D4=D3")
    for rows, k in zip(matrices, [0, 2, 3, 4]):
        expect(readmatrix(rows), stages[k], f"Q6(b) D{k}")

    s = section(text, "6c")
    heading = unstyle(s.splitlines()[0])
    x = match(r"\$X\s*=\s*([A-Z]+)\s*\$", heading, "LCS string X").group(1)
    y = match(r"\$Y\s*=\s*([A-Z]+)\s*\$", heading, "LCS string Y").group(1)
    lengths = [[0]*(len(y)+1) for _ in range(len(x)+1)]
    for i, a in enumerate(x, 1):
        for j, b in enumerate(y, 1):
            lengths[i][j] = lengths[i-1][j-1]+1 if a == b else max(lengths[i-1][j], lengths[i][j-1])
    expect([[int(c) for c in row[1:]] for row in tables(s)[0]], lengths, "Q6(c) all LCS cells")
    current, letters = (len(x), len(y)), []
    lines = re.findall(r"(?m)^\d+\. .*", s)
    for line in lines:
        positions = [tuple(map(int, p)) for p in re.findall(r"\$\((\d+),(\d+)\)\$", line)]
        expect(len(positions), 2, "Q6(c) traceback coordinates")
        start, end = positions
        expect(start, current, "Q6(c) traceback continuity")
        i, j = start
        if x[i-1] == y[j-1]:
            expect(end, (i-1, j-1), "Q6(c) matching diagonal")
            letters.append(x[i-1])
            need(f"Take **{x[i-1]}**" in line, "Q6(c) traceback letter")
        else:
            need(end in [(i-1, j), (i, j-1)], "Q6(c) mismatch move")
            expect(lengths[end[0]][end[1]], lengths[i][j], "Q6(c) traceback preserves length")
        current = end
    need(0 in current, "Q6(c) traceback reaches empty prefix")
    lcs = match(r"LCS = ([A-Z]+), length = (\d+)", s, "LCS result")
    expect(lcs.group(1), "".join(reversed(letters)), "Q6(c) recovered LCS")
    expect(int(lcs.group(2)), lengths[-1][-1], "Q6(c) optimum length")

    s = section(text, "8c")
    # Unlike Floyd's distances, the complete TSP matrix has finite integer costs.
    costs = [[int(c) for c in row[1:]] for row in tables(s)[0]]

    @lru_cache(None)
    def g(i: int, remaining: tuple[int, ...]) -> int:
        return min(costs[i-1][j-1]+g(j, tuple(k for k in remaining if k != j)) for j in remaining) if remaining else costs[i-1][0]

    states = []
    for rows in tables(s)[1:]:
        for row in rows:
            state = integers(row[0])
            states.append((state[0], tuple(state[1:])))
            expect(int(row[2]), g(state[0], tuple(state[1:])), "Q8(c) Held-Karp state")
    required_states = [(i, subset) for size in range(1, len(costs)-1) for i in range(2, len(costs)+1) for subset in it.combinations([j for j in range(2, len(costs)+1) if j != i], size)]
    expect(Counter(states), Counter(required_states), "Q8(c) complete subset-state tables")
    bases = re.findall(r"g\((\d+), \\varnothing\).*?= (\d+)\$", s)
    expect([int(city) for city, _ in bases], list(range(2, len(costs)+1)), "Q8(c) complete base states")
    for city, value in bases:
        expect(int(value), g(int(city), ()), "Q8(c) empty-subset state")
    tours = [(1,)+p+(1,) for p in it.permutations(range(2, len(costs)+1))]
    values = [sum(costs[a-1][b-1] for a, b in it.pairwise(t)) for t in tours]
    expect(g(1, tuple(range(2, len(costs)+1))), min(values), "Q8(c) exhaustive TSP optimum")
    expect(int(match(r"Minimum tour cost = (\d+)", s, "TSP optimum").group(1)), min(values), "Q8(c) reported optimum")
    expect(integers(match(r"costs \*\*([^*]+)\*\* in lexicographic order", s, "all tour costs").group(1)), values, "Q8(c) all tours")


def check_colouring_queens(text: str) -> None:
    s = section(text, "7a")
    edges = [tuple(map(int, p)) for p in re.findall(r"(\d+)-(\d+)", match(r"Sample graph:\*\* (.*)", s, "colour graph").group(1))]
    vertices = sorted({v for e in edges for v in e})
    palette, colours, events = ["Red", "Green", "Blue"], {}, []

    def colour(index):
        if index == len(vertices):
            events[-1] = (*events[-1][:2], "Solution")
            return True
        v = vertices[index]
        for c in palette:
            if all(colours.get(u) != c for u in vertices if (u, v) in edges or (v, u) in edges):
                colours[v] = c
                events.append((v, c, "Coloured"))
                if colour(index+1):
                    return True
                del colours[v]
        events.append((v, "none", "Dead end"))
        return False

    need(colour(0), "Q7(a) 3-colouring exists")
    rows = tables(s)[0]
    expect(len(rows), len(events), "Q7(a) event count")
    for step, (row, (vertex, c, result)) in enumerate(zip(rows, events), 1):
        expect((int(row[0]), row[1], row[2], row[4]), (step, f"v{vertex}", c, result), "Q7(a) colouring/backtracking event")
    final = match(r"Final colouring:\*\* (.*?)\.", s, "final colouring").group(1)
    expect({int(v): c for v, c in re.findall(r"v(\d+) (Red|Green|Blue)", final)}, colours, "Q7(a) final colouring")
    need(all(colours[a] != colours[b] for a, b in edges), "Q7(a) edge constraints")
    chromatic = next(m for m in range(1, len(vertices)+1) if any(all(cs[vertices.index(a)] != cs[vertices.index(b)] for a, b in edges) for cs in it.product(range(m), repeat=len(vertices))))
    expect(int(match(r"chromatic number is \*\*(\d+)", s, "chromatic number").group(1)), chromatic, "Q7(a) exhaustive chromatic number")

    s = section(text, "7c")
    n = int(match(r"N = (\d+)", s, "queen count").group(1))
    solutions = [cols for cols in it.permutations(range(1, n+1)) if all(abs(i-j) != abs(cols[i]-cols[j]) for i in range(n) for j in range(i))]
    rows = tables(s)[0]
    expect(len(rows), n, "Q7(c) first-solution row count")
    for i, row in enumerate(rows, 1):
        expect((int(row[0]), array(row[3])), (i, list(solutions[0][:i])), "Q7(c) partial board")

    def safe(cols, c):
        return all(c != prev and abs(c-prev) != len(cols)-r for r, prev in enumerate(cols))

    expect([c for c in range(1, n+1) if safe([1, 5], c)], [2], "Q7(c) dead-end prefix")
    expect([c for c in range(1, n+1) if safe([1, 5, 2], c)], [], "Q7(c) no safe fourth column")

    def transforms(cols):
        forms = []
        for reflect in [False, True]:
            pts = [(r, n-c if reflect else c-1) for r, c in enumerate(cols)]
            for _ in range(4):
                forms.append(tuple(c+1 for _, c in sorted(pts)))
                pts = [(c, n-1-r) for r, c in pts]
        return forms

    expect(int(match(r"\*\*(\d+) distinct boards", s, "queen solutions").group(1)), len(solutions), "Q7(c) solution count")
    expect(int(match(r"\*\*(\d+)\*\* symmetry classes", s, "symmetry classes").group(1)), len({min(transforms(cols)) for cols in solutions}), "Q7(c) symmetry count")
    expect(array(match(r"second ascending-column solution is (.*)", s, "second solution").group(1)), list(solutions[1]), "Q7(c) second solution")
    board = match(r"```\n([Q. \n]+)\n```", s, "queen board").group(1).splitlines()
    expect([row.split().index("Q")+1 for row in board], list(solutions[0]), "Q7(c) final board")


def decisions(cell: str, names: list[str]) -> tuple[int, ...]:
    if cell.lower() == "root":
        return ()
    pairs = re.findall(r"([A-Z]\d*)\s*=\s*([01])", cell)
    expect([name for name, _ in pairs], names[:len(pairs)], "Search-node decision order")
    need(bool(pairs), f"Unparsed search node: {cell}")
    return tuple(int(b) for _, b in pairs)


@dataclass
class KnapsackNode:
    weight: int
    profit: int
    upper: Fraction | None
    status: str


def check_lc_jobs(text: str) -> None:
    s = section(text, "7b")
    capacity = int(match(r"capacity \$W = (\d+)", s, "LC capacity").group(1))
    given = [(name, int(w), int(p)) for name, w, p in re.findall(r"\*\*([A-Z])\*\* \((\d+), (\d+)\)", s)]
    names = [name for name, _, _ in given]
    need(len(names) >= 4, "Q7(b) at least four items")
    expect(given, sorted(given, key=lambda item: Fraction(item[2], item[1]), reverse=True), "Q7(b) density order")

    def value(bits: tuple[int, ...]) -> tuple[int, int]:
        return sum(w*b for (_, w, _), b in zip(given, bits)), sum(p*b for (_, _, p), b in zip(given, bits))

    def bound(bits: tuple[int, ...]) -> Fraction | None:
        w, p = value(bits)
        if w > capacity:
            return None
        cap, upper = capacity-w, Fraction(p)
        for _, weight, profit in given[len(bits):]:
            take = min(cap, weight)
            upper += Fraction(take*profit, weight)
            cap -= take
        return upper

    root_bound = bound(())
    if root_bound is None:
        raise AssertionError("Q7(b) feasible root")
    heap: list[tuple[Fraction, int, tuple[int, ...]]] = [(-root_bound, 0, ())]
    serial, best, expansions, incumbents = 0, 0, [], [0]
    nodes: dict[tuple[int, ...], KnapsackNode] = {(): KnapsackNode(*value(()), root_bound, "pending")}
    while heap:
        neg, _, bits = heapq.heappop(heap)
        if -neg <= best:
            nodes[bits].status = "pruned"
            continue
        expansions.append(bits)
        nodes[bits].status = "expand"
        for bit in [1, 0]:
            child = bits+(bit,)
            w, p = value(child)
            upper = bound(child)
            nodes[child] = KnapsackNode(w, p, upper, "infeasible" if upper is None else "pending")
            if upper is None:
                continue
            improved = p > best
            if improved:
                best = p
                incumbents.append(best)
            if upper <= best:
                nodes[child].status = "solution" if improved else "pruned"
            else:
                serial += 1
                heapq.heappush(heap, (-upper, serial, child))
    rows = tables(s)[0]
    expect([decisions(row[0], names) for row in rows], list(nodes), "Q7(b) generated-node order and completeness")
    for row in rows:
        bits = decisions(row[0], names)
        node = nodes[bits]
        w, p, upper, status = node.weight, node.profit, node.upper, node.status
        expect([int(row[2]), int(row[3])], [w, p], f"Q7(b) node {bits} weight/profit")
        expect(None if row[4] == "—" else Fraction(row[4]), upper, f"Q7(b) node {bits} bound")
        actual = next((tag for tag in ["infeasible", "solution", "pruned", "expand"] if tag in row[5].lower()), None)
        expect(actual, status, f"Q7(b) node {bits} status")
        if status == "pruned":
            if upper is None:
                raise AssertionError("Q7(b) pruned feasible node must have a bound")
            expect(integers(row[5]), [int(upper), best], "Q7(b) pruning inequality")
        descendants = [value(bits+tail) for tail in it.product([0, 1], repeat=len(given)-len(bits))]
        if upper is not None:
            need(upper >= max(p for w, p in descendants if w <= capacity), "Q7(b) bound admissibility")
    order = match(r"Actual pop/expansion order:\*\* (.*?)\.", s, "LC expansion order").group(1).split(" → ")
    expect([decisions(node, names) for node in order], expansions, "Q7(b) FIFO expansion order")
    updates = match(r"Thus profits (\d+) and (\d+) are incumbents before (\d+)", s, "LC incumbents")
    expect([int(v) for v in updates.groups()], incumbents[1:], "Q7(b) incumbent sequence")
    expect(best, max(p for bits in it.product([0, 1], repeat=len(given)) for w, p in [value(bits)] if w <= capacity), "Q7(b) exhaustive optimum")
    expect(int(match(r"Profit = (\d+)", s, "LC optimum").group(1)), best, "Q7(b) reported optimum")

    s = section(text, "8b")
    given = [(name, int(p), int(d)) for name, p, d in re.findall(r"(J\d+) \(profit (\d+), deadline (\d+)\)", s)]
    names = [name for name, _, _ in given]
    need(bool(names), "Q8(b) job givens")
    expect(given, sorted(given, key=lambda item: item[1], reverse=True), "Q8(b) profit order")

    def feasible(bits: tuple[int, ...]) -> bool:
        deadlines = sorted(d for (_, _, d), b in zip(given, bits) if b)
        return all(i <= deadline for i, deadline in enumerate(deadlines, 1))

    def profit(bits: tuple[int, ...]) -> int:
        return sum(p*b for (_, p, _), b in zip(given, bits))

    best, trace = 0, []

    def visit(bits: tuple[int, ...]) -> None:
        nonlocal best
        current = profit(bits)
        upper = current+sum(p for _, p, _ in given[len(bits):])
        status = "infeasible" if not feasible(bits) else "pruned" if upper <= best else "leaf" if len(bits) == len(given) else "branch"
        trace.append((bits, current, upper, status))
        if status == "leaf":
            best = max(best, current)
        elif status == "branch":
            visit(bits+(1,))
            visit(bits+(0,))

    visit(())
    rows = tables(s)[0]
    expect([decisions(row[0], names) for row in rows], [node[0] for node in trace], "Q8(b) DFS node sequence and completeness")
    for row, (bits, current, upper, status) in zip(rows, trace):
        if status == "infeasible":
            expect(row[2:4], ["—", "—"], "Q8(b) infeasible placeholders")
            violation = match(r"(\d+) jobs with deadline ≤ (\d+)", row[4], "deadline violation")
            count, deadline = map(int, violation.groups())
            expect(count, sum(b and d <= deadline for (_, _, d), b in zip(given, bits)), "Q8(b) infeasibility witness")
            need(count > deadline, "Q8(b) witness actually violates feasibility")
        else:
            expect([int(c) for c in row[2:4]], [current, upper], f"Q8(b) node {bits} profit/bound")
        actual = "leaf" if "Best" in row[4] else "infeasible" if "Infeasible" in row[4] else "pruned" if "Pruned" in row[4] else "branch" if "Branch" in row[4] else None
        expect(actual, status, f"Q8(b) node {bits} status")
        if status == "pruned":
            expect(integers(row[4]), [upper, best], "Q8(b) pruning inequality")
        if feasible(bits):
            reachable = [profit(bits+tail) for tail in it.product([0, 1], repeat=len(given)-len(bits)) if feasible(bits+tail)]
            need(upper >= max(reachable), "Q8(b) bound admissibility")
    expect(best, max(profit(bits) for bits in it.product([0, 1], repeat=len(given)) if feasible(bits)), "Q8(b) exhaustive optimum")
    expect(int(match(r"Maximum profit = \*\*(\d+)", s, "job optimum").group(1)), best, "Q8(b) reported optimum")


def check_visuals(text: str) -> None:
    diagrams = BASE / "diagrams"
    used = []
    for n in range(1, 9):
        for part in "abc":
            images = re.findall(r"!\[[^\]]*\]\((diagrams/[^)]+\.svg)\)", section(text, f"{n}{part}"))
            expect(len(images), 1, f"Q{n}({part}) diagram coverage")
            used.extend(images)
    expect(len(set(used)), 24, "Distinct subquestion diagrams")
    index = (diagrams / "README.md").read_text(encoding="utf-8")
    for path, content in [(BASE / "README.md", text), (diagrams / "README.md", index)]:
        for raw in re.findall(r"\]\(([^)]+)\)", content):
            if not raw.startswith(("http:", "https:", "#")):
                need((path.parent / unquote(raw.split("#")[0])).exists(), f"Broken link in {path.name}: {raw}")
    expect(len(list(diagrams.glob("*.svg"))), 25, "SVG count including roadmap")
    expect(len(list(diagrams.glob("*.excalidraw"))), 25, "Editable-scene count including roadmap")
    for svg in sorted(diagrams.glob("*.svg")):
        scene = json.loads(svg.with_suffix(".excalidraw").read_text(encoding="utf-8"))
        expect((scene["type"], scene["version"]), ("excalidraw", 2), svg.name)
        expect(len({e["id"] for e in scene["elements"]}), len(scene["elements"]), f"{svg.name} unique IDs")
        need(svg.name in index and svg.with_suffix(".excalidraw").name in index, f"{svg.name} index coverage")
        svg_text = "".join("".join(e.itertext()) for e in ET.parse(svg).getroot().iter() if e.tag.endswith("}text"))
        scene_text = "".join(e.get("text", "") for e in scene["elements"] if e["type"] == "text")
        expect(re.sub(r"\s+", "", svg_text), re.sub(r"\s+", "", scene_text), f"{svg.name} source/preview text")
        need(not any(e["type"] == "image" for e in scene["elements"]), f"{svg.name} editable vector content")


def verify(text: str | None = None) -> None:
    """Check disk content, or an in-memory Markdown variant for regression tests."""
    if text is None:
        text = (BASE / "README.md").read_text(encoding="utf-8")
    checks = [check_search, check_strassen, check_insertion_bubble, check_quicksort_merge, check_fractional_mst, check_dp, check_colouring_queens, check_lc_jobs, check_visuals]
    for check in checks:
        check(text)
        print(f"PASS: {check.__name__.removeprefix('check_')}")
    print("PASS: Batch 2 numeric tables, generated search nodes, exhaustive optima, links, and 25 diagram pairs")


if __name__ == "__main__":
    verify()
