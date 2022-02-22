from copy import deepcopy

def CheckNumberOfSolutions(board):
    """
    Check how many solutions the board has.
    
    returns: int (0: no solutions, 1: one solution, 2: many solutions)
    """
    # check if board has any errors
    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            if cell == '.':
                continue
            col = board[i][:j] + board[i][j+1:]
            row = [board[k][j] for k in range(i)] + [board[k][j] for k in range(i+1, 9)]
            box = board[i//3*3:i//3*3+3][j//3*3:j//3*3+3]
            if cell in col or cell in row or cell in box:
                return 0
    
    # check if board is full
    isFull = True
    for i in range(9):
        for j in range(9):
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
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                cellI = i; cellJ = j
                break
        if board[i][j] == '.':
            break
    
    # try all numbers from 1 to 9
    sols = 0
    for num in range(1, 10):
        newBoard = deepcopy(board)
        newBoard[cellI][cellJ] = num
        sols += CheckNumberOfSolutions(newBoard)
        if sols > 1:
            return 2
    
    # return the number of solutions
    return sols