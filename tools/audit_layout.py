"""Layout audit: catch text overflow, node collisions and out-of-canvas nodes."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).parent))

import root_diagrams  # noqa: E402
import ch2_diagrams   # noqa: E402
import ch3_diagrams   # noqa: E402
import ch4_diagrams   # noqa: E402
import ch7_diagrams   # noqa: E402
import ch8_diagrams   # noqa: E402
import ch11_diagrams  # noqa: E402
import ch15_diagrams  # noqa: E402

MODULES = [
    root_diagrams,
    ch2_diagrams,
    ch3_diagrams,
    ch4_diagrams,
    ch7_diagrams,
    ch8_diagrams,
    ch11_diagrams,
    ch15_diagrams,
]

from excalidraw_gen import _anchor_points  # noqa: E402

CHAR_W = 0.56  # Segoe Print runs wide; keep the estimate pessimistic
LINE_H = 1.32


def overlap(a, b):
    return not (
        a.x + a.w <= b.x or b.x + b.w <= a.x or a.y + a.h <= b.y or b.y + b.h <= a.y
    )


def seg_box_intersect(p1, p2, box, margin=4):
    bx, by, bw, bh = box
    x_min, x_max = bx + margin, bx + bw - margin
    y_min, y_max = by + margin, by + bh - margin
    if x_min >= x_max or y_min >= y_max:
        return False

    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1]

    u1 = 0.0
    u2 = 1.0

    for pi, qi in zip(p, q):
        if pi == 0:
            if qi < 0:
                return False
        else:
            t = qi / pi
            if pi < 0:
                if t > u2:
                    return False
                if t > u1:
                    u1 = t
            else:
                if t < u1:
                    return False
                if t < u2:
                    u2 = t
    return u1 <= u2


def main():
    problems = 0
    total_diagrams = 0
    for module in MODULES:
        for d in module.DIAGRAMS:
            total_diagrams += 1
            w, h = d.size
            for n in d.nodes:
                clean_label = n.label.replace("<br/>", "\n").replace("<br>", "\n")
                lines = clean_label.split("\n")
                tw = max(len(line) for line in lines) * n.size * CHAR_W
                th = len(lines) * n.size * LINE_H
                if n.shape.lower() in ("ellipse", "circle") and n.w <= 64:
                    pad = 6
                elif n.shape == "rect":
                    pad = 18
                else:
                    pad = 32
                if tw > n.w - pad:
                    print(f"[TEXT-W] {d.key}/{n.id}: needs {tw:.0f}px, box {n.w:.0f}px -> {lines[0][:40]!r}")
                    problems += 1
                if th > n.h - 6:
                    print(f"[TEXT-H] {d.key}/{n.id}: needs {th:.0f}px, box {n.h:.0f}px")
                    problems += 1
                if n.x < 0 or n.y < 0 or n.x + n.w > w or n.y + n.h > h - 10:
                    print(f"[BOUNDS] {d.key}/{n.id}: {n.x},{n.y} {n.w}x{n.h} vs canvas {w}x{h}")
                    problems += 1
            for i, a in enumerate(d.nodes):
                for b in d.nodes[i + 1:]:
                    if overlap(a, b):
                        print(f"[OVERLAP] {d.key}: {a.id} <-> {b.id}")
                        problems += 1
            ids = {n.id for n in d.nodes}
            nodes_by_id = {n.id: n for n in d.nodes}
            for e in d.edges:
                if e.src not in ids or e.dst not in ids:
                    print(f"[EDGE] {d.key}: {e.src} -> {e.dst} references a missing node")
                    problems += 1
                    continue
                a = nodes_by_id[e.src]
                b = nodes_by_id[e.dst]
                pts = _anchor_points(a, b, d.flow, e.route, e.bend, getattr(e, "pts", None))
                for j in range(len(pts) - 1):
                    p1, p2 = pts[j], pts[j + 1]
                    for n in d.nodes:
                        if n.id in (e.src, e.dst):
                            continue
                        if seg_box_intersect(p1, p2, (n.x, n.y, n.w, n.h)):
                            print(f"[CLASH] {d.key}: edge {e.src}->{e.dst} crosses node {n.id}")
                            problems += 1

    print(f"\nAudited {total_diagrams} diagrams across {len(MODULES)} modules: {problems} problem(s) found")
    return problems


if __name__ == "__main__":
    sys.exit(1 if main() > 0 else 0)
