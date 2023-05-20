def is_valid_state(state, n):
    #check whether the state is valid or not
    
    #check if all states are crrectly placed wrt queens
    return len(state)==n

def search(state, solutions, n):
    if is_valid_state(state , n):
        ste_string=state_to_string(state, n)
        solutions.append(ste_string)
        return 
    
    for candidate in get_candidate(state, n):
        
        #add candidate to the board
        state.append(candidate) 
        
        search(state, solutions, n)
        
        #remove the candidate if the placement is wrong.
        state.pop() 
        
def get_candidate(state, n):
    if not state:
        return range(n)
    position =len(state)
    candidates=set(range(n))
    
    #prune down candidates that place the queen in the attacking position
    for row,col in enumerate(state):
    
        #discard the column that is already occupied by a queen
        candidates.discard(col)
        dist=position-row
        
        #discard diagonals
        candidates.discard(col+dist)
        candidates.discard(col-dist)
    return candidates
def solve(n):
    solutions=[]
    state=[]
    search(state, solutions, n)
    return solutions

def state_to_string(state, n):
    ret=[]
    for i in state:
        string='.'* i + 'Q' + '.' * (n-i-1)
        ret.append(string)
    return ret

print(solve(4))