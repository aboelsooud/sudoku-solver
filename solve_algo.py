# Description: This file contains the algorithm to solve the sudoku puzzle

# This function checks if a number is valid to be placed in a given position
def is_valid(grid, row, col, num):
    # check if the number is already in the row, column or 3x3 sub-grid
    for i in range(9):
        if grid[row][i] == num:
            return False
    
    # check if the number is already in the column
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    # check if the number is already in the 3x3 sub-grid
    row_start = row - row % 3
    col_start = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[row_start + i][col_start + j] == num:
                return False
    
    # if the number is not in the row, column or 3x3 sub-grid, return True
    return True

# This function solves the sudoku puzzle using depth-first search and backtracking
def solve_sudoku(grid, row, col):
    # check if the row and column are at the end of the grid
    if row == 8 and col == 9:
        return True
    
    # check if the column is at the end of the grid and move to the next row if it is
    if col == 9:
        row += 1
        col = 0

    # check if the number is already in the grid and move to the next column if it is
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)
    
    # loop through each number from 1 to 9
    for num in range(1, 10):
        # check if the number is valid to be placed in the grid
        if is_valid(grid, row, col, num):
            # place the number in the grid
            grid[row][col] = num
            # recursively call the function to place the next number in the grid
            if solve_sudoku(grid, row, col + 1):
                # sodoku is solvable if the function returns True after placing the number in the grid
                # so we return True
                return True
        # if the number is not valid, set the number in the grid to 0 again
        grid[row][col] = 0

    # if the sudoku is not solvable, return False
    return False

# This function calls the solve_sudoku function to solve the sudoku puzzle
def solve_algo(board):
    # call the solve_sudoku function to solve the board
    if solve_sudoku(board, 0, 0):
        # if the board is solvable, return the solved board
        return board
    # otherwise, return False
    return False
