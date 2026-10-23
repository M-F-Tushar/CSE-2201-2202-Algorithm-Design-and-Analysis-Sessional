# 1st Batch Theory — Diagram Index

All **27/27 subquestions** have suitable linked visuals: **23 SVG/source pairs**
(22 topic visuals plus one full-paper roadmap). Shared visuals are listed against
every part they genuinely explain. Printed inputs and the two source-paper graphs were
checked against the supplied 2023 scan; extra teaching examples are labeled illustrative.

The `.excalidraw` scene is editable in [Excalidraw](https://excalidraw.com).
After a manual scene edit, re-export its SVG so the Markdown preview stays synchronized.
The scoped generator `tools/b1_theory_diagrams.py` uses the shared engine without
changing shared tools. Running it replaces its 20 listed scenes (including five
corrected old visuals) and this index; it preserves manual scenes 03, 06, 08.
Do not regenerate over later manual edits without reconciling them first.

| Parts | Diagram | Preview | Editable source |
|---|---|---|---|
| Overview: Q1–Q8 | 1st Batch Theory: full-paper roadmap | [SVG](b1-theory-01-question-escalator.svg) | [Excalidraw](b1-theory-01-question-escalator.excalidraw) |
| Q2(a), Q2(c), Q3(b) | Q2(a,c), Q3(b): balanced recurrence | [SVG](b1-theory-02-recursion-tree.svg) | [Excalidraw](b1-theory-02-recursion-tree.excalidraw) |
| Q3(d) | Heap Sort: Max-Heap After Build Step | [SVG](b1-theory-03-heap-build-tree.svg) | [Excalidraw](b1-theory-03-heap-build-tree.excalidraw) |
| Q5(c) | Q5(c): positive-item subset-sum search prefix | [SVG](b1-theory-04-subset-sum-tree.svg) | [Excalidraw](b1-theory-04-subset-sum-tree.excalidraw) |
| Q5(d) | Q5(d): paper graph and backtracking | [SVG](b1-theory-05-hamiltonian-tree.svg) | [Excalidraw](b1-theory-05-hamiltonian-tree.excalidraw) |
| Q7(b) | Q7(b): Bellman-Ford Shortest Paths from Source A | [SVG](b1-theory-06-bellman-ford-graph.svg) | [Excalidraw](b1-theory-06-bellman-ford-graph.excalidraw) |
| Q8(a) | Q8(a): known class relations (not a strict Venn) | [SVG](b1-theory-07-classes-venn.svg) | [Excalidraw](b1-theory-07-classes-venn.excalidraw) |
| Q8(c) | Q8(c): Dijkstra's Shortest Paths from Node A | [SVG](b1-theory-08-dijkstra-graph.svg) | [Excalidraw](b1-theory-08-dijkstra-graph.excalidraw) |
| Q1(a) | Q1(a): design and analysis | [SVG](b1-theory-09-design-analysis.svg) | [Excalidraw](b1-theory-09-design-analysis.excalidraw) |
| Q1(b) | Q1(b): illustrative linear search, n = 5 | [SVG](b1-theory-10-case-analysis.svg) | [Excalidraw](b1-theory-10-case-analysis.excalidraw) |
| Q1(c) | Q1(c): unit-coefficient growth comparison | [SVG](b1-theory-11-growth.svg) | [Excalidraw](b1-theory-11-growth.excalidraw) |
| Q2(b) | Q2(b): illustrative n = 8 loop counts | [SVG](b1-theory-12-loop-counts.svg) | [Excalidraw](b1-theory-12-loop-counts.excalidraw) |
| Q3(a) | Q3(a): illustrative divide, conquer, combine | [SVG](b1-theory-13-merge-sort.svg) | [Excalidraw](b1-theory-13-merge-sort.excalidraw) |
| Q3(c) | Q3(c): quicksort space conventions | [SVG](b1-theory-14-quicksort-space.svg) | [Excalidraw](b1-theory-14-quicksort-space.excalidraw) |
| Q4(a), Q6(d) | Q4(a), Q6(d): unlimited coins {1, 3, 4}, amount 6 | [SVG](b1-theory-15-coin-change.svg) | [Excalidraw](b1-theory-15-coin-change.excalidraw) |
| Q4(b) | Q4(b): Fibonacci F0 = 0, F1 = 1 | [SVG](b1-theory-16-memo-tab.svg) | [Excalidraw](b1-theory-16-memo-tab.excalidraw) |
| Q4(c) | Q4(c): Prim and Kruskal on the stated graph | [SVG](b1-theory-17-mst.svg) | [Excalidraw](b1-theory-17-mst.excalidraw) |
| Q5(a), Q5(b) | Q5(a,b): choose, prune, backtrack | [SVG](b1-theory-18-queens-backtracking.svg) | [Excalidraw](b1-theory-18-queens-backtracking.excalidraw) |
| Q6(a) | Q6(a): valid recurrence and reusable subproblems | [SVG](b1-theory-19-dp-properties.svg) | [Excalidraw](b1-theory-19-dp-properties.excalidraw) |
| Q6(b), Q7(c) | Q6(b), Q7(c): 0/1 knapsack recurrence and table | [SVG](b1-theory-20-knapsack.svg) | [Excalidraw](b1-theory-20-knapsack.excalidraw) |
| Q6(c) | Q6(c): coin grid and maximum-collection DP | [SVG](b1-theory-21-grid.svg) | [Excalidraw](b1-theory-21-grid.excalidraw) |
| Q7(a) | Q7(a): negative edge defeats label-setting Dijkstra | [SVG](b1-theory-22-negative-edge.svg) | [Excalidraw](b1-theory-22-negative-edge.excalidraw) |
| Q8(b) | Q8(b): threshold decision versus optimization | [SVG](b1-theory-23-decision-optimization.svg) | [Excalidraw](b1-theory-23-decision-optimization.excalidraw) |

## Interpretation notes

- Recurrence tree uses a complete n=8 example, not disconnected symbolic leaves.
- Subset-sum and queen trees show only the search prefix; they do not claim full enumeration.
- Hamiltonian visual uses the graph transcribed from the paper and shows the search prefix through the first circuit.
- NP visual states known inclusions only; it assumes neither P=NP nor P≠NP.
- Green graph edges mark the reported MST/shortest-path tree, not extra graph edges.
- Dijkstra keeps the first predecessor on equal distances; F and C each have tied shortest routes.

[Back to answers](../README.md)
