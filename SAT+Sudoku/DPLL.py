# CS76; Lisa Samoylov; 11/17/24
# DPLL solver class for the solve_sudoku.py
# Contains DPLL Class 

import random
# from HELPER import * 
from NEW_HELPER import *
from DPLL_HELPER import *
from READFILE import READFILE 

class DPLL(): 
    # CONSTRUCTOR 
    #=================================
    # INPUT: STR puzzlename = FILENAME 
    #----------------------------------
    def __init__(self, puzzlename): 
        self.puzzlename = puzzlename # puzzlefile with the cnfs 
        self.clauses, self.var_dict = READFILE(puzzlename) 
        self.variables = list(self.var_dict.keys())
        self.assignment = "No assignment made ;)"
        # print("MADE DPLL: ")
        # print("CLAUSES: \n", self.clauses) 
        # print("==============")
        # print("assignment: \n", self.assignment) 
        # print("==============")


    # DPLL ALGORITHM (following AIMA)
    #==================================
    # DPLL SHELL
    def run_dpll(self): # looks for assignment T/F that satisfies all vars 
        clauses = self.clauses 
        symbols = self.variables.copy() # !!! don't want DPLL to mess with class attribute
        assignment  = dict()
        # print("RUNNING DPLL CLAUSES:", clauses)
        # print(clauses)

        return self.dpll_helper(clauses, symbols, assignment, depth = 0)

    # DPLL RECURSIVE HELPER 
    def dpll_helper(self, clauses, symbols, assignment, depth): 

        # 0. PRINT DEBUGGING 
        print("===========================")
        print("INSIDE DPLL_HELPER") 
        print("DEPTH: ", depth)
        # print("ASSIGNMENT: ", assignment)
        # print("#ASSIGNED_VAR: ", len(assignment))
        # print("ASSIGNMENT: ", assignment)
        # print("CLAUSES: ", clauses)
        
        # 1.a FOUND GOOD ASSIGNMENT \(*v*)/
        # if len(assignment) == 729: print("REACHED END: ", assignment)
        if ALL_CLAUSES_SATISFIED(clauses, symbols, assignment):
            self.assignment = assignment # saving the assignment 
            return True
        
        # 1.b UNSATISFIED CLAUSE? /(*.*)\
        if len(FALSE_CLAUSES(clauses, assignment)) >= 1: return False

        # print("MADE IT PAST UNSAT CLAUSES")
        # 2. CHECKING PURE SYMBOLS 
        P, value = FIND_PURE_SYMBOL(self.variables, clauses, assignment)

        # update the assignment if found a pure symbol 
        if P != None: 
            symbols.remove(P) # !!! 
            assignment[P] = value
            return self.dpll_helper(symbols, clauses, assignment, depth = depth + 1) 
    
        # 3. CHECKING FOR UNIT CLAUSES 
        P, value = FIND_UNIT_CLAUSE(clauses, assignment)
        if P != None: 
            symbols.remove(P) # !!!
            assignment[P] = value 
            return self.dpll_helper(symbols, clauses, assignment, depth = depth + 1)
        # print("LEVEL: ", len(assignment))
        # print("SYMBOLS: ", symbols)
        # print("---")
        
        # 4. GRABBING FIRST UNASSIGNED SYMBOL
        P = symbols.pop()

        # making cases where P = True or False 
        true_assignment = assignment.copy()
        remaining_t_symbols = symbols.copy() # clean copy in case dpll messes with it
        true_assignment[P] = True 
        # print("TRUE ASSIGNMENT: ", true_assignment)

        false_assignment = assignment.copy()
        remaining_f_symbols = symbols.copy() # clean copy ""
        false_assignment[P] = False 
        # print("FALSE ASSIGNMENT: ", false_assignment)

        # print("CURRENT CLAUSES: ", clauses)

        return self.dpll_helper(clauses, remaining_t_symbols, true_assignment, depth = depth + 1) or\
              self.dpll_helper(clauses, remaining_f_symbols,false_assignment, depth = depth + 1)
    
    # WRITE SOLUTION 
    #=========================
    def write_solution(self, solfilename): # outputting correct display for Sudoku class 
        print(ALL_CLAUSES_SATISFIED(self.clauses, self.variables, self.assignment))
        with open(solfilename, "w") as file: 
            # iterating through the assignment vars
            for var in self.assignment.keys(): 
                # if var = True
                if self.assignment[var]: 
                    # fetching original symbol (not int)
                    ori_symb = self.var_dict[var]
                    
                    # writing it to the file 
                    # print("SYMBOL: ", ori_symb, var)
                    file.write(str(ori_symb) + "\n")
