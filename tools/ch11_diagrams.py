"""Chapter 11 (Graph Algorithms) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 11 - Graph Algorithms/diagrams"

# 1 ---------------------------------------------------- graph roadmap
graph_roadmap = D(
    key="ch11-01-graph-algorithm-roadmap",
    title="Comprehensive Graph Algorithms Taxonomy and Roadmap",
    size=(1180, 680),
    flow="V",
    nodes=[
        N("root", "Graph G = (V, E)", 490, 60, 200, 52, "blue", "ellipse", bold=True),
        # Categories
        N("c_rep", "Graph Representation", 60, 150, 230, 52, "yellow", size=14, bold=True),
        N("c_trav", "Traversal Algorithms", 350, 150, 230, 52, "yellow", size=14, bold=True),
        N("c_short", "Shortest Path Algorithms", 630, 150, 230, 52, "yellow", size=14, bold=True),
        N("c_mst", "Minimum Spanning Tree", 900, 150, 230, 52, "yellow", size=14, bold=True),
        # Sub-nodes Representation
        N("rep_mat", "Adjacency Matrix\nO(V^2) space, O(1) edge check", 45, 240, 270, 64, "blue", size=13),
        N("rep_list", "Adjacency List\nO(V + E) space, optimal for sparse", 45, 320, 270, 64, "blue", size=13),
        # Sub-nodes Traversal
        N("trav_bfs", "BFS: Level order\nunweighted shortest path", 340, 240, 250, 60, "green", size=13),
        N("trav_dfs", "DFS: Deep traversal\ncycle detection", 340, 310, 250, 60, "green", size=13),
        N("trav_topo", "Topological Sort\nDAG task ordering", 340, 380, 250, 60, "green", size=13),
        N("trav_scc", "Kosaraju / Tarjan\nStrongly connected comps", 340, 450, 250, 60, "green", size=13),
        # Sub-nodes Shortest Path
        N("sp_dijk", "Dijkstra: Nonnegative\nweights O((V+E)log V)", 620, 240, 250, 60, "teal", size=13),
        N("sp_bf", "Bellman-Ford: Negative\nweights & cycle detect", 620, 310, 250, 60, "teal", size=13),
        N("sp_fw", "Floyd-Warshall\nAll-pairs shortest O(V^3)", 620, 380, 250, 60, "teal", size=13),
        # Sub-nodes MST
        N("mst_prim", "Prim's Algorithm\nGrow cut greedily", 895, 240, 240, 60, "violet", size=13),
        N("mst_krusk", "Kruskal's Algorithm\nSort edges + DSU", 895, 310, 240, 60, "violet", size=13),
        N("mst_dsu", "Disjoint Set Union\nUnion-Find with rank", 895, 380, 240, 60, "violet", size=13),
    ],
    edges=[
        E("root", "c_rep"), E("root", "c_trav"), E("root", "c_short"), E("root", "c_mst"),
        E("c_rep", "rep_mat"), E("rep_mat", "rep_list"),
        E("c_trav", "trav_bfs"), E("trav_bfs", "trav_dfs"), E("trav_dfs", "trav_topo"), E("trav_topo", "trav_scc"),
        E("c_short", "sp_dijk"), E("sp_dijk", "sp_bf"), E("sp_bf", "sp_fw"),
        E("c_mst", "mst_prim"), E("mst_prim", "mst_krusk"), E("mst_krusk", "mst_dsu"),
    ],
    caption="Taxonomy of foundational graph representations, search patterns, and optimization algorithms",
)

# 2 ---------------------------------------------------- tree special graph
tree_vs_graph = D(
    key="ch11-02-tree-special-graph",
    title="Tree vs General Graph Comparison",
    size=(1160, 440),
    flow="H",
    containers=[
        N("box_t", "Tree (Special Constrained Graph)", 40, 70, 500, 310, "container"),
        N("box_g", "General Graph (Unconstrained)", 570, 70, 540, 310, "container"),
    ],
    nodes=[
        # Tree
        N("t_a", "A", 140, 120, 50, 50, "green", "circle", bold=True),
        N("t_b", "B", 80, 200, 50, 50, "green", "circle"),
        N("t_c", "C", 200, 200, 50, 50, "green", "circle"),
        N("t_d", "D", 200, 280, 50, 50, "green", "circle"),
        N("t_prop", "Properties:\nConnected & acyclic\n|E| = |V| - 1\nUnique simple path\nbetween any pair", 280, 125, 230, 115, "green", size=13),
        # General Graph
        N("g_p", "P", 620, 130, 50, 50, "blue", "circle"),
        N("g_q", "Q", 740, 130, 50, 50, "blue", "circle"),
        N("g_r", "R", 680, 240, 50, 50, "blue", "circle"),
        N("g_s", "S", 800, 240, 50, 50, "blue", "circle"),
        N("g_prop", "Properties:\nMay contain cycles\nMay be disconnected\n|E| up to V(V-1)/2\nMultiple or zero paths", 860, 125, 230, 120, "blue", size=13),
    ],
    edges=[
        E("t_a", "t_b", directed=False, route="straight"),
        E("t_a", "t_c", directed=False, route="straight"),
        E("t_c", "t_d", directed=False, route="straight"),
        E("g_p", "g_q", directed=False, route="straight"),
        E("g_q", "g_r", directed=False, route="straight"),
        E("g_r", "g_p", directed=False, route="straight"),
        E("g_r", "g_s", directed=False, route="straight"),
    ],
    caption="Every tree is a graph, but only minimally connected acyclic graphs are trees",
)

# 3 ---------------------------------------------------- graph categories
graph_categories = D(
    key="ch11-03-main-graph-categories",
    title="Main Graph Classifications and Properties",
    size=(1140, 500),
    flow="H",
    nodes=[
        N("g", "Graph Categories", 40, 200, 180, 60, "blue", bold=True),
        N("by_weight", "By Edge Weight", 270, 75, 190, 52, "yellow"),
        N("by_dir", "By Directionality", 270, 205, 190, 52, "yellow"),
        N("by_cycle", "By Cyclic Structure", 270, 335, 190, 52, "yellow"),
        # Sub-types
        N("unweighted", "Unweighted: Unit edge cost\n(BFS yields shortest paths)", 530, 45, 350, 54, "teal", size=13),
        N("weighted", "Weighted: Arbitrary edge costs\n(Dijkstra / Bellman-Ford)", 530, 110, 350, 54, "teal", size=13),
        N("undir", "Undirected: Symmetric (u, v) == (v, u)", 530, 175, 350, 54, "green", size=13),
        N("dir", "Directed (Digraph): One-way arcs (u -> v)", 530, 240, 350, 54, "green", size=13),
        N("cyclic", "Cyclic: Contains at least 1 cycle", 530, 305, 350, 54, "orange", size=13),
        N("dag", "DAG (Directed Acyclic Graph):\nPermits topological sorting!", 530, 370, 350, 54, "green", size=13, bold=True),
    ],
    edges=[
        E("g", "by_weight"), E("g", "by_dir"), E("g", "by_cycle"),
        E("by_weight", "unweighted"), E("by_weight", "weighted"),
        E("by_dir", "undir"), E("by_dir", "dir"),
        E("by_cycle", "cyclic"), E("by_cycle", "dag"),
    ],
    caption="Identifying graph properties is the critical first step to selecting the correct algorithmic strategy",
)

# 4 ---------------------------------------------------- graph representation (4-vertex)
graph_rep_sample = D(
    key="ch11-04-graph-representation",
    title="Sample 4-Vertex Graph for Representation Comparison",
    size=(760, 360),
    flow="H",
    nodes=[
        N("a", "A", 100, 90, 56, 56, "blue", "circle", bold=True),
        N("b", "B", 310, 90, 56, 56, "blue", "circle", bold=True),
        N("c", "C", 100, 220, 56, 56, "blue", "circle", bold=True),
        N("d", "D", 310, 220, 56, 56, "blue", "circle", bold=True),
        N("note", "V = {A, B, C, D}\nE = {(A,B), (A,C),\n     (B,D), (C,D)}", 450, 130, 240, 86, "yellow", size=13),
    ],
    edges=[
        E("a", "b", directed=False, route="straight"),
        E("a", "c", directed=False, route="straight"),
        E("b", "d", directed=False, route="straight"),
        E("c", "d", directed=False, route="straight"),
    ],
    caption="Standard 4-cycle graph used to contrast adjacency matrix and list data structures",
)

# 5 ---------------------------------------------------- matrix vs list
matrix_vs_list = D(
    key="ch11-05-matrix-vs-list",
    title="Adjacency Matrix vs Adjacency List Trade-Offs",
    size=(1140, 480),
    flow="H",
    nodes=[
        N("input", "Graph G = (V, E)", 40, 200, 180, 60, "yellow", bold=True),
        # Matrix
        N("mat", "Adjacency Matrix\n2D Array: matrix[u][v]", 270, 100, 280, 64, "blue", size=14),
        N("mat_pro", "Fast Edge Lookup: O(1) query\nSimple 2D array representation", 580, 65, 270, 58, "green", size=13),
        N("mat_con", "High Space: O(V^2) memory\nNeighbor scan: O(V) time", 580, 135, 270, 58, "red", size=13),
        # List
        N("adj", "Adjacency List\nArray of linked lists / vectors", 270, 300, 280, 64, "teal", size=14),
        N("adj_pro", "Space Efficient: O(V + E)\nNeighbor iteration: O(deg(u))", 580, 265, 270, 58, "green", size=13),
        N("adj_con", "Edge Query: O(deg(u))\nCache locality overhead", 580, 335, 270, 58, "yellow", size=13),
    ],
    edges=[
        E("input", "mat"), E("mat", "mat_pro"), E("mat", "mat_con"),
        E("input", "adj"), E("adj", "adj_pro"), E("adj", "adj_con"),
    ],
    caption="Adjacency lists are preferred for sparse graphs (|E| << |V|^2); matrices suit dense graphs (|E| ~ |V|^2)",
)

# 6 ---------------------------------------------------- shortest path choice
shortest_path_choice = D(
    key="ch11-06-shortest-path-choice",
    title="Shortest Path Algorithm Decision Flowchart",
    size=(1180, 600),
    flow="V",
    nodes=[
        N("start", "Shortest Path Problem", 470, 60, 240, 50, "yellow", bold=True),
        N("unweighted", "Are all edges\nequal weight?", 490, 140, 200, 72, "yellow", "diamond", 14),
        N("use_bfs", "Use Breadth-First Search (BFS)\nTime: O(V + E)\nDistance = edge hop count", 70, 138, 340, 76, "green", size=13, bold=True),
        N("negative", "Any negative\nedge weights?", 490, 255, 200, 72, "yellow", "diamond", 14),
        N("use_dijk", "Use Dijkstra's Algorithm\nTime: O((V + E) log V)\nGreedy relaxation via min-heap", 780, 253, 330, 76, "green", size=13, bold=True),
        N("all_pairs", "Need all-pairs\ndistances?", 490, 370, 200, 72, "yellow", "diamond", 14),
        N("use_bf", "Use Bellman-Ford\nTime: O(V * E)\nHandles negative edges & flags cycles", 90, 470, 340, 76, "teal", size=13, bold=True),
        N("use_fw", "Use Floyd-Warshall\nTime: O(V^3)\nMatrix DP relaxing through vertex k", 690, 470, 340, 76, "violet", size=13, bold=True),
    ],
    edges=[
        E("start", "unweighted"),
        E("unweighted", "use_bfs", "Yes"),
        E("unweighted", "negative", "No"),
        E("negative", "use_dijk", "No"),
        E("negative", "all_pairs", "Yes"),
        E("all_pairs", "use_bf", "Single source"),
        E("all_pairs", "use_fw", "All pairs"),
    ],
    caption="Dijkstra assumes optimal substructure holds greedily; negative edges require Bellman-Ford or Floyd-Warshall",
)

# 7 ---------------------------------------------------- bfs unweighted graph
bfs_unweighted = D(
    key="ch11-07-bfs-unweighted-graph",
    title="Unweighted Shortest Path Graph (Source S to Target T)",
    size=(820, 400),
    flow="H",
    nodes=[
        N("s", "S", 60, 160, 56, 56, "yellow", "circle", bold=True),
        N("a", "A", 220, 70, 56, 56, "blue", "circle"),
        N("b", "B", 220, 250, 56, 56, "blue", "circle"),
        N("c", "C", 420, 110, 56, 56, "blue", "circle"),
        N("d", "D", 420, 250, 56, 56, "blue", "circle"),
        N("t", "T", 640, 160, 56, 56, "green", "circle", bold=True),
    ],
    edges=[
        E("s", "a", directed=False, route="straight"),
        E("s", "b", directed=False, route="straight"),
        E("a", "c", directed=False, route="straight"),
        E("b", "c", directed=False, route="straight"),
        E("b", "d", directed=False, route="straight"),
        E("c", "t", directed=False, route="straight"),
        E("d", "t", directed=False, route="straight"),
    ],
    caption="BFS finds shortest path distance: dist(S, T) = 3 (Path: S-A-C-T or S-B-C-T or S-B-D-T)",
)

# 8 ---------------------------------------------------- bfs layer expansion
bfs_layers_graph = D(
    key="ch11-08-bfs-layer-expansion",
    title="BFS Layer Expansion and Distance Frontiers",
    size=(1140, 440),
    flow="H",
    containers=[
        N("box_l0", "Layer 0 (dist = 0)", 40, 70, 200, 310, "container"),
        N("box_l1", "Layer 1 (dist = 1)", 280, 70, 220, 310, "container"),
        N("box_l2", "Layer 2 (dist = 2)", 540, 70, 220, 310, "container"),
        N("box_l3", "Layer 3 (dist = 3)", 800, 70, 220, 310, "container"),
    ],
    nodes=[
        N("s", "S\n(dist = 0)", 70, 180, 140, 56, "yellow", bold=True),
        N("a", "A\n(dist = 1)", 310, 110, 160, 56, "blue"),
        N("b", "B\n(dist = 1)", 310, 250, 160, 56, "blue"),
        N("c", "C\n(dist = 2)", 570, 110, 160, 56, "green"),
        N("d", "D\n(dist = 2)", 570, 250, 160, 56, "green"),
        N("t", "T\n(dist = 3)", 830, 180, 160, 56, "teal", bold=True),
    ],
    edges=[
        E("s", "a", route="straight"), E("s", "b", route="straight"),
        E("a", "c", route="straight"), E("b", "c", route="straight"),
        E("b", "d", route="straight"),
        E("c", "t", route="straight"), E("d", "t", route="straight"),
    ],
    caption="Every edge in the BFS tree connects Layer i to Layer i+1, proving hop-count optimality",
)

# 9 ---------------------------------------------------- dijkstra undirected graph
dijkstra_undir = D(
    key="ch11-09-dijkstra-undirected-graph",
    title="Dijkstra Worked Example 1 - Undirected Weighted Graph",
    size=(720, 400),
    flow="H",
    nodes=[
        N("a", "A", 60, 180, 56, 56, "yellow", "circle", bold=True),
        N("b", "B", 280, 60, 56, 56, "blue", "circle"),
        N("c", "C", 280, 180, 56, 56, "blue", "circle"),
        N("f", "F", 280, 300, 56, 56, "blue", "circle"),
        N("d", "D", 560, 60, 56, 56, "blue", "circle"),
        N("e", "E", 560, 240, 56, 56, "green", "circle", bold=True),
    ],
    edges=[
        E("a", "b", "14", directed=False, route="straight"),
        E("a", "c", "9", directed=False, route="straight"),
        E("a", "f", "7", directed=False, route="straight"),
        E("b", "c", "2", directed=False, route="straight"),
        E("b", "d", "8", directed=False, route="straight"),
        E("c", "e", "11", directed=False, route="straight"),
        E("c", "f", "10", directed=False, route="straight"),
        E("d", "e", "6", directed=False, route="straight"),
        E("f", "e", "15", directed=False, route="straight"),
    ],
    caption="Source A: nearest unvisited neighbors relaxed iteratively with min-priority queue",
)

# 10 ---------------------------------------------------- dijkstra directed graph
dijkstra_dir = D(
    key="ch11-10-dijkstra-directed-graph",
    title="Dijkstra Worked Example 2 - Directed Weighted Graph",
    size=(740, 420),
    flow="H",
    nodes=[
        N("a", "A", 60, 180, 56, 56, "yellow", "circle", bold=True),
        N("f", "F", 300, 60, 56, 56, "blue", "circle"),
        N("b", "B", 300, 180, 56, 56, "blue", "circle"),
        N("c", "C", 300, 300, 56, 56, "blue", "circle"),
        N("d", "D", 580, 120, 56, 56, "green", "circle", bold=True),
        N("e", "E", 580, 260, 56, 56, "blue", "circle"),
    ],
    edges=[
        E("a", "f", "11", route="straight"),
        E("a", "b", "2", route="straight"),
        E("a", "c", "5", route="straight"),
        E("c", "b", "8", route="straight"),
        E("f", "d", "17", route="straight"),
        E("b", "d", "5", route="straight"),
        E("b", "e", "13", route="straight"),
        E("c", "e", "12", route="straight"),
        E("e", "d", "1", route="straight"),
    ],
    caption="Directed edges restrict allowable relaxations; shortest path A to D is A -> B -> D (cost 7)",
)

# 11 ---------------------------------------------------- dijkstra greedy finalization
dijkstra_finalization = D(
    key="ch11-11-dijkstra-greedy-finalization",
    title="Dijkstra Greedy Finalization Sequence (Source A)",
    size=(1180, 380),
    flow="H",
    nodes=[
        N("init", "Initialize:\nd(A)=0, other d=inf", 25, 80, 210, 60, "yellow", size=14),
        N("p_a", "Finalize A\nd(A) = 0", 255, 80, 130, 60, "green", bold=True),
        N("p_f", "Finalize F\nd(F) = 7", 405, 80, 130, 60, "green", bold=True),
        N("p_c", "Finalize C\nd(C) = 9", 555, 80, 130, 60, "green", bold=True),
        N("p_b", "Finalize B\nd(B) = 11", 705, 80, 130, 60, "green", bold=True),
        N("p_d", "Finalize D\nd(D) = 19", 855, 80, 130, 60, "green", bold=True),
        N("p_e", "Finalize E\nd(E) = 20", 1005, 80, 130, 60, "green", bold=True),
        N("relax_note", "Relaxation Step after each pick:\nFor each neighbor v of u: d(v) = min(d(v), d(u) + weight(u, v))\nOnce finalized, a vertex's shortest path distance NEVER changes!",
          200, 220, 780, 80, "teal", size=13, bold=True),
    ],
    edges=[
        E("init", "p_a"), E("p_a", "p_f"), E("p_f", "p_c"),
        E("p_c", "p_b"), E("p_b", "p_d"), E("p_d", "p_e"),
        E("relax_note", "p_a", dashed=True),
    ],
    caption="Greedy choice property: the unvisited vertex with smallest tentative distance can be finalized immediately",
)

# 12 ---------------------------------------------------- bellman-ford six vertex
bf_six_vertex = D(
    key="ch11-12-bellman-ford-six-vertex-graph",
    title="Bellman-Ford Worked Example - Six Vertices with Negative Edges",
    size=(960, 480),
    flow="H",
    nodes=[
        N("a", "A", 60, 180, 56, 56, "yellow", "circle", bold=True),
        N("b", "B", 260, 60, 56, 56, "blue", "circle"),
        N("c", "C", 260, 200, 56, 56, "blue", "circle"),
        N("d", "D", 260, 340, 56, 56, "blue", "circle"),
        N("e", "E", 560, 100, 56, 56, "blue", "circle"),
        N("f", "F", 780, 220, 56, 56, "green", "circle", bold=True),
    ],
    edges=[
        E("a", "b", "6", route="straight"),
        E("a", "c", "4", route="straight"),
        E("a", "d", "5", route="straight"),
        E("c", "b", "-2", route="straight"),
        E("d", "c", "-2", route="straight"),
        E("b", "e", "-1", route="straight"),
        E("d", "f", "-1", route="straight"),
        E("e", "f", "3", route="straight"),
    ],
    caption="Negative edges allow paths through D and C to beat direct edges: A -> D -> C -> B -> E (cost 0!)",
)

# 13 ---------------------------------------------------- bellman-ford negative cycle
bf_negative_cycle = D(
    key="ch11-13-bellman-ford-negative-cycle",
    title="Pathological Negative Cycle Preventing Shortest Path Convergence",
    size=(980, 360),
    flow="H",
    nodes=[
        N("a", "A", 60, 150, 56, 56, "yellow", "circle", bold=True),
        N("b", "B", 260, 70, 56, 56, "red", "circle", bold=True),
        N("c", "C", 260, 230, 56, 56, "red", "circle", bold=True),
        N("d", "D", 440, 150, 56, 56, "red", "circle", bold=True),
        N("warn", "Negative Cycle Detected!\nCycle B -> C -> D -> B:\nWeight = 2 + 2 + (-5) = -1 < 0\nDistances decrease to -inf every cycle!",
          560, 95, 380, 125, "red", size=13, bold=True),
    ],
    edges=[
        E("a", "b", "1", route="straight"),
        E("a", "c", "2", route="straight"),
        E("b", "c", "+2", route="straight", color="#e03131"),
        E("c", "d", "+2", route="straight", color="#e03131"),
        E("d", "b", "-5", route="straight", color="#e03131"),
    ],
    caption="Bellman-Ford detects negative weight cycles during an additional V-th relaxation pass",
)

# 14 ---------------------------------------------------- bellman-ford relaxation flow
bf_relaxation_flow = D(
    key="ch11-14-bellman-ford-relaxation-flow",
    title="Bellman-Ford Algorithm Execution & Cycle Detection Flow",
    size=(1140, 620),
    flow="V",
    nodes=[
        N("init", "Initialize:\ndist[src] = 0, others = inf", 430, 60, 280, 52, "yellow"),
        N("round", "Repeat V - 1 Rounds\n(Longest simple path has <= V-1 edges)", 400, 140, 340, 58, "blue", size=13),
        N("edge", "For each directed edge (u, v) with weight w:\nCheck if dist[u] + w < dist[v]", 360, 225, 420, 60, "blue", size=13),
        N("relax", "Update: dist[v] = dist[u] + w\nparent[v] = u", 410, 315, 320, 54, "green", size=13),
        N("v_pass", "Run V-th Pass to Detect Negative Cycles", 390, 395, 360, 52, "teal", size=13),
        N("check_cyc", "Does any edge still\nimprove distance?", 460, 475, 220, 74, "yellow", "diamond", 14),
        N("cyc_yes", "Negative Cycle Reachable!\nReport error / infinite loop", 110, 485, 290, 60, "red", size=13, bold=True),
        N("cyc_no", "Shortest Distances Confirmed!\nNo negative cycles on paths", 740, 485, 290, 60, "green", size=13, bold=True),
    ],
    edges=[
        E("init", "round"), E("round", "edge"), E("edge", "relax"),
        E("relax", "v_pass"), E("v_pass", "check_cyc"),
        E("check_cyc", "cyc_yes", "Yes"), E("check_cyc", "cyc_no", "No"),
    ],
    caption="Running V-1 rounds guarantees shortest paths; an update on the V-th round proves a negative cycle exists",
)

# 15 ---------------------------------------------------- floyd-warshall detour
fw_detour = D(
    key="ch11-15-floyd-warshall-detour",
    title="Floyd-Warshall Detour Relaxation Principle",
    size=(1040, 440),
    flow="H",
    containers=[
        N("box_dir", "Current Known Direct Path", 50, 110, 420, 270, "container"),
        N("box_det", "Candidate Detour through Vertex k", 520, 110, 470, 270, "container"),
    ],
    nodes=[
        # Direct
        N("i1", "i", 100, 210, 56, 56, "blue", "circle", bold=True),
        N("j1", "j", 360, 210, 56, 56, "blue", "circle", bold=True),
        N("dir_lbl", "Direct distance:\nD[i, j]^(k-1)", 175, 280, 180, 54, "blue", size=13),
        # Detour
        N("i2", "i", 560, 260, 56, 56, "green", "circle", bold=True),
        N("k", "k (Pivot)", 710, 140, 100, 60, "yellow", size=13, bold=True),
        N("j2", "j", 880, 260, 56, 56, "green", "circle", bold=True),
        N("rule", "Recurrence: D[i, j]^(k) = min( D[i, j]^(k-1),  D[i, k]^(k-1) + D[k, j]^(k-1) )",
          140, 60, 760, 40, "teal", size=13, bold=True),
    ],
    edges=[
        E("i1", "j1", "cost D[i,j]", route="straight"),
        E("i2", "k", "D[i,k]", route="straight"),
        E("k", "j2", "D[k,j]", route="straight"),
    ],
    caption="Dynamic programming over intermediate vertices k from 1 to V computes all-pairs distances in O(V^3)",
)

# 16 ---------------------------------------------------- floyd-warshall 4-vertex
fw_four_vertex = D(
    key="ch11-16-floyd-warshall-four-vertex",
    title="Classroom Problem: 4-Vertex Graph with Negative Weights",
    size=(760, 420),
    flow="H",
    nodes=[
        N("v1", "1", 120, 100, 56, 56, "blue", "circle", bold=True),
        N("v2", "2", 360, 100, 56, 56, "blue", "circle", bold=True),
        N("v3", "3", 120, 260, 56, 56, "blue", "circle", bold=True),
        N("v4", "4", 360, 260, 56, 56, "blue", "circle", bold=True),
        N("summary", "Edge Weights:\n(1->2): 1 | (2->1): 4\n(1->3): -2 | (2->3): 3\n(3->4): 2 | (4->1): 5",
          480, 140, 240, 110, "yellow", size=13),
    ],
    edges=[
        E("v1", "v2", "1", route="straight"),
        E("v2", "v1", "4", route="loopl", bend=30),
        E("v1", "v3", "-2", route="straight"),
        E("v2", "v3", "3", route="straight"),
        E("v3", "v4", "2", route="straight"),
        E("v4", "v1", "5", route="straight"),
    ],
    caption="Shortest path 2 to 4 routes through negative edge: 2 -> 1 -> 3 -> 4 with cost 1 - 2 + 2 = 1",
)

# 17 ---------------------------------------------------- topological dag example
topo_dag = D(
    key="ch11-17-topological-dag-example",
    title="Topological Sorting Worked Example on Directed Acyclic Graph",
    size=(880, 380),
    flow="H",
    nodes=[
        N("a", "A", 80, 80, 56, 56, "yellow", "circle", bold=True),
        N("b", "B", 80, 220, 56, 56, "yellow", "circle", bold=True),
        N("c", "C", 300, 150, 56, 56, "blue", "circle", bold=True),
        N("d", "D", 520, 80, 56, 56, "blue", "circle", bold=True),
        N("e", "E", 520, 220, 56, 56, "blue", "circle", bold=True),
        N("f", "F", 740, 150, 56, 56, "green", "circle", bold=True),
    ],
    edges=[
        E("a", "c", route="straight"),
        E("b", "c", route="straight"),
        E("c", "d", route="straight"),
        E("c", "e", route="straight"),
        E("d", "f", route="straight"),
        E("e", "f", route="straight"),
    ],
    caption="Valid topological orders include: [A, B, C, D, E, F] and [B, A, C, E, D, F]",
)

# 18 ---------------------------------------------------- dfs finish-time flow
dfs_finish_flow = D(
    key="ch11-18-dfs-finish-time-flow",
    title="DFS Finishing Time Algorithm for Topological Sort & SCC",
    size=(1080, 600),
    flow="V",
    nodes=[
        N("start", "Scan Every Vertex in Graph G", 400, 60, 280, 52, "yellow"),
        N("unvis", "Unvisited Vertex?", 440, 140, 200, 70, "yellow", "diamond", 15),
        N("visit", "Call DFS(u):\nMark vertex u as VISITED", 400, 240, 280, 52, "blue"),
        N("neigh", "Unvisited outgoing\nneighbor v exists?", 430, 320, 220, 74, "yellow", "diamond", 15),
        N("rec", "Recursively call DFS(v)", 740, 330, 240, 52, "blue"),
        N("push", "All neighbors explored!\nPush u onto Finish Stack", 400, 430, 280, 54, "green", bold=True),
        N("pop", "Reverse Finish Stack -> Yields Valid Topological Ordering!", 240, 510, 600, 50, "teal", bold=True),
    ],
    edges=[
        E("start", "unvis"),
        E("unvis", "visit", "Yes"),
        E("visit", "neigh"),
        E("neigh", "rec", "Yes"),
        E("rec", "neigh"),
        E("neigh", "push", "No"),
        E("push", "unvis", route="loopl", bend=70),
        E("unvis", "pop", "All visited", route="loopr", bend=190),
    ],
    caption="A vertex finishes only after all its descendants have finished, ensuring proper precedence",
)

# 19 ---------------------------------------------------- connected components
connected_components = D(
    key="ch11-19-connected-components-example",
    title="Undirected Graph with 3 Disconnected Components",
    size=(960, 380),
    flow="H",
    containers=[
        N("box_c1", "Component 1 (3 Vertices)", 40, 70, 320, 260, "container"),
        N("box_c2", "Component 2 (2 Vertices)", 400, 70, 260, 260, "container"),
        N("box_c3", "Component 3 (Isolated)", 700, 70, 220, 260, "container"),
    ],
    nodes=[
        N("a", "A", 80, 160, 56, 56, "blue", "circle", bold=True),
        N("b", "B", 180, 110, 56, 56, "blue", "circle", bold=True),
        N("c", "C", 270, 200, 56, 56, "blue", "circle", bold=True),
        N("d", "D", 440, 160, 56, 56, "green", "circle", bold=True),
        N("e", "E", 560, 160, 56, 56, "green", "circle", bold=True),
        N("f", "F", 780, 160, 56, 56, "yellow", "circle", bold=True),
    ],
    edges=[
        E("a", "b", directed=False, route="straight"),
        E("b", "c", directed=False, route="straight"),
        E("d", "e", directed=False, route="straight"),
    ],
    caption="Each full BFS/DFS call from an unvisited vertex discovers one maximal connected component",
)

# 20 ---------------------------------------------------- component discovery flow
component_discovery = D(
    key="ch11-20-component-discovery-flow",
    title="Connected Components Discovery Procedure",
    size=(1060, 520),
    flow="V",
    nodes=[
        N("init", "Mark All Vertices as Unvisited", 380, 60, 300, 52, "yellow"),
        N("check", "Unvisited Vertices\nRemain?", 430, 140, 200, 74, "yellow", "diamond", 14),
        N("pick", "Pick Unvisited Vertex u as Root\nStart new component label", 370, 245, 320, 56, "blue", size=13),
        N("traverse", "Run BFS or DFS from Root u\nMark reached vertices with component ID", 340, 330, 380, 56, "green", size=13),
        N("done", "All Connected Components Identified!\nPartition: V = C1 U C2 U ... U Ck", 360, 415, 340, 56, "teal", size=13, bold=True),
    ],
    edges=[
        E("init", "check"),
        E("check", "pick", "Yes"),
        E("pick", "traverse"),
        E("traverse", "check", "loop back", route="loopr", bend=60),
        E("check", "done", "No", route="loopl", bend=70),
    ],
    caption="Total time O(V + E) since each vertex and edge is processed once across all component runs",
)

# 21 ---------------------------------------------------- kosaraju original graph
kosaraju_orig = D(
    key="ch11-21-kosaraju-original-graph",
    title="Kosaraju Algorithm - Original Directed Graph G",
    size=(1080, 420),
    flow="H",
    nodes=[
        N("n0", "0", 80, 80, 52, 52, "blue", "circle"),
        N("n1", "1", 220, 80, 52, 52, "blue", "circle"),
        N("n2", "2", 150, 220, 52, 52, "blue", "circle"),
        N("n3", "3", 380, 220, 52, 52, "yellow", "circle"),
        N("n4", "4", 560, 150, 52, 52, "green", "circle"),
        N("n5", "5", 720, 80, 52, 52, "green", "circle"),
        N("n6", "6", 720, 220, 52, 52, "green", "circle"),
        N("n7", "7", 920, 150, 52, 52, "violet", "circle"),
    ],
    edges=[
        E("n0", "n1", route="straight"), E("n1", "n2", route="straight"), E("n2", "n0", route="straight"),
        E("n2", "n3", route="straight"), E("n3", "n4", route="straight"),
        E("n4", "n5", route="straight"), E("n5", "n6", route="straight"), E("n6", "n4", route="straight"),
        E("n4", "n7", route="straight"),
    ],
    caption="Three SCCs: {0, 1, 2}, {4, 5, 6}, and singletons {3} and {7}",
)

# 22 ---------------------------------------------------- kosaraju reversed graph
kosaraju_rev = D(
    key="ch11-22-kosaraju-reversed-graph",
    title="Kosaraju Algorithm - Transposed Graph G^T (Reversed Edges)",
    size=(1080, 420),
    flow="H",
    nodes=[
        N("n0", "0", 80, 80, 52, 52, "blue", "circle"),
        N("n1", "1", 220, 80, 52, 52, "blue", "circle"),
        N("n2", "2", 150, 220, 52, 52, "blue", "circle"),
        N("n3", "3", 380, 220, 52, 52, "yellow", "circle"),
        N("n4", "4", 560, 150, 52, 52, "green", "circle"),
        N("n5", "5", 720, 80, 52, 52, "green", "circle"),
        N("n6", "6", 720, 220, 52, 52, "green", "circle"),
        N("n7", "7", 920, 150, 52, 52, "violet", "circle"),
    ],
    edges=[
        E("n1", "n0", route="straight"), E("n2", "n1", route="straight"), E("n0", "n2", route="straight"),
        E("n3", "n2", route="straight"), E("n4", "n3", route="straight"),
        E("n5", "n4", route="straight"), E("n6", "n5", route="straight"), E("n4", "n6", route="straight"),
        E("n7", "n4", route="straight"),
    ],
    caption="Transposing the graph reverses component dependencies while preserving internal cycle reachability",
)

# 23 ---------------------------------------------------- kosaraju 3-step flow
kosaraju_flow = D(
    key="ch11-23-kosaraju-three-step-flow",
    title="Kosaraju's Two-Pass Algorithm Flowchart",
    size=(1180, 440),
    flow="H",
    nodes=[
        N("g", "Original Graph G", 40, 160, 180, 60, "blue", bold=True),
        N("pass1", "Pass 1: Run DFS on G\nPush vertices to Stack\nin order of finishing time", 280, 70, 270, 74, "yellow"),
        N("trans", "Transpose: Build G^T\nReverse every directed edge", 280, 230, 270, 74, "teal"),
        N("pass2", "Pass 2: Pop Stack\nRun DFS on G^T for each\nunvisited popped vertex", 620, 150, 260, 74, "green"),
        N("scc", "Each DFS Tree in G^T\nforms exactly one SCC!", 920, 150, 230, 74, "green", size=13, bold=True),
    ],
    edges=[
        E("g", "pass1"), E("g", "trans"),
        E("pass1", "pass2"), E("trans", "pass2"),
        E("pass2", "scc"),
    ],
    caption="Two DFS sweeps discover all strongly connected components in linear O(V + E) time",
)

# 24 ---------------------------------------------------- mst properties
mst_properties = D(
    key="ch11-24-mst-properties",
    title="Spanning Tree Definition - Connected Subgraph Covering All Vertices",
    size=(1080, 420),
    flow="H",
    containers=[
        N("box_orig", "Original Graph G = (V, E)", 40, 70, 460, 310, "container"),
        N("box_mst", "One Spanning Tree T = (V, E_T)", 560, 70, 480, 310, "container"),
    ],
    nodes=[
        # Original
        N("oa", "A", 90, 130, 52, 52, "blue", "circle"),
        N("ob", "B", 240, 130, 52, 52, "blue", "circle"),
        N("oc", "C", 90, 250, 52, 52, "blue", "circle"),
        N("od", "D", 240, 250, 52, 52, "blue", "circle"),
        N("op", "Edges = 5\nContains Cycles:\nA-B-C, B-C-D", 340, 170, 140, 80, "yellow", size=13),
        # MST
        N("ma", "A", 610, 130, 52, 52, "green", "circle", bold=True),
        N("mb", "B", 760, 130, 52, 52, "green", "circle", bold=True),
        N("mc", "C", 610, 250, 52, 52, "green", "circle", bold=True),
        N("md", "D", 760, 250, 52, 52, "green", "circle", bold=True),
        N("mp", "Edges = |V| - 1 = 3\nNo Cycles (Acyclic)\nFully Connected!", 860, 170, 160, 80, "green", size=13),
    ],
    edges=[
        E("oa", "ob", directed=False, route="straight"),
        E("oa", "oc", directed=False, route="straight"),
        E("ob", "oc", directed=False, route="straight"),
        E("ob", "od", directed=False, route="straight"),
        E("oc", "od", directed=False, route="straight"),
        E("ma", "mb", directed=False, route="straight", color="#2f9e44"),
        E("mb", "mc", directed=False, route="straight", color="#2f9e44"),
        E("mc", "md", directed=False, route="straight", color="#2f9e44"),
    ],
    caption="A spanning tree retains all vertices while removing |E| - |V| + 1 cycle-forming edges",
)

# 25 ---------------------------------------------------- shared worked graph (8-vertex)
shared_worked_graph = D(
    key="ch11-25-shared-worked-graph",
    title="Shared 8-Vertex Benchmark Graph for MST Algorithms",
    size=(1080, 520),
    flow="H",
    nodes=[
        N("v1", "V1", 80, 150, 56, 56, "yellow", "circle", bold=True),
        N("v2", "V2", 280, 70, 56, 56, "blue", "circle"),
        N("v3", "V3", 560, 70, 56, 56, "blue", "circle"),
        N("v4", "V4", 280, 370, 56, 56, "blue", "circle"),
        N("v5", "V5", 380, 210, 56, 56, "blue", "circle"),
        N("v6", "V6", 760, 150, 56, 56, "blue", "circle"),
        N("v7", "V7", 560, 370, 56, 56, "blue", "circle"),
        N("v8", "V8", 760, 330, 56, 56, "blue", "circle"),
    ],
    edges=[
        E("v1", "v5", "2", directed=False, route="straight"),
        E("v1", "v2", "3", directed=False, route="straight"),
        E("v1", "v4", "5", directed=False, route="straight"),
        E("v2", "v3", "7", directed=False, route="straight"),
        E("v2", "v5", "6", directed=False, route="straight"),
        E("v3", "v6", "2", directed=False, route="straight"),
        E("v3", "v5", "10", directed=False, route="straight"),
        E("v4", "v5", "3", directed=False, route="straight"),
        E("v4", "v7", "2", directed=False, route="straight"),
        E("v5", "v7", "5", directed=False, route="straight"),
        E("v5", "v6", "7", directed=False, route="straight"),
        E("v5", "v8", "5", directed=False, route="straight"),
        E("v7", "v8", "4", directed=False, route="straight"),
        E("v8", "v6", "6", directed=False, route="straight"),
    ],
    caption="Standard weighted graph used to illustrate both Prim and Kruskal MST algorithms",
)

# 26 ---------------------------------------------------- prim algorithm graph
prim_graph = D(
    key="ch11-26-prim-algorithm-graph",
    title="Prim's Algorithm - Resulting MST (Total Weight = 22)",
    size=(1080, 480),
    flow="H",
    nodes=[
        N("v1", "V1", 80, 150, 56, 56, "green", "circle", bold=True),
        N("v2", "V2", 280, 70, 56, 56, "green", "circle", bold=True),
        N("v3", "V3", 560, 70, 56, 56, "green", "circle", bold=True),
        N("v4", "V4", 280, 350, 56, 56, "green", "circle", bold=True),
        N("v5", "V5", 380, 200, 56, 56, "green", "circle", bold=True),
        N("v6", "V6", 760, 150, 56, 56, "green", "circle", bold=True),
        N("v7", "V7", 560, 350, 56, 56, "green", "circle", bold=True),
        N("v8", "V8", 760, 330, 56, 56, "green", "circle", bold=True),
    ],
    edges=[
        E("v1", "v5", "1: w=2", directed=False, route="straight", color="#2f9e44"),
        E("v5", "v4", "2: w=3", directed=False, route="straight", color="#2f9e44"),
        E("v4", "v7", "3: w=2", directed=False, route="straight", color="#2f9e44"),
        E("v1", "v2", "4: w=3", directed=False, route="straight", color="#2f9e44"),
        E("v7", "v8", "5: w=4", directed=False, route="straight", color="#2f9e44"),
        E("v8", "v6", "6: w=6", directed=False, route="straight", color="#2f9e44"),
        E("v6", "v3", "7: w=2", directed=False, route="straight", color="#2f9e44"),
    ],
    caption="Edges labeled in the exact order selected by Prim's algorithm starting from V1",
)

# 27 ---------------------------------------------------- prim algorithm flow
prim_flow = D(
    key="ch11-27-prim-algorithm-flow",
    title="Prim's Step-by-Step Edge Selection Trace",
    size=(1220, 360),
    flow="H",
    nodes=[
        N("p_start", "Start:\n{V1}", 25, 100, 105, 54, "yellow", size=13),
        N("p1", "1. Add V1-V5\n(weight 2)", 150, 100, 135, 54, "green", size=13),
        N("p2", "2. Add V5-V4\n(weight 3)", 300, 100, 135, 54, "green", size=13),
        N("p3", "3. Add V4-V7\n(weight 2)", 450, 100, 135, 54, "green", size=13),
        N("p4", "4. Add V1-V2\n(weight 3)", 600, 100, 135, 54, "green", size=13),
        N("p5", "5. Add V7-V8\n(weight 4)", 750, 100, 135, 54, "green", size=13),
        N("p6", "6. Add V8-V6\n(weight 6)", 900, 100, 135, 54, "green", size=13),
        N("p7", "7. Add V6-V3\n(weight 2)", 1050, 100, 135, 54, "green", size=13),
        N("p_done", "MST Complete: 7 Edges, Total Weight = 2 + 3 + 2 + 3 + 4 + 6 + 2 = 22",
          250, 220, 720, 54, "teal", size=13, bold=True),
    ],
    edges=[
        E("p_start", "p1"), E("p1", "p2"), E("p2", "p3"), E("p3", "p4"),
        E("p4", "p5"), E("p5", "p6"), E("p6", "p7"), E("p7", "p_done", route="v"),
    ],
    caption="Prim grows a single connected tree by selecting the cheapest crossing edge at every step",
)

# 28 ---------------------------------------------------- kruskal algorithm graph
kruskal_graph = D(
    key="ch11-28-kruskal-algorithm-graph",
    title="Kruskal's Algorithm - Resulting MST (Total Weight = 22)",
    size=(1080, 480),
    flow="H",
    nodes=[
        N("v1", "V1", 80, 150, 56, 56, "teal", "circle", bold=True),
        N("v2", "V2", 280, 70, 56, 56, "teal", "circle", bold=True),
        N("v3", "V3", 560, 70, 56, 56, "teal", "circle", bold=True),
        N("v4", "V4", 280, 350, 56, 56, "teal", "circle", bold=True),
        N("v5", "V5", 380, 200, 56, 56, "teal", "circle", bold=True),
        N("v6", "V6", 760, 150, 56, 56, "teal", "circle", bold=True),
        N("v7", "V7", 560, 350, 56, 56, "teal", "circle", bold=True),
        N("v8", "V8", 760, 330, 56, 56, "teal", "circle", bold=True),
    ],
    edges=[
        E("v1", "v5", "acc 1: w=2", directed=False, route="straight", color="#0c8599"),
        E("v4", "v7", "acc 2: w=2", directed=False, route="straight", color="#0c8599"),
        E("v3", "v6", "acc 3: w=2", directed=False, route="straight", color="#0c8599"),
        E("v1", "v2", "acc 4: w=3", directed=False, route="straight", color="#0c8599"),
        E("v4", "v5", "acc 5: w=3", directed=False, route="straight", color="#0c8599"),
        E("v7", "v8", "acc 6: w=4", directed=False, route="straight", color="#0c8599"),
        E("v8", "v6", "acc 7: w=6", directed=False, route="straight", color="#0c8599"),
    ],
    caption="Edges labeled in increasing order of weight as accepted by Kruskal's algorithm",
)

# 29 ---------------------------------------------------- kruskal algorithm flow
kruskal_flow = D(
    key="ch11-29-kruskal-algorithm-flow",
    title="Kruskal's Global Edge Sorting and Cycle Avoidance Flow",
    size=(1160, 460),
    flow="V",
    nodes=[
        N("sort", "Sort All Edges by Nondecreasing Weight\n[(V1-V5: 2), (V4-V7: 2), (V3-V6: 2), (V1-V2: 3), ...]", 260, 60, 640, 56, "yellow", size=13, bold=True),
        N("take1", "Accept 3 edges of weight 2:\nV1-V5, V4-V7, V3-V6", 60, 160, 280, 56, "green", size=13),
        N("take2", "Accept 2 edges of weight 3:\nV1-V2, V4-V5", 380, 160, 260, 56, "green", size=13),
        N("take3", "Accept 1 edge of weight 4:\nV7-V8", 680, 160, 240, 56, "green", size=13),
        N("skip", "Skip edges of weight 5 & 6 forming cycles:\nV1-V4, V5-V7, V5-V8, V2-V5", 160, 260, 480, 56, "red", size=13),
        N("take4", "Accept final edge:\nV8-V6 (weight 6)", 680, 260, 240, 56, "green", size=13),
        N("done", "MST Complete: |V| - 1 = 7 edges, Total Weight = 22", 340, 360, 480, 54, "teal", size=13, bold=True),
    ],
    edges=[
        E("sort", "take1"), E("sort", "take2"), E("sort", "take3"),
        E("take2", "skip"), E("take3", "take4"),
        E("skip", "done"), E("take4", "done"),
    ],
    caption="Kruskal processes edges globally, merging disconnected forest trees into a single MST",
)

# 30 ---------------------------------------------------- dsu cycle check
dsu_cycle = D(
    key="ch11-30-dsu-cycle-check",
    title="Disjoint Set Union (DSU) Cycle Detection in Kruskal's Algorithm",
    size=(1020, 500),
    flow="V",
    nodes=[
        N("edge", "Consider Candidate Edge (u, v)", 360, 60, 300, 52, "yellow", size=14, bold=True),
        N("find_u", "Find Set Representative:\nroot_u = FIND(u)", 170, 150, 250, 56, "blue", size=13),
        N("find_v", "Find Set Representative:\nroot_v = FIND(v)", 600, 150, 250, 56, "blue", size=13),
        N("check", "Are roots identical?\nroot_u == root_v", 390, 240, 240, 74, "yellow", "diamond", 14),
        N("rej", "REJECT EDGE!\nu and v already connected;\nadding edge creates a cycle", 90, 355, 340, 76, "red", size=13, bold=True),
        N("acc", "ACCEPT EDGE!\nMerge components:\nUNION(root_u, root_v)", 590, 355, 340, 76, "green", size=13, bold=True),
    ],
    edges=[
        E("edge", "find_u"), E("edge", "find_v"),
        E("find_u", "check"), E("find_v", "check"),
        E("check", "rej", "Yes (Cycle!)"),
        E("check", "acc", "No (Safe!)"),
    ],
    caption="Path compression and union by rank reduce FIND and UNION operations to nearly O(1) amortized time (alpha(V))",
)

# 31 ---------------------------------------------------- DSU sets and union

dsu_sets_union = D(
    key="ch11-31-dsu-sets-and-union",
    title="Disjoint Set Parent Trees and Component Merge",
    size=(1120, 460),
    flow="H",
    containers=[
        N("initial_panel", "Initial: five singleton sets", 30, 85, 500, 300, "container"),
        N("merged_panel", "After UNIONs (0,1), (0,2), (2,3)", 590, 85, 500, 300, "container"),
    ],
    nodes=[
        N("i0", "0", 70, 180, 48, 48, "blue", "circle", bold=True),
        N("i1", "1", 155, 180, 48, 48, "blue", "circle"),
        N("i2", "2", 240, 180, 48, 48, "blue", "circle"),
        N("i3", "3", 325, 180, 48, 48, "blue", "circle"),
        N("i4", "4", 410, 180, 48, 48, "blue", "circle"),
        N("i_arr", "Parent array: [-1, -1, -1, -1, -1]", 85, 280, 390, 48, "light", size=13),
        N("m0", "0", 735, 145, 52, 52, "green", "circle", bold=True),
        N("m1", "1", 665, 240, 48, 48, "blue", "circle"),
        N("m2", "2", 735, 240, 48, 48, "blue", "circle"),
        N("m3", "3", 805, 240, 48, 48, "blue", "circle"),
        N("m4", "4", 990, 180, 48, 48, "yellow", "circle"),
        N("m_arr", "Parent array: [-1, 0, 0, 0, -1]", 640, 315, 390, 48, "light", size=13),
    ],
    edges=[E("m0", "m1"), E("m0", "m2"), E("m0", "m3")],
    caption="A DSU parent forest stores component membership, not the original graph's edges",
)

# 32 ---------------------------------------------------- path compression

dsu_path_compression = D(
    key="ch11-32-dsu-path-compression",
    title="Path Compression Flattens a Find Path",
    size=(1120, 470),
    flow="H",
    containers=[
        N("before_panel", "Before FIND(4): a tall parent chain", 25, 85, 500, 320, "container"),
        N("after_panel", "After FIND(4): visited nodes point to root 0", 595, 85, 500, 320, "container"),
    ],
    nodes=[
        N("b0", "0", 260, 125, 48, 48, "green", "circle", bold=True),
        N("b1", "1", 260, 180, 48, 48, "blue", "circle"),
        N("b2", "2", 260, 235, 48, 48, "blue", "circle"),
        N("b3", "3", 260, 290, 48, 48, "blue", "circle"),
        N("b4", "4", 260, 345, 48, 48, "yellow", "circle"),
        N("b_arr", "parent: [0, 0, 1, 2, 3]", 90, 415, 360, 42, "light", size=13),
        N("a0", "0", 820, 130, 48, 48, "green", "circle", bold=True),
        N("a1", "1", 690, 255, 48, 48, "blue", "circle"),
        N("a2", "2", 775, 255, 48, 48, "blue", "circle"),
        N("a3", "3", 860, 255, 48, 48, "blue", "circle"),
        N("a4", "4", 945, 255, 48, 48, "yellow", "circle"),
        N("a_arr", "parent: [0, 0, 0, 0, 0]", 665, 345, 360, 42, "light", size=13),
    ],
    edges=[
        E("b1", "b0"), E("b2", "b1"), E("b3", "b2"), E("b4", "b3"),
        E("a0", "a1", route="straight"), E("a0", "a2", route="straight"), E("a0", "a3", route="straight"), E("a0", "a4", route="straight"),
    ],
    caption="One find may pay for a longer walk, then shorten future finds along the same path",
)

# 33 ---------------------------------------------------- union by size

dsu_union_by_size = D(
    key="ch11-33-dsu-union-by-size",
    title="Union by Size Attaches the Smaller Tree Under the Larger",
    size=(1120, 480),
    flow="H",
    containers=[
        N("small_panel", "Before: compare component sizes", 25, 85, 500, 330, "container"),
        N("large_panel", "After UNION: attach smaller root below larger", 595, 85, 500, 330, "container"),
    ],
    nodes=[
        N("s0", "A\nsize 3", 170, 145, 78, 58, "green", "circle", size=12, bold=True),
        N("s1", "1", 105, 255, 48, 48, "blue", "circle"),
        N("s2", "2", 200, 255, 48, 48, "blue", "circle"),
        N("t0", "B\nsize 2", 350, 145, 78, 58, "yellow", "circle", size=12, bold=True),
        N("t1", "4", 365, 255, 48, 48, "yellow", "circle"),
        N("r0", "A\nsize 5", 835, 145, 82, 62, "green", "circle", size=12, bold=True),
        N("r1", "1", 675, 285, 48, 48, "blue", "circle"),
        N("r2", "2", 765, 285, 48, 48, "blue", "circle"),
        N("r3", "B", 855, 285, 48, 48, "yellow", "circle"),
        N("r4", "4", 945, 285, 48, 48, "yellow", "circle"),
        N("rule", "Attach B under A; combined set size = 5", 660, 355, 390, 44, "light", size=13),
    ],
    edges=[
        E("s0", "s1", route="straight"), E("s0", "s2", route="straight"), E("t0", "t1", route="straight"),
        E("r0", "r1", route="straight"), E("r0", "r2", route="straight"), E("r0", "r3", route="straight"), E("r3", "r4", route="straight"),
    ],
    caption="The larger root remains the representative, limiting tree growth during merges",
)

# 34 ---------------------------------------------------- lecture Kruskal example

kruskal_lecture_example = D(
    key="ch11-34-kruskal-lecture-example",
    title="Kruskal's Lecture Example: Weight Order and Cycle Rejection",
    size=(1320, 560),
    flow="H",
    containers=[
        N("graph_panel", "Five-vertex input graph: green edges are selected", 25, 95, 470, 390, "container"),
        N("trace_panel", "Process edge tuples in nondecreasing weight order", 535, 95, 760, 390, "container"),
    ],
    nodes=[
        N("v0", "0", 75, 155, 48, 48, "blue", "circle", bold=True),
        N("v1", "1", 255, 110, 48, 48, "blue", "circle", bold=True),
        N("v4", "4", 405, 205, 48, 48, "blue", "circle", bold=True),
        N("v3", "3", 280, 345, 48, 48, "blue", "circle", bold=True),
        N("v2", "2", 75, 345, 48, 48, "blue", "circle", bold=True),
        N("row1", "1   (1, 4, 1)    ACCEPT", 570, 125, 690, 42, "green", size=14),
        N("row2", "2   (0, 1, 1)    ACCEPT", 570, 175, 690, 42, "green", size=14),
        N("row3", "3   (3, 4, 2)    ACCEPT", 570, 225, 690, 42, "green", size=14),
        N("row4", "4   (1, 3, 2)    SKIP: cycle", 570, 275, 690, 42, "red", size=14),
        N("row5", "5   (2, 3, 3)    ACCEPT", 570, 325, 690, 42, "green", size=14),
        N("row6", "6   (0, 2, 5)    SKIP: cycle", 570, 375, 690, 42, "red", size=14),
        N("mst_result", "MST: 4 edges; total weight = 7", 650, 435, 530, 40, "teal", size=15, bold=True),
    ],
    edges=[
        E("v1", "v4", "1", route="straight", color="#2f9e44"),
        E("v0", "v1", "1", route="straight", color="#2f9e44"),
        E("v3", "v4", "2", route="straight", color="#2f9e44"),
        E("v1", "v3", "2", route="straight", color="#e03131", dashed=True),
        E("v2", "v3", "3", route="straight", color="#2f9e44"),
        E("v0", "v2", "5", route="straight", color="#e03131", dashed=True),
    ],
    caption="The same-root test rejects edges 4 and 6; accepted edges form a minimum spanning tree",
)

# 35 ---------------------------------------------------- union by rank

union_by_rank = D(
    key="ch11-35-union-by-rank",
    title="Union by Rank: Prefer the Taller Root and Increment Only on a Tie",
    size=(1320, 500),
    flow="H",
    containers=[
        N("unequal_panel", "Unequal ranks: rank 2 remains the root", 25, 95, 620, 330, "container"),
        N("equal_panel", "Equal ranks: choose a root and raise its rank", 675, 95, 620, 330, "container"),
    ],
    nodes=[
        N("hroot", "H\nrank 2", 90, 145, 84, 58, "green", "circle", size=12, bold=True),
        N("hleaf", "h", 108, 245, 48, 48, "blue", "circle"),
        N("lroot", "L\nrank 1", 255, 145, 84, 58, "yellow", "circle", size=12, bold=True),
        N("lleaf", "l", 273, 245, 48, 48, "blue", "circle"),

        N("hroot_after", "H\nrank 2", 445, 145, 84, 58, "green", "circle", size=12, bold=True),
        N("hleaf_after", "h", 385, 245, 48, 48, "blue", "circle"),
        N("lroot_after", "L\nrank 1", 485, 245, 84, 58, "yellow", "circle", size=12, bold=True),
        N("lleaf_after", "l", 503, 330, 48, 48, "blue", "circle"),
        N("aroot", "A\nrank 1", 745, 145, 84, 58, "green", "circle", size=12, bold=True),
        N("aleaf", "a", 763, 235, 48, 48, "blue", "circle"),
        N("broot", "B\nrank 1", 885, 145, 84, 58, "yellow", "circle", size=12, bold=True),
        N("bleaf", "b", 903, 235, 48, 48, "blue", "circle"),
        N("aroot_after", "A\nrank 2", 1110, 145, 84, 58, "green", "circle", size=12, bold=True),
        N("aleaf_after", "a", 1040, 260, 48, 48, "blue", "circle"),
        N("broot_after", "B\nrank 1", 1135, 260, 84, 58, "yellow", "circle", size=12, bold=True),
        N("bleaf_after", "b", 1153, 345, 48, 48, "blue", "circle"),
    ],
    edges=[
        E("hroot", "hleaf", route="straight"), E("lroot", "lleaf", route="straight"),
        E("hroot_after", "hleaf_after", route="straight"),
        E("hroot_after", "lroot_after", route="straight"),
        E("lroot_after", "lleaf_after", route="straight"),
        E("aroot", "aleaf", route="straight"), E("broot", "bleaf", route="straight"),
        E("aroot_after", "aleaf_after", route="straight"),
        E("aroot_after", "broot_after", route="straight"),
        E("broot_after", "bleaf_after", route="straight"),
    ],
    caption="Rank is a height bound, not a node count; a root's rank increases only when equal ranks merge",
)

DIAGRAMS = [
    graph_roadmap,
    tree_vs_graph,
    graph_categories,
    graph_rep_sample,
    matrix_vs_list,
    shortest_path_choice,
    bfs_unweighted,
    bfs_layers_graph,
    dijkstra_undir,
    dijkstra_dir,
    dijkstra_finalization,
    bf_six_vertex,
    bf_negative_cycle,
    bf_relaxation_flow,
    fw_detour,
    fw_four_vertex,
    topo_dag,
    dfs_finish_flow,
    connected_components,
    component_discovery,
    kosaraju_orig,
    kosaraju_rev,
    kosaraju_flow,
    mst_properties,
    shared_worked_graph,
    prim_graph,
    prim_flow,
    kruskal_graph,
    kruskal_flow,
    dsu_cycle,
    dsu_sets_union,
    dsu_path_compression,
    dsu_union_by_size,
    kruskal_lecture_example,
    union_by_rank,
]
