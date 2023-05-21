def is_valid_state(state, n):
    #check whether the state is valid or not
    
    #check if all states are crrectly placed wrt queens
    return len(state)==n

def search(solutions, state, n):
    if is_valid_state(state, n):
        ste_to_string = state_to_string(state, n)
        solutions.append(ste_to_string)
        return
    
    for candidate in get_candidate(state, n):

        #add candidate to the board
        state.append(candidate)

        search(state, solutions, n)

        #remove candidate if placement gone wrong
        state.pop()

def get_candidate(state, n):
    if not state:
        return range(n)
    position = len(state)
    candidates = set(range(n))

    #prune down candidates that place the queen in attacking position
    for row, col in enumerate(state):
        
        #discard column already taken by the queen
        candidates.discard(col)
        dist = position-row

        #discard diagonals:
        candidates.discard(col+dist)
        candidates.discard(col-dist)
    return candidates
def solve(n):
    solutions = []
    state = []
    search(solutions, state, n)
    return solutions

def state_to_string(state, n):
    result = []
    for i in state:
        string = '.' * i + 'Q' + '.' * (n-i-1)
        result.append(string)
    return result 

print(solve(4))