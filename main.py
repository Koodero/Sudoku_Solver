import os

# Give sudoku board where the 0's represent the blank spaces, board with all 0's in blank_board.py to make easier filling out own board
my_board = [
    [2, 5, 7, 8, 0, 1, 0, 4, 0],
    [9, 8, 0, 6, 7, 0, 5, 0, 1],
    [0, 0, 3, 5, 4, 0, 0, 2, 0],
    [0, 3, 0, 0, 5, 0, 0, 0, 6],
    [7, 0, 0, 0, 9, 0, 2, 1, 0],
    [0, 0, 0, 2, 0, 4, 7, 0, 3],
    [0, 0, 8, 0, 1, 5, 9, 0, 0],
    [0, 6, 1, 0, 0, 8, 0, 0, 0],
    [4, 0, 9, 0, 6, 0, 0, 0, 5]
]


# Function to see if a number is valid and can be put onto board
def is_valid(board, row, column, num):
    not_in_row = num not in board[row]
    not_in_column = num not in [board[i][column]for i in range(9)]
    not_in_section = num not in [board[i][j] for i in range(row//3*3, row//3*3+3) for j in range(column//3*3, column//3*3+3)]
    return not_in_row and not_in_column and not_in_section

# Function to solve the sudoku and show progress
def solve_sudoku(board, row=0, column=0):

    # This part used to clear screen and show progress
    if os.name == 'nt':       # <-- Clearing Windows
        os.system('cls')
    else:                     # <-- Clearing Mac
        os.system('clear')
    for ro in board:
        print(ro)


    # Checking if board is finished and recursively filling the board, backtracking when needed
    if row == 9:
        return True
    elif column == 9:
        return solve_sudoku(board, row+1, 0)
    elif board[row][column] != 0:
        return solve_sudoku(board, row, column+1)
    else:
        for num in range(1, 10):
            if is_valid(board, row, column, num):
                board[row][column] = num
                if solve_sudoku(board, row, column+1):
                    return True
                board[row][column] = 0
        return False
    
    
# Running the function
if __name__ == "__main__":
    solve_sudoku(my_board)
