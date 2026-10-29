"""Ford-Fulkerson worked example (Chapter 12): data, trace and drawing helpers.

The network and the order of augmenting paths follow the video
"Ford Fulkerson algorithm step by step example in 8 minutes" (Er Sahil ka Gyan,
https://youtu.be/Da-VAtoL2sk). The trace is replayed here so every number drawn
in the diagrams is computed, not typed by hand.
"""

import math

from tools.excalidraw_gen import E, INK, N

ORANGE = "#e8590c"  # augmenting path of the current step
GREEN = "#2f9e44"   # carries flow, still has room
RED = "#e03131"     # saturated (full) edge
VIOLET = "#6741d9"  # backward residual edge
PATH_W = 3.6

# ---------------------------------------------------------------- the network
CAP = {
    ("s", "a"): 5, ("s", "c"): 10, ("s", "d"): 12,
    ("c", "a"): 5, ("a", "b"): 8, ("c", "b"): 7, ("c", "t"): 3,
    ("b", "t"): 10, ("d", "c"): 4, ("c", "e"): 2, ("d", "e"): 8, ("e", "t"): 9,
}
PATHS = [
    ["s", "a", "b", "t"],
    ["s", "c", "t"],
    ["s", "d", "e", "t"],
    ["s", "c", "b", "t"],
    ["s", "d", "c", "e", "t"],
]

# vertex centres, relative to a panel origin
POS = {
    "s": (0, 180), "a": (170, 40), "b": (420, 40), "c": (290, 180),
    "t": (580, 180), "d": (170, 320), "e": (420, 320),
}
NODE = 52
R = NODE / 2
ARROW = "\u2192"


def residual(flow, u, v):
    """Residual capacity of u->v: unused room forward plus flow that can be cancelled."""
    return CAP.get((u, v), 0) - flow.get((u, v), 0) + flow.get((v, u), 0)


def residual_edges(flow):
    """Every residual edge with positive capacity: (u, v, amount, is_backward)."""
    out = []
    for (u, v), c in CAP.items():
        f = flow[(u, v)]
        if c - f > 0:
            out.append((u, v, c - f, False))
        if f > 0:
            out.append((v, u, f, True))
    return out


def reachable(flow):
    seen, stack = {"s"}, ["s"]
    while stack:
        u = stack.pop()
        for a, b, _, _ in residual_edges(flow):
            if a == u and b not in seen:
                seen.add(b)
                stack.append(b)
    return seen


def run_trace():
    """Replay the video's augmentations. Returns one record per step."""
    flow = {e: 0 for e in CAP}
    steps, value = [], 0
    for path in PATHS:
        before = dict(flow)
        pairs = list(zip(path, path[1:]))
        res = [residual(flow, u, v) for u, v in pairs]
        b = min(res)
        assert b > 0, path
        for u, v in pairs:
            if (u, v) in CAP:
                flow[(u, v)] += b
            else:
                flow[(v, u)] -= b
        value += b
        steps.append(dict(path=path, pairs=pairs, res=res, b=b, before=before,
                          after=dict(flow), value=value))
    return steps


STEPS = run_trace()
FINAL = STEPS[-1]["after"]
MAX_FLOW = STEPS[-1]["value"]
S_SIDE = reachable(FINAL)

assert [s["b"] for s in STEPS] == [5, 3, 8, 5, 1]
assert MAX_FLOW == 22 and "t" not in S_SIDE
assert sum(CAP[(u, v)] for (u, v) in CAP if u in S_SIDE and v not in S_SIDE) == MAX_FLOW
for x in "abcde":  # flow conservation
    assert sum(f for (u, v), f in FINAL.items() if v == x) == sum(f for (u, v), f in FINAL.items() if u == x)


# ---------------------------------------------------------------- drawing helpers
def fmt_path(path):
    return f" {ARROW} ".join(path)


def centre(ox, oy, v, pos=POS):
    x, y = pos[v]
    return ox + x, oy + y


def vertex_nodes(prefix, ox, oy, colors=None, pos=POS):
    colors = colors or {}
    out = []
    for v in pos:
        cx, cy = centre(ox, oy, v, pos)
        default = "green" if v == "s" else "red" if v == "t" else "blue"
        out.append(N(prefix + v, v, cx - R, cy - R, NODE, NODE, colors.get(v, default),
                     "ellipse", 18, v in "st"))
    return out


def arc(prefix, ox, oy, u, v, label, color=INK, dashed=False, off=0.0, t=0.5, width=0, pos=POS):
    """Straight arrow between two vertex circles.

    off shifts the arrow sideways (so u->v and v->u never overlap);
    t places the label along the arrow (0 = at u, 1 = at v).
    """
    x1, y1 = centre(ox, oy, u, pos)
    x2, y2 = centre(ox, oy, v, pos)
    dx, dy = x2 - x1, y2 - y1
    ln = math.hypot(dx, dy)
    ux, uy = dx / ln, dy / ln
    px, py = -uy, ux
    p0 = (x1 + ux * R + px * off, y1 + uy * R + py * off)
    p1 = (x2 - ux * R + px * off, y2 - uy * R + py * off)
    if t == 0.5:
        pts = [p0, p1]
    else:
        # four collinear points put the label (midpoint of the middle segment) at t
        dlt = min(t, 1 - t) * 0.5

        def lerp(k):
            return (p0[0] + (p1[0] - p0[0]) * k, p0[1] + (p1[1] - p0[1]) * k)

        pts = [p0, lerp(t - dlt), lerp(t + dlt), p1]
    return E(prefix + u, prefix + v, label, dashed=dashed, color=color, pts=pts, width=width)


def flow_edges(prefix, ox, oy, flow, path_pairs=()):
    """Flow network panel: every edge labelled f/c, coloured by state."""
    out = []
    for (u, v), c in CAP.items():
        f = flow[(u, v)]
        label = f"{f}/{c}" + (" full" if f == c else "")
        if (u, v) in path_pairs:
            color, width = ORANGE, PATH_W
        else:
            color, width = (RED if f == c else GREEN if f > 0 else INK), 0
        out.append(arc(prefix, ox, oy, u, v, label, color, width=width))
    return out


def residual_arcs(prefix, ox, oy, flow, path_pairs=()):
    """Residual graph panel: solid forward room, dashed violet backward (undo) edges."""
    out = []
    for u, v, amount, back in residual_edges(flow):
        key = (v, u) if back else (u, v)
        pair = 0 < flow[key] < CAP[key]  # both directions exist -> offset them
        off, t = (7, 0.35) if pair else (0, 0.5)
        if (u, v) in path_pairs:
            color, dashed, width = ORANGE, back, PATH_W
        elif back:
            color, dashed, width = VIOLET, True, 0
        else:
            color, dashed, width = INK, False, 0
        out.append(arc(prefix, ox, oy, u, v, str(amount), color, dashed, off, t, width))
    return out
