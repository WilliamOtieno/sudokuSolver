def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    # check row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # check col
    col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # check square grid
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # getting here means the checks pass
    return True

    


def solve_sudoku(puzzle):
    # Solve using backtracking technique
    # Returns whether a solution exists
    # Mutates puzzle to be solution if it exists

    # 1. Choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # 1.1 If there's nowhere left, we are done
    if row is None:
        return True 

    # 2. If there's a place, make a guess between 1 and 9 inclusive
    for guess in range(1, 10):
        # 3. Check if is valid guess
        if is_valid(puzzle, guess, row, col):
            # 3.1 If valid, place the guess on puzzle
            puzzle[row][col] = guess

            # 4. Now recursively call the function to the puzzle
            if solve_sudoku(puzzle):
                return True
        
        # 5. If not valid or guess doees not solve
        # Initiate backtracking
        puzzle[row][col] = -1 # Reset the guess

    # 6. If none works, then the puzzle is unsolvable
    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,		-1, 5, -1,		-1, -1, -1],
        [-1, -1, -1,	2, -1, -1,		-1, -1, 5],
        [-1, -1, -1,	7, 1, 9,		-1, 8, -1],

        [-1, 5, -1,		-1, 6, 8,		-1, -1, -1],
        [2, -1, 6,		-1, -1, 3,		-1, -1, -1],
        [-1, -1, -1,    -1, -1, -1,		-1, -1, 4],

		[5, -1, -1, 	-1, -1, -1,		-1, -1, -1],
		[6, 7, -1,		1, -1, 5, 		-1, 4, -1],
		[1, -1, 9,		-1, -1, -1,		2, -1, -1]

    ]
print(solve_sudoku(example_board))
print(example_board)
