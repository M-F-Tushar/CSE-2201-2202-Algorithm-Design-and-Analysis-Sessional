"""Chapter 3 (Recurrences Correctness and Loop Invariants) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 3 - Recurrences Correctness and Loop Invariants/diagrams"

# 1 ---------------------------------------------------- recursion tree
recursion_tree = D(
    key="ch3-01-recursion-tree",
    title="Recursion Tree for T(n) = T(n/2) + c",
    size=(760, 600),
    flow="V",
    nodes=[
        N("n1", "n , cost c", 240, 70, 280, 52, "blue"),
        N("n2", "n/2 , cost c", 240, 155, 280, 52, "blue"),
        N("n4", "n/4 , cost c", 240, 240, 280, 52, "blue"),
        N("n8", "n/8 , cost c", 240, 325, 280, 52, "blue"),
        N("dots", "... log2(n) levels total", 240, 410, 280, 52, "blue", bold=True),
        N("base", "n / 2^k = 1 , base case reached\nTotal cost = Theta(log n)", 190, 495, 380, 60, "green", bold=True),
    ],
    edges=[
        E("n1", "n2"),
        E("n2", "n4"),
        E("n4", "n8"),
        E("n8", "dots"),
        E("dots", "base"),
    ],
    caption="Each level does constant work c across log2(n) levels yielding logarithmic complexity",
)

# 2 ---------------------------------------------------- master theorem cases
master_cases = D(
    key="ch3-02-master-theorem-cases",
    title="Master Theorem Decision Flow - T(n) = aT(n/b) + f(n)",
    size=(1200, 560),
    flow="V",
    nodes=[
        N("start", "Recurrence: T(n) = aT(n/b) + f(n)", 430, 70, 340, 52, "yellow", bold=True),
        N("compute", "Compute watershed function:\nn^(log_b a)", 430, 155, 340, 54, "yellow"),
        N("compare", "Compare f(n) with n^(log_b a)", 410, 245, 380, 84, "blue", "diamond", 15),
        N("case1", "Case 1: Leaves Dominate\nf(n) polynomially smaller\nT(n) = Theta(n^(log_b a))", 40, 395, 350, 90, "green", size=14),
        N("case2", "Case 2: Balanced Work\nsame order (+ log^k n factor)\nT(n) = Theta(n^(log_b a) * log^(k+1) n)", 425, 395, 350, 90, "green", size=13),
        N("case3", "Case 3: Root Dominates\nf(n) polynomially larger + regularity\nT(n) = Theta(f(n))", 810, 395, 350, 90, "green", size=14),
    ],
    edges=[
        E("start", "compute"),
        E("compute", "compare"),
        E("compare", "case1", "f(n) smaller"),
        E("compare", "case2", "same order"),
        E("compare", "case3", "f(n) larger"),
    ],
    caption="Compare the work at the leaves against the work done at the root",
)

DIAGRAMS = [recursion_tree, master_cases]
