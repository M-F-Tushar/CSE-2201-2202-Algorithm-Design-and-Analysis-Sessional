"""Builder for include/exclude ("yes"/"no") state-space trees.

Visual language (copied from the lecture slide "Sum of subset problem: state space
tree"): one circle per node holding the running sum, left edge = "yes" (item
included), right edge = "no" (item excluded), one row per item labelled i1, i2, ...
at the left, and a one-line reading note under the tree.

Usage:
    scene = state_space_tree(key, title, subtitle, root, levels, note)
    write_tree(scene, out_dir)

Run `python tools/ch9_state_space_tree.py` for the Chapter 9 replica of the slide.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from excalidraw_gen import D, E, N, PALETTE, T, write

R = 32  # circle radius
LEAF_GAP = 110  # horizontal distance between neighbouring leaves
ROOT_Y = 160  # centre of the root
LEVEL_GAP = 115  # vertical distance between rows
MARGIN = 110  # left/right margin; the level labels live in the left one
MIN_WIDTH = 900  # keeps the one-line reading note from being clipped on small trees
LABEL_GREY = "#495057"


@dataclass
class S:
    """One state: `label` is the value stored at the node.

    yes / no are the children for "item included" / "item excluded".
    color is an engine palette name ("white" = plain, "red" = pruned/dead end,
    "green" = solution, "light" = not explored). note is small text under the node.
    stub draws the node and its incoming edge dashed (branch not explored).
    """

    label: str
    yes: "S | None" = None
    no: "S | None" = None
    color: str = "white"
    note: str = ""
    stub: bool = False
    edge: "str | None" = None  # label of the incoming edge; None = yes/no, "" = none


def _leaf_count(s: S) -> int:
    kids = [c for c in (s.yes, s.no) if c]
    return 1 if not kids else sum(_leaf_count(c) for c in kids)


def _depth(s: S) -> int:
    kids = [c for c in (s.yes, s.no) if c]
    return 0 if not kids else 1 + max(_depth(c) for c in kids)


def state_space_tree(key, title, subtitle, root: S, levels, note, note_color="#1e1e1e",
                     min_width=MIN_WIDTH, level_gap=LEVEL_GAP):
    """Lay out `root` and return a diagram scene (D)."""
    n_leaves, depth = _leaf_count(root), _depth(root)
    width = max((n_leaves - 1) * LEAF_GAP + 2 * R + 2 * MARGIN, min_width)
    x_first = width / 2 - (n_leaves - 1) * LEAF_GAP / 2
    note_lines = _max_note_lines(root)
    last_cy = ROOT_Y + depth * level_gap
    height = int(last_cy + R + (18 + 17 * note_lines if note_lines else 0)
                 + 50 + 26 * (note.count("\n") + 1))

    nodes, edges, texts = [], [], []
    counter = [0]
    ids = {}

    def place(s: S, level: int) -> float:
        kids = [c for c in (s.yes, s.no) if c]
        if kids:
            xs = [place(c, level + 1) for c in kids]
            cx = sum(xs) / len(xs)
        else:
            cx = x_first + counter[0] * LEAF_GAP
            counter[0] += 1
        cy = ROOT_Y + level * level_gap
        nid = f"s{len(ids)}"
        ids[id(s)] = (nid, cx, cy)
        stroke_color = s.color if not s.stub else "light"
        font = 22 if len(s.label) <= 2 else 16 if len(s.label) <= 4 else 13
        nodes.append(N(nid, s.label, cx - R, cy - R, 2 * R, 2 * R, stroke_color, "ellipse", font))
        if s.note:
            ncolor = PALETTE[s.color][0] if s.color not in ("white", "light") else LABEL_GREY
            texts.append(T(f"{nid}-note", s.note, cx, cy + R + 10 + 8.5 * (s.note.count("\n") + 1), 14, ncolor))
        return cx

    place(root, 0)

    def connect(parent: S):
        pid, px, py = ids[id(parent)]
        for child, word, side in ((parent.yes, "yes", -1), (parent.no, "no", 1)):
            if child is None:
                continue
            cid, cx, cy = ids[id(child)]
            dx, dy = cx - px, cy - py
            dist = (dx * dx + dy * dy) ** 0.5
            ux, uy = dx / dist, dy / dist
            start = (px + ux * R, py + uy * R)
            end = (cx - ux * R, cy - uy * R)
            edges.append(E(pid, cid, directed=False, route="straight", pts=[start, end],
                           dashed=child.stub, color="#1e1e1e"))
            mx, my = (start[0] + end[0]) / 2, (start[1] + end[1]) / 2
            word = word if child.edge is None else child.edge
            if word:
                half = len(word) * 17 * 0.28
                texts.append(T(f"{pid}-{cid}-edge", word, mx + side * (half + 11), my - 5, 17,
                               LABEL_GREY))
            connect(child)

    connect(root)

    for level, label in enumerate(levels, start=1):
        texts.append(T(f"level{level}", label, max(44, x_first - R - 55), ROOT_Y + level * level_gap, 24))

    if subtitle:
        texts.append(T("subtitle", subtitle, width / 2, 82, 22))
    texts.append(T("note", note, width / 2, height - 30 - 13 * (note.count("\n") + 1), 19, note_color))

    return D(key, title, (int(width), height), nodes, edges, texts=texts)


def _max_note_lines(s: S) -> int:
    own = len(s.note.split("\n")) if s.note else 0
    return max([own] + [_max_note_lines(c) for c in (s.yes, s.no) if c])


def write_tree(scene: D, out_dir: Path) -> None:
    """Write <key>.svg and <key>.excalidraw, fixing the height of text inside nodes."""
    write(scene, out_dir)
    path = out_dir / f"{scene.key}.excalidraw"
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {element["id"]: element for element in data["elements"]}
    for element in data["elements"]:
        if element["type"] != "text" or not element.get("containerId"):
            continue
        shape = by_id[element["containerId"]]
        element["height"] = len(element["text"].splitlines()) * element["fontSize"] * element["lineHeight"]
        element["y"] = shape["y"] + (shape["height"] - element["height"]) / 2
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def full_binary(weights):
    """Complete include/exclude tree over `weights`; node label = running sum."""

    def grow(total, i):
        s = S(str(total))
        if i < len(weights):
            s.yes = grow(total + weights[i], i + 1)
            s.no = grow(total, i + 1)
        return s

    return grow(0, 0)
