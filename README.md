# Solving-Sudoku
This project is a Python-based Sudoku solver that reads an input file containing an incomplete Sudoku puzzle, processes the puzzle step by step, and outputs the solved puzzle along with the steps taken to reach the solution. The algorithm fills in empty cells based on possible values derived from the existing numbers in the row, column, and 3x3 grid. It utilizes a recursive approach to solve the puzzle efficiently.

Features
- Reads an input file containing a Sudoku puzzle
- Implements a recursive backtracking algorithm to solve the puzzle
- Generates a step-by-step output showing each change made
- Writes the final solution and steps to an output file

How It Works
Reading Input: The program reads the Sudoku puzzle from a text file and converts it into a 9x9 list.
Checking Possible Values: For each empty cell (zero), the program determines possible numbers based on existing values in the row, column, and 3x3 grid.
Recursive Solving: If a cell has only one possible value, it is filled in, and the process continues recursively until the puzzle is solved.
Recording Steps: Each step is recorded and saved in the output file, showing where and how changes were made.
Writing Output: The final solved Sudoku along with all steps is written to a text file.
