# Contributing to Algorithm Design and Analysis (CSE 2201/2202)

Thank you for your interest in improving this educational repository! We welcome contributions ranging from typo fixes and diagram improvements to code corrections and additional practice solutions.

---

## Code of Conduct & Academic Integrity

- This repository is designed as an educational reference for students studying Algorithm Design and Analysis.
- Ensure all contributions follow clean code standards, include explanatory comments, and respect academic integrity guidelines.

---

## How to Contribute

### 1. Reporting Issues
- Check existing issues and pull requests to ensure your observation has not already been reported.
- When reporting an error in an algorithm trace or mathematical proof, please cite the exact chapter, section, and line number along with a step-by-step mathematical derivation.

### 2. Making Changes
1. **Fork** the repository and create your feature branch:
   ```bash
   git checkout -b feature/topic-improvement
   ```
2. **Implement changes** following the repository structure:
   - Theory answers and lecture notes belong in `Chapter X - .../README.md`.
   - Previous year questions belong in `Chapter 0 - Previous Year Questions/`.
   - C++ implementations belong in the respective `Lab Practice/` or `examples/` folders.
   - Diagram generation scripts belong in `tools/`.
3. **Verify all tests pass**:
   ```bash
   python3 tools/verify_b1_theory.py
   python3 tools/verify_b2_theory.py
   python3 tools/verify_ct3.py
   python3 tools/verify_ct4.py
   python3 tools/audit_layout.py
   ```

### 3. Diagram Guidelines
- Diagrams are maintained as paired `.excalidraw` (source of truth) and `.svg` (rendered output) files.
- If modifying a diagram, edit the corresponding `.excalidraw` file and regenerate or re-export the matching `.svg` file.

### 4. Code Standards
- **C++:** Use standard C++17. Ensure code compiles cleanly with `-Wall -Wextra`. Pass containers by const reference (`const vector<int>&`) when read-only to avoid accidental $O(n)$ copying.
- **Python:** Use standard Python 3.8+ style with clear docstrings and unittests.

---

## Submitting Pull Requests

1. Commit your changes with clear, descriptive commit messages.
2. Push your branch to your GitHub fork.
3. Open a Pull Request against the `main` branch with a concise summary of the changes made and tests performed.
