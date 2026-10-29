"""Skeleton of the CT2 Q2 exam figure (weighted directed graph, source S, destination T).

Draws only what the exam paper shows: six vertices and nine weighted directed edges,
with no distances, parents, or highlighted path. Answer steps can be layered on top.

Run from the repository root: python tools/ct2_q2_skeleton.py
Output goes to a subfolder so the 15-pair inventory in CT/diagrams stays unchanged.
"""
from __future__ import annotations

import json
from pathlib import Path

from excalidraw_gen import D, E, N, T, write

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Chapter 0 - Previous Year Questions/3rd Batch/CT/diagrams/skeletons"

R = 32  # vertex radius
CENTERS = {"S": (110, 300), "A": (330, 130), "B": (610, 130),
           "C": (330, 470), "D": (610, 470), "T": (830, 300)}

# (from, to, weight, label centre) -- edge list read from the exam figure.
EDGES = [
    ("S", "A", 5, (205, 190)),
    ("S", "C", -2, (200, 415)),
    ("A", "B", 1, (470, 105)),
    ("C", "A", 2, (306, 300)),
    ("C", "B", 4, (452, 286)),
    ("B", "D", -1, (636, 300)),
    ("B", "T", 3, (746, 192)),
    ("C", "D", 4, (470, 497)),
    ("D", "T", 1, (746, 408)),
]


def build() -> D:
    nodes = [
        N(v, v, x - R, y - R, 2 * R, 2 * R, "yellow" if v in "ST" else "blue", "ellipse", 22)
        for v, (x, y) in CENTERS.items()
    ]
    edges = [E(u, v, route="straight") for u, v, _, _ in EDGES]
    texts = [T(f"w{i}", str(w).replace("-", "\u2212"), cx, cy, 20, "#1e1e1e", True)
             for i, (_, _, w, (cx, cy)) in enumerate(EDGES)]
    return D(
        key="ct2-02-bellman-ford-skeleton",
        title="CT2 Q2: Exam graph (skeleton) \u2014 source S, destination T",
        size=(940, 580),
        nodes=nodes,
        edges=edges,
        texts=texts,
        caption="Vertices S, A, B, C, D, T; 9 directed edges as drawn in the exam figure",
    )


def main():
    scene = build()
    write(scene, OUT)
    path = OUT / (scene.key + ".excalidraw")
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {e["id"]: e for e in data["elements"]}
    for text in data["elements"]:
        if text["type"] != "text" or not text.get("containerId"):
            continue
        shape = by_id[text["containerId"]]
        text["height"] = len(text["text"].splitlines()) * text["fontSize"] * text["lineHeight"]
        text["y"] = shape["y"] + (shape["height"] - text["height"]) / 2
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {scene.key} to {OUT}")


if __name__ == "__main__":
    main()
