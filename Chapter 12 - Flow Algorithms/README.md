# Chapter 12 - Flow Algorithms

[Previous: Chapter 11 - Graph Algorithms](../Chapter%2011%20-%20Graph%20Algorithms/README.md) | [Home](../README.md) | [Next: Chapter 13 - Approximation Algorithms](../Chapter%2013%20-%20Approximation%20Algorithms/README.md)

---

A flow network models something that moves through a graph: water through pipes, packets through links, cars through roads. Each edge can carry only a limited amount. The **maximum-flow problem** asks how much can be pushed from a source $s$ to a sink $t$ at the same time. The same machinery also solves matching problems.

This chapter covers the vocabulary of flow networks, residual graphs, augmenting paths, the Ford-Fulkerson method, the Edmonds-Karp algorithm, the max-flow min-cut idea, and bipartite matching. It builds on the graph representations and BFS of [Chapter 11](../Chapter%2011%20-%20Graph%20Algorithms/README.md). It intentionally contains no implementation code.

---

## Start Here: The Idea in Plain Words

**Think of water pipes.** Water starts at a tank (the **source**, called $s$) and must reach a house (the **sink**, called $t$). Each pipe can carry only so much water. The big question: **how much water can reach the house at the same time?**

**Two easy examples.**

- One pipe from $s$ to $t$ that carries 5. The answer is 5.
- Two pipes in a row, the first carries 5, the second carries 3. The answer is only 3. The narrowest pipe limits everything.

With many pipes joined together, finding the answer is harder. That is what this chapter teaches.

**The method in plain words.**

1. Start with no water moving.
2. Look for **any route** from $s$ to $t$ that still has room in every pipe.
3. Send as much water as the narrowest pipe on that route allows.
4. Repeat. When no route with room is left, you are done.

**One clever part.** Sometimes an early choice was a bad idea. The method lets you **take back** some water you already sent, so it can go a better way. This is the "backward edge" idea. It is the hardest idea in the chapter, so read the worked example slowly.

**Words used in this chapter, in simple terms**

| Word | Simple meaning |
| :--- | :--- |
| Flow network | A map of one-way pipes, each with a size limit. |
| Source / sink | Where the water starts / where it must end. |
| Capacity | The most a pipe can carry. |
| Flow | How much water is really going through a pipe now. |
| Residual graph | A map of the **room left** in each pipe, and how much we may take back. |
| Augmenting path | A route from source to sink that still has room. |
| Bottleneck | The narrowest pipe on a route. |
| Cut | A line that splits the map into a source side and a sink side. |
| Matching | Pairs of people and jobs where nobody is used twice. |

**Before you start:** it helps to know how a graph is drawn and how BFS works ([Chapter 11](../Chapter%2011%20-%20Graph%20Algorithms/README.md)).

---

## Table of Contents

1. [Flow Networks](#flow-networks)
2. [Residual Graph](#residual-graph)
3. [Augmenting Paths and the Ford-Fulkerson Method](#augmenting-paths-and-the-ford-fulkerson-method)
4. [Worked Example](#worked-example)
5. [Edmonds-Karp Algorithm](#edmonds-karp-algorithm)
6. [Max-Flow Min-Cut](#max-flow-min-cut)
7. [Bipartite Matching](#bipartite-matching)
8. [Correctness and Complexity](#correctness-and-complexity)
9. [Practice and Exam Notes](#practice-and-exam-notes)

---

## Flow Networks

A **flow network** is a directed graph $G = (V, E)$ with:

- a **source** $s$, where flow starts, and a **sink** $t$, where it ends;
- a **capacity** $c(u, v) \ge 0$ on every edge, the most that edge can carry.

A **flow** assigns each edge a value $f(u, v)$ that satisfies two rules:

1. **Capacity constraint:** $0 \le f(u, v) \le c(u, v)$.
2. **Flow conservation:** for every vertex other than $s$ and $t$, flow in equals flow out.

The **value** of a flow, $|f|$, is the net flow leaving the source. The **maximum-flow problem** asks for a flow of largest value.

![A flow network with source s, sink t and capacities on every edge](diagrams/ch12-01-flow-network.svg)

See the [diagram index](diagrams/README.md) for editable Excalidraw sources and SVG previews.

| Situation | How to model it |
| :--- | :--- |
| Several sources or sinks | Add a **super-source** with infinite-capacity edges to every source, and a **super-sink** that every sink points to. |
| Vertex capacity | Split the vertex into $v_{in} \to v_{out}$ with that capacity. |
| Undirected edge | Replace it with two opposite directed edges of the same capacity. |

---

## Residual Graph

Given a flow $f$, the **residual graph** $G_f$ shows where more flow could still be sent. For every edge $(u, v)$:

| Residual edge | Residual capacity | Meaning |
| :--- | :--- | :--- |
| Forward $(u, v)$ | $c(u, v) - f(u, v)$ | Unused room: we can push this much more. |
| Backward $(v, u)$ | $f(u, v)$ | Flow already sent: we can **cancel** up to this much. |

Only edges with positive residual capacity appear. The backward edges are the key idea. They let the algorithm undo an earlier choice that turned out to be poor, without starting over.

![Residual graph after pushing one unit along s-a-b-t, with dashed reverse edges](diagrams/ch12-02-residual-graph.svg)

---

## Augmenting Paths and the Ford-Fulkerson Method

An **augmenting path** is a simple path from $s$ to $t$ in the residual graph. Its **bottleneck** is the smallest residual capacity on the path. Pushing the bottleneck amount along the path increases the flow value by exactly that amount:

- on a forward residual edge, the edge's flow increases;
- on a backward residual edge, the flow on the original edge decreases (it is cancelled).

**Ford-Fulkerson method**

1. Start with flow 0 on every edge.
2. Build the residual graph.
3. If there is a path from $s$ to $t$ in the residual graph, push its bottleneck along it, and repeat from step 2.
4. If there is no such path, stop. The current flow is maximum.

![Augmenting loop: build residual graph, find a path, push the bottleneck, repeat](diagrams/ch12-03-augmenting-path-loop.svg)

Ford-Fulkerson is a *method* because it does not say how to find the path. Any search (DFS, BFS, a heuristic) is allowed, and the choice affects the running time.

---

## Worked Example

Use the network in the first diagram: $c(s,a) = 2$, $c(s,b) = 2$, $c(a,b) = 1$, $c(a,t) = 2$, $c(b,t) = 2$.

**Ford-Fulkerson with an unlucky first path.**

| Step | Augmenting path | Bottleneck | Flow value |
| :---: | :--- | :---: | :---: |
| 1 | $s \to a \to b \to t$ | $\min(2, 1, 2) = 1$ | 1 |
| 2 | $s \to a \to t$ | $\min(1, 2) = 1$ | 2 |
| 3 | $s \to b \to t$ | $\min(2, 1) = 1$ | 3 |
| 4 | $s \to b \to a \to t$ (uses the **backward** edge $b \to a$) | $\min(1, 1, 1) = 1$ | 4 |

Step 4 shows why backward edges matter. After steps 1 to 3, the edge $a \to b$ carries one unit, and no forward path is left. The backward edge $b \to a$ cancels that unit of $a \to b$, rerouting it as $a \to t$ instead, so the flow from $b$ can proceed to $t$ through $a$. Without backward edges, the algorithm would stop at value 3, which is **not** maximum.

**Final flow:** $f(s,a) = 2$, $f(s,b) = 2$, $f(a,b) = 0$, $f(a,t) = 2$, $f(b,t) = 2$. The maximum flow value is **4**.

---

## Edmonds-Karp Algorithm

**Edmonds-Karp** is Ford-Fulkerson with one rule: always augment along a **shortest path** (fewest edges) in the residual graph, found with **BFS**.

On the same network, BFS from $s$ finds $s \to a \to t$ first (two edges, bottleneck 2), then $s \to b \to t$ (two edges, bottleneck 2). After these **two** augmentations the flow is 4 and $s$ has no outgoing residual edge. The unlucky four-step sequence above never happens, because the zig-zag path $s \to a \to b \to t$ has three edges and is longer than the alternatives.

Why prefer shortest paths? The shortest-path distance from $s$ to any vertex never decreases during the algorithm, and each augmentation saturates at least one *critical* edge. Together these facts bound the number of augmentations by $O(VE)$, no matter how large the capacities are.

| Method | Path rule | Augmentations | Total time |
| :--- | :--- | :--- | :--- |
| Ford-Fulkerson | Any path (for example DFS) | Up to $\lvert f^*\rvert$ for integer capacities | $O(E \cdot \lvert f^*\rvert)$ |
| Edmonds-Karp | Shortest path by edge count (BFS) | $O(VE)$ | $O(VE^2)$ |

Here $\lvert f^*\rvert$ is the value of the maximum flow. Ford-Fulkerson depends on the *numbers* in the capacities (a path might add only 1 unit per round), while Edmonds-Karp depends only on the *shape* of the graph.

---

## Max-Flow Min-Cut

An **$s$-$t$ cut** $(S, T)$ splits the vertices into two sets with $s \in S$ and $t \in T$. Its **capacity** is the total capacity of edges going **from $S$ to $T$** (edges in the other direction are not counted):

$$c(S, T) = \sum_{u \in S,\ v \in T} c(u, v)$$

Every unit of flow from $s$ to $t$ must cross every cut, so no flow can exceed any cut's capacity. The converse is the central theorem.

**Max-flow min-cut theorem.** For a flow $f$ the following are equivalent:

1. $f$ is a maximum flow.
2. The residual graph $G_f$ has no path from $s$ to $t$.
3. $|f| = c(S, T)$ for some cut $(S, T)$, which is then a **minimum cut**.

**Reading the minimum cut from the answer.** When the algorithm stops, let $S$ be the set of vertices still reachable from $s$ in the residual graph, and $T$ the rest. In the example, $s$ has no outgoing residual edge, so $S = \{s\}$ and $T = \{a, b, t\}$. The cut capacity is $c(s,a) + c(s,b) = 2 + 2 = 4$, equal to the flow value. So 4 is both the maximum flow and the minimum cut.

![Maximum flow 4 equals the minimum cut capacity 4](diagrams/ch12-04-max-flow-min-cut.svg)

---

## Bipartite Matching

A graph is **bipartite** if its vertices split into a left set $L$ and a right set $R$ with every edge between the two sets. A **matching** is a set of edges, no two sharing a vertex. A **maximum matching** has the most edges.

**Reduction to maximum flow.**

1. Add a source $s$ with an edge $s \to u$ for every $u \in L$.
2. Add a sink $t$ with an edge $v \to t$ for every $v \in R$.
3. Direct every original edge from $L$ to $R$.
4. Give every edge capacity **1**.

With integer capacities, a maximum flow can always be chosen with every edge carrying 0 or 1 (the integrality property). The edges $L \to R$ that carry flow 1 form a matching, and **maximum flow value = maximum matching size**.

![Bipartite matching as a unit-capacity flow network, with the matched edges highlighted](diagrams/ch12-05-bipartite-matching.svg)

**Example.** Left $\{A, B, C\}$, right $\{X, Y, Z\}$, edges $A\text{-}X$, $A\text{-}Y$, $B\text{-}X$, $C\text{-}Y$, $C\text{-}Z$.

| Step | Action | Matching |
| :---: | :--- | :--- |
| 1 | $A$ takes its first free neighbor $X$. | $\{A\text{-}X\}$ |
| 2 | $B$ wants $X$, which is taken. The augmenting path $s \to B \to X \to A \to Y \to t$ reassigns $A$ to $Y$ and gives $X$ to $B$. | $\{A\text{-}Y, B\text{-}X\}$ |
| 3 | $C$'s neighbor $Y$ is taken, but $Z$ is free. | $\{A\text{-}Y, B\text{-}X, C\text{-}Z\}$ |

The matching has size 3 and every left vertex is matched, so it is a **perfect matching**. In matching language, an augmenting path is an *alternating path*: it alternates between non-matching and matching edges and starts and ends at unmatched vertices.

A useful link to [Chapter 13](../Chapter%2013%20-%20Approximation%20Algorithms/README.md): in a bipartite graph, the maximum matching size equals the minimum vertex cover size (König's theorem). For general graphs, finding a minimum vertex cover is NP-hard.

---

## Correctness and Complexity

**Termination and correctness.** Each augmentation raises the integer flow value by at least 1, and the value is bounded by the capacity of any cut, so the method terminates when capacities are integers. When it stops there is no augmenting path, and by the theorem above the flow is maximum.

| Algorithm | Time | Notes |
| :--- | :--- | :--- |
| Ford-Fulkerson | $O(E \cdot \lvert f^*\rvert)$ | Integer capacities only; can be slow when $\lvert f^*\rvert$ is large. |
| Edmonds-Karp | $O(VE^2)$ | $O(VE)$ augmentations, each a BFS of $O(E)$. |
| Bipartite matching via Ford-Fulkerson | $O(VE)$ | The flow value is at most $\min(\lvert L\rvert, \lvert R\rvert) \le V$, and each augmentation costs $O(E)$. |

The residual graph needs $O(V + E)$ space. A specialized algorithm (Hopcroft-Karp) matches bipartite graphs in $O(E\sqrt{V})$, but it is beyond the syllabus.

---

## Practice and Exam Notes

- Define flow, capacity, source, sink, residual graph, and augmenting path in one sentence each.
- When tracing, write the residual capacities after each augmentation, and circle the bottleneck edge. Mark backward edges clearly.
- Explain **why backward edges exist**: they let a later path cancel flow that an earlier path should not have used.
- State the difference between Ford-Fulkerson (any path) and Edmonds-Karp (BFS shortest path) and give both bounds.
- To find a minimum cut, take the vertices reachable from $s$ in the final residual graph. Count only edges from $S$ to $T$.
- For matching, draw the flow network with all capacities 1 and report the matched $L$-$R$ edges.
- Frequently asked: the max-flow problem, residual graph construction, a Ford-Fulkerson trace on a given network, and bipartite matching.

### Final Revision Checklist

- I can check the capacity and conservation rules for a given flow.
- I can build a residual graph with forward and backward edges.
- I can find an augmenting path, its bottleneck, and update the flow.
- I can explain why Edmonds-Karp has a running time independent of capacity values.
- I can state the max-flow min-cut theorem and read a minimum cut from a final residual graph.
- I can reduce bipartite matching to maximum flow.

---

[Previous: Chapter 11 - Graph Algorithms](../Chapter%2011%20-%20Graph%20Algorithms/README.md) | [Home](../README.md) | [Next: Chapter 13 - Approximation Algorithms](../Chapter%2013%20-%20Approximation%20Algorithms/README.md)
