"""Chapter 8 (Dynamic Programming) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 8 - Dynamic Programming/diagrams"

# 1 ---------------------------------------------------- dp design flow
dp_design = D(
    key="ch8-01-dp-design-flow",
    title="The Dynamic Programming 5-Step Design Framework",
    size=(1160, 420),
    flow="H",
    nodes=[
        N("prob", "Original\nOptimization Problem", 30, 80, 210, 68, "blue", "ellipse", size=14, bold=True),
        N("s1", "1. Define State\nMeaning of subproblem", 265, 80, 220, 68, "yellow", size=14, bold=True),
        N("s2", "2. Base Cases\nSmallest known solutions", 510, 80, 225, 68, "green", size=14),
        N("s3", "3. Recurrence\nRelation between choices", 760, 80, 225, 68, "yellow", size=14, bold=True),
        N("s4", "4. Evaluation Order\nDependency sequence", 380, 230, 240, 68, "teal", size=14),
        N("s5", "5. Table / Memo\nStore computed states", 660, 230, 240, 68, "green", size=14),
        N("ans", "Target Answer\nRead final cell &\nreconstruct path", 940, 225, 180, 76, "green", size=13, bold=True),
    ],
    edges=[
        E("prob", "s1"), E("s1", "s2"), E("s2", "s3"),
        E("s3", "s4", route="v"), E("s4", "s5"), E("s5", "ans"),
    ],
    caption="DP solves overlapping subproblems by ordering computations and memoizing state results",
)

# 2 ---------------------------------------------------- repeated work removed
repeated_work = D(
    key="ch8-02-repeated-work-removed",
    title="Exponential Redundancy in Naive Recursion vs Memoization",
    size=(1020, 540),
    flow="V",
    nodes=[
        N("root", "Original Call f(n)", 400, 60, 220, 52, "yellow", bold=True),
        N("a1", "Subproblem A", 200, 150, 200, 52, "blue"),
        N("b1", "Subproblem B", 600, 150, 200, 52, "blue"),
        N("c1", "Subproblem C", 100, 240, 180, 52, "yellow"),
        N("d1", "Subproblem D", 300, 240, 180, 52, "yellow"),
        N("c2", "Subproblem C\n(Duplicate!)", 520, 240, 180, 52, "red"),
        N("d2", "Subproblem D\n(Duplicate!)", 720, 240, 180, 52, "red"),
        N("waste", "Repeated Computation!\nNaive recursion recomputes identical states\nleading to O(2^n) time complexity",
          150, 350, 720, 70, "red", bold=True),
        N("dp_fix", "DP Fix: Store in memo table -> O(1) lookup on return\nGuarantees O(n) total running time!",
          140, 435, 740, 60, "green", size=14, bold=True),
    ],
    edges=[
        E("root", "a1"), E("root", "b1"),
        E("a1", "c1"), E("a1", "d1"),
        E("b1", "c2"), E("b1", "d2"),
        E("c2", "waste", dashed=True, color="#e03131"),
        E("d2", "waste", dashed=True, color="#e03131"),
        E("waste", "dp_fix"),
    ],
    caption="Memoization ensures each distinct subproblem state is computed exactly once",
)

# 3 ---------------------------------------------------- greedy vs dp choice
greedy_vs_dp = D(
    key="ch8-03-greedy-vs-dp-choice",
    title="Algorithmic Paradigm Comparison - Greedy Choice vs DP Choice",
    size=(1180, 480),
    flow="H",
    containers=[
        N("box_g", "Greedy Paradigm (Irrevocable Local Choice)", 50, 70, 520, 330, "container"),
        N("box_d", "Dynamic Programming (Systematic Exhaustive Evaluation)", 610, 70, 520, 330, "container"),
    ],
    nodes=[
        # Greedy
        N("g1", "Inspect current state", 70, 120, 235, 52, "yellow", size=14),
        N("g2", "Pick locally best option", 325, 120, 235, 52, "yellow", size=14),
        N("g3", "Never reconsider or undo", 70, 210, 235, 52, "yellow", size=14),
        N("g4", "Requires Greedy-Choice\nProperty", 325, 205, 235, 58, "yellow", size=13),
        N("gres", "Fast (O(n log n)), but fragile\n(Fails without matroid structure)", 135, 290, 350, 60, "red", size=14, bold=True),
        # DP
        N("d1", "Define state representation", 630, 120, 235, 52, "blue", size=14),
        N("d2", "Explore ALL valid\ntransitions", 885, 117, 235, 58, "blue", size=13),
        N("d3", "Reuse cached subproblems", 630, 210, 235, 52, "blue", size=14),
        N("d4", "Combines optimal subpaths", 885, 210, 235, 52, "blue", size=14),
        N("dres", "Always optimal if subproblems overlap\nand optimal substructure holds", 695, 290, 360, 60, "green", size=14, bold=True),
    ],
    edges=[
        E("g1", "g2"), E("g2", "g3"), E("g3", "g4"), E("g4", "gres"),
        E("d1", "d2"), E("d2", "d3"), E("d3", "d4"), E("d4", "dres"),
    ],
    caption="Greedy commits blindly to local heuristics; DP systematically evaluates all possibilities via cached subproblems",
)

# 4 ---------------------------------------------------- optimal subpaths
optimal_subpaths = D(
    key="ch8-04-optimal-subpaths",
    title="Optimal Substructure Principle - Optimal Path Contains Optimal Subpaths",
    size=(1040, 420),
    flow="H",
    nodes=[
        N("a", "A", 80, 150, 56, 56, "green", "circle", bold=True),
        N("b", "B", 340, 150, 56, 56, "green", "circle", bold=True),
        N("d", "D", 680, 150, 56, 56, "green", "circle", bold=True),
        N("x", "X (Alternative detour)", 510, 270, 220, 52, "red"),
        N("note", "Proof by Contradiction:\nIf B->X->D were cheaper than B->D, then A->B->X->D would beat\nthe assumed optimal A->D, which is a contradiction!",
          220, 65, 620, 68, "teal", size=13),
    ],
    edges=[
        E("a", "b", "optimal segment", color="#2f9e44"),
        E("b", "d", "optimal subpath", color="#2f9e44"),
        E("b", "x", "cheaper suffix?", dashed=True, color="#e03131"),
        E("x", "d", "rejoins", dashed=True, color="#e03131"),
    ],
    caption="Optimal substructure: an optimal solution is composed of optimal solutions to its constituent subproblems",
)

# 5 ---------------------------------------------------- dp elements working together
dp_elements = D(
    key="ch8-05-dp-elements-working-together",
    title="Core Dynamic Programming Elements and Cohesion",
    size=(1140, 500),
    flow="H",
    containers=[
        N("box_val", "Problem Prerequisites", 40, 70, 300, 340, "container"),
        N("box_des", "DP Solution Design", 360, 70, 480, 340, "container"),
        N("box_out", "Output & Execution", 860, 70, 240, 340, "container"),
    ],
    nodes=[
        # Prerequisites
        N("substruct", "Optimal Substructure\nGlobal optimum contains\noptimal sub-solutions", 60, 120, 260, 80, "blue"),
        N("overlap", "Overlapping Subproblems\nSame subproblems solved\nmultiple times", 60, 240, 260, 80, "blue"),
        # Design
        N("state", "State: S(i, j)", 380, 120, 200, 54, "yellow", bold=True),
        N("base", "Base Cases: S(0, j)", 610, 120, 200, 54, "green"),
        N("recur", "Recurrence Relation\nS(i, j) = min/max(...)", 450, 200, 300, 60, "yellow", bold=True),
        N("order", "Topological Eval Order", 370, 290, 220, 54, "teal", size=14),
        N("table", "Lookup Table / Memo", 610, 290, 200, 54, "green"),
        # Output
        N("opt_val", "Optimal Value", 880, 140, 200, 60, "green", bold=True),
        N("recon", "Reconstruct Path\n(via trace pointers)", 880, 260, 200, 70, "green", size=14),
    ],
    edges=[
        E("substruct", "recur", route="v", bend=0.5), E("overlap", "table", route="loopb", bend=35),
        E("state", "recur"), E("base", "recur"),
        E("recur", "order"), E("order", "table"),
        E("table", "opt_val"), E("table", "recon"),
    ],
    caption="State definition and recurrence relation form the mathematical core of any dynamic programming algorithm",
)

# 6 ---------------------------------------------------- top-down vs bottom-up
topdown_vs_bottomup = D(
    key="ch8-06-top-down-vs-bottom-up",
    title="Top-Down (Memoization) vs Bottom-Up (Tabulation)",
    size=(1140, 480),
    flow="H",
    containers=[
        N("box_top", "Top-Down (Memoization - Demand Driven)", 40, 70, 520, 330, "container"),
        N("box_bot", "Bottom-Up (Tabulation - Systematic Build)", 580, 70, 520, 330, "container"),
    ],
    nodes=[
        # Top-down
        N("t_goal", "Request Target State f(n)", 60, 120, 230, 52, "violet", size=14),
        N("t_hit", "Cached in Memo?", 320, 110, 180, 72, "yellow", "diamond", 15),
        N("t_ret", "Return cached result", 320, 220, 190, 52, "green", size=14),
        N("t_rec", "Recurse on subproblems\nCompute & store in memo", 60, 220, 230, 64, "blue", size=13),
        N("t_sum", "Pros: Solves only needed states\nCons: Recursion stack overhead", 90, 310, 420, 56, "dark", size=13),
        # Bottom-up
        N("b_base", "Fill Base Cases (0, 1)", 600, 120, 220, 52, "green"),
        N("b_loop", "Iterate through Table loops", 840, 120, 230, 52, "teal", size=14),
        N("b_next", "Compute larger states\nfrom smaller ready states", 600, 210, 230, 64, "blue", size=13),
        N("b_targ", "Reach Target State cell", 840, 210, 230, 64, "green", size=14, bold=True),
        N("b_sum", "Pros: No recursion overhead, space optimizable\nCons: Computes all states within bounds", 630, 310, 430, 56, "dark", size=12),
    ],
    edges=[
        E("t_goal", "t_hit"),
        E("t_hit", "t_ret", "Yes"),
        E("t_hit", "t_rec", "No"),
        E("t_rec", "t_ret"),
        E("b_base", "b_loop"),
        E("b_loop", "b_next"),
        E("b_next", "b_targ"),
    ],
    caption="Top-down explores states lazily; bottom-up builds answers systematically in topological order",
)

# 7 ---------------------------------------------------- climbing stairs dependencies
stairs_dependencies = D(
    key="ch8-07-climbing-stairs-dependencies",
    title="Climbing Stairs State Dependencies (1, 2, or 3 Steps)",
    size=(1140, 360),
    flow="H",
    containers=[
        N("box_base", "Base Cases", 40, 70, 360, 230, "container"),
        N("box_build", "Bottom-Up Computation Sequence", 430, 70, 670, 230, "container"),
    ],
    nodes=[
        N("w0", "Ways(0) = 1", 60, 130, 140, 50, "blue"),
        N("w1", "Ways(1) = 1", 60, 210, 140, 50, "blue"),
        N("w2", "Ways(2) = 2", 230, 170, 140, 50, "blue"),
        N("w3", "Ways(3) = 4", 460, 170, 160, 50, "green"),
        N("w4", "Ways(4) = 7", 680, 170, 160, 50, "green"),
        N("w5", "Ways(5) = 13", 900, 170, 170, 50, "yellow", bold=True),
    ],
    edges=[
        E("w0", "w3", route="loopt", bend=40), E("w1", "w3", route="loopb", bend=35), E("w2", "w3"),
        E("w1", "w4", route="loopb", bend=55), E("w2", "w4", route="loopt", bend=40), E("w3", "w4"),
        E("w2", "w5", route="loopt", bend=60), E("w3", "w5", route="loopb", bend=40), E("w4", "w5"),
    ],
    caption="Recurrence: Ways(n) = Ways(n-1) + Ways(n-2) + Ways(n-3) with sliding 3-variable window",
)

# 8 ---------------------------------------------------- climbing stairs tree
stairs_tree = D(
    key="ch8-08-climbing-stairs-tree",
    title="Climbing Stairs Recursion Tree (1 or 2 Steps for n = 4)",
    size=(1020, 520),
    flow="V",
    nodes=[
        N("c4", "C(4)", 450, 60, 120, 50, "yellow", bold=True),
        N("c3", "C(3)", 240, 160, 120, 50, "yellow"),
        N("c2a", "C(2) [dup 1]", 660, 160, 140, 50, "red"),
        N("c2b", "C(2) [dup 2]", 130, 260, 140, 50, "red"),
        N("c1a", "C(1) = 1 [base]", 340, 260, 160, 50, "green"),
        N("c1b", "C(1) = 1 [base]", 560, 260, 160, 50, "green"),
        N("c0a", "C(0) = 1 [base]", 760, 260, 160, 50, "green"),
        N("c1c", "C(1) = 1 [base]", 40, 360, 160, 50, "green"),
        N("c0b", "C(0) = 1 [base]", 220, 360, 160, 50, "green"),
    ],
    edges=[
        E("c4", "c3"), E("c4", "c2a"),
        E("c3", "c2b"), E("c3", "c1a"),
        E("c2a", "c1b"), E("c2a", "c0a"),
        E("c2b", "c1c"), E("c2b", "c0b"),
    ],
    caption="Notice C(2) evaluated multiple times; DP table reduces this recursion tree to O(n) lookups",
)

# 9 ---------------------------------------------------- knapsack decision traceback
knapsack_decision = D(
    key="ch8-09-knapsack-decision-traceback",
    title="0/1 Knapsack Cell Decision Rule and Traceback Path",
    size=(1140, 540),
    flow="H",
    containers=[
        N("box_rule", "Cell Update Rule: V[i, j]", 40, 70, 540, 400, "container"),
        N("box_trace", "Traceback Procedure (from V[n, W])", 600, 70, 500, 400, "container"),
    ],
    nodes=[
        # Rule
        N("k_state", "Cell V[i, j]\nFirst i items, capacity j", 70, 120, 240, 60, "blue", size=14),
        N("k_fit", "Does item fit?\nw_i <= j", 360, 115, 180, 70, "yellow", "diamond", 15),
        N("k_skip1", "Cannot fit item i:\nCopy V[i-1, j]", 340, 230, 200, 60, "red"),
        N("k_skip2", "Option 1 (Skip):\nV[i-1, j]", 70, 260, 200, 60, "yellow"),
        N("k_take", "Option 2 (Take):\nv_i + V[i-1, j - w_i]", 70, 350, 200, 60, "green", size=14),
        N("k_max", "Store Best:\nmax(Skip, Take)", 340, 330, 200, 60, "green", bold=True),
        # Traceback
        N("t_check", "Compare cell:\nV[i, j] == V[i-1, j]?", 630, 120, 240, 70, "yellow", "diamond", 15),
        N("t_no", "Equal -> Item not taken\nMove to (i-1, j)", 880, 120, 200, 70, "blue", size=13),
        N("t_yes", "Different -> Item taken!\nMove to (i-1, j - w_i)", 630, 260, 280, 74, "green", size=14, bold=True),
        N("t_done", "Continue until i == 0 or j == 0\nFull optimal subset reconstructed", 630, 380, 430, 54, "teal", bold=True),
    ],
    edges=[
        E("k_state", "k_fit"),
        E("k_fit", "k_skip1", "No"),
        E("k_fit", "k_take", "Yes"),
        E("k_fit", "k_skip2", "Yes"),
        E("k_skip1", "k_max"), E("k_skip2", "k_max"), E("k_take", "k_max"),
        E("t_check", "t_no", "Yes"), E("t_check", "t_yes", "No"),
        E("t_yes", "t_done"), E("t_no", "t_done"),
    ],
    caption="0/1 choice: an item can be taken at most once, referencing the strictly previous row i-1",
)

# 10 ---------------------------------------------------- rod cutting unbounded
rod_cutting = D(
    key="ch8-10-rod-cutting-unbounded",
    title="Rod Cutting - Unbounded Knapsack Recurrence",
    size=(1140, 420),
    flow="H",
    nodes=[
        N("rod", "Rod Length j", 40, 150, 160, 60, "blue", bold=True),
        N("cut", "Try Piece of Length i\n(Cut decision)", 250, 140, 220, 80, "yellow", "diamond", 15),
        N("exclude", "Cut length i > j:\nCopy T[i-1, j]", 250, 280, 220, 60, "red"),
        N("split", "Valid Cut (i <= j):\nSplit rod", 530, 150, 180, 60, "green", size=14),
        N("earn", "Sell Piece i: earn p_i\nRemaining length: j - i", 770, 70, 270, 64, "green"),
        N("reuse", "Solve Subproblem: T[i, j - i]\n(SAME row allows repeating!)", 770, 180, 280, 64, "teal", size=13, bold=True),
        N("best", "Best Revenue T[i, j]:\nmax(T[i-1, j], p_i + T[i, j - i])", 680, 300, 340, 68, "green", bold=True),
    ],
    edges=[
        E("rod", "cut"),
        E("cut", "exclude", "Does not fit"),
        E("cut", "split", "Fits"),
        E("split", "earn"), E("split", "reuse"),
        E("earn", "best", route="loopr", bend=55), E("reuse", "best"), E("exclude", "best"),
    ],
    caption="Unbounded knapsack looks at the same row i for j-i, permitting unlimited duplicates of each item",
)

# 11 ---------------------------------------------------- lcs match mismatch
lcs_cell = D(
    key="ch8-11-lcs-cell-traceback",
    title="Longest Common Subsequence (LCS) State Transitions",
    size=(1140, 460),
    flow="H",
    containers=[
        N("box_table", "LCS Table Neighbors for Cell c[i, j]", 50, 70, 440, 330, "container"),
        N("box_logic", "Transition Logic & Traceback", 520, 70, 570, 330, "container"),
    ],
    nodes=[
        # Table neighbors
        N("diag", "c[i-1, j-1]\nDiagonal match", 80, 120, 170, 60, "green"),
        N("up", "c[i-1, j]\nDrop X[i]", 280, 120, 170, 60, "blue"),
        N("left", "c[i, j-1]\nDrop Y[j]", 80, 230, 170, 60, "blue"),
        N("curr", "Target: c[i, j]", 280, 230, 170, 60, "yellow", bold=True),
        # Logic
        N("cmp", "Do characters match?\nX[i] == Y[j]", 550, 140, 220, 80, "yellow", "diamond", 15),
        N("match_act", "Match Action:\nc[i, j] = 1 + c[i-1, j-1]\n(Diagonal arrow)", 810, 100, 260, 70, "green", size=13, bold=True),
        N("mismatch_act", "Mismatch Action:\nc[i, j] = max(up, left)\n(Up or Left arrow)", 810, 220, 260, 70, "blue", size=13),
    ],
    edges=[
        E("diag", "curr", color="#2f9e44"),
        E("up", "curr", color="#1971c2"),
        E("left", "curr", color="#1971c2"),
        E("cmp", "match_act", "Yes"),
        E("cmp", "mismatch_act", "No"),
    ],
    caption="Traceback moves diagonally on character matches and horizontally/vertically on mismatches",
)

# 12 ---------------------------------------------------- matrix chain splits
matrix_chain = D(
    key="ch8-12-matrix-chain-splits",
    title="Matrix Chain Multiplication - Evaluating Interval Splits M[1, 4]",
    size=(1140, 480),
    flow="V",
    nodes=[
        N("intv", "Matrix Interval M[1, 4]\nProduct: A1 * A2 * A3 * A4", 400, 60, 340, 56, "yellow", bold=True),
        # Splits
        N("k1", "Split at k = 1\n(A1) * (A2 A3 A4)\nCost = 580 ops", 80, 170, 280, 74, "red"),
        N("k2", "Split at k = 2\n(A1 A2) * (A3 A4)\nCost = 405 ops", 430, 170, 280, 74, "green", bold=True),
        N("k3", "Split at k = 3\n(A1 A2 A3) * (A4)\nCost = 660 ops", 780, 170, 280, 74, "red"),
        # Optimal
        N("opt", "Optimal Partition: k = 2 (Cost 405)\nParenthesization: ((A1 * A2) * (A3 * A4))\nSaves 255 scalar multiplications compared to worst split!",
          180, 320, 780, 80, "green", bold=True),
    ],
    edges=[
        E("intv", "k1"), E("intv", "k2"), E("intv", "k3"),
        E("k2", "opt", "minimum cost", color="#2f9e44"),
    ],
    caption="Dynamic programming solves matrix chain order in O(n^3) by minimizing over all valid split indices k",
)

# 13 ---------------------------------------------------- optimal bst root choices
optimal_bst = D(
    key="ch8-13-optimal-bst-root-choices",
    title="Optimal Binary Search Tree - Root Selection for Keys {k1, k2, k3}",
    size=(1140, 480),
    flow="V",
    nodes=[
        N("intv", "Key Range E[1, 3]\nKeys: k1, k2, k3", 440, 60, 260, 54, "yellow", bold=True),
        N("r1", "Root = k1\nLeft: empty | Right: {k2, k3}\nExpected Search Cost = 1.30", 60, 170, 300, 74, "blue"),
        N("r2", "Root = k2\nLeft: {k1} | Right: {k3}\nExpected Search Cost = 1.25", 420, 170, 300, 74, "green", bold=True),
        N("r3", "Root = k3\nLeft: {k1, k2} | Right: empty\nExpected Search Cost = 1.45", 780, 170, 300, 74, "blue"),
        N("opt", "Optimal Choice: Root k2 with Expected Cost 1.25\nBalances key access probabilities across left and right subtrees",
          200, 320, 740, 70, "green", bold=True),
    ],
    edges=[
        E("intv", "r1"), E("intv", "r2"), E("intv", "r3"),
        E("r2", "opt", "lowest expected cost", color="#2f9e44"),
    ],
    caption="Cost formula: e[i, j] = w(i, j) + min_{r} (e[i, r-1] + e[r+1, j])",
)

# 14 ---------------------------------------------------- multistage graph layout
multistage_graph = D(
    key="ch8-14-multistage-graph-layout",
    title="Multistage Graph Shortest Path Layout (5 Stages)",
    size=(1140, 560),
    flow="H",
    containers=[
        N("st1", "Stage 1", 40, 70, 180, 420, "container"),
        N("st2", "Stage 2", 260, 70, 180, 420, "container"),
        N("st3", "Stage 3", 480, 70, 180, 420, "container"),
        N("st4", "Stage 4", 700, 70, 180, 420, "container"),
        N("st5", "Stage 5", 920, 70, 180, 420, "container"),
    ],
    nodes=[
        # S1
        N("a", "A", 100, 250, 60, 60, "blue", "circle", bold=True),
        # S2
        N("b", "B", 320, 130, 60, 60, "blue", "circle"),
        N("c", "C", 320, 250, 60, 60, "blue", "circle"),
        N("d", "D", 320, 370, 60, 60, "blue", "circle"),
        # S3
        N("e", "E", 540, 130, 60, 60, "blue", "circle"),
        N("f", "F", 540, 250, 60, 60, "blue", "circle"),
        N("g", "G", 540, 370, 60, 60, "blue", "circle"),
        # S4
        N("h", "H", 760, 130, 60, 60, "blue", "circle"),
        N("i", "I", 760, 250, 60, 60, "blue", "circle"),
        N("j", "J", 760, 370, 60, 60, "blue", "circle"),
        # S5
        N("k", "K", 980, 250, 60, 60, "green", "circle", bold=True),
    ],
    edges=[
        E("a", "b", "9", route="straight"), E("a", "c", "7", route="straight"), E("a", "d", "3", route="straight"),
        E("b", "e", "2", route="straight"), E("b", "f", "7", route="straight"),
        E("c", "e", "3", route="straight"), E("c", "f", "1", route="straight"), E("c", "g", "4", route="straight"),
        E("d", "f", "6", route="straight"), E("d", "g", "11", route="straight"),
        E("e", "h", "6", route="straight"), E("e", "i", "5", route="straight"),
        E("f", "h", "4", route="straight"), E("f", "i", "3", route="straight"), E("f", "j", "5", route="straight"),
        E("g", "i", "6", route="straight"), E("g", "j", "2", route="straight"),
        E("h", "k", "4", route="straight"), E("i", "k", "2", route="straight"), E("j", "k", "5", route="straight"),
    ],
    caption="Edges only cross from Stage i to Stage i+1, forming a natural DAG without cycles",
)

# 15 ---------------------------------------------------- backward dp cost flow
backward_flow = D(
    key="ch8-15-backward-dp-cost-flow",
    title="Backward Dynamic Programming Cost Evaluation (Target K to Source A)",
    size=(1140, 520),
    flow="H",
    containers=[
        N("s_s5", "Stage 5", 960, 70, 140, 380, "container"),
        N("s_s4", "Stage 4", 730, 70, 190, 380, "container"),
        N("s_s3", "Stage 3", 500, 70, 190, 380, "container"),
        N("s_s2", "Stage 2", 270, 70, 190, 380, "container"),
        N("s_s1", "Stage 1", 40, 70, 190, 380, "container"),
    ],
    nodes=[
        N("k_c", "K: Cost 0", 980, 230, 100, 60, "green", bold=True),
        N("h_c", "H: Cost 4", 750, 110, 150, 52, "blue"),
        N("i_c", "I: Cost 2", 750, 230, 150, 52, "green"),
        N("j_c", "J: Cost 5", 750, 350, 150, 52, "blue"),
        N("e_c", "E: Cost 7", 520, 110, 150, 52, "blue"),
        N("f_c", "F: Cost 5", 520, 230, 150, 52, "green"),
        N("g_c", "G: Cost 7", 520, 350, 150, 52, "blue"),
        N("b_c", "B: Cost 9", 290, 110, 150, 52, "blue"),
        N("c_c", "C: Cost 6", 290, 230, 150, 52, "green"),
        N("d_c", "D: Cost 11", 290, 350, 150, 52, "blue"),
        N("a_c", "A: Min Cost 13\nPath: A-C-F-I-K", 50, 215, 170, 80, "green", size=14, bold=True),
    ],
    edges=[
        E("k_c", "i_c", route="straight"), E("k_c", "h_c", route="straight"), E("k_c", "j_c", route="straight"),
        E("i_c", "f_c", route="straight"), E("h_c", "f_c", route="straight"),
        E("f_c", "c_c", route="straight"), E("c_c", "a_c", route="straight"),
    ],
    caption="Backward DP computes cost-to-go from destination back to source, guaranteeing optimal policy",
)

# 16 ---------------------------------------------------- tsp subset expansion
tsp_subset = D(
    key="ch8-16-tsp-subset-expansion",
    title="Traveling Salesperson Problem (TSP) Held-Karp Subset State Expansion",
    size=(1140, 480),
    flow="V",
    nodes=[
        N("start", "Start City 1\nFull Set S = {2, 3, 4}", 440, 60, 260, 60, "yellow", bold=True),
        N("c2", "Choose City 2\nCost: c(1,2) + g(2, {3,4})\n2 + 20 = 22", 80, 180, 290, 80, "blue"),
        N("c3", "Choose City 3\nCost: c(1,3) + g(3, {2,4})\n9 + 12 = 21", 425, 180, 290, 80, "green", bold=True),
        N("c4", "Choose City 4\nCost: c(1,4) + g(4, {2,3})\n10 + 20 = 30", 770, 180, 290, 80, "blue"),
        N("ans", "Minimum Tour Cost = 21\nOptimal sequence: 1 -> 3 -> 2 -> 4 -> 1\nSaves exponential time: O(n^2 * 2^n) vs O(n!) brute-force",
          200, 330, 740, 80, "green", bold=True),
    ],
    edges=[
        E("start", "c2"), E("start", "c3"), E("start", "c4"),
        E("c3", "ans", "optimal choice", color="#2f9e44"),
    ],
    caption="Held-Karp reduces TSP from factorial complexity to exponential complexity using bitmask dynamic programming",
)

# 17 ---------------------------------------------------- reliability design budget
reliability_budget = D(
    key="ch8-17-reliability-design-budget",
    title="Reliability Design Optimization under Cost Constraint (Budget B = 5)",
    size=(1140, 460),
    flow="H",
    nodes=[
        N("budget", "Total Budget\nB = $5", 40, 150, 160, 64, "blue", bold=True),
        N("c111", "Copies: (1, 1, 1)\nCost: $4 | Rel: 0.3360\nFeasible (leaves $1)", 260, 60, 250, 70, "blue", size=14),
        N("c112", "Copies: (1, 1, 2)\nCost: $5 | Rel: 0.4704\nFEASIBLE OPTIMUM!", 260, 150, 250, 70, "green", size=14, bold=True),
        N("c211", "Copies: (2, 1, 1)\nCost: $5 | Rel: 0.4032\nFeasible but suboptimal", 260, 240, 250, 70, "yellow", size=14),
        N("reject", "Other configurations\nCost > $5\nViolates Budget Constraint", 260, 330, 250, 70, "red", size=13),
        N("ans", "Selected Design: Copies (1, 1, 2)\nReliability R = 0.4704\nRedundancy at lowest-reliability stage\nmaximizes system survivability",
          570, 140, 520, 90, "green", size=13, bold=True),
    ],
    edges=[
        E("budget", "c111"), E("budget", "c112"), E("budget", "c211"), E("budget", "reject"),
        E("c112", "ans", "highest reliability", color="#2f9e44"),
    ],
    caption="Reliability DP maximizes product of stage reliabilities subject to total cost <= B",
)

DIAGRAMS = [
    dp_design,
    repeated_work,
    greedy_vs_dp,
    optimal_subpaths,
    dp_elements,
    topdown_vs_bottomup,
    stairs_dependencies,
    stairs_tree,
    knapsack_decision,
    rod_cutting,
    lcs_cell,
    matrix_chain,
    optimal_bst,
    multistage_graph,
    backward_flow,
    tsp_subset,
    reliability_budget,
]
