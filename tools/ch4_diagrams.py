"""Chapter 4 (Searching and Basic Traversal) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 4 - Searching and Basic Traversal/diagrams"

# Helper for the common 7-vertex graph in Ch 4
def make_seven_vertex_nodes(x_off=80, y_off=70, sx=120, sy=90):
    return [
        N("a", "A", x_off + 0 * sx, y_off + 1 * sy, 54, 54, "blue", "circle", bold=True),
        N("b", "B", x_off + 1 * sx, y_off + 0 * sy, 54, 54, "blue", "circle", bold=True),
        N("c", "C", x_off + 1 * sx, y_off + 2 * sy, 54, 54, "blue", "circle", bold=True),
        N("d", "D", x_off + 2 * sx, y_off + 0 * sy, 54, 54, "blue", "circle", bold=True),
        N("e", "E", x_off + 2 * sx, y_off + 1 * sy, 54, 54, "blue", "circle", bold=True),
        N("f", "F", x_off + 2 * sx, y_off + 2 * sy, 54, 54, "blue", "circle", bold=True),
        N("g", "G", x_off + 3 * sx, y_off + 1 * sy, 54, 54, "yellow", "circle", bold=True),
    ]

# 1 ---------------------------------------------------- search vs traversal flow
search_traversal_flow = D(
    key="ch4-01-search-traversal-flow",
    title="Searching vs Traversal - Decision and Process Flow",
    size=(1160, 720),
    flow="V",
    nodes=[
        N("start", "Start from Data Structure", 440, 60, 280, 52, "blue", "ellipse", bold=True),
        N("goal", "Goal?", 490, 140, 180, 68, "yellow", "diamond", 15),
        # Search branch (Left)
        N("search", "Searching\nGoal: find specific item", 100, 240, 260, 60, "yellow", bold=True),
        N("check", "Check Current\nElement", 100, 330, 260, 56, "yellow"),
        N("found", "Target Found?", 130, 420, 180, 68, "yellow", "diamond", 15),
        N("stop", "Stop & Return Result", 25, 530, 180, 54, "green", size=14, bold=True),
        N("move", "Move to Next\nCandidate", 215, 526, 190, 58, "yellow", size=14),
        # Traversal branch (Right)
        N("traverse", "Traversal\nVisit reachable elements", 700, 240, 300, 60, "green", bold=True),
        N("visit", "Visit Current Element\nProcess payload / data", 720, 330, 260, 56, "green"),
        N("frontier", "Add Unvisited Neighbors\nto frontier structure", 720, 420, 260, 56, "green"),
        N("done", "No Elements\nLeft?", 760, 510, 180, 68, "yellow", "diamond", 14),
        N("complete", "Traversal Complete\nAll reachable nodes visited", 710, 610, 280, 54, "green", bold=True),
    ],
    edges=[
        E("start", "goal"),
        E("goal", "search", "Find item"),
        E("goal", "traverse", "Visit all"),
        E("search", "check"),
        E("check", "found"),
        E("found", "stop", "Yes"),
        E("found", "move", "No"),
        E("move", "check", route="loopr", bend=40),
        E("traverse", "visit"),
        E("visit", "frontier"),
        E("frontier", "done"),
        E("done", "visit", "No", route="loopr", bend=60),
        E("done", "complete", "Yes"),
    ],
    caption="Searching stops immediately on finding the target; traversal systematically visits the entire connected component",
)

# 2 ---------------------------------------------------- movement purpose
movement_purpose = D(
    key="ch4-02-movement-purpose",
    title="Same Graph Movement, Different Algorithmic Purpose",
    size=(1020, 460),
    flow="H",
    nodes=make_seven_vertex_nodes(80, 90, 140, 100) + [
        N("s_goal", "Searching Goal:\nStop immediately when\ntarget G is found", 650, 80, 280, 74, "yellow", bold=True),
        N("t_goal", "Traversal Goal:\nVisit all reachable\nvertices A through G", 20, 310, 190, 74, "green", size=13, bold=True),
    ],
    edges=[
        E("a", "b", route="straight"), E("a", "c", route="straight"),
        E("b", "d", route="straight"), E("b", "e", route="straight"),
        E("c", "f", route="straight"), E("e", "g", route="straight"),
        E("f", "g", route="straight"),
        E("g", "s_goal", "target", dashed=True, color="#e03131"),
        E("a", "t_goal", "start", dashed=True, color="#2f9e44", route="v"),
    ],
    caption="Traversal explores every reachable path; search prunes or halts upon locating the key",
)

# 3 ---------------------------------------------------- intro graph traversal
intro_graph = D(
    key="ch4-03-intro-graph-traversal",
    title="Introductory Graph for Traversal Demonstrations",
    size=(760, 420),
    flow="H",
    nodes=make_seven_vertex_nodes(100, 80, 150, 100),
    edges=[
        E("a", "b", directed=False, route="straight"),
        E("a", "c", directed=False, route="straight"),
        E("b", "d", directed=False, route="straight"),
        E("b", "e", directed=False, route="straight"),
        E("c", "f", directed=False, route="straight"),
        E("e", "g", directed=False, route="straight"),
        E("f", "g", directed=False, route="straight"),
    ],
    caption="Undirected connected graph with 7 vertices and 7 edges",
)

# 4 ---------------------------------------------------- bfs traversal graph
bfs_graph = D(
    key="ch4-04-bfs-traversal-graph",
    title="BFS Traversal on 7-Vertex Graph (Source A)",
    size=(760, 420),
    flow="H",
    nodes=make_seven_vertex_nodes(100, 80, 150, 100),
    edges=[
        E("a", "b", directed=False, route="straight"),
        E("a", "c", directed=False, route="straight"),
        E("b", "d", directed=False, route="straight"),
        E("b", "e", directed=False, route="straight"),
        E("c", "f", directed=False, route="straight"),
        E("e", "g", directed=False, route="straight"),
        E("f", "g", directed=False, route="straight"),
    ],
    caption="BFS visits level by level using a FIFO queue starting from node A",
)

# 5 ---------------------------------------------------- bfs level movement
bfs_levels = D(
    key="ch4-05-bfs-level-movement",
    title="BFS Level-by-Level Discovery and Queue Processing Order",
    size=(1080, 500),
    flow="H",
    nodes=[
        # Level 0
        N("l0", "Level 0\nVertex A (dist = 0)", 40, 70, 220, 68, "yellow", bold=True),
        # Level 1
        N("b", "Level 1: Vertex B\n(dist = 1, parent A)", 300, 70, 220, 68, "blue"),
        N("c", "Level 1: Vertex C\n(dist = 1, parent A)", 300, 160, 220, 68, "blue"),
        # Level 2
        N("d", "Level 2: Vertex D\n(dist = 2, parent B)", 560, 70, 220, 68, "green"),
        N("e", "Level 2: Vertex E\n(dist = 2, parent B)", 560, 160, 220, 68, "green"),
        N("f", "Level 2: Vertex F\n(dist = 2, parent C)", 560, 250, 220, 68, "green"),
        # Level 3
        N("g", "Level 3: Vertex G\n(dist = 3, parent E/F)", 820, 160, 220, 68, "teal", bold=True),
        # Processing summary bar
        N("q_flow", "Queue Order: [ A ] -> [ B, C ] -> [ D, E, F ] -> [ G ]\nFIFO structure guarantees shortest unweighted hop count",
          120, 380, 840, 64, "dark", bold=True),
    ],
    edges=[
        E("l0", "b"), E("l0", "c"),
        E("b", "d"), E("b", "e"),
        E("c", "f"),
        E("e", "g"), E("f", "g"),
    ],
    caption="BFS guarantees shortest distance in unweighted graphs because vertices are visited in nondecreasing order of distance",
)

# 6 ---------------------------------------------------- dfs traversal graph
dfs_graph = D(
    key="ch4-06-dfs-traversal-graph",
    title="DFS Traversal on 7-Vertex Graph (Source A)",
    size=(760, 420),
    flow="H",
    nodes=make_seven_vertex_nodes(100, 80, 150, 100),
    edges=[
        E("a", "b", directed=False, route="straight"),
        E("a", "c", directed=False, route="straight"),
        E("b", "d", directed=False, route="straight"),
        E("b", "e", directed=False, route="straight"),
        E("c", "f", directed=False, route="straight"),
        E("e", "g", directed=False, route="straight"),
        E("f", "g", directed=False, route="straight"),
    ],
    caption="DFS explores each branch as deep as possible before backtracking",
)

# 7 ---------------------------------------------------- dfs deep movement
dfs_movement = D(
    key="ch4-07-dfs-backtracking",
    title="DFS Deep Movement and Backtracking Trace",
    size=(1040, 480),
    flow="H",
    nodes=make_seven_vertex_nodes(60, 90, 130, 95) + [
        N("note", "DFS Search Trace:\n1. A -> B -> D (dead end!)\n2. Backtrack to B\n3. B -> E -> G -> F -> C\n4. All 7 vertices reached!",
          620, 240, 360, 120, "yellow", size=14, bold=True),
    ],
    edges=[
        E("a", "b", "1: dive", route="straight", color="#1971c2"),
        E("b", "d", "2: dive", route="straight", color="#1971c2"),
        E("d", "b", "3: backtrack", route="loopl", bend=40, dashed=True, color="#e03131"),
        E("b", "e", "4: branch", route="straight", color="#1971c2"),
        E("e", "g", "5: dive", route="straight", color="#1971c2"),
        E("g", "f", "6: dive", route="straight", color="#1971c2"),
        E("f", "c", "7: dive", route="straight", color="#1971c2"),
    ],
    caption="DFS follows edges forward until a dead end is reached, then backtracks to resume unvisited branches",
)

# 8 ---------------------------------------------------- bfs queue vs dfs stack
bfs_vs_dfs = D(
    key="ch4-08-bfs-queue-vs-dfs-stack",
    title="BFS Queue vs DFS Stack Comparison",
    size=(1180, 500),
    flow="H",
    containers=[
        N("box_bfs", "BFS (FIFO Queue)", 40, 70, 530, 350, "container"),
        N("box_dfs", "DFS (LIFO Stack / Recursion)", 600, 70, 540, 350, "container"),
    ],
    nodes=[
        # BFS
        N("b1", "Discover Start Node A", 60, 115, 230, 54, "blue", size=14),
        N("b2", "Enqueue [B, C]", 310, 115, 230, 54, "blue", size=14),
        N("b3", "Dequeue B, Enqueue [D, E]", 60, 195, 230, 54, "blue", size=14),
        N("b4", "Level-by-Level Order", 310, 195, 230, 54, "blue", size=14),
        N("bres", "BFS Order:\nA, B, C, D, E, F, G\nFinds shortest hops", 130, 280, 350, 76, "green", size=14, bold=True),
        # DFS
        N("d1", "Discover Start Node A", 620, 115, 230, 54, "teal", size=14),
        N("d2", "Push B, Dive to D", 870, 115, 230, 54, "teal", size=14),
        N("d3", "Dead end -> Backtrack", 620, 195, 230, 54, "teal", size=14),
        N("d4", "Branch E -> G -> F -> C", 870, 195, 230, 54, "teal", size=14),
        N("dres", "DFS Order:\nA, B, D, E, G, F, C\nTraverses deeply first", 690, 280, 350, 76, "yellow", size=14, bold=True),
    ],
    edges=[
        E("b1", "b2"), E("b2", "b3"), E("b3", "b4"), E("b4", "bres"),
        E("d1", "d2"), E("d2", "d3"), E("d3", "d4"), E("d4", "dres"),
    ],
    caption="Queue structure forces horizontal expansion (breadth); stack structure forces vertical diving (depth)",
)

DIAGRAMS = [
    search_traversal_flow,
    movement_purpose,
    intro_graph,
    bfs_graph,
    bfs_levels,
    dfs_graph,
    dfs_movement,
    bfs_vs_dfs,
]
