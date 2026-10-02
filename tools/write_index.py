"""Write a diagrams/README.md index for each chapter and the root directory."""

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

HEADER = """# {chapter} — Diagram Index

Every diagram in this section is a hand-drawn **Excalidraw** scene, stored twice:

| File | Purpose |
|------|---------|
| `<name>.svg` | Static export — this is what renders inside the README |
| `<name>.excalidraw` | Editable source — open at [excalidraw.com](https://excalidraw.com) or with the VS Code Excalidraw extension |

> [!IMPORTANT]
> The `.excalidraw` file is the source of truth for manual edits. After changing one,
> re-export the matching `.svg` from Excalidraw (**File → Export image → SVG**, background on)
> so the README stays in sync.

---

## Diagrams

| # | Diagram | Preview | Edit |
|---|---------|---------|------|
"""

TARGETS = [
    ("Algorithm Design and Analysis — Course Roadmap", root_diagrams),
    ("Chapter 2 — Complexity Analysis and Asymptotic Notation", ch2_diagrams),
    ("Chapter 3 — Recurrences Correctness and Loop Invariants", ch3_diagrams),
    ("Chapter 4 — Searching and Basic Traversal", ch4_diagrams),
    ("Chapter 7 — Greedy Algorithms", ch7_diagrams),
    ("Chapter 8 — Dynamic Programming", ch8_diagrams),
    ("Chapter 11 — Graph Algorithms", ch11_diagrams),
    ("Chapter 15 — Lower Bound Theory and NP Completeness", ch15_diagrams),
]


def main() -> None:
    for chapter_title, module in TARGETS:
        out = ROOT / module.OUT
        out.mkdir(parents=True, exist_ok=True)
        rows = [
            f"| {i} | {d.title} | [`{d.key}.svg`]({d.key}.svg) | [`{d.key}.excalidraw`]({d.key}.excalidraw) |"
            for i, d in enumerate(module.DIAGRAMS, 1)
        ]
        body = HEADER.format(chapter=chapter_title) + "\n".join(rows) + "\n"
        (out / "README.md").write_text(body, encoding="utf-8")
        print(f"{out.name if out.parent == ROOT else out.parent.name}: indexed {len(rows)} diagrams")


if __name__ == "__main__":
    main()
