def n_queens_with_first_placed(n, first_row, first_col):
    # Initialize sets to track occupied columns and diagonals
    col = set([first_col])
    posdiag = set([first_row + first_col])  # Positive diagonal (r + c)
    negdiag = set([first_row - first_col])  # Negative diagonal (r - c)

    # Store results
    res = []

    # Create the board with the first queen pre-placed
    board = [["0"] * n for _ in range(n)]
    board[first_row][first_col] = "1"

    def backtrack(r):
        # Base case: If all queens are placed, save the solution
        if r == n:
            copy = [" ".join(row) for row in board]
            res.append(copy)
            return

        # Skip the row where the first queen is pre-placed
        if r == first_row:
            backtrack(r + 1)
            return

        # Try placing a queen in each column of the current row
        for c in range(n):
            # Skip if the column or diagonals are already occupied
            if c in col or (r + c) in posdiag or (r - c) in negdiag:
                continue

            # Place the queen
            col.add(c)
            posdiag.add(r + c)
            negdiag.add(r - c)
            board[r][c] = "1"

            # Recurse for the next row
            backtrack(r + 1)

            # Remove the queen (backtracking step)
            col.remove(c)
            posdiag.remove(r + c)
            negdiag.remove(r - c)
            board[r][c] = "0"

    # Start the backtracking process from row 0
    backtrack(0)

    # Print all valid solutions
    for sol in res:
        for row in sol:
            print(row)
        print()

if __name__ == "__main__":
    # First queen placed at (0, 0) on an 8x8 chessboard
    n_queens_with_first_placed(8, 0, 0)
