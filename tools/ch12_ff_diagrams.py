"""Chapter 12 Ford-Fulkerson diagrams (06-16): foundations, trace, and analysis."""

from tools.excalidraw_gen import D, E, N, T
from tools.ch12_ff_trace import (
    ARROW, CAP, FINAL, GREEN, MAX_FLOW, ORANGE, PATH_W, RED, S_SIDE, STEPS, VIOLET,
    arc, fmt_path, flow_edges, residual_arcs, vertex_nodes,
)

S = "straight"


def hline(src, dst, x0, x1, y, label, color, dashed=False, t=0.5, width=0):
    """Horizontal arrow with its label at fraction t along it."""
    k = min(t, 1 - t) * 0.5
    pts = [(x0, y), (x0 + (x1 - x0) * (t - k), y), (x0 + (x1 - x0) * (t + k), y), (x1, y)]
    return E(src, dst, label, dashed=dashed, color=color, pts=pts, width=width)


def note(nid, x, y, w, h, color, *lines):
    return N(nid, "\n".join(lines), x, y, w, h, color, "rect", 15)


# 6 ---------------------------------------------------- key terms
key_terms = D(
    key="ch12-06-ff-key-terms",
    title="Ford-Fulkerson Foundations: Flow, Capacity, Residual, Bottleneck",
    size=(1200, 730),
    flow="H",
    containers=[
        N("pA", "1. Flow and capacity on one edge", 20, 70, 570, 290, "blue"),
        N("pB", "2. Residual view of the same edge", 610, 70, 570, 290, "violet"),
        N("pC", "3. Saturated (full) edge", 20, 390, 570, 290, "red"),
        N("pD", "4. Augmenting path and its bottleneck", 610, 390, 570, 290, "yellow"),
    ],
    nodes=[
        N("Au", "u", 90, 125, 60, 60, "blue", "ellipse", 18),
        N("Av", "v", 450, 125, 60, 60, "blue", "ellipse", 18),
        N("Bu", "u", 680, 125, 60, 60, "blue", "ellipse", 18),
        N("Bv", "v", 1040, 125, 60, 60, "blue", "ellipse", 18),
        N("Cu", "u", 90, 445, 60, 60, "blue", "ellipse", 18),
        N("Cv", "v", 450, 445, 60, 60, "blue", "ellipse", 18),
        N("Ds", "s", 640, 449, 52, 52, "green", "ellipse", 18, True),
        N("Dx", "x", 790, 449, 52, 52, "blue", "ellipse", 18),
        N("Dy", "y", 940, 449, 52, 52, "blue", "ellipse", 18),
        N("Dt", "t", 1090, 449, 52, 52, "red", "ellipse", 18, True),
    ],
    edges=[
        E("Au", "Av", "3/10", route=S, color=GREEN),
        hline("Bu", "Bv", 740, 1040, 147, "7", GREEN, t=0.35),
        hline("Bv", "Bu", 1040, 740, 165, "3", VIOLET, dashed=True, t=0.35),
        E("Cu", "Cv", "10/10 full", route=S, color=RED),
        E("Ds", "Dx", "6", route=S, color=ORANGE, width=PATH_W),
        E("Dx", "Dy", "2", route=S, color=RED, width=PATH_W),
        E("Dy", "Dt", "9", route=S, color=ORANGE, width=PATH_W),
    ],
    texts=[
        T("tA1", "3 = flow f(u,v): how much is moving now", 305, 235, 15),
        T("tA2", "10 = capacity c(u,v): the most it can carry", 305, 270, 15),
        T("tA3", "rule: 0 \u2264 f(u,v) \u2264 c(u,v)", 305, 310, 15),
        T("tB1", f"forward u{ARROW}v: room left = c \u2212 f = 10 \u2212 3 = 7", 895, 235, 15),
        T("tB2", f"backward v{ARROW}u: can undo up to f = 3", 895, 270, 15),
        T("tB3", "Gf draws only edges with amount > 0", 895, 310, 15),
        T("tC1", f"forward room = 10 \u2212 10 = 0, so u{ARROW}v leaves Gf", 305, 555, 15),
        T("tC2", f"only the backward edge v{ARROW}u (10) stays", 305, 590, 15),
        T("tC3", "the video circles such full edges", 305, 630, 15),
        T("tD1", f"augmenting path: an s{ARROW}t route in Gf with room", 895, 555, 15),
        T("tD2", "bottleneck = min(6, 2, 9) = 2, so push 2", 895, 590, 15),
        T("tD3", f"after the push x{ARROW}y is full; |f| grows by 2", 895, 630, 15),
    ],
    caption="Every step diagram uses these: f/c on the flow network, single numbers on the residual graph Gf",
)

# 7 ---------------------------------------------------- the problem (step 0)
_zero = {e: 0 for e in CAP}
step0 = D(
    key="ch12-07-ff-example-network",
    title="Step 0: The Video's Network, Every Edge Starts at 0/capacity",
    size=(1150, 560),
    flow="H",
    nodes=vertex_nodes("", 80, 110) + [
        note("info", 760, 105, 370, 360, "gray",
             "The problem",
             "Find the maximum flow from s to t.",
             "",
             "7 vertices, 12 directed edges.",
             "Every label is flow/capacity.",
             "No flow yet: every edge is 0/c",
             "and the flow value |f| = 0.",
             "",
             "Out of s: 5 + 10 + 12 = 27",
             "Into t: 10 + 3 + 9 = 22",
             "So the answer can never exceed 22."),
    ],
    edges=flow_edges("", 80, 110, _zero),
    caption="Source s (green) pushes, sink t (red) receives; a, b, c, d, e must pass on all they get",
)


# 8-12 ------------------------------------------------- one diagram per augmentation
LEGEND = ("Orange (bold) = augmenting path, green = carries flow, red = full, "
          "dashed violet = backward (undo) edge in Gf")


def _arrow(u, v):
    return f"{u}{ARROW}{v}"


def step_diagram(k, st):
    b, pairs = st["b"], st["pairs"]
    before, after = st["before"], st["after"]
    prev = st["value"] - b
    room = ", ".join(f"{_arrow(u, v)} = {r}" for (u, v), r in zip(pairs, st["res"]))
    changes = ", ".join(
        f"f({u},{v}) {before[(u, v)]} {ARROW} {after[(u, v)]}"
        + (" FULL" if after[(u, v)] == CAP[(u, v)] else "")
        for u, v in pairs
    )
    backs = ", ".join(_arrow(v, u) for u, v in pairs)
    full = [_arrow(u, v) for u, v in pairs if after[(u, v)] == CAP[(u, v)]]
    lines = [
        f"Search finds the path {fmt_path(st['path'])} in Gf.   Room on each edge: {room}",
        f"Bottleneck = min({', '.join(map(str, st['res']))}) = {b}   {ARROW}   push {b} unit{'s' if b > 1 else ''} along the whole path",
        f"Flow network: {changes}",
        f"Residual graph: every path edge loses {b} of room; backward edges {backs} gain {b}."
        + (f"  Full now, so it leaves Gf: {', '.join(full)}" if full else ""),
        f"Flow value |f| = {prev} + {b} = {st['value']}",
    ]
    return D(
        key=f"ch12-{7 + k:02d}-ff-step-{k}",
        title=f"Step {k}: Augment Along {fmt_path(st['path'])} (bottleneck {b}, flow {prev} {ARROW} {st['value']})",
        size=(1420, 700),
        flow="H",
        containers=[
            N("pL", f"1. Search: residual graph Gf before step {k}", 20, 70, 680, 420, "violet"),
            N("pR", f"2. Push {b}: flow network after step {k} (flow/capacity)", 720, 70, 680, 420, "green"),
        ],
        nodes=vertex_nodes("L", 70, 100) + vertex_nodes("R", 770, 100)
        + [note("info", 20, 510, 1380, 140, "yellow", *lines)],
        edges=residual_arcs("L", 70, 100, before, pairs) + flow_edges("R", 770, 100, after, pairs),
        caption=LEGEND,
    )


STEP_DIAGRAMS = [step_diagram(k, st) for k, st in enumerate(STEPS, 1)]


# 13 --------------------------------------------------- why it stops: final Gf + min cut
_cut_edges = sorted((u, v) for (u, v) in CAP if u in S_SIDE and v not in S_SIDE)
_cut_sum = " + ".join(str(CAP[e]) for e in _cut_edges)
final_cut = D(
    key="ch12-13-ff-final-residual-min-cut",
    title=f"After Step 5: No Augmenting Path Left, Max Flow {MAX_FLOW} = Min Cut {MAX_FLOW}",
    size=(1250, 640),
    flow="H",
    containers=[
        N("cS", "S = vertices reachable from s in Gf", 30, 80, 535, 470, "green"),
        N("cT", "T = {t}", 625, 220, 112, 170, "red"),
    ],
    nodes=vertex_nodes("", 100, 125, {v: "teal" for v in "abcde"}) + [
        note("info", 770, 90, 460, 460, "gray",
             "Why the algorithm stops",
             "Every edge into t is full:",
             "b→t 10/10, c→t 3/3, e→t 9/9.",
             "So Gf has no edge entering t,",
             "and no augmenting path exists.",
             "",
             "Reachable from s in Gf:",
             "S = {s, a, b, c, d, e},  T = {t}",
             "",
             "Min cut = capacity of edges S → T:",
             "c(b,t) + c(c,t) + c(e,t)",
             f"= {_cut_sum} = {MAX_FLOW}",
             "",
             f"|f| = {MAX_FLOW} = cut capacity, so {MAX_FLOW} is optimal"),
    ],
    edges=residual_arcs("", 100, 125, FINAL) + [
        E("s", "s", color=RED, dashed=True, directed=False, pts=[(588, 75), (588, 560)], width=2.6),
    ],
    caption="Final residual graph: solid = room left, dashed violet = undo edges, dashed red line = minimum cut",
)


# 14 --------------------------------------------------- worst case for running time
_WPOS = {"s": (0, 150), "a": (240, 20), "b": (240, 280), "t": (480, 150)}


def _w(prefix, ox, oy, u, v, label, color="#1e1e1e", dashed=False, off=0.0, t=0.5, path=False):
    return arc(prefix, ox, oy, u, v, label, ORANGE if path else color, dashed, off, t,
               PATH_W if path else 0, pos=_WPOS)


worst = D(
    key="ch12-14-ff-worst-case",
    title="Why Ford-Fulkerson Is O(E · |f*|): An Unlucky Path Choice Adds Only 1 per Round",
    size=(1300, 640),
    flow="H",
    containers=[
        N("pL", "Odd rounds: s→a→b→t (bottleneck 1)", 20, 70, 620, 380, "yellow"),
        N("pR", "Even rounds: s→b→a→t uses back edge b→a", 660, 70, 620, 380, "violet"),
    ],
    nodes=vertex_nodes("L", 90, 130, pos=_WPOS) + vertex_nodes("R", 730, 130, pos=_WPOS) + [
        note("info", 20, 470, 1260, 125, "gray",
             "Each round's path goes through the middle edge of capacity 1, so |f| grows by only 1 per round.",
             "Even rounds cancel that unit with the backward edge b→a; odd rounds push it through a→b again.",
             "Max flow |f*| = 2000, so this choice needs 2000 rounds of O(E) each: O(E · |f*|) in total.",
             "BFS (Edmonds-Karp) picks the 2-edge paths s→a→t and s→b→t and finishes in just 2 rounds."),
    ],
    edges=[
        _w("L", 90, 130, "s", "a", "1000", path=True),
        _w("L", 90, 130, "a", "b", "1", path=True),
        _w("L", 90, 130, "b", "t", "1000", path=True),
        _w("L", 90, 130, "s", "b", "1000"),
        _w("L", 90, 130, "a", "t", "1000"),
        _w("R", 730, 130, "s", "a", "999", off=7, t=0.35),
        _w("R", 730, 130, "a", "s", "1", VIOLET, True, off=7, t=0.35),
        _w("R", 730, 130, "b", "a", "1", dashed=True, path=True),
        _w("R", 730, 130, "s", "b", "1000", path=True),
        _w("R", 730, 130, "a", "t", "1000", path=True),
        _w("R", 730, 130, "b", "t", "999", off=7, t=0.35),
        _w("R", 730, 130, "t", "b", "1", VIOLET, True, off=7, t=0.35),
    ],
    caption="Left: the original capacities. Right: the residual graph after round 1. The running time depends on capacity values",
)

# 15 --------------------------------------------------- max-flow/min-cut certificate
_min_cut_pairs = sorted((u, v) for (u, v) in CAP if u in S_SIDE and v not in S_SIDE)
_min_cut_capacity = sum(CAP[edge] for edge in _min_cut_pairs)
assert _min_cut_capacity == MAX_FLOW

max_flow_min_cut_certificate = D(
    key="ch12-15-max-flow-min-cut-certificate",
    title="Max Flow = Min Cut: Turn the Final Residual Graph into a Certificate (22)",
    size=(1480, 880),
    flow="H",
    containers=[
        N("residual-panel", "1. SEARCH THE FINAL RESIDUAL GRAPH Gf", 20, 70, 700, 530, "violet"),
        N("flow-panel", "2. DRAW THE ORIGINAL NETWORK AND ITS CUT", 730, 70, 700, 530, "green"),
    ],
    nodes=(
        vertex_nodes("L", 50, 130, {v: "teal" for v in S_SIDE if v != "s"})
        + vertex_nodes("R", 760, 130, {v: "teal" for v in S_SIDE if v != "s"})
        + [
            N("q1", "1. STOP\nNo s→t path in Gf", 32, 660, 260, 90, "violet", "rect", 14, True),
            N("q2", "2. PARTITION\nS = reached; T = unreached", 326, 660, 260, 90, "blue", "rect", 14, True),
            N("q3", "3. SATURATION\nS→T full; T→S flow is 0", 620, 660, 260, 90, "yellow", "rect", 14, True),
            N("q4", "4. EQUALITY\n|f| = c(S,T) = 22", 914, 660, 260, 90, "orange", "rect", 14, True),
            N("q5", "5. CERTIFICATE\nmax flow = min cut = 22", 1208, 660, 260, 90, "green", "rect", 14, True),
        ]
    ),
    edges=(
        residual_arcs("L", 50, 130, FINAL)
        + flow_edges("R", 760, 130, FINAL, _min_cut_pairs)
        + [
            E("Ls", "Ls", color=RED, dashed=True, directed=False,
              pts=[(550, 125), (550, 530)], width=2.6),
            E("Rs", "Rs", color=RED, dashed=True, directed=False,
              pts=[(1260, 125), (1260, 530)], width=2.6),
            E("q1", "q2"), E("q2", "q3"), E("q3", "q4"), E("q4", "q5"),
        ]
    ),
    texts=[
        T("set-s", "S = {s, a, b, c, d, e}", 1010, 130, 14, GREEN, True),
        T("set-t", "T = {t}", 1370, 130, 14, RED, True),
        T("residual-note", "Reachable set S; t is unreachable in Gf", 370, 570, 13, "#495057"),
        T("cut-note", "Orange S→T edges are saturated; their capacities total 22", 1080, 570, 13, "#495057"),
    ],
    caption="Residual reachability → cut partition → equal values prove optimality; labels on the original network are flow/capacity",
)

exam_network = D(
    key="ch12-16-exam-flow-network",
    title="Exam Question: Flow-22 Network with Capacities",
    size=(760, 520),
    flow="H",
    nodes=vertex_nodes("", 80, 90),
    edges=[arc("", 80, 90, u, v, str(c)) for (u, v), c in CAP.items()],
    caption="Edge labels are capacities c(u,v); s is the source and t is the sink",
)

FF_DIAGRAMS = [key_terms, step0, *STEP_DIAGRAMS, final_cut, worst, max_flow_min_cut_certificate, exam_network]
