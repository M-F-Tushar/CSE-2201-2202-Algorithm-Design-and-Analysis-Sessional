# Chapter 12 — Flow Algorithms — Diagram Index

Each diagram is stored as an editable **Excalidraw** scene and an SVG preview. The `.excalidraw` source can be opened at [excalidraw.com](https://excalidraw.com); the SVG is embedded in the chapter notes.

| # | Diagram | Preview | Editable source |
|---|---------|---------|-----------------|
| 1 | A flow network with source, sink, and capacities | [`ch12-01-flow-network.svg`](ch12-01-flow-network.svg) | [`ch12-01-flow-network.excalidraw`](ch12-01-flow-network.excalidraw) |
| 2 | Residual graph with a reverse edge after one augmentation | [`ch12-02-residual-graph.svg`](ch12-02-residual-graph.svg) | [`ch12-02-residual-graph.excalidraw`](ch12-02-residual-graph.excalidraw) |
| 3 | Ford-Fulkerson / Edmonds-Karp augmenting-path loop | [`ch12-03-augmenting-path-loop.svg`](ch12-03-augmenting-path-loop.svg) | [`ch12-03-augmenting-path-loop.excalidraw`](ch12-03-augmenting-path-loop.excalidraw) |
| 4 | Maximum flow equals minimum cut | [`ch12-04-max-flow-min-cut.svg`](ch12-04-max-flow-min-cut.svg) | [`ch12-04-max-flow-min-cut.excalidraw`](ch12-04-max-flow-min-cut.excalidraw) |
| 5 | Bipartite matching as a unit-capacity flow network | [`ch12-05-bipartite-matching.svg`](ch12-05-bipartite-matching.svg) | [`ch12-05-bipartite-matching.excalidraw`](ch12-05-bipartite-matching.excalidraw) |
| 6 | Ford-Fulkerson foundations: flow/capacity, residual edges, saturated edge, bottleneck | [`ch12-06-ff-key-terms.svg`](ch12-06-ff-key-terms.svg) | [`ch12-06-ff-key-terms.excalidraw`](ch12-06-ff-key-terms.excalidraw) |
| 7 | Ford-Fulkerson Step 0: the video's network with every edge at 0/capacity | [`ch12-07-ff-example-network.svg`](ch12-07-ff-example-network.svg) | [`ch12-07-ff-example-network.excalidraw`](ch12-07-ff-example-network.excalidraw) |
| 8 | Step 1: search s-a-b-t in Gf, push 5 (flow 5) | [`ch12-08-ff-step-1.svg`](ch12-08-ff-step-1.svg) | [`ch12-08-ff-step-1.excalidraw`](ch12-08-ff-step-1.excalidraw) |
| 9 | Step 2: search s-c-t in Gf, push 3 (flow 8) | [`ch12-09-ff-step-2.svg`](ch12-09-ff-step-2.svg) | [`ch12-09-ff-step-2.excalidraw`](ch12-09-ff-step-2.excalidraw) |
| 10 | Step 3: search s-d-e-t in Gf, push 8 (flow 16) | [`ch12-10-ff-step-3.svg`](ch12-10-ff-step-3.svg) | [`ch12-10-ff-step-3.excalidraw`](ch12-10-ff-step-3.excalidraw) |
| 11 | Step 4: search s-c-b-t in Gf, push 5 (flow 21) | [`ch12-11-ff-step-4.svg`](ch12-11-ff-step-4.svg) | [`ch12-11-ff-step-4.excalidraw`](ch12-11-ff-step-4.excalidraw) |
| 12 | Step 5: search s-d-c-e-t in Gf, push 1 (flow 22) | [`ch12-12-ff-step-5.svg`](ch12-12-ff-step-5.svg) | [`ch12-12-ff-step-5.excalidraw`](ch12-12-ff-step-5.excalidraw) |
| 13 | Final residual graph: no augmenting path, max flow 22 = min cut 22 | [`ch12-13-ff-final-residual-min-cut.svg`](ch12-13-ff-final-residual-min-cut.svg) | [`ch12-13-ff-final-residual-min-cut.excalidraw`](ch12-13-ff-final-residual-min-cut.excalidraw) |
| 14 | Ford-Fulkerson worst case: O(E · \|f*\|) with 1-unit augmentations | [`ch12-14-ff-worst-case.svg`](ch12-14-ff-worst-case.svg) | [`ch12-14-ff-worst-case.excalidraw`](ch12-14-ff-worst-case.excalidraw) |

The `.excalidraw` files are the editable source of truth. If you edit one manually, export its matching SVG again so the preview stays current. The generator is `tools/ch12_diagrams.py`; diagrams 6-14 come from `tools/ch12_ff_diagrams.py`, which replays the Ford-Fulkerson trace in `tools/ch12_ff_trace.py` so every number is computed.
