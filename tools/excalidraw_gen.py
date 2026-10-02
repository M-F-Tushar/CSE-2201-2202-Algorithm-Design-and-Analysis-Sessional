"""Hand-authored diagram engine.

Each diagram is laid out by hand (explicit coordinates) and emitted twice:
  * <key>.excalidraw -- an editable Excalidraw scene
  * <key>.svg        -- a static export that renders inside GitHub Markdown

Editing note: the .excalidraw file is the source of truth for manual tweaks.
After editing it in Excalidraw, re-export the .svg from Excalidraw itself.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from pathlib import Path

# Excalidraw's default palette: (stroke, fill)
PALETTE = {
    "blue": ("#1971c2", "#a5d8ff"),
    "green": ("#2f9e44", "#b2f2bb"),
    "red": ("#e03131", "#ffc9c9"),
    "yellow": ("#f08c00", "#ffec99"),
    "violet": ("#6741d9", "#e0d5fa"),
    "teal": ("#0c8599", "#99e9f2"),
    "pink": ("#c2255c", "#fcc2d7"),
    "orange": ("#e8590c", "#ffd8a8"),
    "gray": ("#343a40", "#e9ecef"),
    "dark": ("#1e1e1e", "#ced4da"),
    "white": ("#1e1e1e", "#ffffff"),
    "container": ("#adb5bd", "#f8f9fa"),
    "light": ("#868e96", "#f8f9fa"),
}

FONT_STACK = '"Segoe Print", "Bradley Hand", Chilanka, "Comic Sans MS", "Comic Neue", cursive'
INK = "#1e1e1e"
BG = "#ffffff"


@dataclass
class N:
    """A node. Coordinates are the top-left corner."""

    id: str
    label: str
    x: float
    y: float
    w: float = 200
    h: float = 56
    color: str = "blue"
    shape: str = "rect"  # rect | ellipse | diamond
    size: int = 16
    bold: bool = False

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def cy(self) -> float:
        return self.y + self.h / 2


@dataclass
class E:
    """An edge between two node ids."""

    src: str
    dst: str
    label: str = ""
    dashed: bool = False
    color: str = INK
    route: str = "auto"  # auto | v | h | straight | loopl | loopr | loopt | loopb
    bend: float = 0.5  # where along the gap the elbow turns
    directed: bool = True
    pts: list[tuple[float, float]] = None


@dataclass
class D:
    key: str
    title: str
    size: tuple[int, int]
    nodes: list[N]
    edges: list[E] = field(default_factory=list)
    flow: str = "V"  # V = top-to-bottom, H = left-to-right
    caption: str = ""
    containers: list[N] = field(default_factory=list)


# --------------------------------------------------------------------------
# layout helpers -- keep the hand-written specs short
# --------------------------------------------------------------------------

def col(items, x, y0, w=200, h=56, gap=34, color="blue", shape="rect", size=16):
    """Stack nodes vertically at a fixed x."""
    out, y = [], y0
    for it in items:
        nid, label, c = (it + (color,))[:3] if len(it) == 2 else it
        out.append(N(nid, label, x, y, w, h, c, shape, size))
        y += h + gap
    return out


def row(items, y, x0, w=200, h=56, gap=34, color="blue", shape="rect", size=16):
    """Lay nodes out left-to-right at a fixed y."""
    out, x = [], x0
    for it in items:
        nid, label, c = (it + (color,))[:3] if len(it) == 2 else it
        out.append(N(nid, label, x, y, w, h, c, shape, size))
        x += w + gap
    return out


def row_centered(items, y, cx, w=200, h=56, gap=34, color="blue", shape="rect", size=16):
    """Lay nodes out left-to-right, centred on cx."""
    total = len(items) * w + (len(items) - 1) * gap
    return row(items, y, cx - total / 2, w, h, gap, color, shape, size)


def fan(parent, children, label_map=None):
    """One edge from parent to every child."""
    return [E(parent, c, (label_map or {}).get(c, "")) for c in children]


# --------------------------------------------------------------------------
# deterministic "hand drawn" jitter
# --------------------------------------------------------------------------

def _r(seed: float) -> float:
    """Stable pseudo-random value in [-1, 1]."""
    v = math.sin(seed * 12.9898 + 78.233) * 43758.5453
    return (v - math.floor(v)) * 2 - 1


def _sketch_line(x1, y1, x2, y2, seed, rough=1.6):
    """A slightly bowed line, the way a hand would draw it."""
    ox1, oy1 = _r(seed) * rough, _r(seed + 1) * rough
    ox2, oy2 = _r(seed + 2) * rough, _r(seed + 3) * rough
    mx = (x1 + x2) / 2 + _r(seed + 4) * rough * 1.8
    my = (y1 + y2) / 2 + _r(seed + 5) * rough * 1.8
    return f"M{x1 + ox1:.1f} {y1 + oy1:.1f} Q{mx:.1f} {my:.1f} {x2 + ox2:.1f} {y2 + oy2:.1f}"


def _sketch_rect(x, y, w, h, seed, rough=1.6):
    pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    d = []
    for i in range(4):
        a, b = pts[i], pts[(i + 1) % 4]
        d.append(_sketch_line(a[0], a[1], b[0], b[1], seed + i * 7, rough))
    return " ".join(d)


def _sketch_ellipse(cx, cy, rx, ry, seed, rough=1.6):
    d = []
    for i in range(8):
        a0 = i * math.pi / 4
        a1 = (i + 1) * math.pi / 4
        x1, y1 = cx + rx * math.cos(a0), cy + ry * math.sin(a0)
        x2, y2 = cx + rx * math.cos(a1), cy + ry * math.sin(a1)
        am = (a0 + a1) / 2
        mx = cx + rx * 1.03 * math.cos(am) + _r(seed + i) * rough
        my = cy + ry * 1.03 * math.sin(am) + _r(seed + i + 40) * rough
        d.append(f"M{x1:.1f} {y1:.1f} Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}")
    return " ".join(d)


def _sketch_diamond(x, y, w, h, seed, rough=1.6):
    pts = [(x + w / 2, y), (x + w, y + h / 2), (x + w / 2, y + h), (x, y + h / 2)]
    d = []
    for i in range(4):
        a, b = pts[i], pts[(i + 1) % 4]
        d.append(_sketch_line(a[0], a[1], b[0], b[1], seed + i * 11, rough))
    return " ".join(d)


# --------------------------------------------------------------------------
# edge routing
# --------------------------------------------------------------------------

def _anchor_points(a: N, b: N, flow: str, route: str, bend: float, pts: list = None):
    """Return the polyline for an edge from node a to node b."""
    if pts:
        return pts
    if route == "straight":
        return _straight(a, b)

    # feedback loops route around the outside of the diagram
    if route in ("loopl", "loopr"):
        off = bend if bend > 1 else 60
        if route == "loopl":
            x = min(a.x, b.x) - off
            return [(a.x, a.cy), (x, a.cy), (x, b.cy), (b.x, b.cy)]
        x = max(a.x + a.w, b.x + b.w) + off
        return [(a.x + a.w, a.cy), (x, a.cy), (x, b.cy), (b.x + b.w, b.cy)]

    if route in ("loopt", "loopb"):
        off = bend if bend > 1 else 50
        if route == "loopt":
            y = min(a.y, b.y) - off
            return [(a.cx, a.y), (a.cx, y), (b.cx, y), (b.cx, b.y)]
        y = max(a.y + a.h, b.y + b.h) + off
        return [(a.cx, a.y + a.h), (a.cx, y), (b.cx, y), (b.cx, b.y + b.h)]

    mode = route if route in ("v", "h") else ("v" if flow == "V" else "h")

    if mode == "v":
        if b.cy > a.cy:  # downward
            sy, ey = a.y + a.h, b.y
        else:  # upward
            sy, ey = a.y, b.y + b.h
        if abs(a.cx - b.cx) < 6:
            return [(a.cx, sy), (b.cx, ey)]
        my = sy + (ey - sy) * bend
        return [(a.cx, sy), (a.cx, my), (b.cx, my), (b.cx, ey)]

    if b.cx > a.cx:  # rightward
        sx, ex = a.x + a.w, b.x
    else:  # leftward
        sx, ex = a.x, b.x + b.w
    if abs(a.cy - b.cy) < 6:
        return [(sx, a.cy), (ex, b.cy)]
    mx = sx + (ex - sx) * bend
    return [(sx, a.cy), (mx, a.cy), (mx, b.cy), (ex, b.cy)]


def _straight(a: N, b: N):
    dx, dy = b.cx - a.cx, b.cy - a.cy
    return [_edge_point(a, dx, dy), _edge_point(b, -dx, -dy)]


def _edge_point(n: N, dx, dy):
    """Where a ray leaving the node centre crosses its border."""
    if dx == 0 and dy == 0:
        return (n.cx, n.cy)
    sx = n.w / 2 / abs(dx) if dx else math.inf
    sy = n.h / 2 / abs(dy) if dy else math.inf
    s = min(sx, sy)
    return (n.cx + dx * s, n.cy + dy * s)


# --------------------------------------------------------------------------
# SVG renderer
# --------------------------------------------------------------------------

def _esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _text_block(lines, cx, cy, size, color=INK, weight="normal"):
    lh = size * 1.32
    top = cy - (len(lines) - 1) * lh / 2
    spans = "".join(
        f'<tspan x="{cx:.1f}" y="{top + i * lh:.1f}">{_esc(l)}</tspan>'
        for i, l in enumerate(lines)
    )
    return (
        f'<text text-anchor="middle" dominant-baseline="central" '
        f'font-family=\'{FONT_STACK}\' font-size="{size}" font-weight="{weight}" '
        f'fill="{color}">{spans}</text>'
    )


def render_svg(d: D) -> str:
    w, h = d.size
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-label="{_esc(d.title)}">',
        f'<rect width="{w}" height="{h}" fill="{BG}" rx="10"/>',
    ]

    if d.title:
        out.append(_text_block([d.title], w / 2, 34, 21, INK, "bold"))

    index = {n.id: n for n in d.nodes}
    seed = 3

    # containers rendered first so they sit in the background
    for i, c in enumerate(getattr(d, "containers", [])):
        stroke, fill = PALETTE.get(c.color, PALETTE["container"])
        s = seed + 200 + i * 17
        body = _sketch_rect(c.x, c.y, c.w, c.h, s)
        out.append(f'<rect x="{c.x:.1f}" y="{c.y:.1f}" width="{c.w:.1f}" height="{c.h:.1f}" rx="10" fill="{fill}" opacity="0.4"/>')
        out.append(f'<path d="{body}" fill="none" stroke="{stroke}" stroke-width="1.6" stroke-dasharray="6 4" stroke-linecap="round" opacity="0.8"/>')
        if c.label:
            tw = len(c.label) * 8 + 16
            out.append(f'<rect x="{c.x + 14:.1f}" y="{c.y - 11:.1f}" width="{tw}" height="22" rx="4" fill="{BG}"/>')
            out.append(_text_block([c.label], c.x + 14 + tw / 2, c.y, 13, stroke, "bold"))

    # edges
    for i, e in enumerate(d.edges):
        a, b = index[e.src], index[e.dst]
        pts = _anchor_points(a, b, d.flow, e.route, e.bend, getattr(e, "pts", None))
        dash = ' stroke-dasharray="9 7"' if e.dashed else ""
        segs = " ".join(
            _sketch_line(pts[j][0], pts[j][1], pts[j + 1][0], pts[j + 1][1], seed + i * 13 + j, 1.0)
            for j in range(len(pts) - 1)
        )
        out.append(
            f'<path d="{segs}" fill="none" stroke="{e.color}" stroke-width="1.9" '
            f'stroke-linecap="round"{dash} opacity="0.85"/>'
        )
        if getattr(e, "directed", True):
            out.append(_arrow_head(pts[-2], pts[-1], e.color))
        if e.label:
            mx = (pts[len(pts) // 2 - 1][0] + pts[len(pts) // 2][0]) / 2
            my = (pts[len(pts) // 2 - 1][1] + pts[len(pts) // 2][1]) / 2
            tw = len(e.label) * 8 + 14
            out.append(
                f'<rect x="{mx - tw / 2:.1f}" y="{my - 12:.1f}" width="{tw}" height="24" '
                f'rx="6" fill="{BG}" opacity="0.95"/>'
            )
            out.append(_text_block([e.label], mx, my, 13, "#495057"))

    for i, n in enumerate(d.nodes):
        stroke, fill = PALETTE.get(n.color, PALETTE["blue"])
        s = seed + 900 + i * 17
        shape_type = n.shape.lower()
        if shape_type in ("ellipse", "circle"):
            out.append(
                f'<ellipse cx="{n.cx:.1f}" cy="{n.cy:.1f}" rx="{n.w / 2:.1f}" '
                f'ry="{n.h / 2:.1f}" fill="{fill}"/>'
            )
            body = _sketch_ellipse(n.cx, n.cy, n.w / 2, n.h / 2, s)
            body2 = _sketch_ellipse(n.cx, n.cy, n.w / 2, n.h / 2, s + 55)
        elif shape_type == "diamond":
            pts = f"{n.cx},{n.y} {n.x + n.w},{n.cy} {n.cx},{n.y + n.h} {n.x},{n.cy}"
            out.append(f'<polygon points="{pts}" fill="{fill}"/>')
            body = _sketch_diamond(n.x, n.y, n.w, n.h, s)
            body2 = _sketch_diamond(n.x, n.y, n.w, n.h, s + 55)
        else:
            out.append(
                f'<rect x="{n.x:.1f}" y="{n.y:.1f}" width="{n.w:.1f}" height="{n.h:.1f}" '
                f'rx="10" fill="{fill}"/>'
            )
            body = _sketch_rect(n.x, n.y, n.w, n.h, s)
            body2 = _sketch_rect(n.x, n.y, n.w, n.h, s + 55)
        out.append(f'<path d="{body}" fill="none" stroke="{stroke}" stroke-width="2" stroke-linecap="round"/>')
        out.append(
            f'<path d="{body2}" fill="none" stroke="{stroke}" stroke-width="1.3" '
            f'stroke-linecap="round" opacity="0.55"/>'
        )
        weight = "bold" if n.bold else "normal"
        clean_lines = n.label.replace("<br/>", "\n").replace("<br>", "\n").split("\n")
        out.append(_text_block(clean_lines, n.cx, n.cy, n.size, INK, weight))

    if d.caption:
        out.append(_text_block([d.caption], w / 2, h - 22, 14, "#868e96", "normal"))

    out.append("</svg>")
    return "\n".join(out)


def _arrow_head(p0, p1, color):
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    size = 11
    a1 = ang + math.radians(158)
    a2 = ang - math.radians(158)
    x1, y1 = p1[0] + size * math.cos(a1), p1[1] + size * math.sin(a1)
    x2, y2 = p1[0] + size * math.cos(a2), p1[1] + size * math.sin(a2)
    return (
        f'<path d="M{x1:.1f} {y1:.1f} L{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f}" '
        f'fill="none" stroke="{color}" stroke-width="1.9" stroke-linecap="round" '
        f'stroke-linejoin="round"/>'
    )


# --------------------------------------------------------------------------
# Excalidraw scene renderer
# --------------------------------------------------------------------------

_SHAPE_MAP = {"rect": "rectangle", "ellipse": "ellipse", "circle": "ellipse", "diamond": "diamond"}


def _base(el_id, kind, x, y, w, h, stroke, fill, seed):
    return {
        "id": el_id,
        "type": kind,
        "x": round(x, 2),
        "y": round(y, 2),
        "width": round(w, 2),
        "height": round(h, 2),
        "angle": 0,
        "strokeColor": stroke,
        "backgroundColor": fill,
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 3} if kind == "rectangle" else None,
        "seed": seed,
        "version": 1,
        "versionNonce": seed + 1,
        "isDeleted": False,
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False,
    }


def render_excalidraw(d: D) -> dict:
    elements = []
    index = {n.id: n for n in d.nodes}
    seed = 1000

    if d.title:
        elements.append(
            {
                **_base(f"{d.key}-title", "text", 24, 16, d.size[0] - 48, 30, INK, "transparent", seed),
                "text": d.title,
                "originalText": d.title,
                "fontSize": 20,
                "fontFamily": 1,
                "textAlign": "center",
                "verticalAlign": "top",
                "containerId": None,
                "lineHeight": 1.25,
                "baseline": 20,
            }
        )

    for i, c in enumerate(getattr(d, "containers", [])):
        stroke, fill = PALETTE.get(c.color, PALETTE["container"])
        cid = f"{d.key}-c{i}"
        ctid = f"{d.key}-ct{i}"
        box = _base(cid, "rectangle", c.x, c.y, c.w, c.h, stroke, "transparent", seed + 200 + i)
        box["strokeStyle"] = "dashed"
        elements.append(box)
        if c.label:
            elements.append(
                {
                    **_base(ctid, "text", c.x + 12, c.y + 8, c.w - 24, 18, stroke, "transparent", seed + 300 + i),
                    "text": c.label,
                    "originalText": c.label,
                    "fontSize": 14,
                    "fontFamily": 1,
                    "textAlign": "left",
                    "verticalAlign": "top",
                    "containerId": cid,
                    "lineHeight": 1.25,
                    "baseline": 14,
                }
            )

    for i, e in enumerate(d.edges):
        a, b = index[e.src], index[e.dst]
        pts = _anchor_points(a, b, d.flow, e.route, e.bend, getattr(e, "pts", None))
        ox, oy = pts[0]
        rel = [[round(px - ox, 2), round(py - oy, 2)] for px, py in pts]
        xs = [p[0] for p in rel]
        ys = [p[1] for p in rel]
        el = _base(f"{d.key}-e{i}", "arrow", ox, oy, max(xs) - min(xs), max(ys) - min(ys), e.color, "transparent", seed + i)
        el.update(
            {
                "points": rel,
                "lastCommittedPoint": None,
                "startBinding": None,
                "endBinding": None,
                "startArrowhead": None,
                "endArrowhead": "arrow" if getattr(e, "directed", True) else None,
                "strokeStyle": "dashed" if e.dashed else "solid",
                "roundness": {"type": 2},
                "elbowed": False,
            }
        )
        elements.append(el)

    for i, n in enumerate(d.nodes):
        stroke, fill = PALETTE.get(n.color, PALETTE["blue"])
        shape_id = f"{d.key}-n{i}"
        text_id = f"{d.key}-t{i}"
        kind = _SHAPE_MAP.get(n.shape.lower(), "rectangle")
        shape = _base(shape_id, kind, n.x, n.y, n.w, n.h, stroke, fill, seed + 500 + i)
        shape["boundElements"] = [{"type": "text", "id": text_id}]
        elements.append(shape)
        clean_label = n.label.replace("<br/>", "\n").replace("<br>", "\n")
        elements.append(
            {
                **_base(text_id, "text", n.x + 6, n.cy - 10, n.w - 12, 20, INK, "transparent", seed + 700 + i),
                "text": clean_label,
                "originalText": clean_label,
                "fontSize": n.size,
                "fontFamily": 1,
                "textAlign": "center",
                "verticalAlign": "middle",
                "containerId": shape_id,
                "lineHeight": 1.25,
                "baseline": n.size,
            }
        )


    return {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {"gridSize": None, "viewBackgroundColor": BG},
        "files": {},
    }


def write(d: D, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{d.key}.svg").write_text(render_svg(d), encoding="utf-8")
    (out_dir / f"{d.key}.excalidraw").write_text(
        json.dumps(render_excalidraw(d), indent=2), encoding="utf-8"
    )
