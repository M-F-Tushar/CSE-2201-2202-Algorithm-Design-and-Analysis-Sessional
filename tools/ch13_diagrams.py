"""Chapter 13 (Approximation Algorithms) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 13 - Approximation Algorithms/diagrams"

S = "straight"
GREEN = "#2f9e44"
RED = "#e03131"
GRAY = "#868e96"

# 1 ---------------------------------------------------- exact vs approximate
concept = D(
    key="ch13-01-exact-vs-approximation",
    title="Exact vs Approximation Algorithms for NP-Hard Problems",
    size=(1200, 400),
    flow="H",
    nodes=[
        N("p", "NP-hard\noptimization\nproblem", 40, 140, 200, 90, "yellow", "ellipse", 15, True),
        N("ex", "Exact algorithm\noptimal answer C*\nexponential time in the worst case", 330, 50, 360, 90, "red"),
        N("ap", "Approximation algorithm\npolynomial time\nanswer C is provably close to C*", 330, 230, 360, 90, "blue"),
        N("g", "Performance guarantee\nratio rho(n) = max(C/C*, C*/C)\nminimization: C <= rho * C*", 800, 230, 350, 90, "green", "rect", 15, True),
    ],
    edges=[
        E("p", "ex"),
        E("p", "ap"),
        E("ap", "g"),
    ],
    caption="We give up optimality, but keep a proven bound on how far the answer can be from optimal",
)

# 2 ---------------------------------------------------- vertex cover
vertex_cover = D(
    key="ch13-02-vertex-cover-2-approx",
    title="APPROX-VERTEX-COVER on the Path a-b-c-d-e-f",
    size=(1000, 420),
    flow="H",
    nodes=[
        N("a", "a", 50, 110, 80, 60, "green", "ellipse", 18, True),
        N("b", "b", 220, 110, 80, 60, "green", "ellipse", 18, True),
        N("c", "c", 390, 110, 80, 60, "green", "ellipse", 18, True),
        N("d", "d", 560, 110, 80, 60, "green", "ellipse", 18, True),
        N("e", "e", 730, 110, 80, 60, "green", "ellipse", 18, True),
        N("f", "f", 900, 110, 80, 60, "green", "ellipse", 18, True),
        N("note", "Chosen edges (red): ab, cd, ef - no two share an endpoint, so M is a matching, |M| = 3\nAlgorithm returns both endpoints of each chosen edge: C = {a,b,c,d,e,f}, |C| = 6\nAny cover needs one vertex per matching edge, so OPT >= 3 (e.g. {b,d,e}); 6 <= 2 x OPT", 70, 260, 860, 90, "gray", "rect", 14),
    ],
    edges=[
        E("a", "b", route=S, color=RED, directed=False),
        E("b", "c", route=S, color=GRAY, directed=False),
        E("c", "d", route=S, color=RED, directed=False),
        E("d", "e", route=S, color=GRAY, directed=False),
        E("e", "f", route=S, color=RED, directed=False),
    ],
    caption="The returned cover is exactly twice the optimum here, so the ratio 2 cannot be improved for this algorithm",
)

# 3 ---------------------------------------------------- TSP 2-approximation
tsp = D(
    key="ch13-03-tsp-2-approximation",
    title="TSP 2-Approximation: MST, Walk, Shortcut",
    size=(1000, 430),
    flow="H",
    nodes=[
        N("c0", "0", 80, 110, 80, 60, "yellow", "ellipse", 18, True),
        N("c1", "1", 330, 110, 80, 60, "blue", "ellipse", 18, True),
        N("c2", "2", 580, 110, 80, 60, "blue", "ellipse", 18, True),
        N("c3", "3", 830, 110, 80, 60, "blue", "ellipse", 18, True),
        N("note", "MST edges (green): 2-3 (12), 0-1 (20), 1-2 (30); MST weight = 62 <= OPT\nFull walk 0-1-2-3-2-1-0 costs 2 x 62 = 124\nShortcutting repeated cities (triangle inequality) gives tour 0-1-2-3-0 = 97 <= 124", 100, 310, 800, 90, "gray", "rect", 14),
    ],
    edges=[
        E("c0", "c1", "20", route=S, color=GREEN, directed=False),
        E("c1", "c2", "30", route=S, color=GREEN, directed=False),
        E("c2", "c3", "12", route=S, color=GREEN, directed=False),
        E("c3", "c0", "shortcut 3 to 0: 35", route="loopb", bend=90, color=RED, dashed=True),
    ],
    caption="Preorder walk of the MST from city 0 visits 0, 1, 2, 3 and returns to 0",
)

# 4 ---------------------------------------------------- greedy set cover
set_cover = D(
    key="ch13-04-greedy-set-cover",
    title="Greedy Set Cover on U = {1,...,6}",
    size=(1300, 390),
    flow="H",
    nodes=[
        N("u", "Universe U\n{1,2,3,4,5,6}\nall uncovered", 30, 130, 180, 90, "yellow", "ellipse", 14, True),
        N("r1", "Round 1\nG = {1,2,3,4}\ncovers 4 new elements", 260, 130, 230, 90, "blue", "rect", 14),
        N("r2", "Round 2\nX = {1,3,5}\ncovers 1 new element (5)", 540, 130, 230, 90, "blue", "rect", 14),
        N("r3", "Round 3\nY = {2,4,6}\ncovers 1 new element (6)", 820, 130, 230, 90, "blue", "rect", 14),
        N("res", "Greedy cover\n{G, X, Y}\n3 sets", 1100, 130, 170, 90, "green", "rect", 14, True),
        N("opt", "Optimal cover: {X, Y} - only 2 sets. Ratio 3/2 = 1.5 <= H(4) = 2.08", 260, 290, 790, 56, "violet", "rect", 14),
    ],
    edges=[
        E("u", "r1"),
        E("r1", "r2"),
        E("r2", "r3"),
        E("r3", "res"),
    ],
    caption="Greedy always takes the set covering the most uncovered elements; it is within H(max set size) of optimal",
)

DIAGRAMS = [concept, vertex_cover, tsp, set_cover]
