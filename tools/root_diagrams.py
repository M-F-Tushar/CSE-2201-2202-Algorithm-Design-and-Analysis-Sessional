"""Root README diagram specs -- Course Roadmap."""

from tools.excalidraw_gen import D, E, N

OUT = "diagrams"

roadmap = D(
    key="roadmap-01-course-overview",
    title="Algorithm Design and Analysis - Course Roadmap",
    size=(1140, 1020),
    flow="V",
    containers=[
        N("box_p1", "Phase 1: Foundations and Analysis", 80, 140, 980, 110, "container"),
        N("box_p2", "Phase 2: Basic Algorithms", 80, 290, 980, 110, "container"),
        N("box_p3", "Phase 3: Algorithm Design Paradigms", 40, 440, 1060, 110, "container"),
        N("box_p4", "Phase 4: Graph and Network Algorithms", 180, 590, 780, 110, "container"),
        N("box_p5", "Phase 5: Advanced Algorithmic Theory", 40, 740, 1060, 110, "container"),
    ],
    nodes=[
        N("start", "Start Journey", 445, 60, 250, 50, "gray", "ellipse", bold=True),
        # Phase 1
        N("c1", "Ch 1: Algorithm\nFoundations", 130, 175, 230, 56, "blue"),
        N("c2", "Ch 2: Complexity\nAnalysis", 455, 175, 230, 56, "blue"),
        N("c3", "Ch 3: Recurrences\n& Correctness", 780, 175, 230, 56, "blue"),
        # Phase 2
        N("c4", "Ch 4: Searching\n& Traversal", 130, 325, 230, 56, "teal"),
        N("c5", "Ch 5: Sorting\nAlgorithms", 455, 325, 230, 56, "teal"),
        N("c6", "Ch 6: Divide\n& Conquer", 780, 325, 230, 56, "teal"),
        # Phase 3
        N("c7", "Ch 7: Greedy\nAlgorithms", 60, 475, 220, 56, "yellow"),
        N("c8", "Ch 8: Dynamic\nProgramming", 330, 475, 220, 56, "yellow"),
        N("c9", "Ch 9: Backtracking", 590, 475, 220, 56, "yellow"),
        N("c10", "Ch 10: Branch\n& Bound", 850, 475, 220, 56, "yellow"),
        # Phase 4
        N("c11", "Ch 11: Graph\nAlgorithms", 260, 625, 270, 56, "violet"),
        N("c12", "Ch 12: Flow\nAlgorithms", 610, 625, 270, 56, "violet"),
        # Phase 5
        N("c13", "Ch 13: Approximation\nAlgorithms", 60, 775, 270, 56, "orange"),
        N("c14", "Ch 14: Randomized\n& Parallel", 390, 775, 270, 56, "orange"),
        N("c15", "Ch 15: Lower Bound\n& NP Completeness", 720, 775, 330, 56, "orange"),
        # End
        N("end", "Mastery Achieved", 435, 890, 270, 52, "green", "ellipse", bold=True),
    ],
    edges=[
        E("start", "c2", route="straight"),
        E("c1", "c2"), E("c2", "c3"),
        E("c3", "c5", route="v"),
        E("c4", "c5"), E("c5", "c6"),
        E("c6", "c8", route="v"),
        E("c7", "c8"), E("c8", "c9"), E("c9", "c10"),
        E("c9", "c11", route="v"),
        E("c11", "c12"),
        E("c12", "c14", route="v"),
        E("c13", "c14"), E("c14", "c15"),
        E("c14", "end", route="straight"),
    ],
    caption="Comprehensive curriculum map spanning algorithm foundations to advanced theory",
)

DIAGRAMS = [roadmap]
