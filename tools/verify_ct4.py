"""Verify the CT4 N-Queens answers, examples, diagrams, and local links.

Run from the repository root: python tools/verify_ct4.py
Uses only the Python standard library.
"""
from __future__ import annotations

import json
import re
import unittest
import xml.etree.ElementTree as ET
from html import unescape
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CT = ROOT / "Chapter 0 - Previous Year Questions/3rd Batch/CT"
DIAGRAM_KEYS = [
    "ct4-01-state-space-tree",
    "ct4-02-queen-constraints",
    "ct4-03-backtracking-applications",
    "ct4-04-nqueens-algorithm",
]
QUESTIONS = [
    "What is a state space tree? Explain its role in backtracking. (4 marks)",
    "State the constraints required to ensure that no two queens attack each other. (4 marks)",
    "State two applications of backtracking other than the n-queen problem. (2 marks)",
    "Write a backtracking algorithm to solve the n-queen problem for a given value of n. (10 marks)",
]


def valid_placement(columns):
    for row, col in enumerate(columns):
        for previous_row, previous_col in enumerate(columns[:row]):
            if col == previous_col:
                return False
            if abs(col - previous_col) == row - previous_row:
                return False
    return True


def solve_n_queens(n):
    columns = [-1] * n

    def place(row):
        if row == n:
            return True
        for col in range(n):
            if all(columns[previous] != col
                   and abs(columns[previous] - col) != row - previous
                   for previous in range(row)):
                columns[row] = col
                if place(row + 1):
                    return True
                columns[row] = 0
        return False

    return tuple(columns) if place(0) else None


def enumerate_n_queens(n):
    columns, solutions = [-1] * n, []

    def place(row):
        if row == n:
            solutions.append(tuple(columns))
            return
        for col in range(n):
            if all(columns[previous] != col
                   and abs(columns[previous] - col) != row - previous
                   for previous in range(row)):
                columns[row] = col
                place(row + 1)
                columns[row] = 0

    place(0)
    return solutions


class VerifyCT4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (CT / "README.md").read_text(encoding="utf-8")
        cls.section = cls.text.split("## Class Test 4:", 1)[1].split("## Verification", 1)[0]

    def test_paper_transcription_and_marks(self):
        headings = re.findall(r"(?m)^### (Q\d)\.", self.section)
        self.assertEqual(headings, ["Q1", "Q2", "Q3", "Q4"])
        for question in QUESTIONS:
            self.assertIn(f"**Question (transcribed):** {question}", self.section)
        marks = [int(value) for value in re.findall(r"\((\d+) marks\)", self.section)]
        self.assertEqual(marks, [4, 4, 2, 10])
        self.assertEqual(sum(marks), 20)
        self.assertIn("CSE 2201 - CT - 4.pdf", self.text)

    def test_q4_algorithm_follows_board_code_in_instruction_style(self):
        q4 = self.section.split("### Q4.", 1)[1].lower()
        for phrase in [
            "instruction-style",
            "board[n][n]",
            "issafe(row, col)",
            "board[i][col]",
            "upper-right diagonal",
            "upper-left diagonal",
            "solve(row + 1)",
            "board[row][col] ← 1",
            "board[row][col] ← 0",
            "solve(0)",
            "no solution",
        ]:
            self.assertIn(phrase, q4, phrase)

    def test_n_queens_constraints_and_solutions(self):
        self.assertIn("one queen in each row", self.section.lower())
        self.assertIn("upper-right diagonal", self.section.lower())
        self.assertIn("upper-left diagonal", self.section.lower())
        self.assertTrue(valid_placement((1, 3, 0, 2)))
        self.assertFalse(valid_placement((0, 0)))
        self.assertFalse(valid_placement((0, 1)))
        self.assertEqual(solve_n_queens(1), (0,))
        self.assertIsNone(solve_n_queens(2))
        self.assertIsNone(solve_n_queens(3))
        self.assertEqual(solve_n_queens(4), (1, 3, 0, 2))
        self.assertEqual(set(enumerate_n_queens(4)), {(1, 3, 0, 2), (2, 0, 3, 1)})
        self.assertIn("O(n · n!)", self.section)
        self.assertIn("Θ(n²)", self.section)
        self.assertIn("Θ(n)", self.section)

    def test_diagram_pairs_and_local_links(self):
        for target in re.findall(r"\]\(([^)]+)\)", self.section):
            if target.startswith(("http://", "https://", "#")):
                continue
            path = unquote(urlsplit(target).path)
            self.assertTrue((CT / path).resolve().exists(), target)

        for key in DIAGRAM_KEYS:
            svg = CT / "diagrams" / f"{key}.svg"
            source = svg.with_suffix(".excalidraw")
            self.assertIn(f"diagrams/{key}.svg", self.section)
            self.assertTrue(svg.is_file(), key)
            self.assertTrue(source.is_file(), key)
            self.assertGreater(svg.stat().st_size, 1000, key)
            scene = json.loads(source.read_text(encoding="utf-8"))
            self.assertGreater(len(scene["elements"]), 0, key)
            self.assertIn(f"{key}.svg", (CT / "diagrams/README.md").read_text(encoding="utf-8"))

        self.assertEqual(len(list((CT / "diagrams").glob("*.svg"))), 15)

    def test_diagram_content_matches_answers(self):
        expected = {
            DIAGRAM_KEYS[0]: ["state-space tree", "items w₁ = 2, w₂ = 3", "target s = 3", "prune"],
            DIAGRAM_KEYS[1]: ["x-axis: column c (0..6)", "upper-right", "upper-left", "board[4][3]"],
            DIAGRAM_KEYS[2]: ["Graph coloring", "Subset sum", "sum = 9 = target", "sum = 12 > 9"],
            DIAGRAM_KEYS[3]: ["Backtracking algorithm", "instruction-style", "Read n", "isSafe(row, col)", "upper-right", "upper-left", "solve(row + 1)", "board[row][col] ← 0", "[1, 3, 0, 2]", "O(n·n!)"],
        }
        for key, phrases in expected.items():
            svg = ET.parse(CT / "diagrams" / f"{key}.svg").getroot()
            text = unescape(" ".join(svg.itertext())).lower()
            for phrase in phrases:
                self.assertIn(phrase.lower(), text, (key, phrase))


if __name__ == "__main__":
    unittest.main(verbosity=2)
