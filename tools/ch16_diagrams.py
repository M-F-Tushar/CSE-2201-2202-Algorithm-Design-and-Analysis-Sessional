"""Chapter 16 (String Matching Algorithms) diagram specs."""

from tools.excalidraw_gen import D, E, N

OUT = "Chapter 16 - String Matching Algorithms/diagrams"

# 1 ---------------------------------------------------- Naive vs Rabin-Karp Overview
naive_vs_rk = D(
    key="ch16-01-pattern-matching-naive-vs-rk",
    title="Pattern Matching: Naive Character Checking vs. Rabin-Karp Hash Matching",
    size=(1260, 570),
    flow="V",
    nodes=[
        N("problem", "Pattern Matching Problem\nText T of length n, Pattern P of length m\nCandidate Windows = n - m + 1", 410, 50, 440, 75, "yellow", "rect", 15, True),
        # Left: Naive
        N("naive_title", "Naive Approach: Character by Character", 80, 170, 480, 60, "red", "rect", 16, True),
        N("naive_desc", "• Compare P[0..m-1] with T[i..i+m-1] for every window\n• Up to m character comparisons per window\n• Total comparisons: (n - m + 1) * m\n• Worst-case Time Complexity: O(n * m)", 80, 250, 480, 110, "light", "rect", 14),
        N("naive_verdict", "Slow on large text & repetitive patterns\n(e.g., 'AAAAAB' inside 'AAAAAAAA...')", 80, 385, 480, 70, "red", "rect", 13),
        # Right: Rabin-Karp
        N("rk_title", "Rabin-Karp: Rolling Hash Matching", 700, 170, 480, 60, "green", "rect", 16, True),
        N("rk_desc", "• Convert Pattern P to integer patHash once in O(m)\n• Precompute prefix hashes hs[] in O(n)\n• Compare 1 integer hash per window in O(1)\n• Expected / Average Time: O(n + m)", 700, 250, 480, 110, "light", "rect", 14),
        N("rk_verdict", "Fast integer comparisons via\nmodular arithmetic & sliding window", 700, 385, 480, 70, "green", "rect", 13, True),
        # Summary footer
        N("summary", "Core Idea: Compare hash integers in O(1) instead of character strings", 280, 485, 700, 54, "teal", "ellipse", 15, True),
    ],
    edges=[
        E("problem", "naive_title", "naive check"),
        E("problem", "rk_title", "hash check"),
        E("naive_verdict", "summary", route="v"),
        E("rk_verdict", "summary", route="v"),
    ],
    caption="Rabin-Karp replaces m character comparisons per window with a single O(1) integer hash check.",
)

# 2 ---------------------------------------------------- ASCII Sum vs Polynomial Hash
ascii_vs_poly = D(
    key="ch16-02-ascii-vs-polynomial-hash",
    title="Hash Functions: Why ASCII Sum Fails vs. Why Polynomial Hash Succeeds",
    size=(1300, 580),
    flow="V",
    nodes=[
        # Left: ASCII Sum Hashing (Fails)
        N("ascii_head", "ASCII Sum Hashing (FAILS)", 60, 70, 560, 60, "red", "rect", 16, True),
        N("ascii_formula", "hash(s) = sum of ASCII values\nSymmetric function: ignores character order", 60, 150, 560, 70, "light", "rect", 14),
        N("ascii_ex1", "sum('aba') = 97 + 98 + 97 = 292\nsum('aab') = 97 + 97 + 98 = 292", 60, 245, 560, 70, "yellow", "rect", 14),
        N("ascii_ex2", "sum('abab') = 97 + 98 + 97 + 98 = 390\nsum('baba') = 98 + 97 + 98 + 97 = 390", 60, 340, 560, 70, "yellow", "rect", 14),
        N("ascii_fail", "Collision! Anagrams produce identical hashes!\nReports false matches where pattern does not exist.", 60, 435, 560, 65, "red", "rect", 14, True),
        # Right: Polynomial Rolling Hashing (Fixes it)
        N("poly_head", "Polynomial Rolling Hashing (FIX)", 680, 70, 560, 60, "green", "rect", 16, True),
        N("poly_formula", "hash(s) = s[0]*P^0 + s[1]*P^1 + ... + s[m-1]*P^(m-1) (mod M)\nAsymmetric: each position carries a distinct power weight P^i", 680, 150, 560, 70, "light", "rect", 14),
        N("poly_ex1", "Base 10: 'aba' = 1*10^0 + 2*10^1 + 1*10^2 = 121\nBase 10: 'aab' = 1*10^0 + 1*10^1 + 2*10^2 = 211", 680, 245, 560, 70, "blue", "rect", 14),
        N("poly_details", "Three Essential Engineering Rules:\n1. val(c) = c - 'a' + 1 (starts at 1, so 'a' != 'aa' != 'aaa')\n2. Base P = 31 (prime > 26, prevents collisions like 'ka' vs 'ab')\n3. Modulo M = 10^9 + 7 (large prime keeps numbers within long long)", 680, 340, 560, 110, "teal", "rect", 13),
        N("poly_success", "Success! Position-dependent weights eliminate anagram collisions.", 680, 475, 560, 55, "green", "rect", 14, True),
    ],
    edges=[
        E("ascii_formula", "ascii_ex1"),
        E("ascii_ex1", "ascii_ex2"),
        E("ascii_ex2", "ascii_fail"),
        E("poly_formula", "poly_ex1"),
        E("poly_ex1", "poly_details"),
        E("poly_details", "poly_success"),
    ],
    caption="Positional powers P^i ensure character ordering directly alters the resulting polynomial hash.",
)

# 3 ---------------------------------------------------- Prefix Hash Window Extraction
window_extraction = D(
    key="ch16-03-prefix-hash-window-extraction",
    title="Prefix Hash Array: O(1) Window Hash Extraction Formula",
    size=(1360, 620),
    flow="V",
    nodes=[
        # Text representation
        N("text_bar", "Text T:   a    b    a    b    c    a    b    a    b\nIndex i:  0    1    2    3    4    5    6    7    8", 220, 60, 920, 60, "dark", "rect", 15, True),
        # Prefix explanation
        N("hs_r", "hs[r] = sum of val(T[k]) * P^k for k in 0..r\n(Cumulative weighted hash up to window end r)", 140, 150, 480, 80, "blue", "rect", 14),
        N("hs_l", "hs[l-1] = sum of val(T[k]) * P^k for k in 0..l-1\n(Cumulative weighted hash before window start l)", 740, 150, 480, 80, "gray", "rect", 14),
        # Subtraction step
        N("sub_formula", "Subtract to remove unwanted left prefix:\nwindow_raw = hs[r] - hs[l-1]   (if l > 0; else hs[r])\n= P^l * (T[l]*P^0 + T[l+1]*P^1 + ... + T[r]*P^(m-1))\n= P^l * (hash of the window)", 330, 260, 700, 110, "violet", "rect", 15, True),
        # Multiplication vs division note
        N("mul_note", "Crucial Design Decision: Multiply, Never Divide!\n• Dividing window_raw by P^l causes precision loss and requires modular inverse.\n• Instead: multiply pattern hash by P^l (pw[l]):\n  winHash == (patHash * pw[l]) % MOD", 200, 400, 960, 90, "teal", "rect", 15, True),
        # C++ safety box
        N("cpp_safe", "C++ Modular Subtraction Safety Rule:\nwinHash = (hs[r] - hs[l-1] + MOD) % MOD\n(+ MOD prevents negative values resulting from % operator in C++)", 330, 515, 700, 65, "yellow", "rect", 14, True),
    ],
    edges=[
        E("text_bar", "hs_r"),
        E("text_bar", "hs_l"),
        E("hs_r", "sub_formula"),
        E("hs_l", "sub_formula"),
        E("sub_formula", "mul_note"),
        E("mul_note", "cpp_safe"),
    ],
    caption="Subtracting prefix hashes leaves the window weighted by P^l, matching patHash * P^l without division.",
)

# 4 ---------------------------------------------------- Full Dry Run
dry_run = D(
    key="ch16-04-sliding-window-dry-run",
    title="Rabin-Karp Sliding Window Trace: Text 'ababcabab' with Pattern 'cab'",
    size=(1380, 690),
    flow="V",
    nodes=[
        N("trace_head", "Sliding Window Execution Trace (Base P = 10, patHash('cab') = 213)\nCompare: winHash = (hs[r] - hs[l-1])   vs   target = (patHash * 10^i)", 210, 50, 960, 65, "dark", "rect", 15, True),
        # Steps
        N("w0", "i = 0 | 'aba' | [0..2]\nhs[2] = 121\ntarget = 213 * 10^0 = 213\n121 != 213 -> Mismatch", 60, 145, 380, 95, "yellow", "rect", 13),
        N("w1", "i = 1 | 'bab' | [1..3]\nhs[3] - hs[0] = 2121 - 1 = 2120\ntarget = 213 * 10^1 = 2130\n2120 != 2130 -> Mismatch", 500, 145, 380, 95, "yellow", "rect", 13),
        N("w2", "i = 2 | 'abc' | [2..4]\nhs[4] - hs[1] = 32121 - 21 = 32100\ntarget = 213 * 10^2 = 21300\n32100 != 21300 -> Mismatch", 940, 145, 380, 95, "yellow", "rect", 13),
        N("w3", "i = 3 | 'bca' | [3..5]\nhs[5] - hs[2] = 132121 - 121 = 132000\ntarget = 213 * 10^3 = 213000\n132000 != 213000 -> Mismatch", 60, 270, 380, 95, "yellow", "rect", 13),
        N("w4", "i = 4 | 'cab' | [4..6]\nhs[6] - hs[3] = 2132121 - 2121 = 2130000\ntarget = 213 * 10^4 = 2130000\n2130000 == 2130000 -> MATCH!", 500, 270, 380, 95, "green", "rect", 14, True),
        N("w5", "i = 5 | 'aba' | [5..7]\nhs[7] - hs[4] = 12100000\ntarget = 213 * 10^5 = 21300000\n12100000 != 21300000 -> Mismatch", 940, 270, 380, 95, "yellow", "rect", 13),
        N("w6", "i = 6 | 'bab' | [6..8]\nhs[8] - hs[5] = 212000000\ntarget = 213 * 10^6 = 213000000\n212000000 != 213000000 -> Mismatch", 500, 395, 380, 95, "yellow", "rect", 13),
        # Conclusion
        N("result", "Pattern 'cab' is found at Index 4 (text[4..6] == 'cab')\nSingle-match stops here. Multi-match variant records [4] and continues.", 290, 520, 800, 65, "teal", "rect", 14, True),
        N("zero_collision", "No false collisions possible here: max polynomial difference <= 25*(1 + 31 + 961) = 24,825 < 10^9 + 7", 240, 610, 900, 50, "light", "ellipse", 13),
    ],
    edges=[
        E("trace_head", "w0"),
        E("w0", "w1"),
        E("w1", "w2"),
        E("w2", "w3"),
        E("w3", "w4"),
        E("w4", "w5"),
        E("w5", "w6"),
        E("w6", "result", "scan complete"),
        E("result", "zero_collision"),
    ],
    caption="Dry run trace over all 7 windows: only window 4 matches the shifted pattern hash 2130000.",
)

DIAGRAMS = [naive_vs_rk, ascii_vs_poly, window_extraction, dry_run]
