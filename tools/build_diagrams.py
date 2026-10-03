"""Render every course diagram to .excalidraw + .svg."""

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).parent))

MODULES = [
    "root_diagrams",
    "ch2_diagrams",
    "ch3_diagrams",
    "ch4_diagrams",
    "ch6_diagrams",
    "ch7_diagrams",
    "ch8_diagrams",
    "ch11_diagrams",
    "ch15_diagrams",
]


def main() -> None:
    write = importlib.import_module("tools.excalidraw_gen").write
    total = 0
    for module_name in MODULES:
        module = importlib.import_module(module_name)
        out = ROOT / module.OUT
        for d in module.DIAGRAMS:
            write(d, out)
            total += 1
            print(f"  {d.key}  ({d.size[0]}x{d.size[1]}) -> {out}")
    print(f"\nWrote {total} diagrams (.excalidraw + .svg) across {len(MODULES)} modules")


if __name__ == "__main__":
    main()
