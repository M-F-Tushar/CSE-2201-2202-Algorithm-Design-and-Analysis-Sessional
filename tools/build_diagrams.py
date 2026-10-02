"""Render every course diagram to .excalidraw + .svg."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).parent))

from tools.excalidraw_gen import write  # noqa: E402
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


def main() -> None:
    total = 0
    for module in MODULES:
        out = ROOT / module.OUT
        for d in module.DIAGRAMS:
            write(d, out)
            total += 1
            print(f"  {d.key}  ({d.size[0]}x{d.size[1]}) -> {out}")
    print(f"\nWrote {total} diagrams (.excalidraw + .svg) across {len(MODULES)} modules")


if __name__ == "__main__":
    main()
