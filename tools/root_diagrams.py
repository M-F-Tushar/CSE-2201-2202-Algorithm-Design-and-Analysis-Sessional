"""Root README diagram specs -- Course Roadmap."""

from tools.excalidraw_gen import D, E, N

OUT = "diagrams"

roadmap = D(
    key="roadmap-01-course-overview",
    title="Algorithm Design and Analysis - Course Roadmap",
    size=(1320, 1020),
    flow="V",
    containers=[
        N("box_p1", "Phase 1: Foundations and Analysis", 130, 140, 1060, 110, "container"),
        N("box_p2", "Phase 2: Basic Algorithms", 130, 290, 1060, 110, "container"),
        N("box_p3", "Phase 3: Algorithm Design Paradigms", 40, 440, 1240, 110, "container"),
        N("box_p4", "Phase 4: Graph and Network Algorithms", 270, 590, 780, 110, "container"),
        N("box_p5", "Phase 5: Advanced Theory & String Matching", 40, 740, 1240, 110, "container"),
    ],
    nodes=[
        N("start", "Start Journey", 535, 60, 250, 50, "gray", "ellipse", bold=True),
        # Phase 1
        N("c1", "Ch 1: Algorithm\nFoundations", 180, 175, 230, 56, "blue"),
        N("c2", "Ch 2: Complexity\nAnalysis", 545, 175, 230, 56, "blue"),
        N("c3", "Ch 3: Recurrences\n& Correctness", 910, 175, 230, 56, "blue"),
        # Phase 2
        N("c4", "Ch 4: Searching\n& Traversal", 180, 325, 230, 56, "teal"),
        N("c5", "Ch 5: Sorting\nAlgorithms", 545, 325, 230, 56, "teal"),
        N("c6", "Ch 6: Divide\n& Conquer", 910, 325, 230, 56, "teal"),
        # Phase 3
        N("c7", "Ch 7: Greedy\nAlgorithms", 60, 475, 220, 56, "yellow"),
        N("c8", "Ch 8: Dynamic\nProgramming", 330, 475, 220, 56, "yellow"),
        N("c9", "Ch 9: Backtracking", 600, 475, 220, 56, "yellow"),
        N("c10", "Ch 10: Branch\n& Bound", 870, 475, 220, 56, "yellow"),
        # Phase 4
        N("c11", "Ch 11: Graph\nAlgorithms", 350, 625, 270, 56, "violet"),
        N("c12", "Ch 12: Flow\nAlgorithms", 700, 625, 270, 56, "violet"),
        # Phase 5
        N("c13", "Ch 13: Approximation\nAlgorithms", 60, 775, 250, 56, "orange"),
        N("c14", "Ch 14: Randomized\n& Parallel", 340, 775, 240, 56, "orange"),
        N("c15", "Ch 15: Lower Bound\n& NP Completeness", 610, 775, 300, 56, "orange"),
        N("c16", "Ch 16: String Matching\n(Rabin-Karp)", 940, 775, 290, 56, "orange"),
        # End
        N("end", "Mastery Achieved", 525, 890, 270, 52, "green", "ellipse", bold=True),
    ],
    edges=[
        E("start", "c1", route="straight"),
        E("c1", "c2"), E("c2", "c3"),
        E("c3", "c4", route="v"),
        E("c4", "c5"), E("c5", "c6"),
        E("c6", "c7", route="v"),
        E("c7", "c8"), E("c8", "c9"), E("c9", "c10"),
        E("c10", "c11", route="v"),
        E("c11", "c12"),
        E("c12", "c13", route="v"),
        E("c13", "c14"), E("c14", "c15"), E("c15", "c16"),
        E("c16", "end", route="straight"),
    ],
    caption="Comprehensive curriculum map spanning algorithm foundations to advanced theory and string matching",
)

DIAGRAMS = [roadmap]
