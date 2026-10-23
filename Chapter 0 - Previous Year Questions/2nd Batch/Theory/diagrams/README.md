# 2nd Batch Theory — Diagram Index

**Coverage: 24 of 24 subquestions (Q1(a)–Q8(c)), plus one full-paper roadmap: 25 SVG previews and 25 editable Excalidraw scenes.** Each subquestion in the [answers](../README.md) embeds its corresponding preview; the introduction embeds the separate roadmap.

| Format | Use |
|--------|-----|
| `.svg` | Static preview rendered in Markdown |
| `.excalidraw` | Editable scene; open in Excalidraw |

> [!IMPORTANT]
> These are clear study diagrams, not facsimiles of the exam paper. Printed inputs, including the Q5(c) graph, were checked against the supplied 2024 scan. Q7(a), Q7(b), and Q8(b) do not provide specific graph/item/job data, so those worked examples are chosen for explanation.

## Complete coverage

| Question | Diagram | Preview | Editable source |
|----------|---------|---------|-----------------|
| Full paper | Section-grouped topic roadmap, not a prerequisite chain | [SVG](b2-theory-25-paper-roadmap.svg) | [Excalidraw](b2-theory-25-paper-roadmap.excalidraw) |
| Q1(a) | Time, total space, and auxiliary space | [SVG](b2-theory-15-time-space.svg) | [Excalidraw](b2-theory-15-time-space.excalidraw) |
| Q1(b) | Divide-and-conquer and greedy patterns | [SVG](b2-theory-16-design-paradigms.svg) | [Excalidraw](b2-theory-16-design-paradigms.excalidraw) |
| Q1(c) | Recursion-level costs and tight bounds | [SVG](b2-theory-17-recurrences.svg) | [Excalidraw](b2-theory-17-recurrences.excalidraw) |
| Q2(a) | P, NP, NP-hard, and NP-complete (assuming P ≠ NP) | [SVG](b2-theory-01-np-classes-venn.svg) | [Excalidraw](b2-theory-01-np-classes-venn.excalidraw) |
| Q2(b) | Undirected BFS graph, levels, and shortest path | [SVG](b2-theory-02-bfs-graph.svg) | [Excalidraw](b2-theory-02-bfs-graph.excalidraw) |
| Q2(c) | Activity dependencies from the paper and the requested variation | [SVG](b2-theory-03-activity-dag.svg) | [Excalidraw](b2-theory-03-activity-dag.excalidraw) |
| Q3(a) | Searching versus traversing | [SVG](b2-theory-18-search-traverse.svg) | [Excalidraw](b2-theory-18-search-traverse.excalidraw) |
| Q3(b) | Linear probes and binary-search intervals | [SVG](b2-theory-19-search-trace.svg) | [Excalidraw](b2-theory-19-search-trace.excalidraw) |
| Q3(c) | Strassen's seven products and result | [SVG](b2-theory-04-strassen-split.svg) | [Excalidraw](b2-theory-04-strassen-split.excalidraw) |
| Q4(a) | Insertion shifts and bubble-sort passes | [SVG](b2-theory-20-insertion-bubble.svg) | [Excalidraw](b2-theory-20-insertion-bubble.excalidraw) |
| Q4(b) | Lomuto quicksort partition tree | [SVG](b2-theory-05-quicksort-partition.svg) | [Excalidraw](b2-theory-05-quicksort-partition.excalidraw) |
| Q4(c) | Merge-sort split and merge tree | [SVG](b2-theory-06-mergesort-tree.svg) | [Excalidraw](b2-theory-06-mergesort-tree.excalidraw) |
| Q5(a) | Greedy exchange proof and coin-change counterexample | [SVG](b2-theory-21-greedy-proof.svg) | [Excalidraw](b2-theory-21-greedy-proof.excalidraw) |
| Q5(b) | Fractional knapsack fill and profit | [SVG](b2-theory-22-fractional-knapsack.svg) | [Excalidraw](b2-theory-22-fractional-knapsack.excalidraw) |
| Q5(c) | Kruskal's MST on the graph shown in the paper | [SVG](b2-theory-07-kruskal-mst.svg) | [Excalidraw](b2-theory-07-kruskal-mst.excalidraw) |
| Q6(a) | Fibonacci overlaps and DP dependencies | [SVG](b2-theory-23-fibonacci-dp.svg) | [Excalidraw](b2-theory-23-fibonacci-dp.excalidraw) |
| Q6(b) | Floyd–Warshall graph and intermediate matrices | [SVG](b2-theory-08-floyd-warshall.svg) | [Excalidraw](b2-theory-08-floyd-warshall.excalidraw) |
| Q6(c) | Full LCS table and highlighted traceback | [SVG](b2-theory-09-lcs-table.svg) | [Excalidraw](b2-theory-09-lcs-table.excalidraw) |
| Q7(a) | Illustrative five-vertex colouring graph and backtracking tree | [SVG](b2-theory-10-colouring-tree.svg) | [Excalidraw](b2-theory-10-colouring-tree.excalidraw) |
| Q7(b) | Best-first knapsack tree with FIFO bound ties | [SVG](b2-theory-11-lc-knapsack-tree.svg) | [Excalidraw](b2-theory-11-lc-knapsack-tree.excalidraw) |
| Q7(c) | Five-queens tree, two solutions, and a later dead end | [SVG](b2-theory-12-nqueens-tree.svg) | [Excalidraw](b2-theory-12-nqueens-tree.excalidraw) |
| Q8(a) | TSP threshold decisions versus optimum and witness | [SVG](b2-theory-24-decision-optimization.svg) | [Excalidraw](b2-theory-24-decision-optimization.excalidraw) |
| Q8(b) | Illustrative job-sequencing depth-first B&B tree | [SVG](b2-theory-13-bnb-job-tree.svg) | [Excalidraw](b2-theory-13-bnb-job-tree.excalidraw) |
| Q8(c) | Held–Karp subset states and minimizing dependencies | [SVG](b2-theory-14-tsp-subsets.svg) | [Excalidraw](b2-theory-14-tsp-subsets.excalidraw) |

## Editing and generation

The retained historical scenes are manually laid out. Their geometry is preserved except for targeted corrections; colours and dashed edges in the editable scenes now match their SVG previews. The LC-search diagram labels **actual expansions**, not all generated nodes, and specifies FIFO ties. The job-sequencing tree uses include-first depth-first search with incumbent updates only at complete feasible leaves.

Ten new subquestion diagram pairs, the full-paper roadmap, and four corrected/replaced pairs (BFS, activity DAG, source-graph MST, and LC-search) are generated with the existing shared engine by the batch-local script:

```sh
python tools/b2_theory_diagrams.py
```

Run from the repository root. To regenerate **only the roadmap** without touching any subquestion visuals, use `python tools/b2_theory_diagrams.py --roadmap-only`. The roadmap groups Q1–Q8 by section, labels Q3's matrix multiplication and Q7(b)'s best-first B&B explicitly, and distinguishes specific cross-topic connections from prerequisites. The script also applies targeted repairs to retained manual scenes without changing shared tools. Running it again overwrites its generated scenes; preserve later manual edits before regenerating. Otherwise, after editing an `.excalidraw` source, re-export the matching SVG with its background enabled so both formats remain synchronized.
