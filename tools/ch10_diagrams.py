"""Chapter 10 (Branch and Bound) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 10 - Branch and Bound/diagrams"

# 1 ---------------------------------------------------- branch-and-bound cycle
bnb_cycle = D(
    key="ch10-01-branch-and-bound-cycle",
    title="Branch and Bound: Branch, Bound, Prune",
    size=(1340, 460),
    flow="H",
    nodes=[
        N("prob", "Optimization\nproblem\n(min cost / max profit)", 20, 150, 260, 80, "yellow", "ellipse", 15, True),
        N("br", "Branch\nsplit a live node\ninto children", 310, 150, 200, 80, "blue"),
        N("bd", "Bound\nestimate the best value\nthe child can reach", 550, 150, 240, 80, "blue"),
        N("pr", "Bound no better\nthan the\nincumbent?", 850, 130, 220, 120, "yellow", "diamond", 14),
        N("disc", "Prune\ndiscard the branch", 850, 320, 220, 64, "red"),
        N("keep", "Keep as live node\n(queue / stack / heap)", 1110, 150, 220, 80, "green"),
        N("inc", "Complete feasible solution?\nupdate the incumbent", 520, 320, 290, 64, "violet"),
    ],
    edges=[
        E("prob", "br"),
        E("br", "bd"),
        E("bd", "pr"),
        E("pr", "disc", "Yes", route="v"),
        E("pr", "keep", "No"),
        E("keep", "br", "pick next live node", route="loopt", bend=70),
        E("bd", "inc", "leaf reached", route="v"),
    ],
    caption="Backtracking prunes only infeasible nodes; branch and bound also prunes nodes whose bound cannot beat the best answer so far",
)

# 2 ---------------------------------------------------- FIFO / LIFO / LC
strategies = D(
    key="ch10-02-fifo-lifo-lc-search",
    title="Three Ways to Choose the Next Live Node",
    size=(1120, 470),
    flow="V",
    nodes=[
        N("live", "List of live nodes", 450, 70, 220, 60, "yellow", "ellipse", 16, True),
        N("fifo", "FIFO branch and bound\nlive nodes kept in a QUEUE\nbreadth-first order", 50, 190, 300, 90, "blue"),
        N("lifo", "LIFO branch and bound\nlive nodes kept in a STACK\ndepth-first order", 410, 190, 300, 90, "violet"),
        N("lc", "LC (least-cost) search\nlive nodes kept in a HEAP\nbest-first order", 770, 190, 300, 90, "green"),
        N("fifo2", "Expand the OLDEST\nlive node next", 50, 330, 300, 64, "blue"),
        N("lifo2", "Expand the NEWEST\nlive node next", 410, 330, 300, 64, "violet"),
        N("lc2", "Expand the node with the\nbest estimated cost next", 770, 330, 300, 64, "green"),
    ],
    edges=[
        E("live", "fifo"),
        E("live", "lifo"),
        E("live", "lc"),
        E("fifo", "fifo2"),
        E("lifo", "lifo2"),
        E("lc", "lc2"),
    ],
    caption="LC search usually reaches a good incumbent early and therefore prunes the most nodes",
)

# 3 ---------------------------------------------------- 0/1 knapsack LC tree
knapsack_tree = D(
    key="ch10-03-knapsack-lc-tree",
    title="0/1 Knapsack by LC-Search (capacity 10)",
    size=(1260, 610),
    flow="V",
    nodes=[
        N("root", "1. Root\nw=0  p=0\nub=73", 545, 60, 210, 90, "yellow", size=14, bold=True),
        N("a1", "2. take A\nw=4  p=40\nub=73", 345, 190, 210, 90, "blue", size=14),
        N("a0", "skip A\nw=0  p=0\nub=52  PRUNED", 1005, 190, 210, 90, "red", size=14),
        N("ac", "3. take C\nw=7  p=58\nub=73", 135, 320, 210, 90, "blue", size=14),
        N("anc", "4. skip C\nw=4  p=40\nub=70", 555, 320, 210, 90, "blue", size=14),
        N("acb", "take B\nw=13 > 10\nINFEASIBLE", 15, 450, 210, 90, "red", size=14),
        N("acnb", "skip B\nw=7  p=58\nub=70  PRUNED", 255, 450, 210, 90, "red", size=14),
        N("ancb", "take B\nw=10  p=70\nBEST = 70", 495, 450, 210, 90, "green", size=14, bold=True),
        N("ancnb", "skip B\nw=4  p=40\nub=60  PRUNED", 735, 450, 210, 90, "red", size=14),
    ],
    edges=[
        E("root", "a1", "take"),
        E("root", "a0", "skip"),
        E("a1", "ac", "take"),
        E("a1", "anc", "skip"),
        E("ac", "acb"),
        E("ac", "acnb"),
        E("anc", "ancb"),
        E("anc", "ancnb"),
    ],
    caption="Items (weight, profit): A(4,40) C(3,18) B(6,30) D(5,20). Numbers show the order in which nodes are expanded",
)

# 4 ---------------------------------------------------- job sequencing tree
job_tree = D(
    key="ch10-04-job-sequencing-tree",
    title="Job Sequencing with Deadlines by Branch and Bound",
    size=(900, 690),
    flow="V",
    nodes=[
        N("root", "Root\np=0  ub=152", 400, 60, 200, 80, "yellow", size=14, bold=True),
        N("j1", "J1 = 1\np=100  ub=152", 250, 180, 200, 80, "blue", size=14),
        N("j1n", "J1 = 0\nub=52  PRUNED", 650, 180, 200, 80, "red", size=14),
        N("j4", "J4 = 1\np=127  ub=152", 130, 300, 200, 80, "blue", size=14),
        N("j4n", "J4 = 0\nub=125  PRUNED", 400, 300, 200, 80, "red", size=14),
        N("j3", "J3 = 1\nINFEASIBLE", 10, 420, 200, 80, "red", size=14),
        N("j3n", "J3 = 0\np=127  ub=137", 250, 420, 200, 80, "blue", size=14),
        N("j2", "J2 = 1\nINFEASIBLE", 130, 540, 200, 80, "red", size=14),
        N("j2n", "J2 = 0\nleaf  BEST = 127", 390, 540, 200, 80, "green", size=14, bold=True),
    ],
    edges=[
        E("root", "j1", "take"),
        E("root", "j1n", "skip"),
        E("j1", "j4", "take"),
        E("j1", "j4n", "skip"),
        E("j4", "j3", "take"),
        E("j4", "j3n", "skip"),
        E("j3n", "j2", "take"),
        E("j3n", "j2n", "skip"),
    ],
    caption="Jobs J1(100,d2) J4(27,d1) J3(15,d2) J2(10,d1). Optimal: J4 in slot 1, J1 in slot 2, profit 127",
)

# 5 ---------------------------------------------------- TSP branch and bound
tsp_tree = D(
    key="ch10-05-tsp-branch-and-bound",
    title="TSP Branch and Bound with Reduced Cost Matrix",
    size=(1100, 620),
    flow="V",
    nodes=[
        N("root", "Root (start at city 0)\nrow reduction = 64\nlb = 64", 440, 60, 220, 90, "yellow", size=14, bold=True),
        N("n01", "edge 0 to 1\nlb = 97", 110, 190, 200, 80, "blue", size=14),
        N("n02", "edge 0 to 2\nlb = 108  PRUNED", 450, 190, 200, 80, "red", size=14),
        N("n03", "edge 0 to 3\nlb = 97  PRUNED\n(not below best 97)", 790, 190, 220, 80, "red", size=14),
        N("n12", "edge 1 to 2\nlb = 97", 20, 330, 200, 80, "blue", size=14),
        N("n13", "edge 1 to 3\nlb = 108  PRUNED", 260, 330, 200, 80, "red", size=14),
        N("tour", "edges 2 to 3, 3 to 0\ntour 0-1-2-3-0\ncost = 97", 20, 470, 240, 90, "green", size=14, bold=True),
    ],
    edges=[
        E("root", "n01"),
        E("root", "n02"),
        E("root", "n03"),
        E("n01", "n12"),
        E("n01", "n13"),
        E("n12", "tour"),
    ],
    caption="Cost matrix rows: [0,20,42,35] [20,0,30,34] [42,30,0,12] [35,34,12,0]. Best tour cost 97 equals the DP answer",
)

DIAGRAMS = [bnb_cycle, strategies, knapsack_tree, job_tree, tsp_tree]
