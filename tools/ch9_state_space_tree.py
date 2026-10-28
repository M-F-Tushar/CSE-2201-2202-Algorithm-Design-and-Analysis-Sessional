"""Chapter 9 diagram: the lecture-slide state-space tree for subset sum.

Run from the repository root: python tools/ch9_state_space_tree.py
Writes an editable .excalidraw scene and a matching .svg preview.
"""
from __future__ import annotations

from pathlib import Path

from state_space_tree import full_binary, state_space_tree, write_tree

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Chapter 9 - Backtracking/diagrams"

WEIGHTS, TARGET = [2, 4, 6], 6


def subset_sum_slide():
    return state_space_tree(
        "ch9-05-subset-sum-state-space-tree",
        "Sum of Subset Problem: State-Space Tree for 3 Items",
        "w₁ = 2,   w₂ = 4,   w₃ = 6   and   S = 6",
        full_binary(WEIGHTS),
        ["i₁", "i₂", "i₃"],
        "The sum of the included integers is stored at the node.",
    )


def main():
    scene = subset_sum_slide()
    write_tree(scene, OUT)
    print(f"Wrote {scene.key} to {OUT}")


if __name__ == "__main__":
    main()
