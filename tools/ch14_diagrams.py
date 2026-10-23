"""Chapter 14 (Randomized and Parallel Algorithms) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 14 - Randomized and Parallel Algorithms/diagrams"

S = "straight"
RED = "#e03131"

# 1 ---------------------------------------------------- Las Vegas vs Monte Carlo
kinds = D(
    key="ch14-01-las-vegas-vs-monte-carlo",
    title="Two Kinds of Randomized Algorithms",
    size=(1060, 420),
    flow="V",
    nodes=[
        N("root", "Randomized algorithm\nmakes random choices while running", 330, 70, 400, 70, "yellow", "rect", 16, True),
        N("lv", "Las Vegas\nalways returns the correct answer\nrunning time is a random variable\nExample: randomized quicksort", 60, 230, 420, 110, "green", "rect", 15),
        N("mc", "Monte Carlo\nfixed running time\nanswer may be wrong with small probability\nExample: Miller-Rabin primality test", 580, 230, 420, 110, "blue", "rect", 15),
    ],
    edges=[
        E("root", "lv"),
        E("root", "mc"),
    ],
    caption="This chapter analyzes Las Vegas algorithms: correctness is certain, only the expected running time is probabilistic",
)

# 2 ---------------------------------------------------- pivot quality
pivot = D(
    key="ch14-02-random-pivot-quality",
    title="Random Pivot: Good and Bad Ranks",
    size=(1080, 380),
    flow="V",
    nodes=[
        N("lo", "Pivot rank in the\nlowest quarter\nprobability 1/4 (bad)", 40, 80, 240, 90, "red", "rect", 14),
        N("mid", "Pivot rank in the middle half\nprobability 1/2 (good)\nboth sides have at most 3n/4 elements", 290, 80, 490, 90, "green", "rect", 15, True),
        N("hi", "Pivot rank in the\nhighest quarter\nprobability 1/4 (bad)", 790, 80, 240, 90, "red", "rect", 14),
        N("res", "A good pivot appears in 2 tries on average, so the sizes shrink geometrically:\nrecursion depth is O(log n) and expected comparisons are about 2 n ln n", 140, 240, 800, 80, "violet", "rect", 14),
    ],
    edges=[
        E("mid", "res"),
    ],
    caption="Random pivot choice means no fixed input (sorted, reversed, ...) can force the worst case",
)

# 3 ---------------------------------------------------- fork-join merge sort
forkjoin = D(
    key="ch14-03-fork-join-merge-sort",
    title="Fork-Join View of Parallel Merge Sort",
    size=(900, 600),
    flow="V",
    nodes=[
        N("top", "P-MERGE-SORT(A, p, r)\ncompute midpoint q", 330, 70, 260, 70, "yellow", "rect", 15, True),
        N("left", "spawn\nsort left half A[p..q]", 120, 210, 280, 70, "green", "rect", 15),
        N("right", "call (same thread)\nsort right half A[q+1..r]", 520, 210, 280, 70, "blue", "rect", 15),
        N("sync", "sync\nwait for the spawned child", 330, 350, 260, 70, "yellow", "rect", 15, True),
        N("merge", "MERGE the two sorted halves", 330, 480, 260, 64, "violet", "rect", 15),
    ],
    edges=[
        E("top", "left", "spawn"),
        E("top", "right", "continue"),
        E("left", "sync"),
        E("right", "sync"),
        E("sync", "merge"),
    ],
    caption="The two recursive sorts may run at the same time; sync is the join point before the merge",
)

# 4 ---------------------------------------------------- work and span DAG
dag = D(
    key="ch14-04-work-and-span-dag",
    title="Computation DAG: Work = 7, Span = 5",
    size=(830, 540),
    flow="H",
    nodes=[
        N("n1", "1", 40, 190, 70, 56, "red", "ellipse", 16, True),
        N("n2", "2", 200, 90, 70, 56, "red", "ellipse", 16, True),
        N("n3", "3", 200, 290, 70, 56, "blue", "ellipse", 16),
        N("n4", "4", 370, 190, 70, 56, "red", "ellipse", 16, True),
        N("n5", "5", 540, 90, 70, 56, "red", "ellipse", 16, True),
        N("n6", "6", 540, 290, 70, 56, "blue", "ellipse", 16),
        N("n7", "7", 710, 190, 70, 56, "red", "ellipse", 16, True),
        N("note", "Work T1 = total unit-time nodes = 7\nSpan T-infinity = longest path 1-2-4-5-7 = 5 nodes\nParallelism = T1 / T-infinity = 7/5 = 1.4", 160, 410, 520, 80, "gray", "rect", 14),
    ],
    edges=[
        E("n1", "n2", route=S, color=RED),
        E("n1", "n3", route=S),
        E("n2", "n4", route=S, color=RED),
        E("n3", "n4", route=S),
        E("n4", "n5", route=S, color=RED),
        E("n4", "n6", route=S),
        E("n5", "n7", route=S, color=RED),
        E("n6", "n7", route=S),
    ],
    caption="Red nodes and edges form the critical path (the span); each node takes one unit of time",
)

# 5 ---------------------------------------------------- randomized select shrink
select = D(
    key="ch14-05-randomized-select-shrink",
    title="Randomized Selection: Expected Linear Time",
    size=(1110, 440),
    flow="H",
    nodes=[
        N("s0", "n elements\nwork c n", 30, 145, 200, 130, "blue", "rect", 15),
        N("s1", "at most 3n/4\nwork (3/4) c n", 270, 160, 200, 100, "blue", "rect", 15),
        N("s2", "at most 9n/16\nwork (9/16) c n", 510, 172, 200, 76, "blue", "rect", 15),
        N("s3", "at most 27n/64\nwork (27/64) c n", 750, 181, 200, 58, "blue", "rect", 14),
        N("s4", "...\n1", 990, 175, 80, 70, "green", "ellipse", 15, True),
        N("note", "Only one side of the partition is searched. Work per round: c n (1 + 3/4 + 9/16 + ...) <= 4 c n.\nA good pivot takes 2 tries on average, so E[T(n)] <= 8 c n = O(n)", 90, 320, 860, 76, "gray", "rect", 14),
    ],
    edges=[
        E("s0", "s1", "good pivot"),
        E("s1", "s2"),
        E("s2", "s3"),
        E("s3", "s4"),
    ],
    caption="Unlike quicksort, selection recurses into one side only, which turns n log n into n",
)

DIAGRAMS = [kinds, pivot, forkjoin, dag, select]
