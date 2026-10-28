# CSE 2201 Class Tests 01–04 — Diagram Index

**Coverage: all four test answer sets, with 15 SVG previews and 15 editable Excalidraw scenes.** The complete answers are in [`../README.md`](../README.md), in CT1 → CT2 → CT3 → CT4 order.

| Format | Use |
|--------|-----|
| `.svg` | Static preview rendered in Markdown |
| `.excalidraw` | Editable scene; open in Excalidraw |

> [!IMPORTANT]
> CT1 Q4 uses a labelled illustrative knapsack instance because no item data was visible in its scan. CT2 Q3's diagonal weights (3→1=6, 4→2=7) are uncertain readings. CT3 is identified from its filename as `CSE 2201 - CT - 3.pdf`; its internal header says “Class Test: 01.” CT3 Q3 follows task (c)'s range `[2,6]`, not the conflicting `[1,4]` code comment. CT4 is transcribed from `CSE 2201 - CT - 4.pdf`; it does not specify `n`, so the 4-Queens boards are illustrative examples.

## Complete coverage

| Test / question | Diagram | Preview | Editable source |
|-----------------|---------|---------|-----------------|
| CT1 Q1 | Principle of Optimality in a shortest-route graph | [SVG](ct1-01-principle-optimality.svg) | [Excalidraw](ct1-01-principle-optimality.excalidraw) |
| CT1 Q2 | Repeated calls in naive F(5) recursion | [SVG](ct1-02-fib-recursion.svg) | [Excalidraw](ct1-02-fib-recursion.excalidraw) |
| CT1 Q2 | Bottom-up Fibonacci table | [SVG](ct1-03-fib-table.svg) | [Excalidraw](ct1-03-fib-table.excalidraw) |
| CT1 Q3 | LCS table c[i,j] for AGGTAB and GXTXAYB, with arrows | [SVG](ct1-04-lcs.svg) | [Excalidraw](ct1-04-lcs.excalidraw) |
| CT1 Q4 | Illustrative 0/1 knapsack table V[i,j], with skip/take arrows | [SVG](ct1-05-knapsack.svg) | [Excalidraw](ct1-05-knapsack.excalidraw) |
| CT2 Q1 | DAG with the DFS-based topological order | [SVG](ct2-01-topological.svg) | [Excalidraw](ct2-01-topological.excalidraw) |
| CT2 Q2 | Bellman–Ford graph and shortest route from S to T | [SVG](ct2-02-bellman-ford.svg) | [Excalidraw](ct2-02-bellman-ford.excalidraw) |
| CT2 Q3 | Four-vertex graph used for Floyd–Warshall | [SVG](ct2-03-floyd-warshall.svg) | [Excalidraw](ct2-03-floyd-warshall.excalidraw) |
| CT3 Q1 | Naive DSU chain compared with union by rank | [SVG](ct3-01-union-by-rank.svg) | [Excalidraw](ct3-01-union-by-rank.excalidraw) |
| CT3 Q2 | Divide-and-conquer maximum-subarray recursion tree | [SVG](ct3-02-maximum-subarray.svg) | [Excalidraw](ct3-02-maximum-subarray.excalidraw) |
| CT3 Q3(a–d) | Segment tree with range `[2,6]` cover highlighted | [SVG](ct3-03-segment-tree.svg) | [Excalidraw](ct3-03-segment-tree.excalidraw) |
| CT4 Q1 | Subset-sum state-space tree showing all four include/exclude choices | [SVG](ct4-01-state-space-tree.svg) | [Excalidraw](ct4-01-state-space-tree.excalidraw) |
| CT4 Q2 | Zero-based board showing the column, upper-right, and upper-left scans | [SVG](ct4-02-queen-constraints.svg) | [Excalidraw](ct4-02-queen-constraints.excalidraw) |
| CT4 Q3 | Graph coloring and subset sum as backtracking applications | [SVG](ct4-03-backtracking-applications.svg) | [Excalidraw](ct4-03-backtracking-applications.excalidraw) |
| CT4 Q4 | Instruction-style board algorithm, search trace, and zero-based 4-Queens solution | [SVG](ct4-04-nqueens-algorithm.svg) | [Excalidraw](ct4-04-nqueens-algorithm.excalidraw) |

## Editing and generation

From the repository root, regenerate the restored CT1/CT2 diagrams with `python tools/ct_sequence_diagrams.py`, CT3 with `python tools/ct3_diagrams.py`, or CT4 with `python tools/ct4_diagrams.py`. Run `python tools/verify_ct4.py` to check the CT4 answer and diagram inventory. Each generator overwrites only its own scenes. After editing an `.excalidraw` source manually, re-export its SVG with the background enabled so both formats stay synchronized.
