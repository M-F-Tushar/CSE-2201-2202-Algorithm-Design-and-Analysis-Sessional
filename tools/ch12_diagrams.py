"""Chapter 12 (Flow Algorithms) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 12 - Flow Algorithms/diagrams"

S = "straight"
GREEN = "#2f9e44"
RED = "#e03131"

# 1 ---------------------------------------------------- flow network
flow_network = D(
    key="ch12-01-flow-network",
    title="A Flow Network: Source s, Sink t, Edge Capacities",
    size=(760, 440),
    flow="H",
    nodes=[
        N("s", "s\nsource", 50, 200, 100, 64, "green", "ellipse", 15, True),
        N("a", "a", 300, 80, 90, 60, "blue", "ellipse", 16),
        N("b", "b", 300, 320, 90, 60, "blue", "ellipse", 16),
        N("t", "t\nsink", 570, 200, 100, 64, "red", "ellipse", 15, True),
    ],
    edges=[
        E("s", "a", "2", route=S),
        E("s", "b", "2", route=S),
        E("a", "b", "1", route=S),
        E("a", "t", "2", route=S),
        E("b", "t", "2", route=S),
    ],
    caption="Each edge label is a capacity c(u,v). Flow must respect capacities and be conserved at a and b",
)

# 2 ---------------------------------------------------- residual graph with back edge
residual = D(
    key="ch12-02-residual-graph",
    title="Residual Graph After Pushing 1 Unit Along s-a-b-t",
    size=(800, 470),
    flow="H",
    nodes=[
        N("s", "s", 50, 200, 90, 60, "green", "ellipse", 16, True),
        N("a", "a", 320, 70, 90, 60, "blue", "ellipse", 16),
        N("b", "b", 320, 330, 90, 60, "blue", "ellipse", 16),
        N("t", "t", 610, 200, 90, 60, "red", "ellipse", 16, True),
    ],
    edges=[
        E("s", "a", "1", pts=[(120, 192), (318, 84)]),
        E("a", "s", "1 back", color=RED, dashed=True, pts=[(325, 114), (125, 226)]),
        E("s", "b", "2", pts=[(125, 240), (322, 340)]),
        E("a", "t", "2", pts=[(405, 84), (618, 196)]),
        E("b", "t", "1", pts=[(405, 342), (612, 252)]),
        E("t", "b", "1 back", color=RED, dashed=True, pts=[(640, 262), (402, 372)]),
        E("b", "a", "1 back (cancels a-b)", color=RED, dashed=True, pts=[(365, 330), (365, 130)]),
    ],
    caption="Solid = remaining forward capacity. Dashed red = reverse edges that let later paths undo earlier flow",
)

# 3 ---------------------------------------------------- augmenting loop
loop = D(
    key="ch12-03-augmenting-path-loop",
    title="Ford-Fulkerson / Edmonds-Karp Augmenting Loop",
    size=(1110, 450),
    flow="H",
    nodes=[
        N("start", "Start\nflow f = 0\non every edge", 30, 160, 190, 80, "yellow", "rect", 15, True),
        N("res", "Build residual\ngraph Gf", 280, 160, 190, 80, "blue"),
        N("q", "Path from s\nto t in Gf?", 530, 135, 220, 130, "yellow", "diamond", 14),
        N("push", "Push the bottleneck\nresidual capacity\nalong the path", 830, 160, 230, 80, "green"),
        N("stop", "No path: f is a\nmaximum flow", 535, 320, 210, 70, "violet", "rect", 15, True),
        N("rule", "Path rule: any path (DFS) = Ford-Fulkerson;\nshortest path by edges (BFS) = Edmonds-Karp", 30, 320, 440, 70, "gray", "rect", 14),
    ],
    edges=[
        E("start", "res"),
        E("res", "q"),
        E("q", "push", "Yes"),
        E("q", "stop", "No", route="v"),
        E("push", "res", "update residuals", route="loopt", bend=70),
    ],
    caption="Every push raises the flow value; the loop ends when s can no longer reach t in the residual graph",
)

# 4 ---------------------------------------------------- max-flow min-cut
mincut = D(
    key="ch12-04-max-flow-min-cut",
    title="Maximum Flow = Minimum Cut (value 4)",
    size=(760, 500),
    flow="H",
    nodes=[
        N("s", "s", 50, 200, 90, 60, "green", "ellipse", 16, True),
        N("a", "a", 300, 80, 90, 60, "blue", "ellipse", 16),
        N("b", "b", 300, 320, 90, 60, "blue", "ellipse", 16),
        N("t", "t", 570, 200, 90, 60, "red", "ellipse", 16, True),
        N("note", "Cut S = {s}, T = {a, b, t}\ncapacity = c(s,a) + c(s,b) = 2 + 2 = 4\nequals the flow value, so both are optimal", 150, 410, 460, 70, "gray", "rect", 14),
    ],
    edges=[
        E("s", "a", "2/2", route=S, color=GREEN),
        E("s", "b", "2/2", route=S, color=GREEN),
        E("a", "b", "0/1", route=S),
        E("a", "t", "2/2", route=S, color=GREEN),
        E("b", "t", "2/2", route=S, color=GREEN),
        E("s", "s", color=RED, dashed=True, directed=False, pts=[(215, 60), (215, 395)]),
    ],
    caption="Labels are flow/capacity. The dashed red line is the minimum cut; green edges are saturated",
)

# 5 ---------------------------------------------------- bipartite matching as flow
matching = D(
    key="ch12-05-bipartite-matching",
    title="Bipartite Matching as Maximum Flow (all capacities 1)",
    size=(980, 520),
    flow="H",
    nodes=[
        N("s", "s", 30, 215, 80, 60, "green", "ellipse", 16, True),
        N("A", "A", 260, 90, 80, 56, "blue", "ellipse", 16),
        N("B", "B", 260, 232, 80, 56, "blue", "ellipse", 16),
        N("C", "C", 260, 374, 80, 56, "blue", "ellipse", 16),
        N("X", "X", 570, 90, 80, 56, "violet", "ellipse", 16),
        N("Y", "Y", 570, 232, 80, 56, "violet", "ellipse", 16),
        N("Z", "Z", 570, 374, 80, 56, "violet", "ellipse", 16),
        N("t", "t", 860, 215, 80, 60, "red", "ellipse", 16, True),
    ],
    edges=[
        E("s", "A", route=S),
        E("s", "B", route=S),
        E("s", "C", route=S),
        E("A", "X", route=S),
        E("A", "Y", route=S, color=GREEN),
        E("B", "X", route=S, color=GREEN),
        E("C", "Y", route=S),
        E("C", "Z", route=S, color=GREEN),
        E("X", "t", route=S),
        E("Y", "t", route=S),
        E("Z", "t", route=S),
    ],
    caption="Green edges carry flow: matching A-Y, B-X, C-Z. Maximum flow 3 = maximum matching size 3",
)

DIAGRAMS = [flow_network, residual, loop, mincut, matching]
