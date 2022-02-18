from copy import deepcopy

def CheckNumberOfSolutions(board):
    """
    Check how many solutions the board has.
    
    returns: int (0: no solutions, 1: one solution, 2: many solutions)
    """
    # check if board has any errors
    for i in range(16):
        for j in range(16):
            cell = board[i][j]
            if cell == '.':
                continue
            col = board[i][:j] + board[i][j+1:]
            row = [board[k][j] for k in range(i)] + [board[k][j] for k in range(i+1, 16)]
            box = board[i//4*4:i//4*4+4][j//4*4:j//4*4+4]
            if cell in col or cell in row or cell in box:
                return 0
    
    # check if board is full
    isFull = True
    for i in range(16):
        for j in range(16):
            if board[i][j] == '.':
                isFull = False
                break
        if not isFull:
            break
    if isFull:
        return 1
    
    # check how many solutions board has
    # get the first empty cell
    cellI = 0; cellJ = 0
    for i in range(16):
        for j in range(16):
            if board[i][j] == '.':
                cellI = i; cellJ = j
                break
        if board[i][j] == '.':
            break
    
    # try all numbers from 0 to f
    sols = 0
    for num in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
        newBoard = deepcopy(board)
        newBoard[cellI][cellJ] = num
        sols += CheckNumberOfSolutions(newBoard)
        if sols > 1:
            return 2
    
    # return the number of solutions
    return sols