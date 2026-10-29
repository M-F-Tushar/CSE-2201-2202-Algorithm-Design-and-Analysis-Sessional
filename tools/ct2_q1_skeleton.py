"""Skeleton of the CT2 Q1 exam figure (the DAG used for topological sorting).

Reproduces the exam layout: 5 and 4 on top, the centre vertex between them,
2 and 1 on the sides, 3 at the bottom. Only the six vertices and six directed
edges are drawn -- no finish times, stack, or ordering.

Run from the repository root: python tools/ct2_q1_skeleton.py
Output goes to a subfolder so the 15-pair inventory in CT/diagrams stays unchanged.
"""
from __future__ import annotations

import json
from pathlib import Path

from excalidraw_gen import D, E, N, write

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Chapter 0 - Previous Year Questions/3rd Batch/CT/diagrams/skeletons"

R = 32  # vertex radius

# Label of the small centre vertex. The photo reads as "0" (the usual 0-5 DAG);
# the existing CT2 Q1 answer calls it "6". Change this one constant to relabel.
CENTRE = "0"

CENTERS = {"5": (240, 110), "4": (580, 110), CENTRE: (410, 250),
           "2": (110, 320), "1": (710, 320), "3": (410, 450)}

# Directed edges as drawn in the exam figure.
EDGES = [("5", "2"), ("5", CENTRE), ("4", CENTRE), ("4", "1"), ("2", "3"), ("3", "1")]


def build() -> D:
    nodes = [N(v, v, x - R, y - R, 2 * R, 2 * R, "blue", "ellipse", 22)
             for v, (x, y) in CENTERS.items()]
    edges = [E(u, v, route="straight") for u, v in EDGES]
    return D(
        key="ct2-01-topological-skeleton",
        title="CT2 Q1: Exam DAG (skeleton)",
        size=(820, 540),
        nodes=nodes,
        edges=edges,
        caption=f"6 vertices, 6 directed edges as drawn in the exam figure (centre vertex read as {CENTRE})",
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
