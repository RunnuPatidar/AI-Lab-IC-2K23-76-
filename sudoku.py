def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))


def is_safe(grid, row, col, num):

    # Check the row.
    for j in range(9):
        if grid[row][j] == num:
            return False

    # Check the column.
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Find the top-left corner of the 3x3 subgrid.
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    # Check the 3x3 subgrid.
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid):

    # Find an empty cell.
    for row in range(9):
        for col in range(9):

            if grid[row][col] == 0:

                # Try digits from 1 to 9.
                for num in range(1, 10):

                    if is_safe(grid, row, col, num):
                        grid[row][col] = num

                        # Recursively solve the remaining puzzle.
                        if solve_sudoku(grid):
                            return True

                        # Backtrack if the choice fails.
                        grid[row][col] = 0

                return False

    # No empty cells remain.
    return True


# Take the Sudoku grid as input.
grid = []

print("Enter the Sudoku grid (9 rows, 9 digits per row).")
print("Use 0 for empty cells.")

for i in range(9):
    while True:
        values = input(f"Enter row {i + 1}: ").split()

        if len(values) == 9:
            try:
                row = [int(x) for x in values]

                if all(0 <= x <= 9 for x in row):
                    grid.append(row)
                    break
            except ValueError:
                pass

        print("Invalid input. Enter exactly 9 digits from 0 to 9.")

print("\nOriginal Sudoku:")
print_grid(grid)

if solve_sudoku(grid):
    print("\nSolved Sudoku:")
    print_grid(grid)
else:
    print("\nNo solution exists for this Sudoku.")