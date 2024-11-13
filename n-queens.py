def n_queens(n):
    col = set()
    posdiag = set()
    negdiag = set()

    res = []

    board = [["0"]*n for i in range (n)]
    def backtrack(r):
        if r == n:
            copy = [" ".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r+c) in posdiag or (r-c) in negdiag:
                continue

            col.add(c)
            posdiag.add(r+c)
            negdiag.add(r-c)
            board[r][c]="1"

            backtrack(r+1)

            col.remove(c)
            posdiag.remove(r+c)
            negdiag.remove(r-c)
            board[r][c] = "0"

    backtrack(0)
    for sol in res:
        for row in sol:
            print(row)
        print()

if __name__ == "__main__":
    n_queens(8)