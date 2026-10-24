"""Restore visuals for the earlier CT1 (DP) and CT2 (graph) answer sets.

Run from the repository root: python tools/ct_sequence_diagrams.py
"""
from __future__ import annotations

import json
from pathlib import Path

from excalidraw_gen import D, E, N, write

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Chapter 0 - Previous Year Questions/3rd Batch/CT/diagrams"
GREEN, GRAY = "#2f9e44", "#868e96"


def box(id, text, x, y, w=130, h=58, color="blue", size=15):
    return N(id, text, x, y, w, h, color, size=size)


def wt(id, text, cx, cy, color="gray"):
    return N(id, text, cx - 20, cy - 14, 40, 28, color, size=15)


def emit(scene):
    write(scene, OUT)
    path = OUT / (scene.key + ".excalidraw")
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {element["id"]: element for element in data["elements"]}
    for text in data["elements"]:
        if text["type"] != "text" or not text.get("containerId"):
            continue
        shape = by_id[text["containerId"]]
        text["height"] = len(text["text"].splitlines()) * text["fontSize"] * text["lineHeight"]
        text["y"] = shape["y"] + (shape["height"] - text["height"]) / 2
        assert text["height"] <= shape["height"] - 8, (scene.key, text["text"])
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def ct1_principle():
    positions = {"S": (110, 270), "A": (350, 120), "B": (580, 270), "T": (820, 270)}
    best_cost = {"S": 6, "A": 4, "B": 3, "T": 0}
    nodes = [box(v, f"{v}\nbest to T: {best_cost[v]}", x - 70, y - 30,
                 140, 60, "green") for v, (x, y) in positions.items()]
    edges_and_weights = [("S", "A", 2, GREEN), ("S", "B", 5, GRAY), ("A", "B", 1, GREEN),
                         ("A", "T", 7, GRAY), ("B", "T", 3, GREEN)]
    edges = []
    for i, (u, v, w, color) in enumerate(edges_and_weights):
        x1, y1 = positions[u]
        x2, y2 = positions[v]
        nodes.append(wt(f"w{i}", str(w), (x1+x2)/2, (y1+y2)/2, "green" if color == GREEN else "gray"))
        edges.append(E(u, v, color=color, route="straight"))
    nodes.append(box("note", "Optimal S→T route: S→A→B→T, cost 6. Its suffix A→B→T costs 4,\n"
                              "which is better than direct A→T (7): an optimal route contains optimal parts.",
                     50, 420, 900, 68, "yellow", 15))
    return D("ct1-01-principle-optimality", "CT1 Q1: Principle of Optimality", (1000, 520), nodes, edges)


def ct1_fib_tree():
    # One node per call in the naive F(5) recursion tree: 15 total calls.
    labels = [
        ("F5", "F(5)", 500, 85, "blue"),
        ("F4", "F(4)", 300, 185, "blue"), ("F3a", "F(3)", 700, 185, "yellow"),
        ("F3b", "F(3)", 200, 285, "yellow"), ("F2a", "F(2)", 400, 285, "orange"),
        ("F2b", "F(2)", 600, 285, "orange"), ("F1a", "F(1)", 800, 285, "red"),
        ("F2c", "F(2)", 100, 385, "orange"), ("F1b", "F(1)", 300, 385, "red"),
        ("F1c", "F(1)", 400, 385, "red"), ("F0a", "F(0)", 500, 385, "orange"),
        ("F1d", "F(1)", 600, 385, "red"), ("F0b", "F(0)", 700, 385, "orange"),
        ("F1f", "F(1)", 60, 485, "red"), ("F0c", "F(0)", 140, 485, "orange"),
    ]
    nodes = [box(i, label, x - 40, y, 80, 48, c, 14) for i, label, x, y, c in labels]
    pairs = [("F5","F4"),("F5","F3a"),("F4","F3b"),("F4","F2a"),("F3a","F2b"),("F3a","F1a"),
             ("F3b","F2c"),("F3b","F1b"),("F2a","F1c"),("F2a","F0a"),("F2b","F1d"),("F2b","F0b"),
             ("F2c","F1f"),("F2c","F0c")]
    edges = [E(a,b,route="straight") for a,b in pairs]
    nodes.append(box("note", "15 calls total: F(3) twice; F(2) three times; F(1) five times; F(0) three times.",
                     60, 565, 880, 52, "gray", 15))
    return D("ct1-02-fib-recursion", "CT1 Q2: Repeated calls in naive F(5)", (1000, 650), nodes, edges)


def ct1_fib_table():
    vals = [0, 1, 1, 2, 3, 5]
    nodes = [box(f"i{i}", f"i = {i}", 45 + 165*i, 100, 125, 42, "gray", 15) for i in range(6)]
    nodes += [box(f"f{i}", f"F({i}) = {v}", 45 + 165*i, 170, 125, 58,
                  "blue" if i < 2 else "green", 16) for i,v in enumerate(vals)]
    formulas = ["base", "base", "F(1)+F(0)", "F(2)+F(1)", "F(3)+F(2)", "F(4)+F(3)"]
    nodes += [box(f"rule{i}", formulas[i], 45 + 165*i, 270, 125, 52, "yellow", 13) for i in range(6)]
    nodes.append(box("note", "Store each value once: Θ(n) time. Keeping only the previous two values uses Θ(1) space.",
                     45, 380, 950, 55, "teal", 15))
    edges = [E(f"f{i-1}", f"f{i}", route="h") for i in range(1,6)]
    return D("ct1-03-fib-table", "CT1 Q2: Bottom-up Fibonacci table", (1040, 455), nodes, edges)


def ct1_lcs():
    x, y = "AGGTAB", "GXTXAYB"
    dp = [[0]*(len(y)+1) for _ in range(len(x)+1)]
    for i, a in enumerate(x,1):
        for j, b in enumerate(y,1):
            dp[i][j] = dp[i-1][j-1]+1 if a==b else max(dp[i-1][j],dp[i][j-1])
    selected = {(1,5),(2,1),(3,1),(4,3),(5,5),(6,7)}
    nodes = [box(f"hy{j}", c, 100+j*66, 72, 60, 42, "light", 16) for j,c in enumerate(y,1)]
    nodes += [box(f"hx{i}", c, 34, 124+i*52, 60, 46, "light", 16) for i,c in enumerate(x,1)]
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            color = "green" if (i,j) in selected else "gray"
            nodes.append(box(f"c{i}_{j}", str(dp[i][j]), 100+j*66, 124+i*52, 60, 46, color, 15))
    nodes.append(box("answer", "LCS = GTAB; length = 4", 120, 535, 500, 50, "yellow", 16))
    return D("ct1-04-lcs", "CT1 Q3: LCS table for AGGTAB and GXTXAYB", (700, 610), nodes)


def ct1_knapsack():
    weights, profits, cap = [3,4,5,6], [2,3,1,4], 8
    dp = [[0]*(cap+1) for _ in range(len(weights)+1)]
    for i,(w,p) in enumerate(zip(weights,profits),1):
        for c in range(cap+1):
            dp[i][c] = max(dp[i-1][c],dp[i-1][c-w]+p) if c>=w else dp[i-1][c]
    names = ["none"]+[f"item {i} (w={w}, p={p})" for i,(w,p) in enumerate(zip(weights,profits),1)]
    nodes = [box(f"h{c}", str(c), 220+c*66, 70, 62, 40, "light", 15) for c in range(cap+1)]
    for i,name in enumerate(names):
        nodes.append(box(f"r{i}",name,25,70+(i+1)*52,185,46,"light",13))
        for c,v in enumerate(dp[i]):
            color = "green" if (i,c) in {(1,4),(2,8)} else "gray"
            nodes.append(box(f"c{i}_{c}",str(v),220+c*66,70+(i+1)*52,62,46,color,15))
    nodes.append(box("answer","Illustrative: W=8; maximum profit 5; take items 1 and 2.",
                     35,410,760,52,"yellow",15))
    return D("ct1-05-knapsack", "CT1 Q4: 0/1 knapsack DP table", (820, 470), nodes)


def ct2_topological():
    coords = {"4":(140,120),"5":(450,120),"6":(140,280),"2":(450,280),"3":(450,435),"1":(140,435)}
    order = {"4":1,"5":2,"6":3,"2":4,"3":5,"1":6}
    nodes = [box(v,f"{v}\nposition {order[v]}",x,y,120,58,"green" if v in "45" else "blue",14)
             for v,(x,y) in coords.items()]
    edges = [E("4","6",route="v"),
             E("5","6",pts=[(510,178),(510,225),(200,225),(200,280)]),
             E("5","2",route="v"),
             E("4","1",pts=[(140,149),(90,149),(90,464),(140,464)]),
             E("2","3",route="v"), E("3","1",route="h")]
    nodes.append(box("answer","One valid order: 4, 5, 6, 2, 3, 1",590,200,350,65,"green",16))
    nodes.append(box("note","Edges: 5→6, 4→6, 5→2, 4→1, 2→3, 3→1",590,300,350,70,"gray",14))
    return D("ct2-01-topological", "CT2 Q1: Topological order of the DAG", (980, 540), nodes, edges)


def ct2_bellman_ford():
    coords = {"S":(90,280),"A":(310,120),"C":(310,430),"B":(550,120),"D":(550,430),"T":(790,280)}
    distances = {"S":0,"A":0,"B":1,"C":-2,"D":0,"T":1}
    nodes = [box(v,f"{v}\nd={distances[v]}",x-50,y-28,100,56,"green",15) for v,(x,y) in coords.items()]
    edge_data = [("S","A",5),("S","C",-2),("A","B",1),("C","A",2),("C","B",4),
                 ("C","D",4),("B","D",-1),("B","T",3),("D","T",1)]
    path = {("S","C"),("C","A"),("A","B"),("B","D"),("D","T")}
    edges=[]
    for i,(u,v,w) in enumerate(edge_data):
        x1,y1=coords[u];x2,y2=coords[v]; active=(u,v) in path
        nodes.append(wt(f"w{i}",str(w), (x1+x2)/2, (y1+y2)/2,"green" if active else "gray"))
        edges.append(E(u,v,color=GREEN if active else GRAY,route="straight"))
    nodes.append(box("answer","Shortest path: S→C→A→B→D→T; cost = −2+2+1−1+1 = 1.",
                     50,540,840,58,"yellow",15))
    return D("ct2-02-bellman-ford", "CT2 Q2: Bellman–Ford shortest path from S to T", (940, 635), nodes, edges)


def ct2_floyd():
    coords={"1":(130,110),"2":(470,110),"3":(470,365),"4":(130,365)}
    nodes=[box(v,v,x,y,100,56,"blue",18) for v,(x,y) in coords.items()]
    labels=[("1","2",2,(300,108)),("2","3",3,(500,238)),("3","4",1,(300,348)),
            ("4","3",12,(300,390)),("1","4",5,(108,238)),("4","1",4,(245,238)),
            ("3","1",6,(415,285)),("4","2",7,(300,285))]
    edges=[]
    for i,(u,v,w,(lx,ly)) in enumerate(labels):
        nodes.append(wt(f"w{i}",str(w),lx,ly))
        pts=None
        if (u,v)==("3","4"): pts=[(470.0,393.0),(230.0,393.0)]
        elif (u,v)==("4","3"): pts=[(230.0,423.0),(470.0,423.0)]
        elif (u,v)==("1","4"): pts=[(155.0,166.0),(155.0,365.0)]
        elif (u,v)==("4","1"): pts=[(205.0,365.0),(205.0,166.0)]
        if pts is None:
            edges.append(E(u,v,route="straight"))
        else:
            edges.append(E(u,v,route="straight",pts=pts))
    nodes.append(box("note","Assumed diagonals: 3→1 = 6, 4→2 = 7. Check these labels against the scan.",
                     30,475,650,55,"yellow",14))
    return D("ct2-03-floyd-warshall", "CT2 Q3: Graph used for Floyd–Warshall", (700, 555), nodes, edges)


def main():
    scenes=[ct1_principle(),ct1_fib_tree(),ct1_fib_table(),ct1_lcs(),ct1_knapsack(),
            ct2_topological(),ct2_bellman_ford(),ct2_floyd()]
    for scene in scenes:
        emit(scene)
    print(f"Wrote {len(scenes)} restored CT1/CT2 diagram pairs to {OUT}")


if __name__ == "__main__":
    main()
