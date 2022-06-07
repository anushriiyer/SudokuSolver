matrix_size = 9

def print_solution(grid):
    global matrix_size
    print("Solution:", end = "\n")
    for x in range(matrix_size):
        for y in range (matrix_size):
            print(grid[x][y], end = '  ')
        print()

#brute-force algorithm

def check_valid_move(grid, row, col, num):
    for i in range(matrix_size):
        if grid[row][i] == num:
            return 0
    
    for i in range(matrix_size):
        if grid[i][col] == num:
            return 0
    
    start_row_block = row - row % 3 #indicates the starting square block for row
    start_col_block = col - col % 3 #indicates the starting square block for column

    for x in range(3):
        for y in range(3):
            if grid[x + start_row_block][y + start_col_block] == num:
                return 0
    return 1


def solve_sudoku(grid,row,col):
    global matrix_size

    if row == matrix_size - 1 and col == matrix_size - 1:
        return 1

    if col == matrix_size:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve_sudoku(grid,row,col+1)
    
    for num in range (1, matrix_size + 1):
        if check_valid_move(grid,row,col,num):
            grid[row][col] = num
        
            if solve_sudoku(grid, row, col + 1):
                return 1
        
        grid[row][col] = 0
    
    return 0