from display import display_sudoku_solution
import random, sys
from SAT import SAT
from DPLL import DPLL

if __name__ == "__main__":
    # for testing, always initialize the pseudorandom number generator to output the same sequence
    #  of values:
    random.seed(1)

    puzzle_name = str(sys.argv[1][:-4])
    sol_filename = puzzle_name + ".sol"

    # DPLL
    #---------------
    dpll = DPLL(sys.argv[1])
    result = dpll.run_dpll()

    # SAT 
    #--------------- 
    sat = SAT(sys.argv[1])
    # result = sat.walksat()
    # result = sat.gsat()
    # result = sat.mod_walksat()

    if result:
        # sat.write_solution(sol_filename)
        dpll.write_solution(sol_filename)
        display_sudoku_solution(sol_filename)