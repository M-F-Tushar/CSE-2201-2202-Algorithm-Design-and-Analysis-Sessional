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

DIAGRAMS = [loop_growth, asymptotic_bounds]
