"""Chapter 1 (Introduction and Algorithm Foundations) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 1 - Introduction and Algorithm Foundations/diagrams"

# 1 ---------------------------------------------------- algorithm vs program
algorithm_vs_program = D(
    key="ch1-01-algorithm-vs-program",
    title="Algorithm vs Program - From Problem to Output",
    size=(1100, 270),
    flow="H",
    nodes=[
        N("problem", "Problem Statement\nGCD of a and b", 40, 80, 200, 72, "gray", bold=True),
        N("algo", "Algorithm\nsteps in pseudocode", 300, 80, 200, 72, "blue"),
        N("prog", "Program\nC / Python code", 560, 80, 200, 72, "teal"),
        N("out", "Output\nfor the input", 820, 80, 200, 72, "green"),
        N("note", "A program may run forever (e.g. an OS); an algorithm must always stop",
          150, 190, 800, 44, "dark", size=14, bold=True),
    ],
    edges=[
        E("problem", "algo", "design"),
        E("algo", "prog", "implement"),
        E("prog", "out", "run"),
    ],
    caption="A program is one concrete implementation of an algorithm; the same algorithm can be written in many languages",
)

# 2 ---------------------------------------------------- five properties
algorithm_properties = D(
    key="ch1-02-algorithm-properties",
    title="Five Properties of a Valid Algorithm",
    size=(1020, 300),
    flow="V",
    nodes=[
        N("hub", "A valid algorithm satisfies all five", 300, 50, 420, 52, "green", bold=True),
        N("inp", "Input\n0 or more inputs", 32, 170, 180, 64, "blue", size=14),
        N("out", "Output\n1 or more outputs", 226, 170, 180, 64, "blue", size=14),
        N("def", "Definiteness\nno ambiguous steps", 420, 170, 180, 64, "yellow", size=14),
        N("fin", "Finiteness\nends in finite steps", 614, 170, 180, 64, "yellow", size=14),
        N("eff", "Effectiveness\nbasic, doable steps", 808, 170, 180, 64, "yellow", size=14),
    ],
    edges=[
        E("hub", "inp"),
        E("hub", "out"),
        E("hub", "def"),
        E("hub", "fin"),
        E("hub", "eff"),
    ],
    caption="Input and output define the interface; definiteness, finiteness, and effectiveness make the steps valid",
)

DIAGRAMS = [algorithm_vs_program, algorithm_properties]
