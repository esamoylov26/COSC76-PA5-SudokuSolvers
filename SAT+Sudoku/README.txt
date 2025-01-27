SAT+Sudoku is the original submission for COSC 76 Fall 2024. It contains the SAT file and DPLL file to solve Sudoku. 
DPLL contains my attempts to add propogation to DPLL to speed it up.

Both folders also contains various Sudoku puzzles (provided by COSC 76) and some scaffolding to 
generate Sudoku puzzles and read them (provided by COSC 76).


IMPORTANT FILES: 
--------------------------
solve_sudoku.py = edit file/run in terminal to run DPLL, WalkSAT, and GSAT 

RUN> python solve_sudoku.py sample_puzzle.cnf 

SAT.py = class file for SAT object; has WalkSAT and GSAT algorithm implementations
DPLL.py = class file for DPLL object; has DPLL algorithm implementation 

LESS IMPORTANT FILES:
--------------------------
HELPER.py = has helper functions for SAT and DPLL 
DPLL_HELPER.py = has DPLL helper functions 
READFILE.py = has helper func to read .cnf file and return clauses and variables 

PROVIDED FILES: 
----------------------------
solve_sudoku.py
Sudoku.py = contains sudoku-related helper functions
display.py = contains function to print a sudoku board in the terminal
Sudoku2cnf.py = given a 9x9 Sudoku grid, generates a .cnf file 
