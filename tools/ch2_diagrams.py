"""Chapter 2 (Complexity Analysis and Asymptotic Notation) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 2 - Complexity Analysis and Asymptotic Notation/diagrams"

# 1 ---------------------------------------------------- loop growth rate
loop_growth = D(
    key="ch2-01-loop-growth-rate",
    title="Loop Growth Rate - Additive vs Multiplicative Steps",
    size=(960, 360),
    flow="H",
    nodes=[
        N("linear", "i = i + 1\nadditive step", 60, 90, 260, 68, "yellow"),
        N("linear_t", "runs n times\nT(n) = O(n)", 450, 90, 260, 68, "green"),
        N("log", "i = i * 2\nmultiplicative step", 60, 210, 260, 68, "yellow"),
        N("log_t", "runs log2(n) times\nT(n) = O(log n)", 450, 210, 260, 68, "green"),
    ],
    edges=[
        E("linear", "linear_t"),
        E("log", "log_t"),
    ],
    caption="Multiplicative steps cut down the problem exponentially fast",
)

# 2 ---------------------------------------------------- asymptotic bounds
asymptotic_bounds = D(
    key="ch2-02-asymptotic-bounds",
    title="Asymptotic Bounds - Big-O, Big-Omega, and Big-Theta",
    size=(960, 520),
    flow="V",
    nodes=[
        N("f", "Function f(n)", 370, 70, 220, 52, "blue", "ellipse", bold=True),
        N("o", "Big-O: f(n) <= c * g(n)\nupper bound", 80, 165, 300, 64, "blue"),
        N("omega", "Big-Omega: f(n) >= c * g(n)\nlower bound", 580, 165, 300, 64, "blue"),
        N("theta", "Do Big-O and Big-Omega\nhold with the same g(n)?", 310, 275, 340, 92, "yellow", "diamond", 15),
        N("tight", "Big-Theta: f(n) = Theta(g(n))\ntight bound (exact order)", 310, 415, 340, 64, "green", bold=True),
    ],
    edges=[
        E("f", "o"),
        E("f", "omega"),
        E("o", "theta"),
        E("omega", "theta"),
        E("theta", "tight", "Yes"),
    ],
    caption="A tight bound requires both upper and lower bounds to match with the same g(n)",
)

# 3 ---------------------------------------------------- best / average / worst
best_avg_worst = D(
    key="ch2-03-best-avg-worst-case",
    title="Best, Average, and Worst Case - Linear Search",
    size=(960, 390),
    flow="V",
    nodes=[
        N("search", "Linear Search on n elements", 300, 40, 360, 52, "blue", bold=True),
        N("best", "Best Case\ntarget at position 1\n1 comparison = Theta(1)", 40, 150, 260, 100, "green", size=14),
        N("avg", "Average Case\ntarget at any position\n(n+1)/2 comparisons = Theta(n)", 350, 150, 260, 100, "yellow", size=14),
        N("worst", "Worst Case\ntarget absent or at the end\nn comparisons = O(n)", 660, 150, 260, 100, "orange", size=14),
        N("note", "Each case is a different input; Theta, O, and Omega can be applied to each case's count", 40, 300, 880, 56, "gray", size=14, bold=True),
    ],
    edges=[
        E("search", "best"),
        E("search", "avg"),
        E("search", "worst"),
    ],
    caption="",
)

# 4 ---------------------------------------------------- growth of common classes
growth_classes = D(
    key="ch2-04-growth-classes",
    title="Growth of Common Complexity Classes - Slowest to Fastest",
    size=(1000, 380),
    flow="H",
    nodes=[
        N("c1", "O(1)", 21, 90, 118, 60, "green"),
        N("c2", "O(log n)", 161, 90, 118, 60, "green"),
        N("c3", "O(n)", 301, 90, 118, 60, "teal"),
        N("c4", "O(n log n)", 441, 90, 118, 60, "teal"),
        N("c5", "O(n^2)", 581, 90, 118, 60, "yellow"),
        N("c6", "O(2^n)", 721, 90, 118, 60, "orange"),
        N("c7", "O(n!)", 861, 90, 118, 60, "red"),
        N("e1", "array\nindexing", 21, 200, 118, 64, "gray", size=13),
        N("e2", "binary\nsearch", 161, 200, 118, 64, "gray", size=13),
        N("e3", "linear\nsearch", 301, 200, 118, 64, "gray", size=13),
        N("e4", "merge\nsort", 441, 200, 118, 64, "gray", size=13),
        N("e5", "bubble sort\nnested loops", 581, 200, 118, 64, "gray", size=13),
        N("e6", "all subsets\n(brute force)", 721, 200, 118, 64, "gray", size=13),
        N("e7", "permutations", 861, 200, 118, 64, "gray", size=13),
        N("note", "Each step to the right grows much faster; O(2^n) and O(n!) fail even for small n", 60, 300, 880, 48, "gray", size=14, bold=True),
    ],
    edges=[
        E("c1", "c2", route="straight"),
        E("c2", "c3", route="straight"),
        E("c3", "c4", route="straight"),
        E("c4", "c5", route="straight"),
        E("c5", "c6", route="straight"),
        E("c6", "c7", route="straight"),
        E("c1", "e1", route="straight"),
        E("c2", "e2", route="straight"),
        E("c3", "e3", route="straight"),
        E("c4", "e4", route="straight"),
        E("c5", "e5", route="straight"),
        E("c6", "e6", route="straight"),
        E("c7", "e7", route="straight"),
    ],
    caption="",
)

DIAGRAMS = [loop_growth, asymptotic_bounds, best_avg_worst, growth_classes]
