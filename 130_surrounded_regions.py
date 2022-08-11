class Solution:
    def solve(self, board):
        ROW, COL = len(board), len(board[0])

        def capture(r, c):
            if r not in range(ROW) or c not in range(COL) or board[r][c] != "O":
                return

            board[r][c] = "T"
            capture(r-1, c)
            capture(r+1, c)
            capture(r, c-1)
            capture(r, c+1)
            
        for r in range(ROW):
            for c in range(COL):
                if (r in [0, ROW - 1] or c in [0, COL - 1]) and board[r][c] == "O":
                    capture(r, c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "T":
                    board[r][c] = "O"
