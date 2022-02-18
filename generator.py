import random
from solver import CheckNumberOfSolutions

def BoardIsFull(board):
    for i in range(16):
        for j in range(16):
            if board[i][j] == '.':
                return False
    return True

def ValidCellNumbers(board, i, j):
    # get the numbers that can be placed in the cell
    nums = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    col = board[i][:j] + board[i][j+1:]
    row = [board[k][j] for k in range(i)] + [board[k][j] for k in range(i+1, 16)]
    box = board[i//4*4:i//4*4+4][j//4*4:j//4*4+4]
    for num in nums:
        if num in col or num in row or num in box:
            nums.remove(num)
    return nums

def GenerateFullValidBoard():
    # initialize the board
    board = [['.' for i in range(16)] for j in range(16)]

    while not BoardIsFull(board):
        print(board)

        # get random empty cell
        cellI = random.randint(0, 15)
        cellJ = random.randint(0, 15)
        if board[cellI][cellJ] != '.':
            continue

        # get random number
        cellNum = ValidCellNumbers(board, cellI, cellJ)[random.randint(0, 15)]

        # place the number in the cell
        board[cellI][cellJ] = cellNum

        # check how many solutions the board now has
        # if there are no solutions, undo placing the number
        sols = CheckNumberOfSolutions(board)
        if sols == 0:
            board[cellI][cellJ] = '.'
    
    return board