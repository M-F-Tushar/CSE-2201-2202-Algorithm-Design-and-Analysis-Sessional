"""Swap every ```mermaid block in the READMEs for its Excalidraw SVG.

Diagram order in each spec module matches the exact order the Mermaid blocks appear
in that markdown file.
"""

import re
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

FENCE = re.compile(r"```mermaid\n.*?\n```", re.DOTALL)

TARGETS = [
    (ROOT / "README.md", root_diagrams),
    (ROOT / "Chapter 2 - Complexity Analysis and Asymptotic Notation" / "README.md", ch2_diagrams),
    (ROOT / "Chapter 3 - Recurrences Correctness and Loop Invariants" / "README.md", ch3_diagrams),
    (ROOT / "Chapter 4 - Searching and Basic Traversal" / "README.md", ch4_diagrams),
    (ROOT / "Chapter 7 - Greedy Algorithms" / "README.md", ch7_diagrams),
    (ROOT / "Chapter 8 - Dynamic Programming" / "README.md", ch8_diagrams),
    (ROOT / "Chapter 11 - Graph Algorithms" / "README.md", ch11_diagrams),
    (ROOT / "Chapter 15 - Lower Bound Theory and NP Completeness" / "README.md", ch15_diagrams),
]


def main() -> None:
    for readme, module in TARGETS:
        text = readme.read_text(encoding="utf-8")
        blocks = FENCE.findall(text)
        if len(blocks) != len(module.DIAGRAMS):
            raise SystemExit(
                f"{readme.name}: {len(blocks)} mermaid blocks but "
                f"{len(module.DIAGRAMS)} diagrams - order would drift"
            )

        it = iter(module.DIAGRAMS)

        def swap(_match):
            d = next(it)
            alt = d.title.replace("[", "(").replace("]", ")")
            return f"![{alt}](diagrams/{d.key}.svg)"

        readme.write_text(FENCE.sub(swap, text), encoding="utf-8")
        label = "root" if readme.parent == ROOT else readme.parent.name
        print(f"{label}: replaced {len(blocks)} mermaid blocks with Excalidraw SVGs")


if __name__ == "__main__":
    main()
