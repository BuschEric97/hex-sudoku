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
    nums = [num for num in range(1, 10)]
    col = board[i][:j] + board[i][j+1:]
    row = [board[k][j] for k in range(i)] + [board[k][j] for k in range(i+1, 9)]
    box = board[i//3*3:i//3*3+3][j//3*3:j//3*3+3]
    for num in nums:
        if num in col or num in row or num in box:
            nums.remove(num)
    return nums

def GenerateFullValidBoard():
    # initialize the board
    board = [['.' for i in range(9)] for j in range(9)]

    while not BoardIsFull(board):
        print(board)

        # get random empty cell
        cellI = random.randint(0, 8)
        cellJ = random.randint(0, 8)
        if board[cellI][cellJ] != '.':
            continue

        # get random number
        nums = ValidCellNumbers(board, cellI, cellJ)
        cellNum = nums[random.randint(0, len(nums)-1)]

        # place the number in the cell
        board[cellI][cellJ] = cellNum

        # check how many solutions the board now has
        # if there are no solutions, undo placing the number
        sols = CheckNumberOfSolutions(board)
        if sols == 0:
            board[cellI][cellJ] = '.'
        elif sols == 1:
            return board
    
    return board