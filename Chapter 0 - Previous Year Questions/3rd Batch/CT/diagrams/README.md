# CSE 2201 Class Tests 01–03 — Diagram Index

**Coverage: all three test answer sets, with 11 SVG previews and 11 editable Excalidraw scenes.** The complete answers are in [`../README.md`](../README.md), in CT1 → CT2 → CT3 order.

| Format | Use |
|--------|-----|
| `.svg` | Static preview rendered in Markdown |
| `.excalidraw` | Editable scene; open in Excalidraw |

> [!IMPORTANT]
> CT1 Q4 uses a labelled illustrative knapsack instance because no item data was visible in its scan. CT2 Q3's diagonal weights (3→1=6, 4→2=7) are uncertain readings. CT3 is identified from its filename as `CSE 2201 - CT - 3.pdf`; its internal header says “Class Test: 01.” CT3 Q3 follows task (c)'s range `[2,6]`, not the conflicting `[1,4]` code comment.

## Complete coverage

| Test / question | Diagram | Preview | Editable source |
|-----------------|---------|---------|-----------------|
| CT1 Q1 | Principle of Optimality in a shortest-route graph | [SVG](ct1-01-principle-optimality.svg) | [Excalidraw](ct1-01-principle-optimality.excalidraw) |
| CT1 Q2 | Repeated calls in naive F(5) recursion | [SVG](ct1-02-fib-recursion.svg) | [Excalidraw](ct1-02-fib-recursion.excalidraw) |
| CT1 Q2 | Bottom-up Fibonacci table | [SVG](ct1-03-fib-table.svg) | [Excalidraw](ct1-03-fib-table.excalidraw) |
| CT1 Q3 | LCS table for AGGTAB and GXTXAYB | [SVG](ct1-04-lcs.svg) | [Excalidraw](ct1-04-lcs.excalidraw) |
| CT1 Q4 | Illustrative 0/1 knapsack DP table | [SVG](ct1-05-knapsack.svg) | [Excalidraw](ct1-05-knapsack.excalidraw) |
| CT2 Q1 | DAG with a valid topological order | [SVG](ct2-01-topological.svg) | [Excalidraw](ct2-01-topological.excalidraw) |
| CT2 Q2 | Bellman–Ford graph and shortest route from S to T | [SVG](ct2-02-bellman-ford.svg) | [Excalidraw](ct2-02-bellman-ford.excalidraw) |
| CT2 Q3 | Four-vertex graph used for Floyd–Warshall | [SVG](ct2-03-floyd-warshall.svg) | [Excalidraw](ct2-03-floyd-warshall.excalidraw) |
| CT3 Q1 | Naive DSU chain compared with union by rank | [SVG](ct3-01-union-by-rank.svg) | [Excalidraw](ct3-01-union-by-rank.excalidraw) |
| CT3 Q2 | Divide-and-conquer maximum-subarray recursion tree | [SVG](ct3-02-maximum-subarray.svg) | [Excalidraw](ct3-02-maximum-subarray.excalidraw) |
| CT3 Q3(a–d) | Segment tree with range `[2,6]` cover highlighted | [SVG](ct3-03-segment-tree.svg) | [Excalidraw](ct3-03-segment-tree.excalidraw) |

## Editing and generation

From the repository root, regenerate the restored CT1/CT2 diagrams with `python tools/ct_sequence_diagrams.py` and the CT3 diagrams with `python tools/ct3_diagrams.py`. Each script overwrites its own generated scenes. After editing an `.excalidraw` source, re-export its SVG with the background enabled so both formats stay synchronized.
