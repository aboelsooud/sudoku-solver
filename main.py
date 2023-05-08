from tkinter import *
from solve_algo import solve_algo

# Create the root window
root = Tk()
root.title("Sudoku Solver")
root.geometry("440x550")
root.resizable(0, 0)

# main label for the program
label = Label(root, text = "Fill in the numbers and click solve to solve the sudoku puzzle").grid(row = 0, column = 1, columnspan = 10)

# Labels for error messages and success message
error_label = Label(root, text = "", fg = "red")
success_label = Label(root, text = "", fg = "green")
error_label.grid(row = 15, column = 1, columnspan = 10, pady = 10)
success_label.grid(row = 15, column = 1, columnspan = 10, pady = 10)

# Dictionary to store the Entry widgets for each cell in the grid
cells = {}

# Function to validate the input in the Entry widget
def ValidateNumber(number):
    valid = (number.isdigit() or number == "") and len(number) <= 1
    return valid

# Register the validation function with tkinter
reg = root.register(ValidateNumber)

# Function to draw a 3x3 block in the grid
def draw3x3(row, column, frame):
    for i in range(3):
        for j in range(3):
            # Create an Entry widget and store it in the cells dictionary
            e = Entry(frame, width = 5, justify = "center", validate = "key", validatecommand = (reg, "%P"))
            e.grid(row = row + i + 1, column = column + j + 1, sticky="nsew", padx = 1, pady = 1, ipady = 5)
            cells[(row + i + 1, column + j + 1)] = e

# Function to draw the entire 9x9 grid
def draw9x9():
    for rowNo in range(1, 10, 3):
        for columnNo in range(0, 9, 3):
            # Create a frame to hold each 3x3 block and call draw3x3 to draw it
            frame = Frame(root, bd = 1, relief = SOLID)
            frame.grid(row = rowNo + 1, column = columnNo + 1, rowspan = 3, columnspan = 3)
            draw3x3(rowNo, columnNo, frame)

# Function to clear the grid and reset error and success labels
def ClearGrid():
    error_label.configure(text = "")
    success_label.configure(text = "")
    for i in range(2, 11):
        for j in range(1, 10):
            cells[(i, j)].delete(0, "end")

# Function to get the values from the grid and call the solve function
def getValues():
    board = []
    error_label.configure(text = "")
    success_label.configure(text = "")

    # Create a 2D list from the values in the cells dictionary
    for i in range(2, 11):
        rows = []
        for j in range(1, 10):
            value = cells[(i, j)].get()
            if value == "":
                rows.append(0)
            else:
                rows.append(int(value))
        board.append(rows)

    # Call the solve function
    solve_grid(board)

# This function checks if a Sudoku board is valid, meaning it has no duplicate numbers in rows, columns or 3x3 sub-grids
def check_grid(board):
    # loop through each row of the board
    for i in range(9):
        # initialize a set to store the unique numbers in the row, and a count for the non-zero numbers
        diffs = set()
        cnt = 0
        # loop through each column of the row
        for j in range(9):
            # if the number is non-zero, increment the count and add it to the set
            if board[i][j] != 0:
                cnt += 1
                diffs.add(board[i][j])
        # if the count is not equal to the length of the set, then there are duplicate numbers in the row
        if cnt != len(diffs):
            return False
    
    # loop through each column of the board
    for j in range(9):
        # initialize a set to store the unique numbers in the column, and a count for the non-zero numbers
        diffs = set()
        cnt = 0
        # loop through each row of the column
        for i in range(9):
            # if the number is non-zero, increment the count and add it to the set
            if board[i][j] != 0:
                cnt += 1
                diffs.add(board[i][j])
        # if the count is not equal to the length of the set, then there are duplicate numbers in the column
        if cnt != len(diffs):
            return False

    # loop through each 3x3 sub-grid of the board 
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # initialize a set to store the unique numbers in the sub-grid, and a count for the non-zero numbers
            diffs = set()
            cnt = 0
            for k in range(3):
                for l in range(3):
                    # if the number is non-zero, increment the count and add it to the set
                    if board[i + k][j + l] != 0:
                        cnt += 1
                        diffs.add(board[i + k][j + l])
            # if the count is not equal to the length of the set, then there are duplicate numbers in the sub-grid
            if cnt != len(diffs):
                return False
    
    # if the board is valid, return True
    return True

# This function solves the Sudoku board using the solve_algo function from solve_algo.py
def solve_grid(board):
    # check if the board is valid
    if check_grid(board) == False:
        # if not, display an error message and return
        error_label.configure(text = "Invalid grid")
        return
    
    # call the solve_algo function to solve the board
    solved_board = solve_algo(board)

    # if the board is not solvable, display an error message and return
    if solved_board == False:
        error_label.configure(text = "Invalid grid")
        return
    
    # if the board is solvable, display the solved board in the grid
    for i in range(2, 11):
        for j in range(1, 10):
            cells[(i, j)].delete(0, "end")
            cells[(i, j)].insert(0, solved_board[i - 2][j - 1])

    # display a success message
    success_label.configure(text = "Solved!")

# Create the Solve and Clear buttons
solve_btn = Button(root, command = getValues, text = "Solve", width = 10).grid(row = 20, column = 1, columnspan = 5, pady = 20)
clear_btn = Button(root, command = ClearGrid, text = "Clear", width = 10).grid(row = 20, column = 5, columnspan = 5, pady = 20)

# Call the draw9x9 function to draw the grid
draw9x9()

# Start the main loop
root.mainloop()
