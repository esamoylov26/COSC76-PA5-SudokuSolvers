# CS76; Lisa Samoylov; 11/17/24
# Contains helper functions for DPLL algorithm 
# FIND_PURE_SYMBOL and FIND_UNIT_CLAUSE 

# FIND PURE SYMBOL
# given assignment and list of symbols and clauses, checks to see if there's a symbol 
# that appears in any clause with the same sign 
#=====================================
# INPUT: LIST symbols [INT var]  
#        LIST clauses [LIST [INT var]]
#        DICT assignment {INT var: BOOL T/F}
#
# OUTPUT: INT var, BOOL T/F OR None, None 
#====================================
def FIND_PURE_SYMBOL(symbols, clauses, assignment): 
    # print("---\n IN PURE SYMBOL")
    pos_count = [0]*len(symbols)
    neg_count = [0]*len(symbols) 

    # iterating through all clauses
    for clause in clauses: 
        # iterating through each symbol in clause
        for i in range(len(clause)): 
            symbol = clause[i]
            # print(symbol)

            # scoring 
            if symbol > 0: pos_count[abs(symbol)-1] += 1
            if symbol < 0: neg_count[abs(symbol)-1] += 1
    
    # looking for first pure symbol, if any 
    for i in range(len(symbols)): 
        # found positive pure symbol 
        if pos_count[i] > 0 and neg_count[i] == 0: return i+1, True 

        # found negative pure symbol 
        if neg_count[i] > 0 and pos_count[i] == 0: return i+1, False 
    
    # no pure symbols found :(
    return None, None 

            

# FIND UNIT CLAUSE 
# given list of clauses, checks to see if one of them is a unit clause (i.e. only contains 1 symbol) 
#=====================================
# INPUT: LIST clauses [LIST [INT var]]
#        DICT assignment {INT var: BOOL T/F}
#
# OUTPUT: INT var, BOOL T/F OR None, None 
#====================================
def FIND_UNIT_CLAUSE(clauses, assignment): 
    # iterate through all clauses 
    for clause in clauses: 

        # found unit clause? -- make it satisfied  
        if len(clause) == 1: 
            symbol = clause[0] 

            if symbol < 0: 
                return abs(symbol), False
            
            if symbol > 0: 
                return abs(symbol), True

    # no unit clauses found :(
    return None, None 

