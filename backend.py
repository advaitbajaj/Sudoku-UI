def solver(board):
    row = -1
    col = -1
    empty = True

    # check for empty key
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 0):
                row = i
                col = j
                empty = False
                break

        if (not empty):
            break
    
    if (empty):
        return True
    
    # backtracking
    for number in range(1, 10):
        if (isSafe(board, row, col, number)):
            board[row][col] = number
            if (solver(board)):
                return True
            else:
                board[row][col] = 0
    
    return False;

def isSafe(board, row, col, number):
    # check for rows and cols
    for i in range(len(board)):
        if (board[row][i] == number):
            return False
        
        if (board[i][col] == number):
            return False
    
    # check grid
    rowStart = (row // 3) * 3
    colStart = (col // 3) * 3

    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            if (board[r][c] == number):
                return False
    
    return True




board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]
solver(board)
print(board)

