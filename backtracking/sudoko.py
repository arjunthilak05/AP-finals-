# ✅ Function to check if placing a number is valid at board[row][col]
def is_valid(board, row, col, num):
    # Check if num is already in the current row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False  # Not valid if duplicate is found

    # Find the top-left corner of the 3x3 subgrid
    startRow = row - row % 3
    startCol = col - col % 3

    # Check if num is already in the 3x3 subgrid
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == num:
                return False

    return True  # Valid placement


# ✅ Main function to solve the Sudoku using BACKTRACKING
def solve_sudoku(board):
    # Loop through every cell in the board
    for row in range(9):
        for col in range(9):
            # If the cell is empty (contains 0)
            if board[row][col] == 0:
                # Try placing digits 1 through 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        # Place the number temporarily
                        board[row][col] = num

                        # ✅ Recursive call: try to solve rest of the board
                        if solve_sudoku(board):
                            return True  # Solution found!

                        # ❌ If placing num didn't work later — BACKTRACK
                        board[row][col] = 0

                # ❌ No valid number was found for this cell → Backtrack
                return False

    # ✅ No empty cells left — board is solved
    return True


# ✅ Utility function to print the board nicely
def print_board(board):
    for row in board:
        print(row)


# ✅ Sample Sudoku Puzzle (0 = empty cell)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# ✅ Driver Code to Start Solving
if solve_sudoku(board):
    print("✅ Sudoku solved successfully!\n")
    print_board(board)
else:
    print("❌ No solution exists.")
