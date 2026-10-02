"""Chapter 15 (Lower Bound Theory and NP Completeness) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 15 - Lower Bound Theory and NP Completeness/diagrams"

# 1 ---------------------------------------------------- lower bound concept
lower_bound = D(
    key="ch15-01-lower-bound-concept",
    title="Lower Bound Theory - Bridging the Complexity Gap",
    size=(1120, 360),
    flow="H",
    nodes=[
        N("p", "Problem", 50, 130, 180, 60, "yellow", "ellipse", bold=True),
        N("lb", "Lower Bound: Omega(f(n))\nevery algorithm needs\nat least this many steps", 310, 60, 320, 80, "blue"),
        N("ub", "Upper Bound: O(g(n))\nbest known algorithm's\nrunning time", 310, 180, 320, 80, "blue"),
        N("opt", "Algorithm is\nAsymptotically Optimal!\nNo faster algorithm can exist", 740, 120, 320, 80, "green", bold=True),
    ],
    edges=[
        E("p", "lb"),
        E("p", "ub"),
        E("lb", "opt", "f(n) = g(n)"),
        E("ub", "opt"),
    ],
    caption="When upper and lower bounds match, the problem complexity is completely solved",
)

# 2 ---------------------------------------------------- decision tree model
decision_tree = D(
    key="ch15-02-decision-tree-model",
    title="Comparison Tree Model for n = 3 Elements (Lower Bound Omega(n log n))",
    size=(1140, 620),
    flow="V",
    nodes=[
        # Root
        N("root", "a1 <= a2 ?", 470, 60, 200, 70, "yellow", "diamond", 15),
        # Level 1
        N("n1", "a2 <= a3 ?", 220, 180, 200, 70, "yellow", "diamond", 15),
        N("n2", "a1 <= a3 ?", 720, 180, 200, 70, "yellow", "diamond", 15),
        # Level 2
        N("l1", "<a1, a2, a3>", 50, 310, 160, 52, "green"),
        N("n3", "a1 <= a3 ?", 250, 300, 180, 70, "yellow", "diamond", 14),
        N("l4", "<a2, a1, a3>", 610, 310, 160, 52, "green"),
        N("n4", "a2 <= a3 ?", 820, 300, 180, 70, "yellow", "diamond", 14),
        # Leaves Level 3
        N("l2", "<a1, a3, a2>", 160, 440, 160, 52, "green"),
        N("l3", "<a3, a1, a2>", 340, 440, 160, 52, "green"),
        N("l5", "<a2, a3, a1>", 730, 440, 160, 52, "green"),
        N("l6", "<a3, a2, a1>", 910, 440, 160, 52, "green"),
    ],
    edges=[
        E("root", "n1", "Yes"),
        E("root", "n2", "No"),
        E("n1", "l1", "Yes"),
        E("n1", "n3", "No"),
        E("n3", "l2", "Yes"),
        E("n3", "l3", "No"),
        E("n2", "l4", "Yes"),
        E("n2", "n4", "No"),
        E("n4", "l5", "Yes"),
        E("n4", "l6", "No"),
    ],
    caption="Tree has n! = 6 leaves, requiring minimum height of ceil(log2(n!)) = Omega(n log n)",
)

# 3 ---------------------------------------------------- intractable problems
intractable = D(
    key="ch15-03-intractable-problems",
    title="Tractable vs Intractable Problems",
    size=(940, 360),
    flow="H",
    nodes=[
        N("probs", "All Decision\nProblems", 50, 130, 220, 70, "gray", "ellipse", bold=True),
        N("tract", "Tractable (Polynomial Time)\nO(1), O(log n), O(n), O(n^2), O(n^k)\nSolvable efficiently in practice", 370, 60, 390, 80, "green"),
        N("intract", "Intractable (Super-Polynomial)\nO(2^n), O(n!), O(n^n)\nComputationally infeasible for large n", 370, 190, 390, 80, "red"),
    ],
    edges=[
        E("probs", "tract"),
        E("probs", "intract"),
    ],
    caption="The polynomial time boundary separates computationally practical problems from impractical ones",
)

# 4 ---------------------------------------------------- conditions np-completeness
np_conditions = D(
    key="ch15-04-conditions-np-completeness",
    title="Conditions for Proving NP-Completeness of Problem L",
    size=(1140, 420),
    flow="H",
    nodes=[
        N("every", "Every Problem\nin NP", 40, 80, 200, 64, "blue"),
        N("known", "Known NP-Complete\nProblem L'", 300, 80, 220, 64, "violet", bold=True),
        N("l_cand", "Candidate\nProblem L", 600, 80, 220, 64, "yellow", bold=True),
        N("np_mem", "Condition 1: L in NP\nCandidate solution verifiable\nin polynomial time", 400, 230, 340, 70, "blue"),
        N("npc_res", "L is NP-Complete!\n(Both Condition 1 and\nCondition 2 satisfied)", 860, 150, 240, 80, "green", bold=True),
    ],
    edges=[
        E("every", "known", "poly reduces"),
        E("known", "l_cand", "poly-time reduction L' <=p L"),
        E("l_cand", "np_mem"),
        E("np_mem", "npc_res"),
        E("l_cand", "npc_res"),
    ],
    caption="To prove NP-Completeness: 1) Verify membership in NP; 2) Reduce a known NP-Complete problem to L",
)

# 5 ---------------------------------------------------- np-complete vs np-hard
np_classes = D(
    key="ch15-05-np-complete-vs-np-hard",
    title="Complexity Class Hierarchy (Assuming P != NP)",
    size=(1160, 720),
    flow="V",
    containers=[
        N("box_hard", "NP-Hard (at least as hard as the hardest problem in NP)", 50, 70, 1060, 540, "container"),
        N("box_np", "NP (solvable in nondeterministic poly-time / verifiable in poly-time)", 90, 140, 980, 360, "container"),
    ],
    nodes=[
        N("p_class", "Class P\nSolved deterministically in poly-time\ne.g., Sorting, Shortest Path, MST", 130, 230, 420, 110, "green", size=14, bold=True),
        N("npc_class", "Class NP-Complete\nHardest problems in NP\ne.g., 3-SAT, Clique, Vertex Cover,\nTSP-Decision", 610, 230, 420, 110, "yellow", size=13, bold=True),
        N("npi_class", "NP-Intermediate\n(if P != NP: problems in NP neither in P nor NPC\ne.g., Factoring, Graph Isomorphism)", 140, 380, 400, 80, "teal", size=13),
        N("hard_only", "NP-Hard (outside NP)\nNot necessarily decision problems or verifiable in poly-time\ne.g., Halting Problem, TSP Optimization", 130, 520, 900, 74, "red", size=13),
    ],
    edges=[
        E("p_class", "npc_class", "poly-time reduction", dashed=True),
        E("npc_class", "hard_only", "subsumed by", dashed=True, pts=[(820, 340), (820, 520)]),
    ],
    caption="NP-Complete problems lie at the exact intersection of NP and NP-Hard",
)

DIAGRAMS = [lower_bound, decision_tree, intractable, np_conditions, np_classes]
